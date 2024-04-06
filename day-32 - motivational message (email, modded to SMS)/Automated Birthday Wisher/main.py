import datetime
import smtplib
import pandas as pd
import random

# mechanism used to add 'gemini.ai' file path to be searched when searching for directories
# import sys
# sys.path.append('../')
# from gemini_ai import gemini_ai


# get database
link = 'https://docs.google.com/spreadsheets/d/1LC8bLz4YJSydFmGxwv1151f84xDs5pxFtezWV2M5vok/export?format=csv'
database = pd.read_csv(link)

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)

# print(database)


# send mail function
my_email = 'goldenswiftmk1@gmail.com'
password = 'koqf vilr ptqk qeno'


def send_mail(recipient_email, recipient_name, recipient_remark):

    # get letter

    with open(f'letter_templates/letter_{random.choice([1, 2, 3])}.txt', 'r') as random_letter:
        letter = random_letter.read().replace('[NAME]', recipient_name)

    # letter = gemini_ai(
    #     f'''
    #     Write a birthday message from me, Swift, to my friend, {recipient_name}.
    #     {recipient_remark}
    #     '''
    # )

    print(f'This is the letter:\n{letter}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        # connection.starttls()
        connection.login(my_email, password)

        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=f'Subject: Happy Birthday!\n\n{letter}'
                            )


now = datetime.datetime.now()
this_day = now.day
this_month = now.month


for index, birthday in enumerate(database['Birthday']):
    month = int(birthday.split('/')[0
                ])
    day = int(birthday.split('/')[1])
    name = database['First Name'][index]
    email = database['Email Address'][index]
    remark = database['Remark']

    if month == this_month and day == this_day:
        send_mail(email, name, remark)

# Code up and running on pythonanywhere and I no longer care to get a perfect IDE tick.
