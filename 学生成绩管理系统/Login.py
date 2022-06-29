"""
登录页，面向过程-->面向对象
"""
import tkinter as tk
import tkinter.messagebox
from MenuPage import MenuPage


class LoginPage(object):
    def __init__(self, master=None):
        """
        初始化函数
        :param master:界面对象
        """
        self.root = master
        self.root.title("欢迎进入学生成绩管理系统")
        self.root.geometry("400x180")
        self.frame = tk.Frame(self.root)
        # 光标同时定住多个位置：shift+ctrl+alt
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        # 调用创建页面的方法
        self.create_page()
        self.frame.pack()

    def create_page(self):
        """
        在组件上布局登录页面
        :return:
        """
        # 添加文本
        tk.Label(self.frame).grid(row=0, sticky=tk.W)
        tk.Label(self.frame, text="账号：").grid(row=1, sticky=tk.W, pady=10)
        tk.Label(self.frame, text="密码：").grid(row=2, sticky=tk.W, pady=10)
        # 输入框
        tk.Entry(self.frame, textvariable=self.username).grid(row=1, column=1)
        tk.Entry(self.frame, show="*", textvariable=self.password).grid(row=2, column=1)

        # 添加按钮
        # 点击按钮-->绑定方法-->执行逻辑代码
        tk.Button(self.frame, text="登录", command=self.login_check).grid(row=3)
        tk.Button(self.frame, text="退出").grid(row=3, column=1, sticky=tk.E)

    def login_check(self):
        """
        检查用户输入信息
        :return:
        """
        # 判断账号与密码是否正确 现有的正确账号与密码：123  666
        username = self.username.get()
        password = self.password.get()
        # 正确，则登录成功
        if username == "123" and password == "666":
            # print("恭喜你！登录成功")
            MenuPage(self.root)
            # 销毁 frame 组件
            self.frame.destroy()

        # 否则，登录失败
        else:
            # print("哎呀呀！登录失败")
            # 弹出提示框，提示信息错误
            tk.messagebox.showinfo(title="错误", message="账号或密码错误！")


def main():
    # 1.创建 界面 对象
    root = tk.Tk()
    LoginPage(root)
    # 2.进入消息循环-->启动界面
    root.mainloop()


main()
