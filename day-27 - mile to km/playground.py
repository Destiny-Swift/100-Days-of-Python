import tkinter as tk

# creating a window
window = tk.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text='I am a Label', font=('Arial', 24, 'bold'))
my_label.pack()


button_toggle = 0


# Button
def button_clicked():
    global button_toggle

    if button_toggle == 0:
        button_toggle = 1
        my_label.config(text='I got clicked')
        print('I got clicked')
    else:
        button_toggle = 0
        my_label.config(text='I am a Label')
        print('New Text')

    # get text in the entry
    # my_label.config(text=input1.get())


button = tk.Button(text='Click Me', font='Arial', command=button_clicked)  # calls button_clicked when pressed
button.pack()


# Entry
input1 = tk.Entry(width=40)
# add some text to begin with
input1.insert(0, string='Some text to begin with')
input1.pack(pady=10)  # input1 is used up 👆

# Text
text = tk.Text(height=10, width=45)
# puts cursor in text to begin with
text.focus()
# add some text to begin with

text.insert(chars='Example of multi-line text entry', index=tk.END)

text.pack()


# Spinbox
def spinbox_used():
    # gets current value in spinbox
    print(spinbox.get())


spinbox = tk.Spinbox(from_=-10, to=10, width=5, command=spinbox_used)
spinbox.pack(pady=5)


# Scale
# called with current scale value
def scale_used(value):
    print(value)


scale = tk.Scale(from_=0, to=150, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # prints 1 if on button checked, else 0
    print(checked_state.get())


# variable to hold checked_state, 0=off, 1=on
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text='Is on?', variable=checked_state)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# variable to hold which radiobutton value is checked
radio_state = tk.IntVar()

radiobutton1 = tk.Radiobutton(text='Option 1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text='Option 2', value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):  # Dang Tkinter module and PEP - unused parameter 😤😤
    # gets current selection from listbox

    print(listbox.get(listbox.curselection()))


listbox = tk.Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()


window.mainloop()
