# coding=utf-8
from postgresworker import Worker
import tkinter
from tkinter import messagebox
import sys
import win32serviceutil

# -h "localhost" -u "postgres" -p "password" -port "5432" -d "DB"

def function_witn_warning():
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Alert", "We're gonna reload your PostgreSQL server, please don't be alarmed")
    r.service_info('Restart',)


if __name__ == '__main__':
    worker = Worker(database="postgres")
    r = Reload
    val1 = worker.execCurrentBuffer()[0]
    val2 = worker.execLowBuffer()[0]
    val3 = worker.execBuffer()[0]
    val1 = val1[0].split(" ")
    val2 = val2[0].split(" ")

    newSize = int(val1[0]) * 1.05 + int(val2[0]) / 1024
    # проверяю штуку для alert
    i = 3
    if (i == 3):
        var = worker.execAlterSystem()
        function_witn_warning()
    print(str(newSize) + "MB", val3[0])
