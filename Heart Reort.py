# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 18:20:19 2022

@author: VIHAAN KATHURIA
"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Heart Report")
root.geometry("400x400")

q1_rb = StringVar(value = "0")
q1 = Label(root,text = "Do you experience  shortness of breath during routine activities?")
q1.pack()
q1_rb1 = Radiobutton(root,text = "Yes",variable = q1_rb,value = "yes")
q1_rb1.pack()
q1_rb2 = Radiobutton(root,text = "No",variable = q1_rb,value = "no")
q1_rb2.pack()

q2_rb = StringVar(value = "0")
q2 = Label(root,text = "Do you have swelling in the feet/ankle/legs(shoes feel tighter or abdomen?")
q2.pack()
q2_rb1 = Radiobutton(root,text = "Yes",variable = q2_rb,value = "yes")
q2_rb1.pack()
q2_rb2 = Radiobutton(root,text = "No",variable = q2_rb,value = "no")
q2_rb2.pack()

q3_rb = StringVar(value = "0")
q3 = Label(root,text = "Do you feel any of these symtoms - confusion,disorientation or loss of memory?")
q3.pack()
q3_rb1 = Radiobutton(root,text = "Yes",variable = q3_rb,value = "yes")
q3_rb1.pack()
q3_rb2 = Radiobutton(root,text = "No",variable = q3_rb,value = "no")
q3_rb2.pack()

q4_rb = StringVar(value = "0")
q4 = Label(root,text = "Do you experience shortness of breath while at rest/lying down?")
q4.pack()
q4_rb1 = Radiobutton(root,text = "Yes",variable = q4_rb,value = "yes")
q4_rb1.pack()
q4_rb2 = Radiobutton(root,text = "No",variable = q4_rb,value = "no")
q4_rb2.pack()

q5_rb = StringVar(value = "0")
q5 = Label(root,text = "Do you experience persistent wheezing/coughing that produces whitee or pink blood tinged mucus?")
q5.pack()
q5_rb1 = Radiobutton(root,text = "Yes",variable = q5_rb,value = "yes")
q5_rb1.pack()
q5_rb2 = Radiobutton(root,text = "No",variable = q5_rb,value = "no")
q5_rb2.pack()

def start():
    score = 0
    if q1_rb.get()=="yes":
        score = score + 20
        print(score)
    if q2_rb.get()=="yes":
        score = score + 20
        print(score)
    if q3_rb.get()=="yes":
        score = score + 20
        print(score)
        
    if q4_rb.get()=="yes":
        score = score + 20
        print(score)
        
    if q5_rb.get()=="yes":
        score = score + 20
        print(score)
        
    if score <= 20:
        messagebox.showinfo("Heart Report","You don't need to visit a doctor")
    
    elif score == 40 or score==60:
        messagebox.showinfo("Heart Report","You might need to visit a doctor")
    
    else:
        messagebox.showinfo("Heart Report","I strongly advise you to visit a doctor")
        
    

btn = Button(root, text = "Heart Report",command = start)
btn.pack()

root.mainloop()
