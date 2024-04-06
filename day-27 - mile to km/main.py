from tkinter import *

FONT = ('Arial', 14, 'normal')

window = Tk()
window.title('Mile to KM Converter')
# window.minsize(width=400, height=150)
window.config(pady=40, padx=40, bg='#EEEEEE')

is_equal_label = Label(text='is equal to', font=FONT, fg='#00ADB5', bg='#EEEEEE')
is_equal_label.grid(column=0, row=1)


miles_input = Entry(width=10, font=FONT, fg='#222831', bg='#EEEEEE')
miles_input.grid(column=1, row=0)


km_result_label = Label(text=0, font=FONT, fg='#00ADB5')
km_result_label.grid(column=1, row=1)


def miles_to_km():
    if miles_input.get() == '':
        miles = 0
    else:
        try:
            miles = float(miles_input.get())
            km = round(miles / 0.6213711922, 2)
            km_result_label.config(text=f'{km}')
        except ValueError:
            miles = 0
            km_result_label.config(text='Behave nah...')


# continuous function in Tkinter GUI, using what we have alongside recursion
def running():
    miles_to_km()
    window.after(ms=100, func=running)


running()

calculate_button = Button(text='Calculate', command=miles_to_km, font=FONT)
# calculate_button.grid(column=1, row=2)  # don't need the calculate button when we've got instant calculation 😎


miles_label = Label(text='Miles', font=FONT, fg='#393E46', bg='#EEEEEE')
miles_label.grid(column=2, row=0)


km_label = Label(text='KM', font=FONT, fg='#393E46', bg='#EEEEEE')
km_label.grid(column=2, row=1)


window.mainloop()
