def rgb_to_gray(rgb_list):
    return [(r + g + b) // 3 for r, g, b in rgb_list]

rgb_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255), (0, 0, 0)]
gray_list = [(gray, gray, gray) for r, g, b in rgb_list for gray in [rgb_to_gray([(r, g, b)])[0]]]
print(gray_list)
