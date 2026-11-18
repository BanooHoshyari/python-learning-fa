from tkinter import Tk, Label, Button, Entry,Grid

window = Tk()
window.title("test")
window.geometry("600x500+200+100")
text_label = Label(window, text="Hello World", bd=1, fg="blue", bg="lightgray", width=10, height=3)

text_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2,sticky="nsew",path=5)

empty_box = Entry(window, width=50, bd=2)
empty_box.grid(row=1, column=0, padx=10, pady=10, columnspan=2,sticky="nsew",path=5)
empty_box1 = Entry(window, width=50, bd=2)
empty_box1.grid(row=1, column=2, padx=10, pady=10, columnspan=2,sticky="nsew",path=5)


def test1():
    try:
        x = int(empty_box.get())
        y = int(empty_box1.get())
    except ValueError:
        text_label.config(text="Please enter numbers")
        return

    text_label.config(text=str(x + y))


btn=Button(window, text="+", command=test1)
btn.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

window.mainloop()