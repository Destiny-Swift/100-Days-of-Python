from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0

timer = None  # we have to save the recursion trick to a variable to enable us cancel it later on 😫

# need to stay above rest of code
window = Tk()
window.minsize(width=480, height=100)

# title
title_label = Label(text='Timer', font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# store marks
marks = []

# some variable for preventing hitting thr=e start button twice and creating simultaneous timers 😤
timer_started = False

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global marks, timer, timer_started
    marks = []

    title_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    window.after_cancel(str(timer))  # some warning I can't get rid of. Dang 😤 (got rid of 10:34, 1/16/24 🌚)
    check_marks.config(text='')

    timer_started = False

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global timer_started

    if not timer_started:  # if timer_started == False; bt PEP wouldn't let me 🙂
        timer_started = True

        global REPS

        REPS += 1  # so it works with our if statements 🙄

        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if REPS in [1, 3, 5, 7]:
            count_down(work_sec)
            title_label.config(text='Work', fg=GREEN)

        elif REPS in [2, 4, 6]:
            count_down(short_break_sec)
            title_label.config(text='Break', fg=PINK)

        elif REPS == 8:
            count_down(long_break_sec)
            title_label.config(text='Break', fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = count // 60
    seconds = count % 60

    if len(str(minutes)) < 2:
        minutes = f'0{minutes}'

    if len(str(seconds)) < 2:
        seconds = f'0{seconds}'

    new_time = f'{minutes}:{seconds}'

    canvas.itemconfig(timer_text, text=new_time)

    if count >= 0:  # >= so zero gets displayed in the timer
        global timer

        timer = window.after(1000, count_down, count - 1)
    else:
        global timer_started
        timer_started = False
        start_timer()  # for sake of 4th pomodoro mark showing

        if REPS % 2 == 0:
            marks.append('✔')
            check_marks.config(text=''.join(marks), font=(FONT_NAME, 12, 'bold'))


# ---------------------------- UI SETUP ------------------------------- #

window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)

# text
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 40, 'bold'), fill='white')
canvas.grid(row=1, column=1)


# Buttons
# start
start_button = Button(text='Start', bg='white', highlightthickness=True, command=start_timer)
start_button.grid(row=2, column=0)

# reset
reset_button = Button(text='Reset', bg='white', highlightthickness=False, command=reset_timer)
reset_button.grid(row=2, column=2)


# indicator
check_marks = Label(text='', bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)


window.mainloop()
