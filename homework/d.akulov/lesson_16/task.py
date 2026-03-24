import dotenv
import os
import mysql.connector as mysql
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
path_file = os.path.dirname(os.path.dirname(os.path.join(base_path)))
j_path = os.path.join(path_file, "eugene_okulik", "Lesson_16",
                      "hw_data", "data.csv")

with open(j_path, newline="") as file:
    file_hw = csv.DictReader(file)
    count = 0
    for i in file_hw:
        count += 1
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
        WHERE s.name = '%s' and s.second_name = '%s'
        and g.title = '%s'
        and b.title = '%s' and s2.title = '%s'
        and l.title = '%s' and m.value = '%s';
        """ % (i["name"], i["second_name"], i["group_title"],
               i["book_title"], i["subject_title"], i["lesson_title"],
               i["mark_value"]))

        if not cursor.fetchall():
            print(i["name"], i["second_name"], "в базе не найден. "
                                               "Строка файла", count)

db.close()
