# histograms

The goal of this script (or possibly scripts) is to take the input data from the scrapped Twitter sets and create a histogram of tweet frequency. This gives a visual representation of how each trend/phenomenon unfolded - e.g. whether it was sustained tweeting over several days, or if there were "waves" of activity.

Next, we create an additional histogram - this time just representing tweets by tweeters on our "suspects list" - the folks who were tweeting most frequently. We want to determine if there is a correlation between their activity and what the masses were tweeting. Is there a distinct "lead time" that might be a result of these people "instigating" others to participate? Or is it largely just noise?

It would be possible to create this kind of histogram using an Excel PivotTable and PivotChart, but Excel _sucks_ when working with these enormous sets of data, and would likely require someone to manually select usernames for the filter criteria. That sucks so let's not do that.

## chart-all.py

This script takes an input CSV and charts the frequency of _all_ tweets - grouped by hour.

Basic usage:

```
python3 chart-all.py -i [INPUT CSV FILE] -o [OUTPUT PNG FILE]
```

There are some additional options, such as setting a chart title and specifying which column contains the timestamps

Run with the `-h` flag to display all command line arguments

Example:

```
python3 chart-all.py -i ../data/batman.csv -o batman-all.png -t "Batman - Frequency of All Tweets"
```