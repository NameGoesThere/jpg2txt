import convert

# Defines greyscale for text file, where density of character is proportional to brightness.
greyscale=" .:-=+*#%@"

# Writes output to out.txt.
open("out.txt","w").write(convert.convertJpg("img.jpg",greyscale))