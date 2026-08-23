import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config

from MusicSp.logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    REPO_LINK = config.UPSTREAM_REPO
    if not REPO_LINK:
        return
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO
    try:
        repo = Repo()
        LOGGER(__name__).info(f"Git Client Found [VPS DEPLOYER]")
    except GitCommandError:
        LOGGER(__name__).info(f"Invalid Git Command")
    except InvalidGitRepositoryError:
        try:
            repo = Repo.init()
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
            else:
                origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()
            
            branch = config.UPSTREAM_BRANCH or "main"
            available_refs = [ref.name.split("/")[-1] for ref in origin.refs]
            
            if branch not in available_refs:
                if "main" in available_refs:
                    branch = "main"
                elif "master" in available_refs:
                    branch = "master"
                elif len(available_refs) > 0:
                    branch = available_refs[0]

            ref_target = None
            if branch in origin.refs:
                ref_target = origin.refs[branch]
            elif f"origin/{branch}" in origin.refs:
                ref_target = origin.refs[f"origin/{branch}"]
            elif len(origin.refs) > 0:
                ref_target = origin.refs[0]

            if ref_target is not None:
                if branch not in repo.heads:
                    repo.create_head(branch, ref_target)
                repo.heads[branch].set_tracking_branch(ref_target)
                repo.heads[branch].checkout(True)
                
            try:
                repo.create_remote("origin", config.UPSTREAM_REPO)
            except BaseException:
                pass
            nrs = repo.remote("origin")
            nrs.fetch(branch)
            try:
                nrs.pull(branch)
            except GitCommandError:
                repo.git.reset("--hard", "FETCH_HEAD")
            LOGGER(__name__).info(f"Fetching updates from upstream repository...")
        except Exception as e:
            LOGGER(__name__).warning(f"Git auto-sync warning (continuing boot): {e}")
    except Exception as e:
        LOGGER(__name__).warning(f"Git setup skipped: {e}")
