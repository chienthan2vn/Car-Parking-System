import streamlit as st
from service import da_service
import pandas as pd
import datetime

def register():
    csdl = da_service.da_service()

    st.header("Đăng kí xe gửi mới")
    col1, col2 = st.columns([2,2])
    with col1:
        name = st.text_input("Tên người dùng")
        cmt = st.text_input("Chứng minh thư")
        bsx = st.text_input("Biển số xe")
        type = st.text_input("Kiểu xe")
        button = st.button("Đăng kí")
    with col2:
        today = datetime.datetime.now()
        ndk = st.date_input("Ngày đăng kí", today)
        hsd = st.selectbox('Hạn sử dụng (G1: 1 tuần, G2: 1 tháng, G3: 1 năm)', ('G1', 'G2', 'G3', ''), index=3)
        if hsd != '':
            st.text_input("Giá tiền", str(int(csdl.cost(hsd))) + "k Đồng", disabled=True)
        else:
            st.text_input("Giá tiền", disabled=True)

    if button:
        if csdl.check_register('BSX', bsx) == 0 and name != "" and cmt != "" and bsx != "" and type != "" and hsd != "":
            csdl.register(bsx, name, cmt, ndk, hsd, type)
            st.success("Đăng kí thành công!")
        elif name == "" or cmt == "" or bsx == "" or type == "" or hsd == "":
            st.warning("Vui lòng nhập đầy đủ thông tin!")
        else:
            st.warning("Xe này đã đăng kí!")
