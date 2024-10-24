"""

 * __init__.py: Init file for Ongaku

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

import os
import pickle
from collections import defaultdict
from logging import getLogger

if not os.path.isfile("db.pickle"):
    with open("db.pickle", "wb+") as db_file:
        pickle.dump(defaultdict(int), db_file)

from logging import CRITICAL

from ub_core import LOGGER, BOT, bot, Message, Config

LOGGER.setLevel(level=CRITICAL + 1)
getLogger("root").setLevel(level=CRITICAL + 1)
