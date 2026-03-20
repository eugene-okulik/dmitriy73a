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
print(id_students, "id_students")

cursor.execute(
    "INSERT INTO books (title, taken_by_student_id) VALUES "
    "('Та самая книга том 1 урок 15 попытка сделать нормально 3', %i);"
    % (id_students))
id_book1 = cursor.lastrowid
print(id_book1, "id_book1")

cursor.execute(
    "INSERT INTO books (title, taken_by_student_id) VALUES ('Та самая книга том 2 попытка сделать нормально 3', %i);"
    % (id_students))
id_book2 = cursor.lastrowid
print(id_book2, "id_book2")

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES ('Та самая Группа 3', '20.03.26', '20.03.26');")
id_group = cursor.lastrowid
print(id_group, "group")

cursor.execute("update students set group_id=%i where id=%i;" % (id_group, id_students))

cursor.execute("INSERT INTO subjects (title) VALUES ('Тот самый лучший предмет 3');")
id_subjects1 = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES ('Тот самый худший предмет 3');")
id_subjects2 = cursor.lastrowid
print(id_subjects1, id_subjects2, "subjects1 and id_subjects2")

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES "
               "('занятие 1 для лучшего предмета урок 15-3', %i), "
               "('занятие 2 для лучшего предмета урок 15-3', %i), "
               "('занятие 1 для худшего предмета урок 15-3', %i), "
               "('занятие 2 для худшего предмета урок 15-3', %i);"
               % (id_subjects1, id_subjects1, id_subjects2, id_subjects2))
# пришлось тут костылить в надежде что ни кто параллельно ни чего не вставит)
id_les1, id_les2, id_les3, id_les4 = cursor.lastrowid + 3, cursor.lastrowid + 2, cursor.lastrowid + 1, cursor.lastrowid
# ну и как ожидалось первый раз вышла лажа, пытался минусовать, переделал на +
# а надо было херней не заниматься и сразу вставить отдельными записями)
print([id_les1, id_les2, id_les3, id_les4], "тут принтуем lesson id_les1...")

cursor.execute("INSERT INTO marks (value, lesson_id, student_id) "
               "VALUES "
               "('хорошо', %i, %i), "
               "('молодец', %i, %i), "
               "('4', %i, %i), "
               "('3', %i, %i);"
               % (id_les1, id_students, id_les2, id_students, id_les3, id_students, id_les4, id_students))
db.commit()

# для отладки
# 22477 id_students
# 5186 id_book1
# 5187 id_book2
# 22148 group
# 14169 14170 subjects1 and id_subjects2
# [75482, 75481, 75480, 75479] тут принтуем lesson id_les1...


cursor.execute("select s.name, l.title, m.value from students s "
               "inner join marks m "
               "on s.id = m.student_id "
               "inner join lessons l "
               "on m.lesson_id = l.id "
               "where s.id = %i;" % (id_students))
for i in cursor.fetchall():
    print(i)

cursor.execute(
    "select s. name, b.title from students s inner join books b on s.id = b.taken_by_student_id where s.id = %i;"
    % (id_students))
for i in cursor.fetchall():
    print(i)

# пришлось добавлять имена колонок, иначе в словаре title перезатирался
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
