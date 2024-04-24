import tkinter
import random

screen_width = 750
screen_height = 450

t = tkinter.Tk()
c = tkinter.Canvas(width=screen_width, height=screen_height, bg='white')
c.pack()

x_obj_1, x_obj_2, y_obj_1, y_obj_2 = 700, 700, 50, 300
status = False

def obj_1():
    global x_obj_1, y_obj_1
    #c.create_rectangle(x_obj_1, y_obj_1, x_obj_1 + 10, y_obj_1 + 10, tags='obj_1',fill='black')
    lx = x_obj_1
    ly = y_obj_1
    lo = "obj_1"
    lCol = "black"
    c.create_rectangle(lx, ly, lx+30,ly+12, tags=lo,fill=lCol, outline=lCol)
    c.create_rectangle(lx+22, ly+2, lx+28, ly+7, tags=lo, fill="white", outline="white")
    c.create_rectangle(lx+21, ly+12, lx+30,ly+15, fill=lCol, tags=lo, outline=lCol)
    c.create_rectangle(lx+6, ly+15, lx+30,ly+18, fill=lCol, tags=lo, outline=lCol)
    c.create_rectangle(lx+15, ly+18, lx+39, ly+42, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+15, ly+30, lx+54, ly+54, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx, ly+30, lx+15, ly+34, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx, ly+35, lx+5, ly+44, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+54, ly+30, lx+60, ly+15, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+20, ly+54, lx+25, ly+74, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+35, ly+54, lx+40, ly+74, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+12, ly+74, lx+25, ly+80, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+27, ly+74, lx+40, ly+80, tags=lo, fill=lCol, outline=lCol)

def obj_2():
    global x_obj_2, y_obj_2
    #c.create_rectangle(x_obj_2, y_obj_2, x_obj_2 + 10, y_obj_2 + 10, tags='obj_2',fill='black')
    lx = x_obj_2
    ly = y_obj_2
    lo = "obj_2"
    lCol = "green"
    c.create_rectangle(lx, ly, lx+30,ly+12, tags=lo,fill=lCol, outline=lCol)
    c.create_rectangle(lx+22, ly+2, lx+28, ly+7, tags=lo, fill="white", outline="white")
    c.create_rectangle(lx+21, ly+12, lx+30,ly+15, fill=lCol, tags=lo, outline=lCol)
    c.create_rectangle(lx+6, ly+15, lx+30,ly+18, fill=lCol, tags=lo, outline=lCol)
    c.create_rectangle(lx+15, ly+18, lx+39, ly+42, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+15, ly+30, lx+54, ly+54, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx, ly+30, lx+15, ly+34, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx, ly+35, lx+5, ly+44, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+54, ly+30, lx+60, ly+15, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+20, ly+54, lx+25, ly+74, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+35, ly+54, lx+40, ly+74, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+12, ly+74, lx+25, ly+80, tags=lo, fill=lCol, outline=lCol)
    c.create_rectangle(lx+27, ly+74, lx+40, ly+80, tags=lo, fill=lCol, outline=lCol)

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
    c.bind('<Button-1>', handle_switch)
    global x_obj_1, x_obj_2, y_obj_1, y_obj_2, status
    finish_line = 100
    obj_1_next_move, obj_2_next_move = random.randint(1, 10), random.randint(1, 10)
    if status == True and x_obj_1 > finish_line and x_obj_2 > finish_line:
        c.delete('coords')
        if min(x_obj_1-obj_1_next_move, x_obj_2-obj_2_next_move) > finish_line:
            x_obj_1 -= obj_1_next_move
            x_obj_2 -= obj_2_next_move
        else:
            if  x_obj_1-obj_1_next_move < finish_line and (x_obj_2-obj_2_next_move) < finish_line: # adding situations where they both cross the finish line
                if (x_obj_1-obj_1_next_move) == (x_obj_2-obj_2_next_move):
                    x_obj_1 = finish_line
                    x_obj_2 = finish_line
                    c.create_text(750/2,450/2,text='Remíza',fill='black')
                elif (x_obj_1-obj_1_next_move) < (x_obj_2-obj_2_next_move):
                    x_obj_1 = finish_line
                    x_obj_2 = finish_line + 1
                    c.create_text(750/2,450/2,text='Vyhral obj_1',fill='black')
                else:
                    x_obj_2 = finish_line
                    x_obj_1 = finish_line + 1
                    c.create_text(750/2,450/2,text='Vyhral obj_2',fill='black')
            elif x_obj_1-obj_1_next_move < finish_line and (x_obj_1-obj_1_next_move) < (x_obj_2-obj_2_next_move):
                x_obj_1 = finish_line
                c.create_text(750/2,450/2,text='Vyhral obj_1',fill='black')
            elif x_obj_2-obj_2_next_move < finish_line and (x_obj_1-obj_1_next_move) > (x_obj_2-obj_2_next_move):
                x_obj_2 = finish_line
                c.create_text(750/2,450/2,text='Vyhral obj_2',fill='black')
        print(f'pos1 {x_obj_1}, pos2 {x_obj_2}') # maybe use the distance form finish line?
        if x_obj_1 > finish_line and x_obj_2 > finish_line:
            c.move('obj_1', -obj_1_next_move, 0)
            c.move('obj_2', -obj_2_next_move, 0)
        c.create_text(x_obj_1+obj_1_next_move,y_obj_1-30,text=str(x_obj_1-finish_line),tags='coords',fill='black') #counting the distance from the finish line
        c.create_text(x_obj_2+obj_2_next_move,y_obj_2-30,text=str(x_obj_2-finish_line),tags='coords',fill='black') #counting the distance from the finish line
        c.after(100, handle_race)
    else:
        return 0
        
def main(event):
    global status
    if status == False: # so that you can not run the function more times by more clicks of space...
        status = True
        obj_1()
        obj_2()
        finish()
        handle_race()


c.bind_all('<space>', main)
t.mainloop()