from sunau import Au_read


def rectangle_area(height, width):
    area = height * width
    return area

def main():
    rectangle_height = float(input('Enter height of rectangle: '))
    rectangle_width = float(input('Enter width of rectangle: '))
    area = rectangle_area(rectangle_height, rectangle_width)

    print(f'The are of this rectangle is {area}')

main()