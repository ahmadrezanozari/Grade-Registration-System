import sqlite3

# ایجاد اتصال به دیتابیس و ایجاد جداول
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# ایجاد جدول برای دانشجویان
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name NVARCHAR(20) NOT NULL,
    family NVARCHAR(30) NOT NULL
)''')

# ایجاد جدول برای اساتید
cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    firstname NVARCHAR(20) NOT NULL,
    lastname NVARCHAR(20) NOT NULL
)''')

# ایجاد جدول برای دروس
cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
    course_code TEXT PRIMARY KEY,
    course_name NVARCHAR(20) NOT NULL,
    teacher_id INTEGER,
    credit_hours INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
)''')

# ایجاد جدول برای نمرات
cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    course_code NVARCHAR(30),
    student_id INTEGER,
    grade REAL,
    FOREIGN KEY (course_code) REFERENCES courses(course_code),
    FOREIGN KEY (student_id) REFERENCES students(id)
)''')

# ذخیره تغییرات و بستن اتصال
connection.commit()
connection.close()
