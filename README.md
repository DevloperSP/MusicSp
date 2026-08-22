<h1 align="center">
  <img src=".assets/animated_title.svg" alt="MusicSp - Developer Sparrow" height="55">
</h1>

<p align="center">
  <img src=".assets/social_preview.jpg" alt="MusicSp Telegram Music Bot Banner" width="100%" style="border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
</p>

<p align="center">
  <img src=".assets/equalizer.svg" width="50%" height="40" alt="Audio Equalizer Wave">
</p>

<p align="center">
  <b>✨ 𝑴𝒖𝒔𝒊𝒄𝑺𝒑 — 𝑵𝒆𝒙𝒕-𝑮𝒆𝒏 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕 𝑴𝒖𝒔𝒊𝒄 & 𝑽𝒊𝒅𝒆𝒐 𝑺𝒕𝒓𝒆𝒂𝒎𝒊𝒏𝒈 𝑬𝒏𝒈𝒊𝒏𝒆 🎶</b>
  <br>
  <i>⚡ 𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 𝑷𝒚𝒕𝒉𝒐𝒏, 𝑲𝒖𝒓𝒊𝒈𝒓𝒂𝒎 & 𝑷𝒚𝑻𝒈𝑪𝒂𝒍𝒍𝒔 • 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑺𝒑𝒂𝒓𝒓𝒐𝒘 𝑪𝒐𝒓𝒆 🦅</i>
</p>

<p align="center">
  <a href="https://github.com/DevloperSP/MusicSp/stargazers"><img src="https://img.shields.io/github/stars/DevloperSP/MusicSp?style=for-the-badge&color=2563EB" alt="GitHub Stars"></a>
  <a href="https://github.com/DevloperSP/MusicSp/network/members"><img src="https://img.shields.io/github/forks/DevloperSP/MusicSp?style=for-the-badge&color=3B82F6" alt="GitHub Forks"></a>
  <a href="https://github.com/DevloperSP/MusicSp/blob/main/LICENSE"><img src="https://img.shields.io/github/license/DevloperSP/MusicSp?style=for-the-badge&color=10B981" alt="License"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.10%20%7C%203.12-F59E0B?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://t.me/Mecobots"><img src="https://img.shields.io/badge/Telegram-Community-06B6D4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Community"></a>
</p>

---

## 🌟 𝑷𝒓𝒐𝒋𝒆𝒄𝒕 𝑶𝒗𝒆𝒓𝒗𝒊𝒆𝒘

**MusicSp** *(also known across Telegram as **Sparrow Music Bot** / **Developer Sparrow Core**)* is a modern, ultra-fast, open-source streaming bot engineered in **Python 3**. It harnesses the asynchronous speed of **Kurigram / Pyrogram** for Telegram MTProto communication and **PyTgCalls (WebRTC)** for high-fidelity audio and crystal-clear HD video streaming directly in Telegram Voice Chats, Supergroups, and Channel Live Streams.

Designed for peak stability and seamless user experience, MusicSp features multi-source music streaming (YouTube, Spotify, Apple Music, SoundCloud, Resso, Telegram Direct Files), interactive colorful inline buttons with custom emoji support, intelligent multi-assistant load distribution, and async MongoDB storage.

---

## 💎 𝑲𝒆𝒚 𝑭𝒆𝒂𝒕𝒖𝒓𝒆𝒔 & 𝑪𝒂𝒑𝒂𝒃𝒊𝒍𝒊𝒕𝒊𝒆𝒔

- 🎧 **Multi-Source Streaming**: Stream audio and videos seamlessly from YouTube, Spotify, Apple Music, SoundCloud, Resso, and direct Telegram audio/video documents.
- 📹 **Dual Audio & HD Video Modes**: Effortlessly toggle between voice chat audio streaming (`/play`) and high-definition video chat broadcasting (`/vplay`).
- 🎨 **Colourful Interactive UI**: Custom inline buttons styled with Kurigram `ButtonStyle` (Primary, Success, Danger) and premium custom emoji animations.
- ⚡ **Multi-Assistant Scaling**: Supports up to 5 assistant sessions (`STRING_SESSION` to `STRING_SESSION5`) for smooth load-balancing across multiple active chats.
- 🎚️ **Live Stream Controls**: Real-time seeking (`/seek`), speed alteration (`/speed` from 0.5x to 2.0x), track loop (`/loop`), and random queue shuffle (`/shuffle`).
- 📜 **Smart Queue & Playlist Management**: Queuing engine with track search slider, personal saved playlist management (`/playlist`), and live queue inspection (`/queue`).
- 🌐 **Multilingual Engine**: Native support for multiple international languages with instant language selection (`/lang`).
- 🛡️ **Fail-Safe & Crash-Proof**: Fully asynchronous architecture backed by Motor MongoDB, isolated virtual environment (`.venv`) support, and resilient network failover.

