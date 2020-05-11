from django.db import connections
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def select(db, table, field, value):
    with connections[db].cursor() as cursor:
                qry = "SELECT * FROM " + table + " WHERE " + field + " = %s"
                cursor.execute(qry,[value])
                return namedtuplefetchall(cursor)
                cursor.close()

def selectStartingWith(db, table, field, value):
    with connections[db].cursor() as cursor:
                qry = "SELECT * FROM " + table + " WHERE " + field + " LIKE %s%%"
                cursor.execute(qry,[value])
                return namedtuplefetchall(cursor)
                cursor.close()

def formQuery(db, columns, table, values):
    columnsComma = ', '.join(columns)
    #columns and values dict to comma seperated values
    #for loop for every key/value pair in values append AND + field + like %s%% and append values to value variable in cursor execute
    with connections[db].cursor() as cursor:
                qry = "SELECT "+ columnsComma + " FROM " + table + " "
                i=0
                for x in columns:
                    if i<1:
                        qry = qry + "WHERE " + x + " LIKE %s "
                        i = i + 1
                    else:
                        qry = qry + "AND " + x + " LIKE %s "
                cursor.execute(qry,values)
                return namedtuplefetchall(cursor)
                cursor.close()