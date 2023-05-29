from PIL import Image

image = Image.open("img.jpg")

string=""

greyscale=" .:-=+*#%@"

def getAscii(color,scale)->str:
    out=scale[len(scale)-1]
    for i in range(len(scale)):
        if color[0] + color[1] + color[2] >= 765/len(scale)*(i+1):
            out=greyscale[i]
    return out

for y in range(image.size[1]):
    for x in range(image.size[0]):
        string+=" "+getAscii(image.getpixel((x,y)),greyscale)
    string+="\n"

open("out.txt","w").write(string)