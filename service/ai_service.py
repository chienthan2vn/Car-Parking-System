from ultralytics import YOLO
import cv2
from datetime import datetime
import easyocr
import sys
sys.path.append("./")
from service import da_service

class ai_service:
    def __init__(self):
        self.model = YOLO('./model/best.pt')
        self.reader = easyocr.Reader(['en'])
        self.csdl = da_service.da_service()

    def detect(self, img):
        # img = cv2.imread(img)
        results = self.model.predict(img, conf=0.7)
        boxs = results[0].boxes.data
        for i in range(len(boxs)):
            xmin, ymin, xmax, ymax, _, label = int(boxs[i][0]), int(boxs[i][1]), int(boxs[i][2]), int(boxs[i][3]), int(boxs[i][4]), int(boxs[i][5])
            # cv2.putText(img, str(label), (xmin - 10, ymin - 10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (232, 71, 71),2)
            # cv2.rectangle(img, (xmin, ymin),(xmax, ymax),(232, 71, 71),2)
            print(ymin, ymax, xmin, xmax)
            img = img[ymin:ymax,xmin:xmax]
        return img

    def process(self, img):
        img_new = self.detect(img)

        text = self.reader.readtext(img_new, detail = 0)
        bsx = "-".join(text)
        bsx = bsx.replace(".", "")
        print("BSX:", bsx)
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time_csdl = time.split(' ')
        time_img = time.replace('-', '_').replace(' ', '_').replace(':', '_')
        name_img = "./img/" + bsx + '_' + time_img
        new_link, trans = self.csdl.get_car_new(bsx, time_csdl[1], time_csdl[0], name_img)

        """
        trans == 0, xe khong duoc phep gui
        trans == 1, xe di ra
        trans == 2, xe di vao
        """ 
        if trans == 0:
            return 0
        elif trans == 1:
            cv2.imwrite(new_link, img)
            return 1
        elif trans == 2:
            cv2.imwrite(new_link, img)
            return 2

# cap = cv2.VideoCapture(0)
# test = ai_service()
# while True:
#     _, frame = cap.read()
#     frame = test.detect(frame)
#     cv2.imshow('image', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# image = cv2.imread('./train/train/img_1710.jpg')
# image = test.detect(image)
# cv2.imshow("hehe", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()