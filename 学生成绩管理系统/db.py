"""
小目标：将输入的数据添加到 students.txt 文件中-->
1.将输入的数据构建成字典
2.添加至列表中

2.1 读取students.txt-->转换成list
2.2 将构建成字典 添加 至 list 中
2.3 将list数据写入到students.txt中
"""
import json


class StudentDB(object):
    def __init__(self):
        # 初始化学员数据
        self.students = []
        # 读取文件数据
        self.read_students_data()

    def read_students_data(self):
        """
        读取学员数据
        :return:
        """
        with open("students.txt", mode="r", encoding="utf-8") as f:
            text = f.read()

        if text:
            # open-->read/write-->str
            # print(type(text))
            # 需求：文本(json对象)-->list(python对象)
            self.students = json.loads(text)
            # print(self.student)
            # print(type(self.student))

    def insert(self, student_data):
        """
        往self.students里面添加数据的方法
        :return:
        """
        # 添加数据
        self.students.append(student_data)
        print(self.students)
        # 保存数据
        self.save_data()

    def save_data(self):
        """
        保存数据
        :return:
        """
        with open("students.txt", mode="w", encoding="utf-8") as f:
            # 怎么将list(python)-->str(json)
            res = json.dumps(self.students, ensure_ascii=False)
            # print(type(res))
            f.write(res)
            # 添加一个参数

    def return_all_data(self):
        """
        将students.txt中的数据返回出去
        :return: 返回到函数的调用处
        """
        return self.students

    def delete_by_name(self, name):
        """
        根据姓名删除students.txt中对应的数据
        :param name: 姓名
        :return:
        """
        # [1,2,3] --> [2,3] -->L.pop(下标)，del 元素，L.remove(元素)
        # [{},{},{}]-->如何删除列表中的一个元素？
        # print(self.students)
        # 取出[]中每一个元素
        for student in self.students:
            # 如果输入姓名 与 students.txt 中某条数据的 name 的值相等
            if name == student["name"]:
                # 删除该数据
                self.students.remove(student)
                # 删除一条数据之后，直接结束循环-->强制提前结束循环(意外中断)
                break
        else:
            print("没有删除成功")
            return False

        # 思考：如果循环结束都没有找到有该学员-->打印输出"没有删除成功"
        # 转换为-->不会进入if条件判断-->for循环正常执行完毕-->else
        self.save_data()
        return True

    def search_by_name(self, name):
        """
        根据用户名查找数据
        :return:
        """
        # name = "子白"  self.students=[{},{},{}]
        for student in self.students:
            # print(student)
            if name == student["name"]:
                # 学员存在，返回该学员的信息。
                return student
        else:
            # 学员不存在，返回False
            return False

    def modify(self, stu):
        """
        修改数据
        :return:
        """
        # 字典中有什么方法可以方便修改数据？
        # dict.update() 对于相同key，对应的value值会替换
        # 只有用户输入name在self.students中-->存在则替换，不存在则提示
        for student in self.students:
            if stu["name"] == student["name"]:
                # 学员存在，则替换
                student.update(stu)
                self.save_data()
                return True
        else:
            # 学员不存在，返回False
            return False


db = StudentDB()
# db.insert({'name': '小天', 'math': '87', 'chinese': '100', 'english': '87'})
# db.delete_by_name("aaa")
# res = db.search_by_name("子白")
# print(res)