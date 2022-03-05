## 使用方法：首先更改保存路径信息（L258-L279），然后通过注释不同行来获得相应形状文件。

import numpy as np
import cv2
import random
import math

# ---------------------------------------------------------------------- #
#                              Add Noise
# ---------------------------------------------------------------------- #
## sp noise
# def sp_noise(image,prob):
#   '''
#   添加椒盐噪声
#   prob:噪声比例
#   '''
#   output = np.zeros(image.shape,np.uint8)
#   thres = 1 - prob
#   for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#       rdn = random.random()
#       if rdn < prob:
#         output[i][j] = 0
#       elif rdn > thres:
#         output[i][j] = 255
#       else:
#         output[i][j] = image[i][j]
#   return output
#
# ## Gaussion noise
# def gasuss_noise(image, mean=0, var=0.001):
#   '''
#     添加高斯噪声
#     mean : 均值
#     var : 方差
#   '''
#   image = np.array(image/255, dtype=float)
#   noise = np.random.normal(mean, var ** 0.5, image.shape)
#   out = image + noise
#   if out.min() < 0:
#     low_clip = -1.
#   else:
#     low_clip = 0.
#   out = np.clip(out, low_clip, 1.0)
#   out = np.uint8(out*255)
#   # cv.imshow("gasuss", out)
#   return out

# ---------------------------------------------------------------------- #
#                          5-pts star function
# ---------------------------------------------------------------------- #
def get_point(angle, d, base):
  angle = angle / 180.0 * math.pi
  _x, _y = math.cos(angle) * d, math.sin(angle) * d
  return [base[0] + _x, base[1] - _y]

# ---------------------------------------------------------------------- #
#                          Generize Background
# ---------------------------------------------------------------------- #
num_of_img = 150

for i in range(num_of_img):

  if i <= num_of_img/2:
    # Create a black image
    # img = np.zeros((224, 224, 3), np.uint8)
    img = np.random.randint(0, 10,(224, 224, 3), np.uint8)

  else:
    # Create a white image
    img = np.random.randint(245, 255,(224, 224, 3), np.uint8)

# ---------------------------------------------------------------------- #
#                       Generize Random Parameter
# ---------------------------------------------------------------------- #

  ## Color
  color_Red = np.random.randint(0, 255)
  color_Green = np.random.randint(0, 255)
  color_Blue = np.random.randint(0, 255)

  ## Width of lines
  # width_of_line = np.random.randint(-15, 15)

  ## Rectangle
  # top_right_point   = np.random.randint(1, 112, size=2)
  # bottom_left_point = np.random.randint(112, 224, size=2)

  ## Circle
  # center_point = np.random.randint(56, 168, size=2)
  # radius = np.random.randint(14, 56)

  # Ellipse
  # center_point = np.random.randint(56, 168, size=2)
  # spin_angel = np.random.randint(0, 360)
  # axesLength_length = np.random.randint(70, 84)
  # axesLength_width = np.random.randint(14, 56)

  # Triangle
  # pts_tri = np.random.randint(28, 196, size=(3,2))
  # # pts = np.array([[10,5],[20,30],[70,20]], np.int32)
  # pts_tri = pts_tri.reshape((-1,1,2))
  # WoL_Triangle = np.random.randint(1, 15)

  ## Star
  # pts_star = []
  # center_point = np.random.randint(56, 168, size=2)
  # start_angle = np.random.randint(0, 360)
  # length = np.random.randint(28, 112)
  # y = length / (math.cos(0.2 * math.pi) + math.sin(0.2 * math.pi) / math.tan(0.1 * math.pi))
  #
  # for j in range(5):
  #   _x, _y = math.cos(start_angle), math.sin(start_angle)
  #   pts_star.append(get_point(start_angle, length, center_point))
  #   start_angle -= 36
  #   pts_star.append(get_point(start_angle, y, center_point))
  #   start_angle -= 36
  #   pass
  #
  # WoL_Triangle = np.random.randint(1, 15)
  # pts_star = np.array([pts_star], np.int32)

  ## diamond
  # pts_diamond = []
  # center_point = np.random.randint(56, 168, size=2)
  # start_angle = np.random.randint(0, 180)
  # x = np.random.randint(28, 56)
  # y = np.random.randint(56, 112)
  #
  # for j in range(2):
  #   pts_diamond.append(get_point(start_angle, x, center_point))
  #   start_angle = start_angle + 90
  #   pts_diamond.append(get_point(start_angle, y, center_point))
  #   start_angle = start_angle + 90
  #   pass
  #
  # WoL_Triangle = np.random.randint(1, 15)
  # pts_diamond = np.array([pts_diamond], np.int32)

  ## Pentagon
  # pts_pent = []
  # center_point = np.random.randint(56, 168, size=2)
  # start_angle = np.random.randint(0, 180)
  # x = np.random.randint(28, 112)
  #
  # for j in range(6):
  #   pts_pent.append(get_point(start_angle, x, center_point))
  #   start_angle = start_angle + 72
  #   pass
  #
  # WoL_Triangle = np.random.randint(1, 15)
  # pts_pent = np.array([pts_pent], np.int32)

  ## Hexagon
  # pts_hex = []
  # center_point = np.random.randint(56, 168, size=2)
  # start_angle = np.random.randint(0, 180)
  # x = np.random.randint(28, 112)
  #
  # for j in range(6):
  #   pts_hex.append(get_point(start_angle, x, center_point))
  #   start_angle = start_angle + 60
  #   pass
  #
  # WoL_Triangle = np.random.randint(1, 15)
  # pts_hex = np.array([pts_hex], np.int32)

  ## Octagon
  # pts_oct = []
  # center_point = np.random.randint(56, 168, size=2)
  # start_angle = np.random.randint(0, 180)
  # x = np.random.randint(28, 112)
  #
  # for j in range(8):
  #   pts_oct.append(get_point(start_angle, x, center_point))
  #   start_angle = start_angle + 45
  #   pass
  #
  # WoL_Triangle = np.random.randint(1, 15)
  # pts_oct = np.array([pts_oct], np.int32)

  ## Trapezoid
  pts_trap = []
  center_point = np.random.randint(28, 168, size=2)
  start_angle_a = np.random.randint(0, 45)
  start_angle_b = np.random.randint(45, 90)
  x = np.random.randint(70, 112)
  y = np.random.randint(28, 56)

  pts_trap.append(center_point)
  pts_trap.append(get_point(start_angle_a, x, center_point))
  pts_trap.append(get_point(start_angle_b, y, center_point))
  point_tmp = get_point(start_angle_b, y, center_point)
  pts_trap.append(get_point((start_angle_a), y, point_tmp))
  WoL_Triangle = np.random.randint(1, 15)
  pts_trap = np.array([sorted(pts_trap, key=lambda x: x[0])], np.int32)
