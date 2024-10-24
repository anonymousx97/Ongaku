"""

 * commands.py: Commands utility file for Ongaku

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
import os

from ub_core.utils import run_shell_cmd

from ongaku import BOT, Config, Message
from ongaku.extra_config import MediaPlayer
from ongaku.worker import get_current_song
from scripts.neofetch import create_neofetch_overlay


@BOT.add_cmd("about")
async def about(bot: BOT, message: Message):
    about = (
        f"A **smol and fluffy** telegram bot to update your bio with music playing on your android phone in real time!"
        f"\n\n[Get it now!]({Config.REPO.remote().url})"
    )
    await message.reply(about, disable_web_page_preview=True)


@BOT.add_cmd("sync")
async def sync(bot: BOT, message: Message):
    _, bio_update_str = await get_current_song()
    if bio_update_str is None:
        bio_update_str = "Notification is stale"
    await message.reply(bio_update_str)


@BOT.add_cmd("history")
async def history(bot: BOT, message: Message):
    history = MediaPlayer.export_history_str()

    if not history:
        history = "Ongaku: Nothing has been played in the current session"

    final_str = f"<pre language='...'>{history[0:3950]}</pre>"

    await message.reply(text=final_str, del_in=30)


@BOT.add_cmd("nf")
async def neofetch(bot: BOT, message: Message):
    response = await message.reply("`Ongaku: Please wait...`")

    neofetch_str = await run_shell_cmd("neofetch --stdout")

    if "not found" in neofetch_str:
        await response.edit("Ongaku: Neofetch is not installed\nTip: Check README.md")
        return

    if "-t" in message.flags:
        await response.edit(f"`{neofetch_str}`")
        return

    generate_neofetch_gif: None | str = await asyncio.to_thread(
        create_neofetch_overlay, neofetch_str
    )

    if isinstance(generate_neofetch_gif, str):
        await response.edit(generate_neofetch_gif)
        return

    if not os.path.isfile("neofetch.gif"):
        await response.edit("An Error Occured while Generating GIF.")
        return

    await response.edit("Uploading...", del_in=10, block=False)

    caption = (
        f"User : {bot.me.mention}"
        f"\nGit-Branch : {Config.REPO.active_branch}"
        f"\nRepo : [Link]({Config.REPO.remote().url})"
    )

    await message.reply_animation(animation="neofetch.gif", caption=caption)
    os.remove("neofetch.gif")
