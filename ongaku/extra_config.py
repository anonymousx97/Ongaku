"""

 * misc.py: File to provide known name extensions to Ongaku

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
import os
import pickle

with open("db.pickle", "rb") as db_file:
    SONG_DB: dict[str, int] = pickle.load(db_file)


class MediaPlayer:

    KEEP_ALIVE: int = int(os.environ.get("KEEP_ALIVE", 0))

    if KEEP_ALIVE:
        KEEP_ALIVE_STR: str = (
            "Ongaku: Bot is set to work until manually stopped.\n        "
            "It can be stopped by Ctrl+C or killing the process(s)\n"
        )
    else:
        KEEP_ALIVE_STR: str = (
            "Ongaku: Bot is set to stop if there is no music notification.\n        "
            "You can change this behavior."
        )

    HISTORY: list[str] = []

    LAST_SONG: str = ""

    if os.environ.get("PREFER_NOW_PLAYING_PIXEL_MODE"):
        PLAYERS: list[str] = ["com.google.android.as"]

    elif os.environ.get("MUSIC_PLAYER"):
        PLAYERS: list[str] = [os.environ.get("MUSIC_PLAYER")]

    else:
        PLAYERS: list[str] = [
            "com.mxtech.videoplayer.pro",
            "com.spotify.music",
            "com.google.android.apps.youtube.music",
            "it.vfsfitvnm.vimusic",
            "org.videolan.vlc",
            "com.apple.android.music",
            "com.amazon.mp3",
            "com.spotify.lite",
            "com.soundcloud.android",
            "deezer.android.app",
            "com.aspiro.tidal",
            "com.mxtech.videoplayer.ad",
        ]

    WORKER_TASK: asyncio.Task | None = None

    @staticmethod
    def dump_to_db(song_name):
        MediaPlayer.LAST_SONG = song_name
        if song_name not in MediaPlayer.HISTORY:
            MediaPlayer.HISTORY.append(song_name)
        SONG_DB[song_name] += 1

    @staticmethod
    def export_history_str() -> str:
        return "\n".join(
            [
                f"<b>{idx+1}</b>. <i>{song_name}</i> <code>{SONG_DB[song_name]} play(s)</code>"
                for idx, song_name in enumerate(MediaPlayer.HISTORY)
            ]
        )


BLOAT = {
    "aac",
    "amr",
    "mp3",
    "m4a",
    "ogg",
    "opus",
    "wav",
    "wma",
    "flac",
    "hq",
    "hd",
    "high quality",
    "audio",
    "(audio)",
    "audio only",
    "(audio only)",
    "explicit",
    "clean",
    "short version",
    "long version",
    "(lyrics)",
    "official audio",
    "[official audio]",
    "(official audio)",
    "(official)",
    "(official music video)",
    "(Official Video - Clean Version)",
    "explicit",
    "(explicit)",
    "(explicit music video)",
    "album",
    "full version",
    "(dirty)",
    "(dirty version)",
    "(uncensored lyrics)",
    "(uncensored)",
    "uncensored version",
    "(uncensored version)",
    "playlist",
    "(playlist)",
    "live",
    "(live)",
    "(Lofi)",
    "(lo-fi)",
    "(slowed)",
    "(reverbed)",
    "(slow)",
    "(reverb)",
    "(slowed & reverb)",
    "(remix)",
    "(mashup)",
    "lyrics",
}

ORIGINAL_BIO: str = ""

SUPER_USERS: list[int] = json.loads(os.environ.get("USERS", "[]"))