# ---------------------------------------------------------------------- #
#                          Generize Shape
# ---------------------------------------------------------------------- #

# Draw a diagonal blue line with thickness of 5 px
# cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 15)

  # Rectangle
  # cv2.rectangle(img,top_right_point,bottom_left_point,(color_Red,color_Green,color_Blue),width_of_line)

  # Circle
  # cv2.circle(img,center_point,radius,(color_Red,color_Green,color_Blue),width_of_line)

  # Ellipse
  # cv2.ellipse(img,center_point,(axesLength_length,axesLength_width),spin_angel,0,360,(color_Red,color_Green,color_Blue),width_of_line)

  if i % 2 == 0:
    ## Triangle
    # cv2.polylines(img,[pts_tri],True,(color_Red,color_Green,color_Blue),WoL_Triangle)

    # Star
    # cv2.polylines(img,[pts_star],True,(color_Red,color_Green,color_Blue),WoL_Triangle)

    # Diamond
    # cv2.polylines(img,[pts_diamond],True,(color_Red,color_Green,color_Blue),WoL_Triangle)

    # Pentagon
    # cv2.polylines(img, [pts_pent], True, (color_Red, color_Green, color_Blue), WoL_Triangle)

    # Hexagon
    # cv2.polylines(img,[pts_hex],True,(color_Red,color_Green,color_Blue),WoL_Triangle)

    # Octagon
    # cv2.polylines(img, [pts_oct], True, (color_Red, color_Green, color_Blue), WoL_Triangle)

    # Trapezoid
    cv2.polylines(img, [pts_trap], True, (color_Red, color_Green, color_Blue), WoL_Triangle)
  else:
    ## Triangle
    # cv2.fillPoly(img,[pts_tri], (color_Red,color_Green,color_Blue))

    # Star
    # cv2.fillPoly(img,[pts_star], (color_Red,color_Green,color_Blue))

    # Diamond
    # cv2.fillPoly(img,[pts_diamond], (color_Red,color_Green,color_Blue))

    # Pentagon
    # cv2.fillPoly(img,[pts_pent], (color_Red,color_Green,color_Blue))

    # Hexagon
    # cv2.fillPoly(img,[pts_hex], (color_Red,color_Green,color_Blue))

    # Octagon
    # cv2.fillPoly(img,[pts_oct], (color_Red,color_Green,color_Blue))

    # Trapezoid
    cv2.fillPoly(img, [pts_trap], (color_Red,color_Green,color_Blue))
# ---------------------------------------------------------------------- #
#                              Save Shape(.png)
# ---------------------------------------------------------------------- #
  # img = sp_noise(img, prob=0.01)
  # cv2.imwrite('./shape/rectangle/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/circle/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/ellipse/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/triangle/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/star/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/diamond/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/pentagon/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/hexagon/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/octagon/' + str(i) + '.png', img)
  cv2.imwrite('./shape/trapezoid/' + str(i) + '.png', img)

  # cv2.imwrite('./shape/rectangle_val/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/circle_val/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/ellipse_val/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/triangle_val/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/star_val/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/diamond_val/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/pentagon_val/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/hexagon_val/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/octagon_val/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/trapezoid_val/' + str(i) + '.png', img)

# ---------------------------------------------------------------------- #
#                         Show Generized Shape
# ---------------------------------------------------------------------- #
# img = sp_noise(img, prob=0.01)
# # img = gasuss_noise(img, mean=0, var=0.0001)
#
# cv2.imshow('img', img)
# k = cv2.waitKey(0)
# # cv2.destroyAllWindows()
# #
# if k == 27:         # 按下esc时，退出
#     cv2.destroyAllWindows()
# elif k == ord('s'): # 按下s键时保存并退出
#     cv2.imwrite('test.png',img)
#     cv2.destroyAllWindows()
