# Calculate how many buckets of paint you need to buy based on the square area of your wall

test_h = int(input('Enter height: '))
test_w = int(input('Enter width: '))
coverage_per_can = 5


def paint_calc(height, width, coverage):
    area = height * width
    num_of_cans = round((area / coverage), 2)

    if num_of_cans % 2 != 0:
        num_of_cans = int((num_of_cans // 1) + 1)

    # Alternative method to the awesomeness I did above there
    # import math
    # math.ceil(area)

    return num_of_cans


print(f'You will need {paint_calc(height=test_h, width=test_w, coverage=coverage_per_can)} cans of paint to paint '
      f'your wall')
