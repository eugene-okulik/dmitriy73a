import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl"
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name) VALUES ('TotSamiy3', 'TogoSamogo3');")
id_students = cursor.lastrowid

books = [("книга 1", id_students), ("книга 2", id_students)]
cursor.executemany("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", books)

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES ('Та самая Группа 3', '20.03.26', '20.03.26');")
id_group = cursor.lastrowid

cursor.execute("update students set group_id=%i where id=%i;" % (id_group, id_students))

subjects = [("предмет 1",), ("предмет 2",)]
id_subjects_all = []
for i in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s);", i)
    id_subjects_all.append(cursor.lastrowid)
id_subjects1, id_subjects2 = id_subjects_all

lessons = [("занятие 1", id_subjects1), ("занятие 2", id_subjects1),
           ("занятие 3", id_subjects2), ("занятие 4", id_subjects2)]
id_lessons_all = []
for i in lessons:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s);", i)
    id_lessons_all.append(cursor.lastrowid)
id_les1, id_les2, id_les3, id_les4 = id_lessons_all

marks = [("ну такое", id_les1, id_students), ("так себе", id_les2, id_students),
         ("2", id_les3, id_students), ("0.5", id_les4, id_students)]
cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", marks)

db.commit()

print("Все оценки студента")
cursor.execute("select s.name, l.title, m.value from students s "
               "inner join marks m "
               "on s.id = m.student_id "
               "inner join lessons l "
               "on m.lesson_id = l.id "
               "where s.id = %i;" % (id_students))
for i in cursor.fetchall():
    print(i)

print("Все книги, которые находятся у студента")
cursor.execute(
    "select s. name, b.title from students s inner join books b on s.id = b.taken_by_student_id where s.id = %i;"
    % (id_students))
for i in cursor.fetchall():
    print(i)

print("Для вашего студента выведите всё, что о нем есть в базе")
cursor.execute("""
SELECT
    s.name,
    s.second_name,
    b.title AS b_title,
    m.value,
    g.title AS g_title,
    l.title AS l_title,
    s2.title AS s_title
FROM students s
INNER JOIN books b ON s.id = b.taken_by_student_id
INNER JOIN marks m ON s.id = m.student_id
INNER JOIN `groups` g ON s.group_id = g.id
INNER JOIN lessons l ON m.lesson_id = l.id
INNER JOIN subjects s2 ON l.subject_id = s2.id
WHERE s.id = %i;
""" % (id_students))
for i in cursor.fetchall():
    print(i)

db.close()
