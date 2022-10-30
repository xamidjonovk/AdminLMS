from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_faculty""")
        faculties = dictfetchall(cursor)
        return faculties


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT adminapp_group.id, adminapp_group.name, adminapp_faculty.name as faculty
         from adminapp_group left join adminapp_faculty on adminapp_group.faculty_id = adminapp_faculty.id
         """)
        groups = dictfetchall(cursor)
        return groups


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_kafedra""")
        kafedra = dictfetchall(cursor)
        return kafedra


def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_subject""")
        subjects = dictfetchall(cursor)
        return subjects


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT adminapp_teacher.id, adminapp_teacher.first_name, adminapp_teacher.last_name,
        adminapp_teacher.age, adminapp_kafedra.name as kafedra_name, adminapp_subject.name as subject_name from 
        adminapp_teacher left join adminapp_kafedra on adminapp_teacher.kafedra_id = adminapp_kafedra.id
        left join adminapp_subject on adminapp_teacher.subject_id = adminapp_subject.id""")
        teachers = dictfetchall(cursor)
        return teachers


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT adminapp_student.id, adminapp_student.first_name, adminapp_student.last_name, 
        adminapp_student.age, 
        adminapp_group.name as group_name, adminapp_student.image as image  from adminapp_student
        left join adminapp_group on adminapp_student.group_id = adminapp_group.id""")
        student = dictfetchall(cursor)
        return student
