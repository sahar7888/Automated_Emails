""" Ref: Intermediate to Advanced Python with 10 OOP Projects-Udemy
"""


import yagmail
import pandas
from news import NewsFeed
import datetime
import time

""" Automatically Sending news on an specific topic of interest at a certain time to multiple recipients """
def email_automation():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today,
                         language='en')
    print(news_feed)
    email = yagmail.SMTP(user="saharpythonproject@gmail.com", password="sahar_python_3472")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today",
               contents=f"Hi {row['name']},\n See what is about {row['interest']} today. {news_feed.get()} \n Sahar")


while True:
    if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 21:
        df = pandas.read_excel('Book1.xlsx')

        # print(df)

        for index, row in df.iterrows():
            email_automation()

    time.sleep(60)

