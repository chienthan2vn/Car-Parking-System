import streamlit as st
from streamlit_option_menu import option_menu
from service import da_service, ai_service
from PIL import Image
import cv2
import time

csdl = da_service.da_service()
ai = ai_service.ai_service()
cap = cv2.VideoCapture("tcp://192.168.213.69:5000")
bsx, day, time_in, time_out, link_img, link_img_out = None, None, None, None, None, None

def main_page():
    csdl.update_csdl()
    new = csdl.get_new()
    bsx, day, time_in, time_out, link_img, link_img_out = str(new.bsx), str(new.day), str(new.timein), str(new.timeout), str(new.link_img), str(new.link_img_out)
    col1, col2, col3 = st.columns([2,2,6])
    with col1:
        st.text_input("Biển số xe", bsx, disabled=True)
        st.text_input("Ngày gửi xe", day, disabled=True)
        st.header("Ảnh xe vào")
        if link_img != 'None':
            image = Image.open(link_img)
            st.image(image)
    with col2:
        st.text_input("Thời gian vào", time_in, disabled=True)
        st.text_input("Thời gian ra", time_out, disabled=True)
        st.header("Ảnh xe ra")
        if link_img_out != 'None':
            image = Image.open(link_img_out)
            st.image(image)
    with col3:
        FRAME_WINDOW = st.image([], width=820)
        delay = 1
        while True:
            _, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

            with open("./trans/check.txt", mode='r') as f:
                data = f.read()

            if data == '1':
                print(delay)
                delay += 1
                if delay == 200:
                    delay = 0
                    flag = ai.process(frame)
                    with open("./trans/re.txt", mode='w') as f:
                        f.write(str(flag))
                    st.experimental_rerun()
            else:
                delay = 0
            FRAME_WINDOW.image(frame)

    #Số lượng xe vào, ra, xe còn trong bãi, đề xuất vị trí
        