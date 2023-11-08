from database.data_sql import createTable, putTask, getTaskList, deleteTable, closeConn

prompt="""
1) Add data
2) Retrieve data
3) Clean DB completely
4) Exit
"""

# a template to maintain the task data
class Task:
    task=""
    date=""

    def getInput(self):
        self.task = input("Enter the task: ")
        self.date = input("Enter the date: ")

def iterData(li):
    for task in li:
        #access tuple of data from the cursor data :: tuple:index access & dict:key access
        print("Task: ", task["task"], "\n", "Deadline: ", task["date"],"\n", sep="")

def confirmDel():
    x=input("Are you sure you want to clean the DB entirely ? [y/n]: ")
    if (x=="y" or x=="Y"):
        deleteTable()
        print("DB cleaned successfully!")
    else:
        print("DB clean operation failed!")


print("Welcome to the task to do app!")
#create table
createTable()

while (ip:=input(prompt))!=3:
    if ip=="1":
        task = Task()
        task.getInput()
        print(task.task, task.date)
        putTask(task.task, task.date)
        print("Task added!")

    elif ip=="2":
        data = getTaskList()
        iterData(data)

    elif ip=="3":
        confirmDel()

    elif ip=="4":
        print("Exiting app as per user wish!")
        closeConn()
        break

    else:
        print("Unexpected input!")
        closeConn()
        break