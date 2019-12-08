import utils
from PIL import Image

data = utils.get_day(2019, 8)
data = data[0]

WIDTH = 25
HEIGHT = 6

BLACK = '0'
WHITE = '1'
TRANSPARENT = '2'

def data_to_image(data):
    image = []
    layers = len(data) // (WIDTH*HEIGHT)
    for l in range(layers):
        layer = []
        for row in range(HEIGHT):
            layer.append(data[(l*HEIGHT*WIDTH) + (row*WIDTH): (l*HEIGHT*WIDTH)+(row*WIDTH)+WIDTH])

        image.append(layer)

    check = list(map(lambda x: ''.join(x), image))
    check = ''.join(check)
    assert(check == data)
    return image

def process(image):
    image = image.copy()
    output = [[0 for x in range(25)] for x in range(6)]
    for layer in reversed(image):
        for row_index, row in enumerate(layer):
            for col_index, pixel in enumerate(row):
                if pixel != TRANSPARENT:
                    output[row_index][col_index] = pixel

    output_as_int = []
    for row in output:
        output_as_int.append(list(map(int, row)))
    output_as_int = [y for x in output_as_int for y in x]
    return output_as_int

image = data_to_image(data)

#layer index, number of zeroes
fewest_zeroes_layer = (0, 10000)
for l in range(len(image)):
    layer_as_one = ''.join(image[l])
    number_of_zeroes = len(list(filter(lambda x: x=='0', layer_as_one)))
    if number_of_zeroes < fewest_zeroes_layer[1]:
        fewest_zeroes_layer = (l, number_of_zeroes)

number_of_ones = len(list(filter(lambda x: x=='1', ''.join(image[fewest_zeroes_layer[0]]))))
number_of_twos = len(list(filter(lambda x: x=='2', ''.join(image[fewest_zeroes_layer[0]]))))
utils.print_part_1(number_of_ones*number_of_twos)

pixels = process(image)
img = Image.new('1', (WIDTH, HEIGHT))
img.putdata(pixels)
img.save('day8.tif')