---

## 🎧 𝑺𝒖𝒑𝒑𝒐𝒓𝒕𝒆𝒅 𝑴𝒖𝒔𝒊𝒄 & 𝑽𝒊𝒅𝒆𝒐 𝑺𝒐𝒖𝒓𝒄𝒆𝒔

| 📻 Platform | 🎵 Audio Stream | 📺 Video Stream | 📑 Playlist Support | 🔍 Input Method |
| :--- | :---: | :---: | :---: | :--- |
| **YouTube** | ✅ | ✅ | ✅ | Direct Link, Playlist Link, Song Title Search |
| **Spotify** | ✅ | ❌ | ✅ | Track Link, Album Link, Playlist Link, Artist Link |
| **Apple Music** | ✅ | ❌ | ✅ | Song Link, Playlist Link |
| **SoundCloud** | ✅ | ❌ | ❌ | Track Link |
| **Resso** | ✅ | ❌ | ❌ | Track Link |
| **Telegram Media** | ✅ | ✅ | ❌ | Audio Files, Video Files, Voice Notes, Documents |

---

## 🎛️ 𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 & 𝑼𝒔𝒂𝒈𝒆 𝑴𝒂𝒏𝒖𝒂𝒍

<details>
<summary><b>🎵 𝑼𝒔𝒆𝒓 𝑷𝒍𝒂𝒚𝒃𝒂𝒄𝒌 𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 (Click to Expand)</b></summary>
<br>

| Command | Description |
| :--- | :--- |
| `/play <query/link>` | Stream audio in group voice chat. |
| `/vplay <query/link>` | Stream HD video in group voice chat. |
| `/cplay <query/link>` | Stream audio in linked channel voice chat. |
| `/cvplay <query/link>` | Stream video in linked channel voice chat. |
| `/queue` | View the current queue of upcoming songs. |
| `/playlist` | View or play your personal saved playlist. |
| `/lyrics <song name>` | Search and fetch synchronized song lyrics. |
| `/ping` | Check bot latency, CPU load, and server uptime. |
| `/stats` | View global bot usage statistics. |
| `/settings` | Open interactive chat configuration menu. |
| `/help` | Open the interactive help panel. |
| `/repo` | Display repository information. |

</details>

<details>
<summary><b>🎚️ 𝑨𝒅𝒎𝒊𝒏 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕 𝑪𝒐𝒏𝒕𝒓𝒐𝒍𝒔 (Click to Expand)</b></summary>
<br>

| Command | Description |
| :--- | :--- |
| `/pause` | Temporarily pause current track playback. |
| `/resume` | Resume playback from paused state. |
| `/skip` | Skip current track and play next in queue. |
| `/end` or `/stop` | Stop playback and clear the active queue. |
| `/mute` | Mute assistant in the group voice chat. |
| `/unmute` | Unmute assistant in the group voice chat. |
| `/seek <seconds>` | Jump forward or backward in active track. |
| `/speed <0.5x - 2.0x>` | Adjust stream playback speed. |
| `/loop <1-10 / disable>` | Repeat current track or active queue. |
| `/shuffle` | Randomize the order of queued tracks. |

</details>

<details>
<summary><b>👑 𝑺𝒖𝒅𝒐 & 𝑶𝒘𝒏𝒆𝒓 𝑴𝒂𝒏𝒂𝒈𝒆𝒎𝒆𝒏𝒕 (Click to Expand)</b></summary>
<br>

| Command | Description |
| :--- | :--- |
| `/broadcast <text>` | Broadcast an announcement to all served chats. |
| `/gban <user_id>` | Global ban malicious users across all bot chats. |
| `/ungban <user_id>` | Remove global ban from a user ID. |
| `/restart` | Restart bot and assistant sessions cleanly. |
| `/update` | Pull and merge latest updates from Git upstream. |
| `/logs` | Retrieve recent execution error and activity logs. |

</details>

---

## 🚀 𝑫𝒆𝒑𝒍𝒐𝒚𝒎𝒆𝒏𝒕 𝑮𝒖𝒊𝒅𝒆𝒔 (𝑪𝒍𝒊𝒄𝒌 𝒕𝒐 𝑬𝒙𝒑𝒂𝒏𝒅)

<details>
<summary><b>🟣 𝑶𝒏𝒆-𝑪𝒍𝒊𝒄𝒌 𝑯𝒆𝒓𝒐𝒌𝒖 𝑫𝒆𝒑𝒍𝒐𝒚𝒎𝒆𝒏𝒕</b></summary>
<br>

