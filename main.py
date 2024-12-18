import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

class student:
    def __init__(self,name,family,id):
        self.name=name
        self.family=family
        self.id=id

    def registration(self):
        print(f"دانشجو  {self.name} {self.family} با شماره {self.id} ثبت شد.")


    def save_to_db(self,cursor):
        try:
            cursor.execute('insert into students(id,name,family) values (?,?,?)',(self.id,self.name,self.family))
            print(f"دانشجو {self.name} {self.family} با موفقیت در دیتابیس ذخیره شد.")
        except Exception as e:
            print(f"خطا در ذخیره‌سازی دانشجو در دیتابیس: {e}")

    def getgrade(self,course_code,grade):
        print(f" نمره دانشجو{self.name} {self.family} بری درس {course_code} ثبت شد.")
        return grade

    def calculate_grade(self,grades):
        if grades:
            gpa = sum(grades) / len(grades)
            print(f" معدل دانشجو {self.name} برابر است با: {gpa}")
            return gpa
        else:
            print("نمره ای برای محاسبه معدل وجود ندارد!")
            return 0


class teacher:
    def __init__(self,firstname,lastname,teacherid):
        self.firstname=firstname
        self.lastname=lastname
        self.teacherid=teacherid

    def registration(self):
        print(f"استاد {self.firstname} {self.lastname} با شماره {self.teacherid} ثبت شد. ")


    def save_to_db(self,cursor):
        try:
            cursor.execute('insert into teachers(id,firstname,lastname)values (?,?,?)',(self.teacherid,self.firstname,self.lastname))
            print(f"استاد {self.firstname} {self.lastname} با موفقیت در دیتابیس ذخیره شد.")
        except Exception as e:
            print(f"خطای ذخیره سازی دز دیتابیس: {e}")



    def assign_course(self,course_name):
        print(f"درس {course_name} به استاد {self.firstname}{self.lastname} داده شد.")


class course:
    def __init__(self,coursecode,coursename,teacher,credit_hours):
        self.coursecode=coursecode
        self.coursename=coursename
        self.teacher=teacher
        self.credit_hours=credit_hours

    def registration(self):
        print(f"درس {self.coursename} با کد {self.coursecode} و تعداد واحد {self.credit_hours} ثبت شد.")

    def save_to_db(self, cursor):
        try:
            cursor.execute('insert into courses(course_code,course_name,teacher_id,credit_hours) values(?,?,?,?)'
                           ,(self.coursecode,self.coursename,self.teacher,int(self.credit_hours)))
            print(f"درس {self.coursename} با موفقیت در دیتابیس ذخیره شد.")
        except Exception as e:
            print(f"خطا در ذخیره‌سازی درس در دیتابیس: {e}")

    def getcourse(self):
        print(f"اطلاعات درس {self.coursename}:")
        print(f"کد درس {self.coursecode}, استاد  {self.teacher.firstname}{self.teacher.lastname} ,تعداد واحد {self.credit_hours} ")

class grades:
    def __init__(self,coursecode,student_id,grade):
        self.coursecode=coursecode
        self.student_id=student_id
        self.grade=grade

    def addgrade(self,grade):
        self.grade=grade
        print(f"نمره {grade} برای دانشجو {self.student_id} در درس {self.coursecode} ثبت شد.")

    def save_to_db(self, cursor):
        try:
            cursor.execute('insert into grades (course_code, student_id, grade) VALUES (?, ?, ?)',
                           (self.coursecode, self.student_id, self.grade))
            print(f"نمره دانشجو با موفقیت در دیتابیس ذخیره شد.")
        except Exception as e:
            print(f"خطا در ذخیره‌سازی نمره در دیتابیس: {e}")

    def generate_report(self):
        print(f"گزارش نمرات دانشجو {self.student_id} برای درس {self.coursecode} : {self.grade}")


class mainpanel:
    def __init__(self,students,teachers,courses,grades):
        self.students=students
        self.teachers=teachers
        self.courses=courses
        self.grades=grades
        # self.students = []
        # self.teachers = []
        # self.courses = []
        # self.grades = []

    def register_student(self,student):
        self.students.append(student)
        student.registration()
        # print(f" دانشجو {self.students}درس {self.courses} را دریافت کرد.")
        print(f"دانشجو {student.name} {student.family} ثبت شد و آماده دریافت درس است.")

    def register_teacher(self,teacher):
        self.teachers.append(teacher)
        teacher.registration()

    def register_course(self,course):
        self.courses.append(course)
        course.registration()

    def add_grades(self,grades,course_code,student_id,grade):
        newgrade=grades(course_code,student_id,grade)
        self.grades.append(newgrade)
        newgrade.addgrade(grade)

    def search_course(self,course_code):
        for course in self.courses:
            if course.coursecode == course_code:
                course.getcourse()


    def generate_report(self):
        print("گزارش معدل تمامی دانشجویان:")
        for student in self.students:
            student_grades = [g.grade for g in self.grades if g.student_id == student.id]
            student.calculate_grade(student_grades)

# panel = mainpanel(student,course,grades)
# ایجاد نمونه از کلاس mainpanel
panel = mainpanel([], [], [], [])

# ثبت دانشجویان
s1 = student("bardia", "saedi", 1)
panel.register_student(s1)
grade = s1.getgrade(course_code="tarikh", grade=18)
s1.calculate_grade([grade])
s1.save_to_db(cursor)

s2 = student("parham", "askari", 2)
panel.register_student(s2)
grade = s2.getgrade(course_code="tarikh", grade=14.5)
s2.calculate_grade([grade])
s2.save_to_db(cursor)

s3 = student("atoosa", "heidari", 3)
panel.register_student(s3)
grade = s3.getgrade(course_code="tarikh", grade=17.5)
s3.calculate_grade([grade])
s3.save_to_db(cursor)

s4 = student("banafshe", "shahi", 4)
panel.register_student(s4)
grade = s4.getgrade(course_code="tarikh", grade=15)
s4.calculate_grade([grade])
s4.save_to_db(cursor)

# ثبت استاد و درس
t10 = teacher("asma", "mahmoodi", 10)
panel.register_teacher(t10)
t10.save_to_db(cursor)
# ثبت درس و ذخیره در دیتابیس
course1 = course("tarikh", "tarikh", t10, 3)
panel.register_course(course1)
course1.save_to_db(cursor)

# اضافه کردن نمرات برای دانشجویان
panel.add_grades(grades, "tarikh", 1, 18)
panel.add_grades(grades, "tarikh", 2, 14.5)
panel.add_grades(grades, "tarikh", 3, 17.5)
panel.add_grades(grades, "tarikh", 4, 15)

# ذخیره نمرات در دیتابیس
for g in panel.grades:
    g.save_to_db(cursor)

# جستجو و نمایش درس
panel.search_course("tarikh")

# نمایش گزارش معدل دانشجویان
panel.generate_report()
# پایان کار با دیتابیس
connection.commit()
connection.close()