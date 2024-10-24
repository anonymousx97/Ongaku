#!/usr/bin/env python3

"""

 * create_config.py: File to authenticate Ongaku with a telegram account

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

from pyrogram import Client

if os.path.isfile("BOT.session"):
    os.remove("BOT.session")


API_ID = int(os.environ.get("API_ID", 0)) or int(input("Enter API_ID: "))
API_HASH = os.environ.get("API_HASH") or input("Enter API_HASH: ")


async def main():
    async with Client(
        name="BOT", api_id=API_ID, api_hash=API_HASH, in_memory=True
    ) as app:
        session = await app.export_session_string()

        await app.send_message("me", f"#STRING_SESSION\n\n`{session}`")

        log_chat = await app.create_channel("Ongaku Logs")

        me_id = app.me.id

    config_env = f"""

WORKING_DIR="ongaku"
# DO NOT CHANGE

### Required ###

API_ID={API_ID}

API_HASH={API_HASH}

KEEP_ALIVE=0

# • Set 1 to make Ongaku run all the time.
# • Set 0 to make Ongaku run only when notification is present.

SESSION_STRING={session}

# • The session you received in your saved messages
#    when you started Ongaku for the first time.

OWNER_ID={me_id}

# • Your telegram user ID

CMD_TRIGGER=.

# • Trigger for bot, Defaults to "."

LOG_CHAT={log_chat}

# • Channel ID for receiving Ongaku logs

### Optional ###

#MUSIC_PLAYER="music app package name"
# • Only Check for a Specific Player
# • Defaults to cross check against all popular players
# • Make sure your music app has notifications support!


#PREFER_NOW_PLAYING_PIXEL_MODE=0

# • To activate set to 1
# • Detect nearby playing music on Google Pixel devices instead of detecting Music from Music Player
"""

    with open("config.env", "w+") as config_file:
        config_file.write(config_env)

    print("config.env generated successfully.")

    print(f"To change any vars type ' nano {os.getcwd()}/config.env' ")

if __name__=="__main__":
    asyncio.run(main())
