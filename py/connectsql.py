import pymssql


def connect(db):
    connect = pymssql.connect(server = '.' , database = db)

    if connect:
        print('connect succeed')
    return connect

