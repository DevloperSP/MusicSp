import json
from typing import Callable, Dict

def apply_patches():
    try:
        import pyrogram
        from pyrogram import Client
        from pyrogram.raw.base import InputPeer
        from pyrogram.raw.types import (
            Channel,
            ChannelForbidden,
            Chat,
            ChatForbidden,
            GroupCall,
            GroupCallDiscarded,
            InputGroupCall,
            MessageActionChatDeleteUser,
            MessageActionInviteToGroupCall,
            MessageService,
            PeerChat,
            UpdateChannel,
            UpdateGroupCall,
            UpdateGroupCallConnection,
            UpdateGroupCallParticipants,
            UpdateNewChannelMessage,
            UpdateNewMessage,
        )
        from pytgcalls.version_manager import VersionManager
        from pytgcalls.mtproto.client_cache import ClientCache
        from pytgcalls.mtproto.pyrogram_client import PyrogramClient

        if getattr(PyrogramClient, "_is_sp_patched", False):
            return

        def patched_pyrogram_client_init(self, cache_duration: int, client: Client):
            self._app: Client = client
            if VersionManager.version_tuple(
                pyrogram.__version__,
            ) > VersionManager.version_tuple(
                "2.0.0",
            ):
                self._app.send = self._app.invoke
            self._handler: Dict[str, Callable] = {}
            self._cache: ClientCache = ClientCache(
                cache_duration,
                self,
            )

            @self._app.on_raw_update()
            async def on_update(_, update, __, data2):
                try:
                    if isinstance(update, UpdateGroupCallParticipants):
                        participants = getattr(update, "participants", [])
                        for participant in participants:
                            result = self._cache.set_participants_cache(
                                update.call.id,
                                self.chat_id(participant.peer),
                                participant.muted,
                                participant.volume,
                                participant.can_self_unmute,
                                participant.video is not None or participant.presentation is not None,
                                participant.presentation is not None,
                                participant.video is not None,
                                participant.raise_hand_rating,
                                participant.left,
                            )
                            if result is not None:
                                if "PARTICIPANTS_HANDLER" in self._handler:
                                    await self._handler["PARTICIPANTS_HANDLER"](
                                        self._cache.get_chat_id(update.call.id),
                                        result,
                                        participant.just_joined,
                                        participant.left,
                                    )
                    if isinstance(update, UpdateGroupCall):
                        raw_chat_id = getattr(update, "chat_id", None)
                        if raw_chat_id is not None and isinstance(data2, dict) and raw_chat_id in data2:
                            chat_id = self.chat_id(data2[raw_chat_id])
                        elif hasattr(update, "call") and hasattr(update.call, "id") and hasattr(self._cache, "get_chat_id"):
                            chat_id = self._cache.get_chat_id(update.call.id)
                        else:
                            chat_id = None

                        if chat_id is not None:
                            if isinstance(update.call, GroupCall):
                                if getattr(update.call, "schedule_date", None) is None:
                                    self._cache.set_cache(
                                        chat_id,
                                        InputGroupCall(
                                            access_hash=update.call.access_hash,
                                            id=update.call.id,
                                        ),
                                    )
                            if isinstance(update.call, GroupCallDiscarded):
                                self._cache.drop_cache(chat_id)
                                if "CLOSED_HANDLER" in self._handler:
                                    await self._handler["CLOSED_HANDLER"](chat_id)
                    if isinstance(update, UpdateChannel):
                        chat_id = self.chat_id(update)
                        if isinstance(data2, dict) and len(data2) > 0 and hasattr(update, "channel_id") and update.channel_id in data2:
                            if isinstance(data2[update.channel_id], ChannelForbidden):
                                self._cache.drop_cache(chat_id)
                                if "KICK_HANDLER" in self._handler:
                                    await self._handler["KICK_HANDLER"](chat_id)
                    if isinstance(update, (UpdateNewChannelMessage, UpdateNewMessage)):
                        if hasattr(update, "message") and isinstance(update.message, MessageService):
                            if isinstance(update.message.action, MessageActionInviteToGroupCall):
                                if "INVITE_HANDLER" in self._handler:
                                    await self._handler["INVITE_HANDLER"](update.message.action)
                            if isinstance(update.message.action, MessageActionChatDeleteUser):
                                if hasattr(update.message, "peer_id") and isinstance(update.message.peer_id, PeerChat):
                                    chat_id = self.chat_id(update.message.peer_id)
                                    if isinstance(data2, dict) and hasattr(update.message.peer_id, "chat_id") and update.message.peer_id.chat_id in data2:
                                        if isinstance(data2[update.message.peer_id.chat_id], ChatForbidden):
                                            self._cache.drop_cache(chat_id)
                                            if "KICK_HANDLER" in self._handler:
                                                await self._handler["KICK_HANDLER"](chat_id)
                    if isinstance(data2, dict):
                        for group_id in data2:
                            if isinstance(update, (UpdateNewChannelMessage, UpdateNewMessage)):
                                if hasattr(update, "message") and isinstance(update.message, MessageService):
                                    if isinstance(data2[group_id], (Channel, Chat)):
                                        chat_id = self.chat_id(data2[group_id])
                                        if getattr(data2[group_id], "left", False):
                                            self._cache.drop_cache(chat_id)
                                            if "LEFT_HANDLER" in self._handler:
                                                await self._handler["LEFT_HANDLER"](chat_id)
                except Exception:
                    pass

        PyrogramClient.__init__ = patched_pyrogram_client_init
        PyrogramClient._is_sp_patched = True
    except Exception:
        pass

apply_patches()
