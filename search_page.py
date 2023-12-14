import streamlit as st
from service import da_service
import pandas as pd

def search_page():
    sv = da_service.da_service()
    options = ["Xe đăng kí", "Xe gửi", "Xe còn trong bãi", ""]
    option1 = st.selectbox("Tìm kiếm thông tin", options, index=3)
    if option1 == "Xe đăng kí":
        st.header("Tìm kiếm thông tin xe thông qua biển số xe hoặc CMT")
        option2 = st.selectbox("Tìm kiếm thông tin", ["Biển số xe", "CMT", ""], index=2)
        if option2 == "Biển số xe":
            bsx = st.text_input("Nhập biển số xe")
            button = st.button("Tìm kiếm")
            if button:
                rs = sv.check_register("BSX", bsx)
                if rs == 0:
                    st.warning("Không tìm thấy thông tin")
                else:
                    bsx, user, name, cmt, ndk, hsd, type = rs.bsx, rs.user, rs.name, rs.cmt, rs.ndk, rs.hsd, rs.type
                    col1, col2 = st.columns(2)
                    with col1:
                        st.text_input("Biển số xe", bsx)
                        st.text_input("Tên chủ xe", name)
                        st.text_input("Chứng minh thư", cmt)
                    with col2:
                        st.text_input("Kiểu xe", type)
                        st.text_input("Ngày đăng kí", ndk)
                        st.text_input("Gói đăng kí", hsd)
        if option2 == "CMT":
            cmt = st.text_input("Nhập CMT")
            button = st.button("Tìm kiếm")
            if button:
                rs = sv.check_register("CMT", cmt)
                if rs == 0:
                    st.warning("Không tìm thấy thông tin")
                else:
                    bsx, user, name, cmt, ndk, hsd, type = rs.bsx, rs.user, rs.name, rs.cmt, rs.ndk, rs.hsd, rs.type
                    col1, col2 = st.columns(2)
                    with col1:
                        st.text_input("Biển số xe", bsx)
                        st.text_input("Tên chủ xe", name)
                        st.text_input("Chứng minh thư", cmt)
                    with col2:
                        st.text_input("Kiểu xe", type)
                        st.text_input("Ngày đăng kí", ndk)
                        st.text_input("Gói đăng kí", hsd)

    elif option1 == "Xe gửi":
        st.header("Tìm kiếm lịch sử gửi xe của xe")
        bsx = st.text_input("Nhập biển số xe")
        button = st.button("Tìm kiếm")
        if button:
            rs = sv.check_car(bsx)
            if rs:
                day, timein, timeout = [], [], []
                df = pd.DataFrame(columns=["Ngày gửi", "Thời gian vào", "Thời gian ra"])
                for r in rs:
                    day.append(r.day)
                    timein.append(r.timein)
                    timeout.append(r.timeout)
                df["Ngày gửi"] = day
                df["Thời gian vào"] = timein
                df["Thời gian ra"] = timeout

                df["Ngày gửi"] = df["Ngày gửi"].astype(str)
                df["Thời gian vào"] = df["Thời gian vào"].astype(str)
                df["Thời gian ra"] = df["Thời gian ra"].astype(str)
                st.table(df)
            else:
                st.warning("Không tìm thấy thông tin")

    elif option1 == "Xe còn trong bãi":
        st.header("Tìm kiếm các xe còn trong bãi")
        rs = sv.car_still_parking()
        if rs:
            bsx, day, timein = [], [], []
            df = pd.DataFrame(columns=["Biển số xe", "Ngày gửi", "Thời gian vào"])
            for r in rs:
                bsx.append(r.bsx)
                day.append(r.day)
                timein.append(r.timein)

            df["Biển số xe"] = bsx
            df["Ngày gửi"] = day
            df["Thời gian vào"] = timein
            
            df["Biển số xe"] = df["Biển số xe"].astype(str)
            df["Ngày gửi"] = df["Ngày gửi"].astype(str)
            df["Thời gian vào"] = df["Thời gian vào"].astype(str)
            st.table(df)
        else:
            st.warning("Không có xe gửi trong bãi")

