from tkinter import *
root=Tk()
root.geometry("600x600")
root.resizable(0,0)
root.title("Welcome To Login Page")
un=Label(root,text="Enter Name",font=("Arial",25))
un.grid(row=0,column=0,pady=25,sticky="W")

d1=Entry(root,font=("Arial",20))
d1.grid(row=0,column=1,pady=25)

un1=Label(root,text="Enter Password",font=("Arial",25))
un1.grid(row=1,column=0,pady=25)

d2=Entry(root,font=("Arial",20),textvariable="password",show="*")
d2.grid(row=1,column=1,pady=25)

c=Button(root,text="Login",font=("Arial",20))
c.grid(row=2,column=0,columnspan=2,pady=25)

root.mainloop()
