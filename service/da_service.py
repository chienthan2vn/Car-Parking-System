import mysql.connector
import sys
import streamlit as st
sys.path.append("./")
from entities import account, car, cost, park

class da_service():
    def __init__(self):
        # Tạo đối tượng kết nối
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="btl_iot"
        )
        self.cursor = self.connection.cursor()

    def update_csdl(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="btl_iot"
        )
        self.cursor = self.connection.cursor()

    """
    ==========================ACCOUNT==========================
    get_acc: Lấy thông tin toàn bộ tài khoản
    check_acc: Kiểm tra thông tin tài khoản mật khẩu đúng không
    """
    def get_acc(self):
        acc_list = list()
        # Thực hiện truy vấn SQL
        self.cursor.execute("SELECT * FROM account")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        for row in results:
            user, pwd, pri = row
            sav = account.Account(user, pwd, pri)
            acc_list.append(sav)
        return acc_list
    
    def check_acc(self, user, pwd):
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"SELECT * FROM account WHERE user = '{user}' AND pwd = '{pwd}'")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        if results: return True
        return False
    
    """
    ==========================CAR==========================
    get_register: lấy dữ liệu xe đăng kí
    check_register: Kiểm tra xe đăng kí thông qua CMT hoặc Biển số xe
    register: Đăng kí xe gửi mới
    """
    def get_register(self):
        car_list = list()        
        # Thực hiện truy vấn SQL
        self.cursor.execute("SELECT * FROM car")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        for row in results:
            bsx, user, name, cmt, ndk, hsd, type = row
            sav = car.Car(bsx, user, name, cmt, ndk, hsd, type)
            car_list.append(sav)
        return car_list
    
    def check_register(self, method, value):
        car_list = list() 
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"SELECT * FROM car WHERE {method} = '{value}'")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        if results:
            for row in results:
                bsx, user, name, cmt, ndk, hsd, type = row
                car_list = car.Car(bsx, user, name, cmt, ndk, hsd, type)
                return car_list
        return 0
    
    def register(self, bsx, name, cmt, ndk, hsd, type):
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"SELECT * FROM car WHERE BSX = '{bsx}'")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        if results: return False
        else:
            self.cursor.execute(f"INSERT INTO car (BSX, User, Name, CMT, NDK, HSD, Type) VALUES ('{bsx}', 'admin', '{name}', '{cmt}', '{ndk}', '{hsd}', '{type}')")
            print(self.connection.commit())

    """
    ==========================Parking==========================
    get_new: Lấy dữ liệu mới nhất
    get_car: Lấy dữ liệu gửi xe
    get_car_day: Lấy dữ liệu gửi xe theo ngày
    parking: Lưu dữ liệu xe gửi vào
    car_still_parking: Dữ liệu xe còn trong bãi
    check_car: Tìm kiếm lịch sử gửi xe của 1 xe
    exits_parking: Lưu dữ liệu xe thoát khỏi bãi đậu -> đổi flag 0->1 và lưu giờ ra
    """
    def get_car_new(self, bsx, time, day, link_img):
        self.cursor.execute(f"SELECT COUNT(*) FROM car WHERE BSX = '{bsx}'")
        front = self.cursor.fetchall()
        if front[0][0] == 1:
            self.cursor.execute(f"SELECT Flag FROM park WHERE BSX='{bsx}' ORDER BY ID DESC LIMIT 1")
            results = self.cursor.fetchall()
            if not results or results[0][0] == 1:
                link_img = link_img + "in.jpg"
                self.cursor.execute(f"INSERT INTO park(BSX, DAY, Time_in, Link_IMG, Flag) VALUES ('{bsx}', '{day}', '{time}', '{link_img}', 0)")
                print(self.connection.commit())
                return link_img, 2
            elif results[0][0] == 0:
                link_img = link_img + "out.jpg"
                self.cursor.execute(f"UPDATE park SET Flag=1, Time_out='{time}', Link_IMG_out='{link_img}' WHERE Flag=0 AND BSX='{bsx}' ORDER BY ID DESC LIMIT 1")
                print(self.connection.commit())
                return link_img, 1          
        else:
            return 0, 0

    def get_new(self):
        car_list = list() 
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"SELECT * FROM park ORDER BY updated_at DESC LIMIT 1")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        for row in results:
            ID, bsx, day, timein, timeout, link_img, flag, link_img_out, update_at = row
            car_list = park.Park(ID, bsx, day, timein, timeout, link_img, link_img_out, flag)
        return car_list

    def get_car(self):
        car_list = list()        
        # Thực hiện truy vấn SQL
        self.cursor.execute("SELECT * FROM park")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        for row in results:
            ID, bsx, day, timein, timeout, link_img, flag, link_img_out, update_at = row
            sav = park.Park(ID, bsx, day, timein, timeout, link_img, link_img_out, flag)
            car_list.append(sav)
        return car_list
    
    def check_car(self, value):
        car_list = list() 
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"SELECT * FROM park WHERE BSX = '{value}'")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        for row in results:
            ID, bsx, day, timein, timeout, link_img, flag, link_img_out, update_at = row
            sav = park.Park(ID, bsx, day, timein, timeout, link_img, link_img_out, flag)
            car_list.append(sav)
        return car_list
    
    def get_car_day(self, day):
        car_list = list()        
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"SELECT * FROM park WHERE DATE_FORMAT(DAY, '%Y-%m-%d') = '{day}'")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        for row in results:
            ID, bsx, day, timein, timeout, link_img, flag, link_img_out, update_at = row
            sav = park.Park(ID, bsx, day, timein, timeout, link_img, link_img_out, flag)
            car_list.append(sav)
        return car_list
    
    def car_still_parking(self):
        car_list = list() 
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"SELECT * FROM park WHERE Flag = 0")
        results = self.cursor.fetchall()
        for row in results:
            ID, bsx, day, timein, timeout, link_img, flag, link_img_out, update_at = row
            sav = park.Park(ID, bsx, day, timein, timeout, link_img, link_img_out, flag)
            car_list.append(sav)
        return car_list

    def parking(self, bsx, day, timein, link_img, link_img_out):
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"INSERT INTO park (BSX, DAY, Time_in, Link_IMG, Flag, Link_IMG_out) VALUES ('{bsx}', '{day}', '{timein}', '{link_img}', '{link_img_out}' 0)")
        print(self.connection.commit())

    def exits_parking(self, bsx, timeout):
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"UPDATE park SET Time_out = '{timeout}', Flag = 1 WHERE BSX = '{bsx}' AND Flag = 0")
        print(self.connection.commit())
    
    """
    ==========================COST==========================
    get_cost: Lấy thông tin về giá của các gói gửi xe
    cost: Thông tin giá của 1 gói
    """
    def get_cost(self):
        cost_list = list()
        # Thực hiện truy vấn SQL
        self.cursor.execute("SELECT * FROM cost")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        for row in results:
            name, type, money = row
            sav = cost.Cost(name, type, money)
            cost_list.append(sav)
        return cost_list
    
    def cost(self, goi):
        # Thực hiện truy vấn SQL
        self.cursor.execute(f"SELECT Money FROM cost WHERE Name = '{goi}'")
        # Truy xuất dữ liệu
        results = self.cursor.fetchall()
        return results[0][0]