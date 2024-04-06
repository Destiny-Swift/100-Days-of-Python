import datetime
import smtplib
import random

# get quotes
with open("quotes.txt", 'r', encoding='utf-8') as quotes_file:
    all_quotes = quotes_file.readlines()
    quote = random.choice(all_quotes)

# set function to send email
sender_email = 'goldenswiftmk1@gmail.com'
password = 'koqf vilr ptqk qeno'
recipient_email = 'reubenchimadestiny@gmail.com'


def send_mail():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(sender_email, password)

        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg=f"Monday Motivation\n\n{quote}"
                            )


# send email on Monday
weekday = datetime.datetime.now().weekday()
if weekday == 0:
    send_mail()

# Improve by pulling quotes off an API or database and sending via SMS
