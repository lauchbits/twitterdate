import tweepy
import datetime

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                    consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token=ACCESS_KEY,
                    access_token_secret=ACCESS_SECRET)

auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


day = int(datetime.datetime.now().day)
appendix = "th"
if (day % 10 == 1):
    appendix = "st"
elif (day % 10 == 2):
    appendix = "nd"
elif (day % 10 == 3):
    appendix= "rd"

month = int(datetime.datetime.now().month)
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = months[month - 1]

year = datetime.datetime.now().year

week_day = datetime.datetime.now().weekday()
week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
week_day = week_days[week_day]

text = f'Today is {week_day} the {day}{appendix} of {month} {year}'

client.create_tweet(text=text)
