import cv2
from os import listdir

src = "./train/"

for im in listdir(src):
    link = src + im
    img = cv2.imread(link)
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(link, img)