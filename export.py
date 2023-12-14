import streamlit as st
from service import da_service
import pandas as pd

def export():
    sv = da_service.da_service()
    op = ["Lấy dữ liệu xe đăng kí", "Lấy toàn bộ dữ liệu gửi xe", "Lấy dữ liệu gửi xe theo ngày", "Lấy thông tin về giá", ""]
    option1 = st.selectbox("Tìm kiếm thông tin", op, index=4)

    if option1 == op[0]:
        st.header("Lấy dữ liệu xe đăng kí")
        df = pd.DataFrame(columns=['bsx', 'user', 'name', 'cmt', 'ndk', 'hsd', 'type'])
        rs = sv.get_register()
        for r in rs:
            df.loc[len(df.index)] = [r.bsx, r.user, r.name, r.cmt, r.ndk, r.hsd, r.type]
        st.table(df)
        df = df.to_csv().encode('utf-8')
        st.download_button(label="Download",data=df,file_name='car_register.csv')

    elif option1 == op[1]:
        st.header("Lấy toàn bộ dữ liệu gửi xe")
        df = pd.DataFrame(columns=['bsx', 'day', 'timein', 'timeout', 'link_img'])
        rs = sv.get_car()
        for r in rs:
            df.loc[len(df.index)] = [r.bsx, r.day, r.timein, r.timeout, r.link_img]

        df['timein'] = df['timein'].astype(str)
        df['timeout'] = df['timeout'].astype(str)
        st.table(df)
        df = df.to_csv().encode('utf-8')
        st.download_button(label="Download",data=df,file_name='history_all_car.csv')

    elif option1 == op[2]:
        st.header("Lấy dữ liệu gửi xe theo ngày")
        df = pd.DataFrame(columns=['bsx', 'day', 'timein', 'timeout', 'link_img'])
        day = st.date_input("Chọn ngày")
        rs = sv.get_car_day(day)
        for r in rs:
            df.loc[len(df.index)] = [r.bsx, r.day, r.timein, r.timeout, r.link_img]

        df['timein'] = df['timein'].astype(str)
        df['timeout'] = df['timeout'].astype(str)
        st.table(df)
        df = df.to_csv().encode('utf-8')
        st.download_button(label="Download",data=df,file_name='history_' + str(day) + '_car.csv')

    elif option1 == op[3]:
        st.header("Lấy thông tin về giá gửi xe")
        df = pd.DataFrame(columns=['name', 'type', 'money'])
        rs = sv.get_cost()
        for r in rs:
            df.loc[len(df.index)] = [r.name, r.type, r.money]

        st.table(df)
        df = df.to_csv().encode('utf-8')
        st.download_button(label="Download",data=df,file_name='cost_car.csv')