from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    checklabel.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN #*60
    short_break_sec = SHORT_BREAK_MIN #*60
    long_break_min = LONG_BREAK_MIN #*60

    if reps %2 ==0:
        count_down(work_sec)
        label.config(text="Work", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
    elif reps % 2 !=0 and reps!=7:
        count_down(short_break_sec)
        label.config(text="Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=PINK)
    elif reps ==7:
        count_down(long_break_min)
        label.config(text="Break", font=(FONT_NAME, 40, "bold"), bg=RED, fg=RED)
    reps +=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec<10:
        count_sec = f"0{count_sec}"
    if count_min<10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        checklabel.config(text = f"{math.floor(reps/2)*'✓'}")
        window.attributes('-topmost', True)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.config(padx=100,pady=50,bg = YELLOW)

canvas = Canvas(width=220,height=224,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105,112,image = tomato_img)

timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

#Button to make the screen go below:

def toggle_topmost(event):
    # Disable the topmost attribute
    window.attributes('-topmost', False)
window.bind('<Button-1>', toggle_topmost)

#Label

label = Label(text="Timer", font=(FONT_NAME, 30, "bold"),bg=YELLOW,fg=GREEN)
label.grid(row=0,column=1)


checklabel = Label(text="", font=(FONT_NAME, 30, "bold"),bg=YELLOW,fg=GREEN)
checklabel.grid(row=3,column=1)
#Buttons


#Button start
start = Button(text="start", command=start_timer,width=10, height=2,bg=GREEN, fg='white', font=(FONT_NAME, 10, "bold"),highlightthickness=0)
start.grid(row=2,column=0)


#Buttons

#Button reset
reset = Button(text="reset", command=reset_timer,width=10, height=2, bg=GREEN, fg='white', font=(FONT_NAME, 10, "bold"),highlightthickness=0)
reset.grid(row=2,column=2)



window.mainloop()