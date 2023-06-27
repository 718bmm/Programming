from PIL import Image, ImageFilter

with Image.open("./pokemons/pikachu.png") as img:
    img.load()

# print(img)

# print(img.format)
# print(img.size)
# print(img.mode)
# all attributes and methods we have access to
# print(dir(img))

# filters: SMOOTH, SHARPEN
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img.save('blur_pikachu.png', 'png') # png accept filtering


# filtered_img = img.convert('L') # greyscale
# filtered_img.save('blur_pikachu.png', 'png')
# filtered_img.show() # показывает сохранённую картину
# rotated = filtered_img.rotate(90)
# rotated.save('rotated.png', 'png')
# rotated.show()

# transposed_img = img.transpose(Image.TRANSVERSE)
# transposed_img.show

# resized = filtered_img.resize((300, 300))
# resized.save('resized.png', 'png')

box = (50, 50, 300, 300)
region = img.crop(box)
region.save('grey_pikachu.png', 'png')

img = Image.open('./astro.png')
print(img.size)

# we will lose original aspect ratio width & height
# new_img = img.resize((400, 200)) # (5611, 5339) try to set to 200
# new_img.save('thumb.png', 'png')

img.thumbnail((400, 400)) # максимальное значение ширины и высоты
print(img.size)
img.save('thumbnail.jpg')


# filemane = "./pokemons/pikachu.png"
# with Image.open(filemane) as img:
#     img.load() # similar to read in files

# type(img)