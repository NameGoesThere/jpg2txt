from PIL import Image


# Turns pixel brightness into a user-defined greyscale.
def getAscii(color, scale) -> str:
    out = scale[len(scale) - 1]
    for i in range(len(scale)):
        if color[0] + color[1] + color[2] >= 765 / len(scale) * (i + 1):
            out = scale[i]
    return out


# Converts jpg file into Ascii characters using the getAscii function.
def convertJpg(path, scale) -> str:
    string = ""
    image = Image.open(path)
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            string += " " + getAscii(image.getpixel((x, y)), scale)
        string += "\n"

    return string
