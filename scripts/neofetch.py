"""

 * neofetch.py: File to generate neofetch gif for Ongaku

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

from io import BytesIO

try:
    from PIL import Image, ImageDraw, ImageFont, ImageSequence

    pil_installed = True

    gif_frames: list[Image] | None = ImageSequence.Iterator(
        Image.open("resources/images/neofetch_template.gif")
    )

    font: ImageFont.FreeTypeFont | None = ImageFont.truetype(
        font="resources/NotoSans-Regular.ttf", size=22
    )

except ModuleNotFoundError:
    pil_installed = False
    gif_frames = font = None


def create_neofetch_overlay(text: str) -> str | None:
    if not pil_installed:
        return "Ongaku: PIL is not installed\nTip: Check README.md"

    text_lines: list[str] = text.splitlines()[1:]

    x, y = 100, 25

    total_frames: list[Image] = []

    overlay_text: str = "Ongaku is running \n"

    for idx, frame in enumerate(gif_frames):
        try:
            overlay_text += f"{text_lines[idx]}\n"
        except IndexError:
            pass

        draw = ImageDraw.Draw(frame)
        draw.text(xy=(x, y), text=overlay_text, font=font, fill="white")

        frame_io = BytesIO()
        frame.save(frame_io, format="GIF")

        total_frames.append(Image.open(frame_io))

    total_frames[0].save(
        "neofetch.gif", save_all=True, append_images=total_frames[1:], format="GIF"
    )

    # in_memory results in Lower Quality

    # neo_gif = BytesIO()
    # frames[0].save(neo_gif, save_all=True, append_images=frames[1:], format="GIF")
    # neo_gif.name = "neofetch.gif"
