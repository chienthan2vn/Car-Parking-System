import streamlit as st
import main
from service import da_service

def login_page():
    if not is_logged_in():
        show_login_page()
    else:
        main.run()

def is_logged_in():
    return st.session_state.get('logged_in', False)

def show_login_page():
    col1, col2, col3 = st.columns([3,3,3])
    with col2:
        username = st.text_input("Tên người dùng", placeholder="username")
        password = st.text_input("Mật khẩu", type="password", placeholder="password")
        login_button = st.button("Đăng nhập")

    if login_button:
        csdl = da_service.da_service()
        if csdl.check_acc(user=username, pwd=password):
            st.success("Đăng nhập thành công!")
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Tên đăng nhập hoặc mật khẩu không đúng.")