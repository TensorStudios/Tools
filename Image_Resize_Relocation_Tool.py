from PIL import Image
import glob, os

inputpath = r"C:/Users/emnet/Desktop/Start/"
outputpath = "C:/Users/emnet/Desktop/Stop/"

for dirpath, dirnames, filenames in os.walk(inputpath):
    structure = os.path.join(outputpath, dirpath[len(inputpath):])
    if not os.path.isdir(structure):
        os.mkdir(structure)
    else:
        print("Folder does already exits!")

outputfolders = glob.glob(outputpath + "*/")
print(outputfolders)

inputfolders = glob.glob(inputpath + "*/")
print(inputfolders)

for i in range(len(inputfolders)):
    print(inputfolders[i])
    img = glob.glob(inputfolders[i] + "*.png")
    for x in range(len(img)):
        im = Image.open(img[x])
        size = im.size
        print(f"This image is currently sized: {im.size}")
        factor = 2
        print("scaling factor " + str(factor))
        new_size = (size[0] * factor, size[1] * factor)
        print("the new image will be " + str(new_size))
        im = im.resize(new_size)
        im.save(outputfolders[i] + os.path.basename(img[x]))

img2 = glob.glob(inputpath + "*.png")
for y in range(len(img2)):
    im = Image.open(img2[y])
    size = im.size
    print(f"This image is currently sized: {im.size}")
    factor = 2
    print("scaling factor " + str(factor))
    new_size = (size[0]*factor, size[1]*factor)
    print("the new image will be " + str(new_size))
    im = im.resize(new_size)
    im.save(outputpath + os.path.basename(img2[y]))
