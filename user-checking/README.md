# User Checking

Even though the API is gone (but also maybe not fully gone) there are still ways to get data from Twitter. It's still a public website that we can browse to. So if we have a list of usernames we can check if they exist, if they're deleted, or if they're suspended.

Aaaaannddd, we may be able to automate this checking

- selenium - a python library to interact with a browser
- chrome - a web browser, but we'll run it in a headless mode (so nothing appears onscreen)

You will need the Chrome Driver for selenium. You can download it from https://chromedriver.chromium.org/downloads
Be sure to add the executable to your `PATH` - on macOS I did this by copying the binary to `/usr/local/bin/chromedriver`

## Installation:


Install selenium with pip:

```
pip3 install selenium
```

---