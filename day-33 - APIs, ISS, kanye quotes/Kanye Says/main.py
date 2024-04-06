from tkinter import *
import requests


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text='Kanye quote goes here', width=250, font=("Arial", 20, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)


def get_quote():
    pass
    # Write your code here.
    quote = requests.get("https://api.kanye.rest").json()['quote']
    canvas.itemconfig(quote_text, text=quote)
    # maybe something in the recent version of python or something, but I should've been able to reference 'canvas'
    # despite declaring it after the function


get_quote()

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
