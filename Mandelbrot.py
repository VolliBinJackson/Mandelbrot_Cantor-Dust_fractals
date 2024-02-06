from PIL import Image

# Some notes:
# We have to consider the recursive formula  z_n+1 = z^2 + c with initial value z0 = 0. In each iteration
# we square the previous number and seed the result with the value of c, where c is a complex number.
# The main logic is basically we iterate through the picture and check if the point belongs
# to the mandelbrot set (in case if it remains bounded when running the recursive formula)
# Last but not least: You can change the colors of the resulting picture by manipulating RGB
# values in function indexToColor. Don't forget the modulo operation in case you want to.


# attributes
width = 1000
height = 1000
img = bytearray(width * height * 4)

xs = -2.1  # start position in x-axis
ys = -1.3  # start position in y-axis
dx = 2.8 / width  # added with xs (direction)
dy = 2.6 / height  # added with ys (direction)


# functions
def mandelbrot(complex_num):
    z = complex(0, 0)
    i = 0
    while i < 255 and abs(z) < 2:  # |z| >= 2  =>  |z| escapes towards infinity
        z = z*z + complex_num
        i += 1
    return i


def indexToColor(picture, index, i):
    picture[index+0] = i
    picture[index+1] = (i*5) % 256
    picture[index+2] = (i*10) % 256
    picture[index+3] = 255


# main
i = 0
for y in range(height):
    for x in range(width):
        complex_num = complex(xs + x * dx, ys + y * dy)
        colorIndex = mandelbrot(complex_num)
        indexToColor(img, i*4, colorIndex)
        i += 1

img_bytes = bytes(img)
image = Image.frombytes("RGBA", (width, height), img_bytes)
image.save("mandelbrot.png")

image.show()

