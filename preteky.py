import tkinter
import random

screen_width = 750
screen_height = 450

t = tkinter.Tk()
c = tkinter.Canvas(width=screen_width, height=screen_height, bg='white')
c.pack()

x_obj_1, x_obj_2, y_obj_1, y_obj_2 = 700, 700, 50, 400
status = False

def obj_1():
    global x_obj_1, y_obj_1
    c.create_rectangle(x_obj_1, y_obj_1, x_obj_1 + 10, y_obj_1 + 10, tags='obj_1',fill='black')

def obj_2():
    global x_obj_2, y_obj_2
    c.create_rectangle(x_obj_2, y_obj_2, x_obj_2 + 10, y_obj_2 + 10, tags='obj_2',fill='black')

def finish():
    c.create_rectangle(95,0,105,450,fill='red')

def handle_switch(event):
    global status
    if status == False:
        status = True
        handle_race()
    else:
        status = False

def handle_race():
    global x_obj_1, x_obj_2, y_obj_1, y_obj_2, status
    finish_line = 100
    obj_1_next_move, obj_2_next_move = random.randint(1, 10), random.randint(1, 10)
    if status == True and x_obj_1 > finish_line and x_obj_2 > finish_line:
        c.delete('coords')
        if min(x_obj_1-obj_1_next_move, x_obj_2-obj_2_next_move) > finish_line:
            
            x_obj_1 -= obj_1_next_move
            x_obj_2 -= obj_2_next_move
        else:
            if x_obj_1-obj_1_next_move < finish_line and (x_obj_1-obj_1_next_move) < (x_obj_2-obj_2_next_move):
                x_obj_1 = finish_line
                c.create_text(750/2,450/2,text='Vyhral obj_1',fill='black')
            elif x_obj_2-obj_2_next_move < finish_line and (x_obj_1-obj_1_next_move) > (x_obj_2-obj_2_next_move):
                x_obj_2 = finish_line
                c.create_text(750/2,450/2,text='Vyhral obj_2',fill='black')
        print(f'pos1 {x_obj_1}, pos2 {x_obj_2}')
        if x_obj_1 > finish_line and x_obj_2 > finish_line:
            c.move('obj_1', -obj_1_next_move, 0)
            c.move('obj_2', -obj_2_next_move, 0)
        c.create_text(x_obj_1+obj_1_next_move,y_obj_1-30,text=x_obj_1,tags='coords',fill='black')
        c.create_text(x_obj_2+obj_2_next_move,y_obj_2-30,text=x_obj_2,tags='coords',fill='black')
        c.after(100, handle_race)
    else:
        return 0
        
def main(event):
    global status
    status = True
    obj_1()
    obj_2()
    finish()
    handle_race()

c.bind('<Button-1>', handle_switch)
c.bind_all('<space>', main)
t.mainloop()
