

from tkinter import *
from datetime import date 

root = Tk()
root.geometry("700x500")
root.title("Age Calculator")

photo = PhotoImage(file="filename.png")
myimage = Label(image=photo)
myimage.grid(row=0,column=1)


def calculateAge():
    today = date.today()
    birthdate = date(int(yearEntry.get(),int(monthEntry.get()),int(dayEntry.get())))
    age = today.year - birthdate.year - ((today.month,today.day) < (birthdate.month, birthdate.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6, column=1)