from django.db import connections

def select(db, columns, table, field, value):
    columnsComma = ', '.join(columns)
    with connections[db].cursor() as cursor:
                qry = "SELECT "+ columnsComma + " FROM " + table + " WHERE " + field + " = %"
                cursor.execute(qry,[value])
                return cursor.fetchall()
                cursor.close()

def formQuery(db, columns, table, values):
    columnsComma = ', '.join(columns)
    valuesLike = [sub + '%' for sub in values]
    with connections[db].cursor() as cursor:
                qry = "SELECT "+ columnsComma + " FROM " + table + " "
                for i, x in enumerate(columns):
                    if not i:
                        qry += "WHERE " + x + " LIKE %s "
                    else:
                        qry += "AND " + x + " LIKE %s "
                cursor.execute(qry,valuesLike)
                return cursor.fetchall()
                cursor.close()