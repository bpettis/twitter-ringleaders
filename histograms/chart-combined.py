#! /bin/python3

import csv, argparse
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



# Setup command line arguments:
argParser = argparse.ArgumentParser(description='''
**Twitter Histogram Generator (Retweets Only) **


This silly little program takes an input CSV file containing tweets and generates a histogram of tweet frequency.
It's a great way to visualize trends of Twitter activity.
                                    
This script will chart multiple series:
    - all tweets
    - the frequency of Retweets - based on the text beginning with "RT @"
    - tweets by specified "top users" - based on an input TXT file of usernames.
    
Created by Ben Pettis''',
    usage='''%(prog)s -i [input file] -o [output file]
run "%(prog)s --help" to view more information''',
    formatter_class=argparse.RawTextHelpFormatter
)
argParser.add_argument("-i", "--input", required=True, help="Path to the CSV file to read from")
argParser.add_argument("-o", "--output", required=True, help="Path to output the histogram to")
argParser.add_argument("-c", "--column-number", type=int, default=3, help="Index of column in CSV which contains the timestamps. Start counting at 0! - (default is 3)")
argParser.add_argument("-r", "--retweet-column", type=int, default=2, help="Index of column in CSV which contains the Tweet Text. Start counting at 0! - (default value is 2)")
argParser.add_argument("-t", "--title", type=str, default='Tweet Frequency', help="Title that should be displayed above the chart")

args = argParser.parse_args()


def create_chart(df):
    # Create a plot
    plt.figure(figsize=(25, 15))


    # Add the data (Group the datetime elements by hour)
    df.plot(kind="bar", width=0.75)


    # Limit how many x-ticks get displayed
    ax = plt.gca()
    ax.set_xticks(ax.get_xticks()[::6]) # Display every 6th tick

    # Set some display settings
    plt.margins(0.2)
    plt.xticks(rotation = -45, ha="left", rotation_mode="anchor")
    plt.grid(axis='y', alpha=0.75)

    # Add some labels
    plt.title(args.title)
    plt.xlabel('Timestamp')
    plt.ylabel('Tweets')
    
    plt.tight_layout()

    # Output to file
    plt.savefig(args.output, dpi=150)

def main():
    print(f'Reading data from {args.input}')

    # Get the column with the date/timestamps out of the CSV file and load it into a pandas dataframe
    df = pd.read_csv(args.input)
    print(f'Loaded dataframe with {df.size} rows')

    # Make sure that the date column is the correct data type
    dateColumn = df.columns[args.column_number]
    print(f'Using column {args.column_number} - which is labelled "{dateColumn}"')

    df[dateColumn] = pd.to_datetime(df[dateColumn], errors='coerce', dayfirst=True, utc=True, infer_datetime_format=True, cache=True)
    # df[dateColumn] = df[dateColumn].astype("datetime64[s]")

    print('Preview of converted DataFrame:')
    print(df[[dateColumn]].head(5))

    startDate = min(df[dateColumn])
    endDate = max(df[dateColumn])
    print(f'Chart will range from {startDate} to {endDate}')

    

    # Filter the dataframe to only chart retweets
    retweetColumn = df.columns[args.retweet_column]
    print('\nNow filtering Retweets\n')
    print(f'Reading column {args.retweet_column} - which is labelled "{retweetColumn}"')
    boolean_series = df[retweetColumn].str.startswith("RT @", na = False)
    retweetsDf = df[boolean_series]
    print('Preview of filtered DataFrame:')
    print(retweetsDf)

    # Combine the dataframes for easier charting
    combined = pd.DataFrame([df[dateColumn].groupby(df[dateColumn].dt.to_period('H')).count(), retweetsDf[dateColumn].groupby(retweetsDf[dateColumn].dt.to_period('H')).count()]).transpose()
    combined.columns = ['all_tweets', 'retweets']
    
    

    print('Preview of combined DataFrame:')
    print(combined)

    # Send the dataframe to our charter function    
    try:
        create_chart(combined)
        print(f'Created a chart and saved to {args.output}')
    except Exception as e:
        print(f'Error when making chart: {type(e)}')
        print(e)


if __name__ == '__main__':
    startTime = datetime.now()
    print(f'Started execution at {startTime}')
    main()
    endTime = datetime.now()
    totalTime = endTime - startTime
    print(f'Finished at {endTime} - a total of {totalTime}')