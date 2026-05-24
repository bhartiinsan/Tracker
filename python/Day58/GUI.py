

#GUI PROGRAMMING
#TKINTER-----------> STANDARD PYTHON LIB H TO CREATE DEKHSTOP APPLICATION.
#Tk is a class


from tkinter import Tk, Button

root = Tk()

# # root.state("zoomed")     #zoomed at fujlkl screen



root.geometry("700x400")
root.resizable(width=False, height=False)               # set initial width,  height
root.configure(bg="blue")

# root.title("BHARTIII")


b1 = Button(root, text="Sumbit", width=8,
            font=("arial", 20, "bold"), bd=9, fg="blue", bg="pink",
            activebackground="black", activeforeground="purple")

b2 = Button(root, text="ok", width=8,
            font=("arial", 20, "bold"), bd=5,
            activebackground="white", activeforeground="red",
            fg="blue", bg="pink")

b1.place(x=100, y=150)
b2.place(x=250, y=150)

root.mainloop()          # make the window visible

