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