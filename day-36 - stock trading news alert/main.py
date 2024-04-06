import requests
from datetime import datetime
# import html
# from twilio.rest import Client
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
stock_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
api_key = '6B4JY3FGOIPDPI96'
stock_params = {
    'symbol': STOCK,
    'apikey': api_key,
}

response = requests.get(stock_url, params=stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
# print(stock_data)


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
last_stock_close = float([item for item in stock_data.values()][0]['4. close'])
penultimate_stock_close = float([item for item in stock_data.values()][1]['4. close'])

stock_difference = last_stock_close - penultimate_stock_close
percentage_stock_change = round((stock_difference / penultimate_stock_close) * 100, 2)
# print(percentage_stock_change)

if abs(percentage_stock_change) >= 0.1:
    # print('Get News')

    # STEP 2: Use https://newsapi.org
    news_url = 'https://newsapi.org/v2/everything'
    news_api_key = 'f503222cd27947ccb6ef13b3b59ab127'
    news_params = {
        'qInTitle': 'Tesla',
        'from': f'{datetime.now().date}',  # f'{datetime.now().date}',
        'language': 'en',
        'sort_by': 'relevancy',
        'apiKey': news_api_key,
        'pageSize': 3,  # I only get the first 3 news articles
        # 'page': 2,
        # 'sources': ''
    }

    response = requests.get(news_url, params=news_params)
    response.raise_for_status()
    news = response.json()
    # print(news)

    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_pieces = [
        {
            'title': news_article['title'],
            'content': news_article['content'].split('[+')[0]
        }
        for news_article in news['articles']
    ]

    # STEP 3: Use https://www.twilio.com

    # Send a separate message with the percentage change and each article's title and description to your phone number.
    for piece in news_pieces:
        # Email
        sender_email = 'goldenswiftmk1@gmail.com'
        password = 'koqf vilr ptqk qeno'
        recipient_email = 'destinyreubenchima@gmail.com'

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  # send email
            connection.login(sender_email, password)

            connection.sendmail(
                from_addr=sender_email,
                to_addrs=recipient_email,
                msg=(f"Subject: "
                     f"TSLA: {'🔺' if last_stock_close > penultimate_stock_close else '🔻'}{percentage_stock_change}%"
                     f"\n\nHeadline: {piece['title']}"
                     f"\nBrief: {piece['content']}").encode('utf-8')
            )
        print('Email Sent')

        # SMS - fucking twilio asking to upgrade my account after I've exhausted the free credit
        # twilio_account_sid = 'AC5d701f98f98deb06a18944c0c5c3851a'
        # twilio_auth_token = '4a43d3ecbde6e50f187055a1511b18c0'
        # client = Client(twilio_account_sid, twilio_auth_token)
        #
        # message = client.messages.create(
        #     body=f""
        #          f"TSLA: {'🔺' if last_stock_close > penultimate_stock_close else '🔻'}{percentage_stock_change}%"
        #          f"\nHeadline: {html.escape(piece['title'])}"
        #          f"\nBrief: {html.escape(piece['content'])}",
        #     from_='+12569603009',
        #     to='+2347012222695'
        # )
        #
        # print(message.sid)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.

or

TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
"""
