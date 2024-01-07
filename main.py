# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import tkinter
from tkinter import *

def run_gui():
    #top = tkinter.Tk()
    #top.mainloop()

    root = Tk()

    main_menu = Menu(root)
    root.config(menu=main_menu)

    file_menu = Menu(main_menu, tearoff=0)
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Load")

    main_menu.add_cascade(label="File", menu=file_menu)

    main_canvas = Canvas(root, width=800, height=600, background="lightblue")
    main_canvas.pack()

    main_canvas.create_line([1, 2, 3, 4, 5, 6, 7, 8, 80, 90, 100, 200])
    root.mainloop()



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_gui()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
