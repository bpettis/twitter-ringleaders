# User Checking

Even though the API is gone (but also maybe not fully gone) there are still ways to get data from Twitter. It's still a public website that we can browse to. So if we have a list of usernames we can check if they exist, if they're deleted, or if they're suspended.

Aaaaannddd, we may be able to automate this checking

- selenium - a python library to interact with a browser
- chrome - a web browser, but we'll run it in a headless mode (so nothing appears onscreen)


The script works by visiting the Web page for specified Twitter users, and looking at the page content to assess the account status. For example, if it finds the phrase "Twitter suspends accounts that violate the Twitter Rules." - it likely means that the account is suspend.

This _does_ mean that there is a possibility for false positives, because if an active account posts a tweet containing the search terms, it will get flagged accordingly. So things should be double checked, but this is great for working with large numbers at scale. I have included the '`</span>`' in the search phrases to try and only grab the correct markers

## Installation:


Install selenium with pip:

```
pip3 install selenium
```

You will need the Chrome Driver for selenium. You can download it from https://chromedriver.chromium.org/downloads
Be sure to add the executable to your `PATH` - on macOS I did this by copying the binary to `/usr/local/bin/chromedriver`

## Usage

Set the input and output file locations at the top of the script


The script expects to read from a CSV file where the twitter usernames are stored in the 2nd column:

e.g.: 
```
id_str,from_user,text,created_at,time,geo_coordinates,user_lang,in_reply_to_user_id_str,in_reply_to_screen_name,from_user_id_str,in_reply_to_status_id_str,source,profile_image_url,user_followers_count,user_friends_count,user_location,status_url,entities_str

1.26426E+18	PaulMichels17	RT @ZSJusticeL: Ben Affleck enjoying a Cuban while watching #ZackSnydersJusticeLeague being released. https://t.co/kUinnUDZG1	Sat May 23 18:01:55 +0000 2020	23/05/2020 19:01:55					1.19615E+18		<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>	http://pbs.twimg.com/profile_images/1196153268205961217/RQo0WOvS_normal.jpg	79	47		http://twitter.com/PaulMichels17/statuses/1264255250585849857	{"hashtags":[{"text":"ZackSnydersJusticeLeague","indices":[60,85]}],"symbols":[],"user_mentions":[{"screen_name":"ZSJusticeL","name":"ZSJL 05.20.21","id":78358011,"id_str":"78358011","indices":[3,14]}],"urls":[],"media":[{"id":1264189302424039400,"id_str":"1264189302424039424","indices":[102,125],"media_url":"http://pbs.twimg.com/tweet_video_thumb/EYtNePvVcAA3uO1.jpg","media_url_https":"https://pbs.twimg.com/tweet_video_thumb/EYtNePvVcAA3uO1.jpg","url":"https://t.co/kUinnUDZG1","display_url":"pic.twitter.com/kUinnUDZG1","expanded_url":"https://twitter.com/ZSJusticeL/status/1264189377359429632/photo/1","type":"photo","sizes":{"large":{"w":512,"h":218,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"medium":{"w":512,"h":218,"resize":"fit"},"small":{"w":512,"h":218,"resize":"fit"}},"source_status_id":1264189377359429600,"source_status_id_str":"1264189377359429632","source_user_id":78358011,"source_user_id_str":"78358011"}]}
```

Note that the usernames should be listed with _only_ the username, and nothing else. (no @, or twitter.com prefixes)