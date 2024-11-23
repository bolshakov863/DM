from tkinter import*

# область переменных
w =
h =
player_size =
x1, y1 =
player1_color =
x_finish =

# область функций
def key_handler(event):
    pass

# область создания окна и холста
window = Tk()
window.title('Догони меня если сможешь')
canvas = Canvas(window, width=w, height=h, bg='white')

#область объектов
player1_id =
finish_id =

# область вызова
window.bind('<KeyRelease>', key_handler)
window.mainloop()