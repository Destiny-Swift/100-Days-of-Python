import smtplib

sender_email = 'goldenswiftmk1@gmail.com'
password = 'koqf vilr ptqk qeno'

# recipient_email = 'destinyreubenchima@gmail.com'


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    @staticmethod
    def create_message(price,
                       city_from,
                       fly_from,
                       city_to,
                       fly_to,
                       departure_date,
                       return_date,
                       book_link):
        return (f'Subject: Low Price Alert!\n\n'
                f'Low Price Alert!\nOnly ₦{price} to fly from {city_from}-{fly_from} to {city_to}-'
                f'{fly_to}, from {departure_date} to {return_date}'
                f'\n\nBook flight now:\n{book_link}').encode('utf-8')

    @staticmethod
    def send_emails(email_list, message):
        for email in email_list:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  # send email
                connection.login(sender_email, password)

                connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=email,
                    msg=message
                )
