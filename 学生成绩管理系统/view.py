"""
1.普通的创建Frame容器-->tk.Frame()
2.继承tk.Frame-->意味着我们有一个权力-->重写tk.Frame这个类里面所有的属性及方法
2.1 重写创建Frame容器的方法
"""
import tkinter as tk
from db import db
# 实现表头的模块
from tkinter import ttk


# 1.创建录入类
class InputFrame(tk.Frame):
    def __init__(self, master=None):
        # 调用父类的__init__方法帮助我们创建Frame对象，主容器是我们传进去的master
        # 创建Frame容器并返回-->self-->当前的Frame容器
        super().__init__(master)
        # 主界面
        self.root = master
        # 创建StringVar对象
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        # 创建状态
        self.status = tk.StringVar()
        # 创建录入页面
        self.create_page()

    def create_page(self):
        # 创建文本，问题：当前谁才表示Frame对象-->self
        tk.Label(self).grid(row=0, sticky=tk.W, pady=10)
        tk.Label(self, text="姓名：").grid(row=1, sticky=tk.W, pady=10)
        tk.Label(self, text="数学：").grid(row=2, sticky=tk.W, pady=10)
        tk.Label(self, text="语文：").grid(row=3, sticky=tk.W, pady=10)
        tk.Label(self, text="英语：").grid(row=4, sticky=tk.W, pady=10)
        # 创建输入框
        tk.Entry(self, textvariable=self.name).grid(row=1, column=1, sticky=tk.E)
        tk.Entry(self, textvariable=self.math).grid(row=2, column=1, sticky=tk.E)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=1, sticky=tk.E)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=1, sticky=tk.E)
        # 创建按钮
        tk.Button(self, text="录入", command=self.recode_student).grid(row=5, column=1, sticky=tk.E, pady=10)
        # 添加提示文本
        tk.Label(self, textvariable=self.status).grid(row=6, column=1, sticky=tk.E, pady=10)

    def recode_student(self):
        """
        获取用户输入数据并且添加到students.txt文件中来(数据库)
        :return:
        """
        name = self.name.get()
        math = self.math.get()
        chinese = self.chinese.get()
        english = self.english.get()
        # 获取录入数据并且打印
        # print(name, math, chinese, english)
        student_data = {
            "name": name,
            "math": math,
            "chinese": chinese,
            "english": english
        }
        db.insert(student_data)
        # 设置数据，set()
        self.status.set("插入数据成功")
        # 调用清空文本的方法
        self.clear_data()

    def clear_data(self):
        """
        清空文本
        :return:
        """
        self.name.set("")
        self.math.set("")
        self.chinese.set("")
        self.english.set("")


# 2.创建查询类
class QueryFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # 界面容器(父容器)
        self.root = master
        # 创建查询的界面
        self.create_page()

    def create_page(self):
        """
        创建查询界面
        :return:
        """
        # print("查询页面")
        # 1.表头
        self.create_tree_view()
        # 2.显示数据
        self.show_data_frame()
        # 3.创建刷新按钮-->点击按钮，再次读取数据显示上去
        tk.Button(self, text="刷新数据", command=self.show_data_frame).pack(anchor=tk.E, pady=5)

    def create_tree_view(self):
        """
        创建表头
        :return:
        """
        # 1.创建表头对象
        column = ("name",  "math", "chinese", "english")
        # 注意：self不能落下。self.变量名-->实例属性-->各个实例方法使用
        self.tree_view = ttk.Treeview(self, columns=column, show="headings")
        # 2.添加列,注意：标识符与column中的每个都要对应
        self.tree_view.column("name", width=80, anchor="center")
        self.tree_view.column("math", width=80, anchor="center")
        self.tree_view.column("chinese", width=80, anchor="center")
        self.tree_view.column("english", width=80, anchor="center")
        # 3.给对应的列添加标题
        self.tree_view.heading("name", text="姓名")
        self.tree_view.heading("math", text="数学")
        self.tree_view.heading("chinese", text="语文")
        self.tree_view.heading("english", text="英语")
        # 4.显示组件
        self.tree_view.pack()

    def show_data_frame(self):
        """
        显示数据
        :return:
        """
        # 显示一条数据,注意：index默认从0开始。不够灵活
        # self.tree_view.insert("", 0, values=("牛牛", 80, 90, 100))
        # 问题：直接从stundents.txt中拿到所有数据，直接显示上去呢？
        self.delete()
        students = db.return_all_data()
        print(students)  # [{},{},{}..] --> list
        # 获取：元素所在列表的下标，元素本身
        for index, stu in enumerate(students):
            # print(index, stu)
            values = (stu["name"], stu["math"], stu["chinese"], stu["english"])
            self.tree_view.insert("", index, values=values)

    def delete(self):
        obj = self.tree_view.get_children()   # 获取所有对象
        print(obj)
        for o in obj:
            print(o)
            self.tree_view.delete(o)   # 删除对象


