from io import BytesIO
import os

try:
    from PIL import Image, ImageDraw, ImageFont, ImageSequence

    pil_installed = True
except ModuleNotFoundError:
    pil_installed = False


def neofetch(stdout):
    if not pil_installed:
        return _, "Ongaku: PIL is not installed\nTip: Check README.md"
    err = None
    stdout = stdout.splitlines()
    x, y = 100, 25
    gif = Image.open("ongaku/resources/images/neofetch_template.gif")
    frames = []
    font = ImageFont.truetype("ongaku/resources/NotoSans-Regular.ttf", 23)
    count = 1
    text = "Ongaku is running \n"
    for frame in ImageSequence.Iterator(gif):
        try:
            text += f"{stdout[count]}\n"
        except IndexError:
            pass
        draw = ImageDraw.Draw(frame)
        draw.text(xy=(x, y), text=text, font=font, fill="white")
        pic = BytesIO()
        frame.save(pic, format="GIF")
        frame = Image.open(pic)
        frames.append(frame)
        count += 1
    # neo_gif = BytesIO()
    # frames[0].save(neo_gif, save_all=True, append_images=frames[1:], format="GIF")
    # neo_gif.name = "neofetch.gif"
    frames[0].save(
        "neofetch.gif", save_all=True, append_images=frames[1:], format="GIF"
    )
    if not os.path.isfile("neofetch.gif"):
        err = "Neofetch GIF generation failed."
    return "neofetch.gif", err