Deploy **MusicSp** instantly on Heroku with pre-configured buildpacks:

<p align="center">
  <a href="https://dashboard.heroku.com/new?template=https://github.com/DevloperSP/MusicSp">
    <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku">
  </a>
</p>

1. Click the **Deploy to Heroku** button above.
2. Enter your `API_ID`, `API_HASH`, `BOT_TOKEN`, `MONGO_DB_URI`, `OWNER_ID`, `LOG_GROUP_ID`, and `STRING_SESSION`.
3. Click **Deploy App** and turn on the worker dyno in your dashboard.

</details>

<details>
<summary><b>🐧 𝑼𝒃𝒖𝒏𝒕𝒖 / 𝑫𝒆𝒃𝒊𝒂𝒏 𝑽𝑷𝑺 𝑫𝒆𝒑𝒍𝒐𝒚𝒎𝒆𝒏𝒕 (.𝒗𝒆𝒏𝒗 𝑨𝒖𝒕𝒐𝒎𝒂𝒕𝒆𝒅)</b></summary>
<br>

MusicSp includes automated environment setup scripts (`setup` & `start`) that configure an isolated Python virtual environment (`.venv`) to completely prevent Ubuntu 24.04 PEP 668 restrictions:

```bash
# 1. Update and upgrade system packages
sudo apt-get update && sudo apt-get upgrade -y

# 2. Clone the MusicSp repository
git clone https://github.com/DevloperSP/MusicSp
cd MusicSp

# 3. Run automated setup installer (Creates .venv & installs all dependencies)
bash setup

# 4. Configure your environment variables
cp sample.env .env
vi .env

# 5. Launch the MusicSp bot
bash start
```

</details>

<details>
<summary><b>🐳 𝑫𝒐𝒄𝒌𝒆𝒓 𝑪𝒐𝒏𝒕𝒂𝒊𝒏𝒆𝒓 𝑫𝒆𝒑𝒍𝒐𝒚𝒎𝒆𝒏𝒕</b></summary>
<br>

Deploy with containerization using the pre-configured [`Dockerfile`](Dockerfile):

```bash
# 1. Clone repository
git clone https://github.com/DevloperSP/MusicSp
cd MusicSp

# 2. Setup environment variables
cp sample.env .env
vi .env

# 3. Build Docker container image
docker build -t musicsp .

# 4. Run Docker container in detached mode
docker run -d --name musicsp_bot --env-file .env musicsp
```

</details>

<details>
<summary><b>💻 𝑴𝒂𝒏𝒖𝒂𝒍 𝑳𝒐𝒄𝒂𝒍 / 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒎𝒆𝒏𝒕 𝑺𝒆𝒕𝒖𝒑</b></summary>
<br>

For local development and testing:

```bash
# 1. Clone repository
git clone https://github.com/DevloperSP/MusicSp && cd MusicSp

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -U pip
pip install -U -r requirements.txt

# 4. Configure .env and run
cp sample.env .env
python3 -m MusicSp
```

</details>

---

## ⚙️ 𝑬𝒏𝒗𝒊𝒓𝒐𝒏𝒎𝒆𝒏𝒕 𝑽𝒂𝒓𝒊𝒂𝒃𝒍𝒆𝒔 (𝑪𝒐𝒏𝒇𝒊𝒈𝒖𝒓𝒂𝒕𝒊𝒐𝒏)

<details>
<summary><b>📋 𝑽𝒊𝒆𝒘 𝑭𝒖𝒍𝒍 𝑬𝒏𝒗𝒊𝒓𝒐𝒏𝒎𝒆𝒏𝒕 𝑽𝒂𝒓𝒊𝒂𝒃𝒍𝒆𝒔 𝑻𝒂𝒃𝒍𝒆</b></summary>
<br>