# 3.创建删除类
class DeleteFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # 初始化删除学生的姓名
        self.del_name = tk.StringVar()
        # 初始化提示文本
        self.status = tk.StringVar()

        # 创建删除界面
        self.create_page()

    def create_page(self):
        """
        删除界面
        :return:
        """
        # 1.搭建删除页面
        # print("删除界面")
        # pack布局!!
        tk.Label(self, text="删除数据").pack()
        tk.Label(self, text="根据姓名删除信息").pack(anchor=tk.W, padx=20)
        tk.Entry(self, textvariable=self.del_name).pack(side=tk.LEFT, padx=20, pady=5)
        tk.Button(self, text="删除", command=self.delete_data).pack(side=tk.RIGHT)
        # 添加提示文本，如：已删除，或用户名不存在
        tk.Label(self, textvariable=self.status).pack()
        # 2.点击按钮会从students.txt中删除对应的信息
        # self.delete_data()

    def delete_data(self):
        """
        点击删除按钮的时候，才会调用
        根据用户输入的姓名删除数据
        如果用户名存在-->删除
        不在-->提示用户，该姓名不存在
        :return:
        """
        # 1.获取用户输入的姓名
        name = self.del_name.get()
        # 问题：db中如何告诉view，该用户是否删除呢？
        result = db.delete_by_name(name)
        # 如果已删除，则result为True，提示：**学员已被删除
        # 如果未删除，则result为False，提示：**学员不存在
        if result:
            # 提示,get()用来获取，set()用来设置值
            self.status.set(f"{name}已被删除")
            self.del_name.set("")
        else:
            self.status.set(f"{name}不存在")
            self.del_name.set("")


# 4.创建修改类
class UpdateFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        # 创建StringVar
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        # 创建修改界面
        self.create_page()

    def create_page(self):
        """
        修改界面
        :return:
        """
        # 文本
        tk.Label(self).grid(row=0, sticky=tk.W, pady=10)
        tk.Label(self, text="姓名：").grid(row=1, sticky=tk.W, pady=10)
        tk.Label(self, text="数学：").grid(row=2, sticky=tk.W, pady=10)
        tk.Label(self, text="语文：").grid(row=3, sticky=tk.W, pady=10)
        tk.Label(self, text="英语：").grid(row=4, sticky=tk.W, pady=10)
        # 创建输入框
        tk.Entry(self, textvariable=self.name).grid(row=1, column=1, sticky=tk.E)
        tk.Entry(self, textvariable=self.math).grid(row=2, column=1, sticky=tk.E)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=1, sticky=tk.E)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=1, sticky=tk.E)
        # 创建查询按钮
        tk.Button(self, text="查询", command=self.search_score).grid(row=5, column=0, sticky=tk.W, pady=10)
        # 创建修改按钮
        tk.Button(self, text="修改", command=self.update_data).grid(row=5, column=1, sticky=tk.E, pady=10)
        # 添加提示文本
        tk.Label(self, textvariable=self.status).grid(row=6, column=1, sticky=tk.E, pady=10)

    def search_score(self):
        """
        定义查询成绩的方法
        :return:
        """
        # 1. 获取用户输入的学生姓名
        name = self.name.get()
        # 2.去db中查询用户输入姓名所在的数据
        # 如果学员存在-->{"name":"",...}
        # 如果学员不存在-->False
        student = db.search_by_name(name)
        if student:
            # 设置成绩到输入框中
            self.math.set(student["math"])
            self.chinese.set(student["chinese"])
            self.english.set(student["english"])
        else:
            # 提示学员信息
            # self.math.set("")
            # self.chinese.set("")
            # self.english.set("")
            self.status.set(f"没有查询到{name}的信息")

    def update_data(self):
        """
        定义修改成绩的方法
        :return:
        """
        # 1.修改成绩-->获取用户输入的所有信息
        name = self.name.get()
        math = self.math.get()
        chinese = self.chinese.get()
        english = self.english.get()
        # 2.把数据用字典保存起来
        stu = {
            "name": name,
            "math": math,
            "chinese": chinese,
            "english": english
        }
        # print(stu)
        # 修改db中，数据name值为子白的成绩
        res = db.modify(stu)
        if res:
            self.status.set(f"{name}的信息更新完毕")
        else:
            self.status.set(f"{name}不存在，更新失败")


# 4.创建关于类
class AboutMe(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.create_page()

    def create_page(self):
        tk.Label(self, text="关于逻辑教育>>>").pack(anchor=tk.W)





