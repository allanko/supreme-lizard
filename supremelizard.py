# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import mediacloud, datetime, tweepy, random

# load config
parser = SafeConfigParser()
parser.read('config.txt')
MY_API_KEY = parser.get('MEDIACLOUD', 'MY_API_KEY')
mc = mediacloud.api.MediaCloud(MY_API_KEY)

# top ten words of the last 7 days from mediacloud
sources = 'media_sets_id:1' # us mainstream media
query = '*'

step = datetime.timedelta(2)
today = datetime.date.today() 

stories = mc.storyList(query, solr_filter = [mc.publish_date_query(today - step, today), sources], rows = 50)
headlines = [s['title'] for s in stories if 'Trump' in s['title']]
pick = random.choice(headlines)
if 'Donald Trump' in pick:
    print pick.replace('Donald Trump', 'Supreme Lizard')
elif 'the Trump' in pick:
    print pick.replace('the Trump', 'Supreme Lizard')
else:
    print pick.replace('Trump', 'Supreme Lizard')

# tweeting
CONSUMER_KEY = parser.get('TWITTER', 'CONSUMER_KEY')
CONSUMER_SECRET = parser.get('TWITTER', 'CONSUMER_SECRET')
ACCESS_KEY = parser.get('TWITTER', 'ACCESS_KEY')
ACCESS_SECRET = parser.get('TWITTER', 'ACCESS_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(' '.join(words))