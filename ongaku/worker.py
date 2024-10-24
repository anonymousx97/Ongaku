"""

 * worker.py: Main logic file of Ongaku

  Copyright (C) 2023 likeadragonmaid, Ryuk

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""

import asyncio
import json
import re
from signal import SIGINT, raise_signal

from ub_core.utils import run_shell_cmd

from ongaku import bot, extra_config
from ongaku.extra_config import MediaPlayer


async def init_task():
    extra_config.ORIGINAL_BIO = (await bot.get_chat("me")).bio or ""
    MediaPlayer.WORKER_TASK = asyncio.create_task(media_worker(), name="ongaku_worker")


async def media_worker():
    while True:
        updated = await update_bio()
        if updated is None and not MediaPlayer.KEEP_ALIVE:
            print("Ongaku: No Notification Detected.")
            raise_signal(SIGINT)
            break

        await asyncio.sleep(30)


async def update_bio():
    now_playing_info = await get_current_song()

    if now_playing_info == (None, None):
        return None

    song_name, bio_update_str = now_playing_info

    if song_name == MediaPlayer.LAST_SONG:
        return False

    MediaPlayer.dump_to_db(song_name)

    await bot.update_profile(bio=bio_update_str)
    await bot.log_text(bio_update_str)

    print("    " + song_name)

    return True


async def get_current_song() -> tuple[str | None, str | None]:
    notification_json = json.loads(await run_shell_cmd("termux-notification-list"))

    for notification in notification_json:
        if notification["packageName"] in MediaPlayer.PLAYERS:
            notification_title = notification["title"]
            notification_content = notification["content"]

            if notification_content == "Tap to see your song history":
                return clean_song_name(notification_title)

            if notification_content:
                notification_content += " - "

            return clean_song_name(notification_content + notification_title)
    else:
        return None, None


def clean_song_name(song_name: str) -> tuple[str, str]:
    song_name = song_name.replace("_", " ")

    debloated_song_name = " ".join(
        [
            word
            for word in re.split("\W+", song_name)
            if word.lower() not in extra_config.BLOAT
        ]
    )

    final_name = f"▷ Now listening: {debloated_song_name}"

    if len(final_name) > 70:
        final_name = f"▷ {debloated_song_name}"[0:70]

    return debloated_song_name, final_name
