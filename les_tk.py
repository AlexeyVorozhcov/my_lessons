import tkinter as tk

main_win = tk.Tk()
main_win.title('My Programm')
w, h, x, y = 500, 500, 200, 200
fstroka = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)
main_win.geometry(fstroka)
main_win.resizable(True, True)
main_win.minsize(400,400)
main_win.maxsize(600,600)

icon = tk.PhotoImage(file = 'icon.png')
main_win.iconphoto(False, icon)

main_win.config(bg='#EFF0F3')

main_win.mainloop()