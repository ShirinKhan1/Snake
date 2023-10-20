FPS = 60
TUPLE_AREA = (2, 5)
COUNT_AREA = TUPLE_AREA[0] * TUPLE_AREA[1]
icons = [
    'images/frankenstein.png',
    'images/pumpkin.png',
    'images/witch.png',
    'images/candy-bag.png']
colors = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0]]
numbers = list(range(1, 5))

# Цвета
cream = (253, 244, 227)
black = (0, 0, 0)

area_len_px, area_height_px = 271, 174

question = [1, 5, 10]
bool_question = lambda x: x in question


def tuples(count_area: tuple):  # write(y,x) не пытайся понять логику ;D
    list_areas = []
    start_y = 900 - 14 - area_height_px
    for i in range(count_area[0]):
        start_x = 30
        for j in range(count_area[1]):
            list_areas.append((start_x, start_y))
            start_x += area_len_px + 30
        start_y -= area_height_px + 20
    return list_areas


list_tuples = tuples(TUPLE_AREA)

if __name__ == '__main__':
    print(bool_question(2))
