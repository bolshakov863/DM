from tkinter import *

# область переменных
w = 800
h = 500
player_size = 100
x1, y1 = 50, 50
player1_color = 'red'
x_finish = w - 50

# область функций
def key_handler(event):
    canvas.move(player1_id, 10,0)

# область создания окна и холста
window = Tk()
window.title('Догони меня если сможешь')
canvas = Canvas(window, width=w, height=h, bg='white')
canvas.pack()

#область объектов
player1_id = canvas.create_rectangle(x1,y1, x1 + player_size,y1 + player_size, fill = player1_color)
finish_id = canvas.create_rectangle(x_finish, 0, x_finish + 10, h, fill ='black')

# область вызова
window.bind('<KeyRelease>', key_handler)
window.mainloop()