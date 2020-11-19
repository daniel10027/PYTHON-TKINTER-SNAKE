import tkinter as tk
import random

global Row, Column
Row = 20
Column = 20
Unit_size = 20
Height = Row * Unit_size
Width = Column * Unit_size
global Direction
Direction = 2
global FPS
FPS = 150
global Have_food
Have_food = 0
global Food_coord
Food_coord = [0, 0]
global Score
Score = 0
global snake_list
snake_list = [[11, 10], [10, 10], [9, 10]]
global game_map
game_map = []

def draw_a_unit(canvas, col, row, unit_color = "green") :
    
    x1 = col * Unit_size
    y1 = row * Unit_size
    x2 = (col + 1) * Unit_size
    y2 = (row + 1) * Unit_size
    
    canvas.create_rectangle(x1, y1, x2, y2, fill = unit_color, outline = "white")
def put_a_backgroud(canvas, color = 'silver') :
    # Building pixel grid on canvas
    for x in range(Column) :
        for y in range(Row) :
            draw_a_unit(canvas, x, y, unit_color = color)
            game_map.append([x, y])
def draw_the_snake (canvas, snake_list, color = 'green') :
   
    for i in snake_list :
        draw_a_unit(canvas, i[0], i[1], unit_color = color)
def snake_move(snake_list, dire) :
    
    global Row, Column
    global Have_food
    global Food_coord
    global Score
    new_coord = [0, 0]
    if dire % 2 == 1:
        new_coord[0] = snake_list[0][0]
        new_coord[1] = snake_list[0][1] + dire
    else :
        new_coord[0] = snake_list[0][0] + (int)(dire / 2)
        new_coord[1] = snake_list[0][1]
    snake_list.insert(0, new_coord)
    
    for coord in snake_list :
        if coord[0] not in range(Column) :
            coord[0] %= Column
            break
        elif coord[1] not in range(Row) :
            coord[1] %= Row
            break
    if snake_list[0] == Food_coord :
        draw_a_unit(canvas, snake_list[0][0], snake_list[0][1], )
        Have_food = 0
        Score += 10
        str_score.set('Your Score:' + str(Score))
    else :
        
        draw_a_unit(canvas, snake_list[-1][0], snake_list[-1][1], unit_color = "silver")
        draw_a_unit(canvas, snake_list[0][0], snake_list[0][1], )
        snake_list.pop()
    return snake_list

def callback (event) :
    
    global Direction
    ch = event.keysym
    if  ch == 'Up':
        if snake_list[0][0] != snake_list[1][0] :
            Direction = -1
    elif ch == 'Down' :
        if snake_list[0][0] != snake_list[1][0] :
            Direction = 1
    elif ch == 'Left' :
        if snake_list[0][1] != snake_list[1][1] :
            Direction = -2
    elif ch == 'Right' :
        if snake_list[0][1] != snake_list[1][1] :
            Direction = 2
    return


def snake_death_judge (snake_list) :
    
    set_list = snake_list[1 :]
    if snake_list[0] in set_list :
        return 1
    else :
        return 0
def food(canvas, snake_list) :
   
    global Column, Row, Have_food, Food_coord
    global game_map
    if Have_food :
        return
    Food_coord[0] = random.choice(range(Column))
    Food_coord[1] = random.choice(range(Row))
    while Food_coord in snake_list :
        Food_coord[0] = random.choice(range(Column))
        Food_coord[1] = random.choice(range(Row))
    draw_a_unit(canvas, Food_coord[0], Food_coord[1], unit_color = 'red')
    Have_food = 1
def game_loop() :
    global FPS
    global snake_list
    win.update()
    food(canvas, snake_list)
    snake_list = snake_move(snake_list, Direction)
    flag = snake_death_judge(snake_list)
    if flag :
        over_lavel = tk.Label(win, text = 'Game Over', font = ('Regular script', 25), width = 15, height = 1)
        over_lavel.place(x = 40, y = Height / 2, bg = None)
        return
    win.after(FPS, game_loop)
    

win = tk.Tk()
win.title('Python Snake')
canvas = tk.Canvas(win, width = Width, height = Height + 2 * Unit_size)
canvas.pack()
str_score = tk.StringVar()
score_label = tk.Label(win, textvariable = str_score, font = ('Regular script', 20), width = 15, height = 1)
str_score.set('Your Score:' + str(Score))
score_label.place(x = 80, y = Height)
put_a_backgroud(canvas)
draw_the_snake(canvas, snake_list)

canvas.focus_set()
canvas.bind("<KeyPress-Left>",  callback)
canvas.bind("<KeyPress-Right>", callback)
canvas.bind("<KeyPress-Up>",    callback)
canvas.bind("<KeyPress-Down>",  callback)
#Game progress code
game_loop()
win.mainloop()