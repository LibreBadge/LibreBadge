from django.db import connections
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def select(db, table, field, value):
    with connections['cardholders'].cursor() as cursor:
                qry = "SELECT * FROM " + table + " WHERE " + field + " = " + value
                cursor.execute(qry,[])
                return namedtuplefetchall(cursor)
                cursor.close()

def selectLike(db, table, field, value):
    with connections['cardholders'].cursor() as cursor:
                qry = "SELECT * FROM " + table + " WHERE " + field + " LIKE " + value
                cursor.execute(qry,[])
                return namedtuplefetchall(cursor)
                cursor.close()