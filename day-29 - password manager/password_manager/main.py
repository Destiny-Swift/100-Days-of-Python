from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# set up windows
window = Tk()


# ------------------------------------------ CONSTANTS ----------------------------------------------- #

FONT = ('Arial', 11)


# ----------------------------------------- NEED TO BE DEFINED UP (Dang) --------------------------------------#

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)


# ------------------------------------------- PASSWORD GENERATOR-------------------------------------------------- #
def generate_password():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    symbols = list('''!#$%&()*+''')

    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(num_letters)]
    password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
    password_numbers = [random.choice(numbers)for _ in range(num_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)  # copies generated password to clipboard for pasting 😎


# ------------------------------------------- SAVE PASSWORD-------------------------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops', message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f'''These are the details entered: 
        \nEmail/Username: {email} \nPassword: {password}
        \nIs it okay to save?''')

        if is_ok:

            try:
                with open('data.json', 'r') as database:
                    data = json.load(database)

            except FileNotFoundError:
                with open('data.json', 'w') as database:
                    json.dump(new_data, database, indent=4)

            else:
                # updating old data; making new data
                data.update(new_data)

                # writing new data
                with open('data.json', 'w') as database:
                    json.dump(data, database, indent=4)

            finally:  # just had to complete it 🙂
                # clear after getting values
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

                messagebox.showinfo(title='Password Added', message='Success')

        else:
            password_entry.focus()


# --------------------------------------------FIND PASSWORD---------------------------------------------#
def find_password():

    website = website_entry.get()

    try:
        with open('data.json') as database:
            data = json.load(database)

    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No data file found')

    else:

        if website in data:
            email = data[website]['email']
            password = data[website]['password']

            messagebox.showinfo(title=website, message=f'Email: {email} \nPassword: {password}')
            pyperclip.copy(password)

        else:
            messagebox.showerror(title='Error', message='No details fot the file exists')


# ------------------------------------------- UI SETUP-------------------------------------------------- #
window.title('Password Manager')
window.minsize(width=530, height=300)
window.config(padx=60, pady=60)

# image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# labels
website_label = Label(text='Website:', font=FONT)
website_label.grid(row=1, column=0)

email_username_label = Label(text='Email/Username:', font=FONT)
email_username_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=FONT)
password_label.grid(row=3, column=0)


# entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, pady=3)
website_entry.focus()

email_username_entry = Entry(width=43)
email_username_entry.grid(row=2, column=1, columnspan=2, pady=3)
email_username_entry.insert(END, 'reubenchimadestiny@gmail.com')


# buttons
generate_button = Button(text='Generate', command=generate_password, bg='white')
generate_button.grid(row=3, column=2, pady=2)

add_button = Button(text='Add', width=36, command=save_password, bg='white')
add_button.grid(row=4, column=1, columnspan=2)


search_button = Button(text='Search', width=7, bg='sky blue', command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
