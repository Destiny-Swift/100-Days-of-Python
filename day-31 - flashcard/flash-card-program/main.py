from tkinter import *
import pandas
import random

# CONSTANTS
BACKGROUND_COLOR = '#B1DDC6'

window = Tk()
window.title('Flash')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

try:
    data = pandas.read_csv('data/words_to_learn')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')

to_learn = data.to_dict(orient='records')

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancelling the timer operation next_card() before after
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_text, text=current_card['French'], fill='black')

    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_text, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)  # PhotoImage must be saved in a variable before use


def is_known():
    to_learn.remove(current_card)
    next_card()

    # reading would start from this file unless empty, which would e caught by an exception; up 👆
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv('./data/words_to_learn.csv', index=False)


# canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Arial', 25, 'italic'))
card_text = canvas.create_text(400, 263, text='', font=('Arial', 50, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


flip_timer = window.after(3000, flip_card)

next_card()  # called after flip_timer declaration to solve NameError 🙂


window.mainloop()
