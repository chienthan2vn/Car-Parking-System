import streamlit as st
from streamlit_option_menu import option_menu
import main_page, about_page, search_page, export, register
import time

st.set_page_config(page_title="Smart Parking System", layout="wide")

def run():
    options = ['Trang chủ','Đăng kí mới','Tìm kiếm','Xuất báo cáo','Đăng xuất','Thông tin phần mềm']
    with st.sidebar:        
        app = option_menu(
            menu_title='Menu',
            options=options,
            icons=['menu-up','sign-intersection','search','cloud-download','reply','info-circle-fill'],
            menu_icon='menu-button-wide',
            default_index=0,
            styles={
                "container": {"padding": "5!important","background-color":'black'},
                "icon": {"color": "white", "font-size": "23px"}, 
                "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},}
            )

    if app == "Đăng xuất":
        st.warning('This is a warning', icon="⚠️")
    if app == "Trang chủ":
        main_page.main_page()
        time.sleep(20)
        st.experimental_rerun()
    if app == "Đăng kí mới":
        register.register()
    if app == "Tìm kiếm":
        search_page.search_page()
    if app == "Xuất báo cáo":
        export.export()
    if app == "Thông tin phần mềm":
        about_page.about_page()
