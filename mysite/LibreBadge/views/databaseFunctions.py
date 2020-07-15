from django.db import connections

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def formQuery(db, columns, table, values):
    columnsComma = ', '.join(columns)
    valuesLike = [sub + '%' for sub in values]
    like = True
    if values[0] != '': #checks if primary key was submitted
        like = False #search by primary key
        del valuesLike[0]; #removes primary key from values like
        valuesLike.insert(0,(values[0])) #replaces primary key with the like operator wiht primary key without like operator
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
                qry = qry[:-1]
                qry += ";"
                cursor.execute(qry,valuesLike)
                return cursor.fetchall()
                cursor.close()

def query(db, columns, table):
    columnsComma = ', '.join(columns)
    like = True
    with connections[db].cursor() as cursor:
                qry = "SELECT "+ columnsComma + " FROM " + table
                qry += ";"
                cursor.execute(qry)
                return dictfetchall(cursor)
                cursor.close()

def formCreate(db, columns, table, values):
    columnsComma = ', '.join(columns)
    noData = []
    with connections[db].cursor() as cursor:
                qry = "SELECT "+ columns[0] + " FROM " + table + " WHERE " + columns[0] + " = %s "
                cursor.execute(qry,[values[0]])
                row = cursor.fetchall()
                cursor.close()
    for value in values:
        noData.append('')
    if values == noData:
        raise Exception("No data submited")
    if row != []:
        raise Exception("Record with the same primary key already exists")
    with connections[db].cursor() as cursor:
                qry = "INSERT INTO "+ table + " (" + columnsComma + ") VALUES ("
                for i in enumerate(columns):
                        qry += "%s, "
                qry = qry[:-2]
                qry += ");"
                cursor.execute(qry,values)
                return cursor.fetchall()
                cursor.close()