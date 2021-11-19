from PIL import Image

#load image one
image_green = Image.open('week7/images/penguin.jpg')
green_width, green_height = image_green.size
pixels_green = image_green.load()

#load image two
image_background = Image.open('week7/images/sunset.jpg')
background_width, background_height = image_background.size
pixels_background = image_background.load()

#new image the same size
new_image = Image.new('RGB', image_green.size)

new_image_pixels = new_image.load()

#iterate through green image
for column in range(0, green_height):
    for point in range(0, green_width):
        (r,g,b) = pixels_green[point, column]
        (br, bg, bb) = pixels_background[point, column]
        if (r < 80 and g > 100 and b < 80):
            new_image_pixels[point, column] = (br, bg, bb)
        else: 
            new_image_pixels[point, column] = (r, g, b)

new_image.save('week7/images/newimage.jpg')


image_green.show()
image_background.show()
new_image.show()