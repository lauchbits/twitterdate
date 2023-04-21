import tweepy
import datetime

CONSUMER_KEY = '1kkd8Lov88a42EOBxXYC3G2Yl'
CONSUMER_SECRET = 'P3I465NNhIFU9smml497tOCWJ7KXxmB4xyxM5CuI3AuXoCa9uu'
ACCESS_KEY = '1570059201367384066-Ni8vTSPzzWS0vnOtJkZWuLJskWq2Px'
ACCESS_SECRET = 'XzCI2ZXMspM0iCAKAorAqbe5UMzIbgof1Dhw94xpVNDvY'
BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAAE5NhAEAAAAAa6HROMoIT2C5QIYAj5d8NFhDoO4%3DmMIAiPTOmygI5820MIXOu1VMzlNzjKNH4X0ZhcO0bhTFKsW2n2"


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