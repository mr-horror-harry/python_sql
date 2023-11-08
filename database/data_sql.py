import sqlite3
connection = sqlite3.connect("./database/task_db.db")
#parse data from tuple to dict
connection.row_factory = sqlite3.Row

def createTable():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS task_to_do (task TEXT, date TEXT)")

def putTask(task, date):
    with connection:
        connection.execute("INSERT INTO task_to_do VALUES (?, ?);", (task, date))

def getTaskList():
    with connection:
        cursor_dataset = connection.execute("SELECT * FROM task_to_do")
        return cursor_dataset

def deleteTable():
    with connection:
        connection.execute("DROP TABLE IF EXISTS task_to_do")
        #to avoid the serial/auto increment error!
        connection.execute("CREATE TABLE IF NOT EXISTS task_to_do (task TEXT, date TEXT)")

def closeConn():
    connection.close()