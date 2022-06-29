import tkinter as tk
from view import *


# 1.创建菜单栏
class MenuPage(object):
    def __init__(self, master=None):
        """
        初始化方法
        :param master:界面对象
        """
        self.menu_root = master
        self.menu_root.geometry("600x400")

        # 初始化各个Frame容器
        self.input_frame = InputFrame(self.menu_root)
        self.query_frame = QueryFrame(self.menu_root)
        self.delete_frame = DeleteFrame(self.menu_root)
        self.upate_frame = UpdateFrame(self.menu_root)
        self.about_frame = AboutMe(self.menu_root)
        self.input_frame.pack()
        # 创建菜单栏
        self.create_menu()

    def create_menu(self):
        """
        创建菜单栏
        :return:
        """
        # 1.创建Menu对象，传入父容器
        menubar = tk.Menu(self.menu_root)
        # 2.添加 录入/查询...
        menubar.add_command(label="录入", command=self.input_data)
        menubar.add_command(label="查询", command=self.query_data)
        menubar.add_command(label="删除", command=self.delete_data)
        menubar.add_command(label="修改", command=self.update_data)
        menubar.add_command(label="关于", command=self.about_me)
        # 3.设置菜单栏
        self.menu_root.config(menu=menubar)

    def input_data(self):
        """
        录入数据的方法
        :return:
        """
        # 1.显示组件
        self.input_frame.pack()
        self.query_frame.pack_forget()
        self.about_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.upate_frame.pack_forget()

        print("点我录入数据奥！")

    def query_data(self):
        """
        查询数据的方法
        :return:
        """
        self.input_frame.pack_forget()
        self.query_frame.pack()
        self.about_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.upate_frame.pack_forget()
        print("点我查询数据奥！")

    def delete_data(self):
        """
        删除数据的方法
        :return:
        """
        self.input_frame.pack_forget()
        self.query_frame.pack_forget()
        self.about_frame.pack_forget()
        self.delete_frame.pack()
        self.upate_frame.pack_forget()
        print("点我删除数据奥！")

    def update_data(self):
        """
        更新数据的方法
        :return:
        """
        self.input_frame.pack_forget()
        self.query_frame.pack_forget()
        self.about_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.upate_frame.pack()
        print("点我更新数据奥！")

    def about_me(self):
        """
        关于我
        :return:
        """
        self.input_frame.pack_forget()
        self.query_frame.pack_forget()
        self.about_frame.pack()
        self.delete_frame.pack_forget()
        self.upate_frame.pack_forget()
        print("关于逻辑教育>>>")


# def main():
#     # 1.初始化界面对象
#     menu_root = tk.Tk()
#     MenuPage(menu_root)
#     # 2.启动界面
#     menu_root.mainloop()
#
#
# main()