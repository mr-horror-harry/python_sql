from database.data_sql import createTable, putTask, getTaskList

prompt="""
1) Add data
2) Retrieve data
3) Exit
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
        print("Task: ", task["task"], "\n", "Deadline: ", task["date"],"\n\n", sep="")

print("Welcome to the task to do app!")
#create table
createTable()

while (ip:=input(prompt))!=3:
    if ip=="1":
        task = Task()
        task.getInput()
        print(task.task, task.date)
        putTask(task.task, task.date)

    elif ip=="2":
        data = getTaskList()
        iterData(data)

    else:
        print("Unexpected input!")
        break