from tkinter import Button, Label, Entry, Tk, Canvas
from sympy import N
from math import sqrt

task = input('введите номер задания: ')

if task == '1':
    def up():
        print('up')


    def down():
        print('down')


    def left():
        print('left')


    def right():
        print('right')

    root = Tk()
    root.geometry('100x100')

    b_up = Button(root, text='↑', command=up)
    b_down = Button(root, text='↓', command=down)
    b_left = Button(root, text='←', command=left)
    b_right = Button(root, text='→', command=right)
    b_up.pack(side='top')
    b_down.pack(side='bottom')
    b_left.pack(side='left')
    b_right.pack(side='right')

    root.mainloop()

elif task == 2:
    def command():
        expression = entry.get()
        result = N(expression)
        l['text'] = str(result)

    root = Tk()
    root.geometry('250x100')

    entry = Entry(root, width=25)
    entry.place(x=20, y=20)

    b = Button(root, text='=', command=command)
    b.place(x=20, y=50)

    l = Label(root)
    l.place(x=80, y=55)

    root.mainloop()

elif task == 3:
    def move_to_click(event):
        global circle_x, circle_y, animation_id

        if animation_id:
            root.after_cancel(animation_id)

        target_x = event.x
        target_y = event.y

        animate(circle_x, circle_y, target_x, target_y)


    def animate(start_x, start_y, target_x, target_y):
        global circle_x, circle_y, animation_id

        dx = target_x - circle_x
        dy = target_y - circle_y
        distance = sqrt(dx ** 2 + dy ** 2)

        if distance < speed:
            circle_x = target_x
            circle_y = target_y
            update_circle_position()
            return

        dx = dx / distance * speed
        dy = dy / distance * speed

        circle_x += dx
        circle_y += dy

        update_circle_position()

        animation_id = root.after(20, lambda: animate(circle_x, circle_y, target_x, target_y))


    def update_circle_position():
        canvas.coords(
            circle,
            circle_x - circle_radius,
            circle_y - circle_radius,
            circle_x + circle_radius,
            circle_y + circle_radius
        )


    root = Tk()
    root.title("Движение круга к точке клика")

    circle_x = 250
    circle_y = 200
    circle_radius = 20
    speed = 5
    animation_id = None

    canvas = Canvas(root, width=500, height=400, bg='white')
    canvas.pack()

    circle = canvas.create_oval(
        circle_x - circle_radius,
        circle_y - circle_radius,
        circle_x + circle_radius,
        circle_y + circle_radius,
        fill='blue'
    )

    canvas.bind('<Button-1>', move_to_click)

    root.mainloop()


