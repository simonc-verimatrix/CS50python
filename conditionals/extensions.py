#Check file extensions and output their media files type
# .gif -> image/gif
# .jpg -> image/jpeg
# .jpeg -> image/jpeg
# .png -> image/png
# .pdf -> application/pdf
# .txt -> text/plain
# .zip -> application/zip

ext = input("File Name: ")
ext = ext.lower()

gif = ".gif" in ext
jpg = ".jpg" in ext
jpeg = ".jpeg" in ext
png = ".png" in ext
pdf = ".pdf" in ext
txt = ".txt" in ext
zip1 = ".zip" in ext

if gif == True:
    print("image/gif")
elif jpg == True or jpeg == True:
    print("image/jpeg")
elif png == True:
    print("image/png")
elif pdf == True:
    print("application/pdf")
elif txt == True:
    print("text/plain")
elif zip1 == True:
    print("application/zip")
else:
    print("application/octet-stream")
