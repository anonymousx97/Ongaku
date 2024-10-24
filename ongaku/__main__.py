"""

 * __main__.py: Main file for Ongaku

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
import sys

from pyrogram import idle
from ub_core import Config, bot

from ongaku import extra_config

if __name__ == "__main__":

    async def boot():
        print(extra_config.MediaPlayer.KEEP_ALIVE_STR)

        await bot.start()
        print(
            "Ongaku: Started\nOngaku: Notifications are checked every 30 seconds\n        "
            "to avoid spamming the API(s)."
            "\nOngaku: Send .sync in any chat to force notification detection."
            "\n\nNow Playing:"
        )

        await asyncio.to_thread(bot._import)

        await asyncio.gather(*Config.INIT_TASKS)
        Config.INIT_TASKS.clear()

        await bot.log_text(text="<i>Started</i>")

        await idle()

        extra_config.MediaPlayer.WORKER_TASK.cancel()
        print("Ongaku: Bio has been restored to original.\nOngaku: Stopped")
        await bot.update_profile(bio=extra_config.ORIGINAL_BIO)

        await bot.log_text(text="Ongaku: Stopped")
        await bot.shut_down()

        sys.exit(bot.exit_code)

    bot.run(boot())
