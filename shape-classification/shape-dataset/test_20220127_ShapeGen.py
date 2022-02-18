## Time: 2022.01.29
## Author: DYL
## Description: 生成任意数量，任意形状（矩形，圆形，椭圆，三角形）图片(.jpg/.png)数据集

import numpy as np
import cv2
import random

# ---------------------------------------------------------------------- #
#                              Add Noise
# ---------------------------------------------------------------------- #
## sp noise
def sp_noise(image,prob):
  '''
  添加椒盐噪声
  prob:噪声比例
  '''
  output = np.zeros(image.shape,np.uint8)
  thres = 1 - prob
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      rdn = random.random()
      if rdn < prob:
        output[i][j] = 0
      elif rdn > thres:
        output[i][j] = 255
      else:
        output[i][j] = image[i][j]
  return output

## Gaussion noise
def gasuss_noise(image, mean=0, var=0.001):
  '''
    添加高斯噪声
    mean : 均值
    var : 方差
  '''
  image = np.array(image/255, dtype=float)
  noise = np.random.normal(mean, var ** 0.5, image.shape)
  out = image + noise
  if out.min() < 0:
    low_clip = -1.
  else:
    low_clip = 0.
  out = np.clip(out, low_clip, 1.0)
  out = np.uint8(out*255)
  # cv.imshow("gasuss", out)
  return out

# ---------------------------------------------------------------------- #
#                          Generize Background
# ---------------------------------------------------------------------- #
num_of_img = 50

for i in range(num_of_img):

  if i <= num_of_img/2:
    # Create a black image
    img = np.zeros((224, 224, 3), np.uint8)
  else:
    # Create a white image
    img = np.random.randint(250, 255,(224, 224, 3), np.uint8)

# ---------------------------------------------------------------------- #
#                       Generize Random Parameter
# ---------------------------------------------------------------------- #

  ## Color
  color_Red = np.random.randint(0, 255)
  color_Green = np.random.randint(0, 255)
  color_Blue = np.random.randint(0, 255)

  ## Width of lines
  width_of_line = np.random.randint(-15, 15)

  ## Rectangle
  top_right_point   = np.random.randint(1, 112, size=2)
  bottom_left_point = np.random.randint(112, 224, size=2)

  ## Circle
  # center_point = np.random.randint(56, 168, size=2)
  # radius = np.random.randint(14, 56)

  # Ellipse
  # center_point = np.random.randint(56, 168, size=2)
  # spin_angel = np.random.randint(0, 360)
  # axesLength_length = np.random.randint(70, 84)
  # axesLength_width = np.random.randint(14, 56)

  ## Triangle
  # pts = np.random.randint(28, 196, size=(3,2))
  # # pts = np.array([[10,5],[20,30],[70,20]], np.int32)
  # pts = pts.reshape((-1,1,2))
  # WoL_Triangle = np.random.randint(1, 15)

# ---------------------------------------------------------------------- #
#                          Generize Shape
# ---------------------------------------------------------------------- #

# Draw a diagonal blue line with thickness of 5 px
# cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 15)

  # Rectangle
  cv2.rectangle(img,top_right_point,bottom_left_point,(color_Red,color_Green,color_Blue),width_of_line)

  # # Circle
  # cv2.circle(img,center_point,radius,(color_Red,color_Green,color_Blue),width_of_line)
  #
  # # Ellipse
  # cv2.ellipse(img,center_point,(axesLength_length,axesLength_width),spin_angel,0,360,(color_Red,color_Green,color_Blue),width_of_line)
  #
  # # Triangle
  # cv2.polylines(img,[pts],True,(color_Red,color_Green,color_Blue),WoL_Triangle)

# ---------------------------------------------------------------------- #
#                              Save Shape(.png)
# ---------------------------------------------------------------------- #
  # img = sp_noise(img, prob=0.01)
  cv2.imwrite('./shape/rectangle/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/circle/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/ellipse/' + str(i) + '.png', img)
  # cv2.imwrite('./shape/triangle/' + str(i) + '.png', img)
# ---------------------------------------------------------------------- #
#                         Show Generized Shape
# ---------------------------------------------------------------------- #
# img = sp_noise(img, prob=0.01)
# # img = gasuss_noise(img, mean=0, var=0.0001)
#
# cv2.imshow('img', img)
# k = cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# if k == 27:         # 按下esc时，退出
#     cv2.destroyAllWindows()
# elif k == ord('s'): # 按下s键时保存并退出
#     cv2.imwrite('test.png',img)
#     cv2.destroyAllWindows()