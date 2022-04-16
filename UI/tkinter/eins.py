import tkinter as tk

def hit_me():
    global i
    if i == 1:
        i = 0
        var.set("you hit me")
    else:
        i = 1
        var.set("")

i=1
window = tk.Tk()
window.title("my window")
window.geometry("800x400")
var = tk.StringVar()
l = tk.Label(window,textvariable=var,bg='green',width=40,height=10)
l.pack()
b = tk.Button(window,text="hit me",width=40,height=10,command=hit_me)
b.pack()

window.mainloop()