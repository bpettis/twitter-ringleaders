# Line Charts

These scripts were developed after the histogram scripts. As the name implies, they create line charts (to more easily view some of the trends)
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

---

# To-Do

[] Write Readme for the retweet and combined charting scripts
[] include some example data in the repo