| Variable | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `API_ID` | **Yes** | — | Telegram API ID from [my.telegram.org](https://my.telegram.org). |
| `API_HASH` | **Yes** | — | Telegram API Hash from [my.telegram.org](https://my.telegram.org). |
| `BOT_TOKEN` | **Yes** | — | Telegram Bot Token from [@BotFather](https://t.me/BotFather). |
| `OWNER_ID` | **Yes** | — | Telegram numeric ID of the bot owner. |
| `MONGO_DB_URI` | **Yes** | — | MongoDB Atlas connection URI string. |
| `LOG_GROUP_ID` | **Yes** | — | Telegram Private Group ID for logging (e.g., `-100xxxxxxx`). |
| `STRING_SESSION` | **Yes** | — | Pyrogram v2 / Kurigram String Session for Assistant 1. |
| `STRING_SESSION2` - `5` | Optional | `None` | Multi-assistant string sessions for load balancing. |
| `SPOTIFY_CLIENT_ID` | Optional | `None` | Spotify Developer API Client ID. |
| `SPOTIFY_CLIENT_SECRET`| Optional | `None` | Spotify Developer API Client Secret. |
| `API_URL` | Optional | `None` | Custom YouTube audio extraction API URL. |
| `API_KEY` | Optional | `None` | Authentication Key for custom YouTube API. |
| `DURATION_LIMIT` | Optional | `1700` | Maximum song duration limit in minutes. |
| `AUTO_LEAVING_ASSISTANT`| Optional | `False` | Auto-leave voice chat assistant when call terminates. |

</details>

---

## 🏗️ 𝑺𝒚𝒔𝒕𝒆𝒎 𝑨𝒓𝒄𝒉𝒊𝒕𝒆𝒄𝒕𝒖𝒓𝒆

```mermaid
graph LR
    User([👤 Telegram User / Group]) -->|Commands / Play Request| Bot[🤖 MusicSp Bot Core]
    Bot -->|Async Query| DB[(🗄️ MongoDB Atlas)]
    Bot -->|Metadata Search| Fetcher[📡 YouTube / Spotify / Apple]
    Bot -->|Stream Dispatch| VC[🔊 PyTgCalls WebRTC Engine]
    VC -->|Audio & Video Feed| Call([🎙️ Group Voice Chat / Video Call])
    Assistant[👥 Assistant Userbot] -->|Active Call Participant| Call
```

---

## ❓ 𝑭𝒓𝒆𝒒𝒖𝒆𝒏𝒕𝒍𝒚 𝑨𝒔𝒌𝒆𝒅 𝑸𝒖𝒆𝒔𝒕𝒊𝒐𝒏𝒔

<details>
<summary><b>1. How does MusicSp solve the Ubuntu 24.04 PEP 668 error?</b></summary>
<br>
Modern Linux systems enforce PEP 668 to protect system Python packages. MusicSp's <code>bash setup</code> automatically creates and manages an isolated <code>.venv</code> virtual environment, and <code>bash start</code> executes the bot via <code>.venv/bin/python</code>.
</details>

<details>
<summary><b>2. Why is the Assistant account not joining the Voice Chat?</b></summary>
<br>
Ensure the Assistant account (from <code>STRING_SESSION</code>) has joined the group, the group voice chat is already started, and the bot has permissions to invite users and manage voice chats.
</details>

<details>
<summary><b>3. Can I use custom cookies or YouTube download APIs?</b></summary>
<br>
Yes! You can configure <code>API_URL</code> and <code>API_KEY</code> in your <code>.env</code> file for lightning-fast external audio resolution without hitting server rate-limits.
</details>

---

## 🤝 𝑪𝒐𝒏𝒕𝒓𝒊𝒃𝒖𝒕𝒊𝒐𝒏 & 𝑳𝒊𝒄𝒆𝒏𝒔𝒆

Contributions are welcome! Follow these steps:
1. 🍴 **Fork the Repository** to your GitHub account.
2. 🌿 **Create a Feature Branch**: `git checkout -b feature/cool-feature`
3. ✍️ **Commit Changes**: `git commit -m 'Add cool feature'`
4. 🚀 **Push Branch**: `git push origin feature/cool-feature`
5. 📬 **Submit a Pull Request** to our `main` branch.

- **License**: Distributed under the [GNU Affero General Public License v3.0 (AGPL-3.0)](LICENSE).
- **Core Engine**: Built & maintained with ❤️ by [DevloperSP](https://github.com/DevloperSP) (**Developer Sparrow**).

---

## 💬 𝑪𝒐𝒎𝒎𝒖𝒏𝒊𝒕𝒚 & 𝑺𝒖𝒑𝒑𝒐𝒓𝒕

<p align="center">
  <a href="https://t.me/Mecobots">
    <img src="https://img.shields.io/badge/Join-Developer%20Home-2563EB?style=for-the-badge&logo=telegram&logoColor=white" alt="Developer Home">
  </a>
  <a href="https://t.me/Spparow_92">
    <img src="https://img.shields.io/badge/Contact%20Owner-%40Spparow__92-0088cc?style=for-the-badge&logo=telegram&logoColor=white" alt="Contact Owner">
  </a>
  <a href="https://t.me/MusicSp1_bot">
    <img src="https://img.shields.io/badge/Demo%20Bot-%40MusicSp1__bot-06B6D4?style=for-the-badge&logo=telegram&logoColor=white" alt="Demo Bot">
  </a>
</p>

<p align="center">
  <sub>✨ <b>MusicSp</b> — Crafted with excellence for Telegram voice & video streaming communities.</sub>
</p>
