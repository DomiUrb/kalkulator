from tkinter import Tk, Label, Button

def click_action(button):
    button.config(text = f'Wow!')


root = Tk()
root.title('Moja aplikacja')
root.geometry("600x400")

click_button = Button(root,text="Kliknij!", width=8)
click_button.config(command=lambda: click_action(click_button))
label = Label(root, text="Witaj w moim programie!", font=30, fg="blue")
label.pack()
click_button.pack()

root.mainloop()
