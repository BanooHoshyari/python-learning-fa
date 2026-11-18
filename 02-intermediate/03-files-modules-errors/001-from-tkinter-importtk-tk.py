from tkinter import Entry, Tk, Label
window=Tk()
window.title("test")
window.geometry("600x500+200+100")
lable1=Label(window, text="Hello World",bd=1,fg="blue",bg="lightgray",width=200, height=50 )
taxbox=Entry(window, text="Hello World",bd=1,fg="blue",bg="lightgray",width=200, height=50 )
lable1.pack()
taxbox.pack()

window.mainloop()



