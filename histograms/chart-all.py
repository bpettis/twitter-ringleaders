#! /bin/python3

import csv, argparse
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



# Setup command line arguments:
argParser = argparse.ArgumentParser(description='''
**Twitter Histogram Generator **


This silly little program takes an input CSV file containing tweets and generates a histogram of tweet frequency.
It's a great way to visualize trends of Twitter activity
    
Created by Ben Pettis''',
    usage='''%(prog)s -i [input file] -o [output file]
run "%(prog)s --help" to view more information''',
    formatter_class=argparse.RawTextHelpFormatter
)
argParser.add_argument("-i", "--input", required=True, help="Path to the CSV file to read from")
argParser.add_argument("-o", "--output", required=True, help="Path to output the histogram to")
argParser.add_argument("-c", "--column-number", type=int, default=3, help="Index of column in CSV which contains the timestamps. Start counting at 0! - (default is 3)")
argParser.add_argument("-t", "--title", type=str, default='Tweet Frequency', help="Title that should be displayed above the chart")

args = argParser.parse_args()


def create_chart(df, col):
    # df.plot.hist(column=col, grid=True, bins=20, rwidth=0.9,
    #                 color='#607c8e')

    plt.figure(figsize=(50, 10))

    df.groupby(df[col].dt.to_period('H')).count().unstack().plot(kind='bar')

    plt.title(args.title)
    plt.xlabel('Timestamp')
    plt.ylabel('Tweets')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig(args.output, dpi=150)

def main():
    print(f'Reading data from {args.input}')

    # Get the column with the date/timestamps out of the CSV file and load it into a pandas dataframe
    df = pd.read_csv(args.input)
    print(f'Loaded dataframe with {df.size} rows')

    # Make sure that the date column is the correct data type
    column = df.columns[args.column_number]
    print(f'Using column {args.column_number} - which is labelled "{column}"')

    # df[column] = pd.to_datetime(df[column], unit='h')
    df[column] = df[column].astype("datetime64")

    print('Preview of converted DataFrame:')
    print(df[[column]].head(5))

    # Send the dataframe to our charter function    
    try:
        create_chart(df, column)
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