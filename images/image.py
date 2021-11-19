from PIL import Image
image_original = Image.open('week7/images/earth.jpg')

width, height = image_original.size
pixels_original = image_original.load()
r, g, b = pixels_original[500, 200]
r1, g1, b1 = pixels_original[200, 500]
r2, g2, b2 = pixels_original[500, 200]
r3, g3, b3 = pixels_original[100, 200]
r4, g4, b4 = pixels_original[300, 300]
pixels_original[100, 200] = (170, 255, 0)
pixels_original[600, 500] = (170, 255, 0)
pixels_original[600, 200] = (170, 255, 0)
pixels_original[50, 200] = (170, 255, 0)
pixels_original[200, 200] = (170, 255, 0)

image_original.show()
print(f' 0: {r,g,b}, 1: {r1, g1, b1}, 2: {r2, g2, b2}, 3: {r3, g3, b3}, 4: {r4, g4, b4}')


#When I am ready to save: image_original.save('file_here.jpg')

# while pixels_original = (76,244,24)

# for pixel in pixels:
#if pixel_spaceship = (76,244,24):
#   pixel_spaceship = pixel_earth
