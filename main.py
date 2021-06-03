from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x300")
window.title("Username and Password")
window["bg"] = "lightyellow"


class Info:
    def __init__(self, window):
        self.username = Label(window, text="Username: ", bg="lightyellow")
        self.username.place(x=150, y=50)
        self.username_entry = Entry(window)
        self.username_entry.place(x=250, y=50)
        self.password = Label(window, text="Password: ", bg="lightyellow")
        self.password.place(x=150, y=90)
        self.password_entry = Entry(window)
        self.password_entry.place(x=250, y=90)
        self.verify = Button(window, text="Verify", command=self.verify, bg="pink")
        self.verify.place(x=50, y=150)
        self.clear = Button(window, text="Clear", command=self.clear, bg="lightblue")
        self.clear.place(x=280, y=150)
        self.exit = Button(window, text="Exit", command=self.exit, bg="lightgreen")
        self.exit.place(x=500, y=150)
        self.data = {'Byron': 'Toby03', 'Zoe': 'Sunshine', 'Ronald': 'Ron_Bon', 'Adam': 'BigJ',
                     'Aneeqah': 'Pierced_Nips', 'Ghiyaath': 'Yaartie'}

    def verify(self):
        user = self.username_entry.get()
        pw = self.password_entry.get()
        if user == "" or pw == "":
            messagebox.showerror(message="Please enter details")

        elif user in self.data:
            if pw == self.data[user]:
                messagebox.showinfo(message="Success")
            else:
                messagebox.showerror(message="Password is incorrect")
        else:
            messagebox.showerror(message="Username not found")

    def clear(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()


obj = Info(window)
window.mainloop()
