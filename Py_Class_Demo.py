# 定义一个学生类
# 要求
# 1. 属性包含学生姓名、学号、语数英三科的成绩
# 2. 能够设置学生某个科目的成绩
# 3. 能够打印出该学生所有科目的成绩

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, score):
        if course in self.grades:
            self.grades[course] = score

    def print_grade(self):
        print(f"学生{self.name}（学号{self.student_id}）的成绩是")
        for course in self.grades:
            print(f"{course}：{self.grades[course]}分")

chen = Student("小陈", 100618)
chen.set_grade("语文", 90)
chen.set_grade("数学", 85)
chen.set_grade("英语", 95)
# print(chen.name)
# print(chen.grades)
chen.print_grade()
