from django.db import connections

def formQuery(db, columns, table, values):
    columnsComma = ', '.join(columns)
    valuesLike = [sub + '%' for sub in values]
    like = True
    if values[0] is not '':
        like = False
        del valuesLike[0];
        valuesLike.insert(0,(values[0]))
    with connections[db].cursor() as cursor:
                qry = "SELECT "+ columnsComma + " FROM " + table + " "
                for i, x in enumerate(columns):
                    if not i:
                        if like is False:
                            qry += "WHERE " + x + " = %s "
                        else:
                            qry += "WHERE " + x + " LIKE %s "
                    else:
                        qry += "AND " + x + " LIKE %s "
                cursor.execute(qry,valuesLike)
                return cursor.fetchall()
                cursor.close()

def formCreate(db, columns, table, values):
    with connections[db].cursor() as cursor:
                qry = "SELECT "+ columns[0] + " FROM " + table + " WHERE " + columns[0] + " = %s "
                cursor.execute(qry,values[0])
                row = cursor.fetchall()
                cursor.close()
    if row is not None:
        raise Exception("Record with the same primary key already exists")
    with connections[db].cursor() as cursor:
                qry = "INSERT INTO " + table " ("+ columnsComma + ") Values (" + values + ");"
                cursor.execute(qry,valuesLike)
                return cursor.fetchall()
                cursor.close()