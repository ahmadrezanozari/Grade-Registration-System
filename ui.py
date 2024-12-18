import sqlite3
import tkinter as tk
from tkinter import ttk

# اتصال به دیتابیس
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# توابع مربوط به ثبت دانشجو
def open_student_form():
    def register_student():
        name = entry_name.get()
        family = entry_family.get()
        student_id = entry_id.get()
        try:
            cursor.execute("INSERT INTO students (id, name, family) VALUES (?, ?, ?)",
                           (student_id, name, family))
            connection.commit()
            label_result.config(text="دانشجو با موفقیت ثبت شد.", fg="green")
        except Exception as e:
            label_result.config(text=f"خطا: {e}", fg="red")

    # فرم ثبت دانشجو
    student_form = tk.Toplevel()
    student_form.title("فرم ثبت دانشجو")

    tk.Label(student_form, text="شماره دانشجویی").grid(row=0, column=0)
    entry_id = tk.Entry(student_form)
    entry_id.grid(row=0, column=1)

    tk.Label(student_form, text="نام").grid(row=1, column=0)
    entry_name = tk.Entry(student_form)
    entry_name.grid(row=1, column=1)

    tk.Label(student_form, text="نام خانوادگی").grid(row=2, column=0)
    entry_family = tk.Entry(student_form)
    entry_family.grid(row=2, column=1)

    tk.Button(student_form, text="ثبت", command=register_student).grid(row=3, column=0, columnspan=2)
    label_result = tk.Label(student_form, text="")
    label_result.grid(row=4, column=0, columnspan=2)

# توابع مربوط به ثبت استاد
def open_teacher_form():
    def register_teacher():
        firstname = entry_firstname.get()
        lastname = entry_lastname.get()
        teacher_id = entry_id.get()
        try:
            cursor.execute("INSERT INTO teachers (id, firstname, lastname) VALUES (?, ?, ?)",
                           (teacher_id, firstname, lastname))
            connection.commit()
            label_result.config(text="استاد با موفقیت ثبت شد.", fg="green")
        except Exception as e:
            label_result.config(text=f"خطا: {e}", fg="red")

    # فرم ثبت استاد
    teacher_form = tk.Toplevel()
    teacher_form.title("فرم ثبت استاد")

    tk.Label(teacher_form, text="شماره استاد").grid(row=0, column=0)
    entry_id = tk.Entry(teacher_form)
    entry_id.grid(row=0, column=1)

    tk.Label(teacher_form, text="نام").grid(row=1, column=0)
    entry_firstname = tk.Entry(teacher_form)
    entry_firstname.grid(row=1, column=1)

    tk.Label(teacher_form, text="نام خانوادگی").grid(row=2, column=0)
    entry_lastname = tk.Entry(teacher_form)
    entry_lastname.grid(row=2, column=1)

    tk.Button(teacher_form, text="ثبت", command=register_teacher).grid(row=3, column=0, columnspan=2)
    label_result = tk.Label(teacher_form, text="")
    label_result.grid(row=4, column=0, columnspan=2)

# توابع مربوط به ثبت درس
def open_course_form():
    def register_course():
        course_code = entry_code.get()
        course_name = entry_name.get()
        teacher_id = entry_teacher_id.get()
        credit_hours = entry_credit.get()
        try:
            cursor.execute("INSERT INTO courses (course_code, course_name, teacher_id, credit_hours) VALUES (?, ?, ?, ?)",
                           (course_code, course_name, teacher_id, credit_hours))
            connection.commit()
            label_result.config(text="درس با موفقیت ثبت شد.", fg="green")
        except Exception as e:
            label_result.config(text=f"خطا: {e}", fg="red")

    # فرم ثبت درس
    course_form = tk.Toplevel()
    course_form.title("فرم ثبت درس")

    tk.Label(course_form, text="کد درس").grid(row=0, column=0)
    entry_code = tk.Entry(course_form)
    entry_code.grid(row=0, column=1)

    tk.Label(course_form, text="نام درس").grid(row=1, column=0)
    entry_name = tk.Entry(course_form)
    entry_name.grid(row=1, column=1)

    tk.Label(course_form, text="شماره استاد").grid(row=2, column=0)
    entry_teacher_id = tk.Entry(course_form)
    entry_teacher_id.grid(row=2, column=1)

    tk.Label(course_form, text="تعداد واحد").grid(row=3, column=0)
    entry_credit = tk.Entry(course_form)
    entry_credit.grid(row=3, column=1)

    tk.Button(course_form, text="ثبت", command=register_course).grid(row=4, column=0, columnspan=2)
    label_result = tk.Label(course_form, text="")
    label_result.grid(row=5, column=0, columnspan=2)

# توابع مربوط به ثبت نمره
def open_grades_form():
    def register_grade():
        course_code = entry_course_code.get()
        student_id = entry_student_id.get()
        grade = entry_grade.get()
        try:
            cursor.execute("INSERT INTO grades (course_code, student_id, grade) VALUES (?, ?, ?)",
                           (course_code, student_id, grade))
            connection.commit()
            label_result.config(text="نمره با موفقیت ثبت شد.", fg="green")
        except Exception as e:
            label_result.config(text=f"خطا: {e}", fg="red")

    # فرم ثبت نمرات
    grade_form = tk.Toplevel()
    grade_form.title("فرم ثبت نمرات")

    tk.Label(grade_form, text="کد درس").grid(row=0, column=0)
    entry_course_code = tk.Entry(grade_form)
    entry_course_code.grid(row=0, column=1)

    tk.Label(grade_form, text="شماره دانشجو").grid(row=1, column=0)
    entry_student_id = tk.Entry(grade_form)
    entry_student_id.grid(row=1, column=1)

    tk.Label(grade_form, text="نمره").grid(row=2, column=0)
    entry_grade = tk.Entry(grade_form)
    entry_grade.grid(row=2, column=1)

    tk.Button(grade_form, text="ثبت", command=register_grade).grid(row=3, column=0, columnspan=2)
    label_result = tk.Label(grade_form, text="")
    label_result.grid(row=4, column=0, columnspan=2)

# پنل اصلی
root = tk.Tk()
root.title("پنل اصلی")

tk.Button(root, text="ثبت دانشجو", command=open_student_form).grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, text="ثبت استاد", command=open_teacher_form).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="ثبت درس", command=open_course_form).grid(row=1, column=0, padx=10, pady=10)
tk.Button(root, text="ثبت نمره", command=open_grades_form).grid(row=1, column=1, padx=10, pady=10)

root.mainloop()

# بستن اتصال به دیتابیس
connection.close()
