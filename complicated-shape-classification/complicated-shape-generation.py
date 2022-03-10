import cv2
import numpy as np
import random

# img = np.zeros((224, 224, 3), np.uint8)

def rectangle(img, color_Red,color_Green,color_Blue, width_of_line):
    top_right_point = np.random.randint(1, 112, size=2)
    bottom_left_point = np.random.randint(112, 224, size=2)
    return cv2.rectangle(img, top_right_point, bottom_left_point, (color_Red, color_Green, color_Blue), width_of_line)

def circle(img, color_Red,color_Green,color_Blue, width_of_line):
    center_point_circle = np.random.randint(56, 168, size=2)
    radius = np.random.randint(14, 56)
    return cv2.circle(img,center_point_circle,radius,(color_Red,color_Green,color_Blue),width_of_line)

def ellipse(img, color_Red,color_Green,color_Blue, width_of_line):
    center_point_ellipse = np.random.randint(56, 168, size=2)
    spin_angel = np.random.randint(0, 360)
    axesLength_length = np.random.randint(70, 84)
    axesLength_width = np.random.randint(14, 56)
    return cv2.ellipse(img,center_point_ellipse,(axesLength_length,axesLength_width),spin_angel,0,360,(color_Red,color_Green,color_Blue),width_of_line)

def triangle(img, color_Red,color_Green,color_Blue, width_of_line):
    pts_tri = np.random.randint(28, 196, size=(3, 2))
    pts_tri = pts_tri.reshape((-1, 1, 2))
    return cv2.polylines(img,[pts_tri],True,(color_Red,color_Green,color_Blue),width_of_line)

# rectangle(img, color_Red, color_Green, color_Blue, width_of_line)
# circle(img, color_Red, color_Green, color_Blue, width_of_line)
# ellipse(img, color_Red, color_Green, color_Blue, width_of_line)
# triangle(img, color_Red, color_Green, color_Blue, width_of_line)

# -------------------------------------------------------------------------------------------- #
#                                    随机组合形状生成
# -------------------------------------------------------------------------------------------- #
num_of_img = 160
for num in range(num_of_img):
    if num <= num_of_img / 2:
        # Create a black image
        # img = np.zeros((224, 224, 3), np.uint8)
        img = np.random.randint(0, 10, (224, 224, 3), np.uint8)

    else:
        # Create a white image
        img = np.random.randint(245, 255, (224, 224, 3), np.uint8)

    ## Color
    color_Red = np.random.randint(0, 255)
    color_Green = np.random.randint(0, 255)
    color_Blue = np.random.randint(0, 255)

    ## Width of lines
    width_of_line = np.random.randint(0, 10)
# ----------------------------------------1个形状---------------------------------------------------- #
    single_shape_num = np.random.randint(2, 5)
    for i in range(single_shape_num):
        ## rectangle
        # rectangle(img, color_Red,color_Green,color_Blue, width_of_line)

        ## circle
        # circle(img, color_Red,color_Green,color_Blue, width_of_line)

        ## ellipse
        # ellipse(img, color_Red,color_Green,color_Blue, width_of_line)

        ## triangle
        triangle(img, color_Red,color_Green,color_Blue, width_of_line)

    # cv2.imwrite('./shape_task2/rectangle/rect_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/circle/cir_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/ellipse/elli_' + str(num) + '.png', img)
    cv2.imwrite('./shape_task2/triangle/tri_' + str(num) + '.png', img)

# ----------------------------------------2个形状---------------------------------------------------- #
    ## 1st Shape
    # shape_num1 = np.random.randint(1, 3)
    # for i in range(shape_num1):
        # rectangle(img, color_Red,color_Green,color_Blue, width_of_line)
        # circle(img, color_Red,color_Green,color_Blue, width_of_line)
        # ellipse(img, color_Red,color_Green,color_Blue, width_of_line)
        # triangle(img, color_Red,color_Green,color_Blue, width_of_line)

    ## 2st Shape
    # shape_num2 = np.random.randint(1, 3)
    # for i in range(shape_num2):
        # circle(img, color_Red,color_Green,color_Blue, width_of_line)
        # ellipse(img, color_Red,color_Green,color_Blue, width_of_line)
        # triangle(img, color_Red,color_Green,color_Blue, width_of_line)

    # cv2.imwrite('./shape_task2/rect-cir/rc_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/rect-elli/re_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/rect-tri/rt_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/cir-elli/ce_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/cir-tri/ct_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/elli-tri/et_' + str(num) + '.png', img)

# ----------------------------------------3个形状---------------------------------------------------- #
    ## 1st Shape
    # shape_num1 = np.random.randint(1, 3)
    # for i in range(shape_num1):
        # rectangle(img, color_Red,color_Green,color_Blue, width_of_line)
        # circle(img, color_Red,color_Green,color_Blue, width_of_line)
        # ellipse(img, color_Red,color_Green,color_Blue, width_of_line)
        # triangle(img, color_Red,color_Green,color_Blue, width_of_line)

    ## 2st Shape
    # shape_num2 = np.random.randint(1, 3)
    # for i in range(shape_num2):
        # circle(img, color_Red,color_Green,color_Blue, width_of_line)
        # ellipse(img, color_Red,color_Green,color_Blue, width_of_line)
        # triangle(img, color_Red,color_Green,color_Blue, width_of_line)

    ## 3st Shape
    # shape_num3 = np.random.randint(1, 3)
    # for i in range(shape_num3):
        # ellipse(img, color_Red,color_Green,color_Blue, width_of_line)
        # triangle(img, color_Red,color_Green,color_Blue, width_of_line)

    # cv2.imwrite('./shape_task2/rect-cir-elli/rce_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/rect-elli-tri/ret_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/rect-cir-tri/rct_' + str(num) + '.png', img)
    # cv2.imwrite('./shape_task2/cir-elli-tri/cet_' + str(num) + '.png', img)
# ----------------------------------------4个形状---------------------------------------------------- #
#     ## 1st Shape
#     shape_num1 = np.random.randint(1, 3)
#     for i in range(shape_num1):
#         rectangle(img, color_Red,color_Green,color_Blue, width_of_line)
#
#     ## 2st Shape
#     shape_num2 = np.random.randint(1, 3)
#     for i in range(shape_num2):
#         circle(img, color_Red,color_Green,color_Blue, width_of_line)
#
#     ## 3st Shape
#     shape_num3 = np.random.randint(1, 3)
#     for i in range(shape_num3):
#         ellipse(img, color_Red,color_Green,color_Blue, width_of_line)
#
#     ## 4st Shape
#     shape_num4 = np.random.randint(1, 3)
#     for i in range(shape_num4):
#         triangle(img, color_Red,color_Green,color_Blue, width_of_line)
#
#     cv2.imwrite('./shape_task2/rect-cir-elli-tri/4shape_' + str(num) + '.png', img)

# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
