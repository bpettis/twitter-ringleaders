#! /bin/python3

import csv, argparse
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



# Setup command line arguments:
argParser = argparse.ArgumentParser(description='''
**Twitter Line Chart Generator **


This silly little program takes an input CSV file containing tweets and generates a line chart of tweet frequency.
It's a great way to visualize trends of Twitter activity
    
Created by Ben Pettis''',
    usage='''%(prog)s -i [input file] -o [output file]
run "%(prog)s --help" to view more information''',
    formatter_class=argparse.RawTextHelpFormatter
)
argParser.add_argument("-i", "--input", required=True, help="Path to the CSV file to read from")
argParser.add_argument("-o", "--output", required=True, help="Path to output the graph image to")
argParser.add_argument("-c", "--column-number", type=int, default=3, help="Index of column in CSV which contains the timestamps. Start counting at 0! - (default is 3)")
argParser.add_argument("-t", "--title", type=str, default='Tweet Frequency', help="Title that should be displayed above the chart")
argParser.add_argument("-x", "--x-ticks", type=int, default=6, help="Interval of x-ticks to display. (Default is every 6th tick)")
argParser.add_argument("-s", "--start", help="Earliest date of data that should be charted (useful for large datasets)")
argParser.add_argument("-e", "--end", help="Latest date of data that should be charted (useful for large datasets)")


args = argParser.parse_args()


def create_chart(df, col, startDate, endDate):
    # Create a plot
    plt.figure(figsize=(25, 15))

    # Set the size of elements:
    plt.rcParams.update({'font.size': 24})
    plt.rcParams.update({'axes.titlesize': 28})
    plt.rcParams.update({'axes.labelsize': 24})
    plt.rcParams.update({'xtick.labelsize': 28})
    plt.rcParams.update({'ytick.labelsize': 28})


    # Add the data (Group the datetime elements by hour)
    chartData = df[col].groupby(df[col].dt.to_period('H')).count()
    print(type(chartData))
    print(chartData)
    # Use chartData.index to get the date labels
    # Use chartData.values to get the counts
    chartData.plot(kind='line', linewidth=5)

    timestamps = pd.date_range(startDate, endDate, freq='H')
    print('Timestamps (with extra gaps added):')
    print(timestamps)

    # Limit how many x-ticks get displayed
    ax = plt.gca()
    interval = args.x_ticks
    # ax.set_xticks(timestamps[::interval]) # Add the x-ticks (from the list of hours)

    # Set some display settings
    plt.margins(0.2)
    plt.xticks(ticks = timestamps[::interval], labels = timestamps[::interval], rotation = -45, ha="left", rotation_mode="anchor")
    plt.grid(axis='y', alpha=0.75)

    # Setup the y-axis minumum
    plt.ylim(bottom=0)

    


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
    column = df.columns[args.column_number]
    print(f'Using column {args.column_number} - which is labelled "{column}"')

    df[column] = pd.to_datetime(df[column], errors='coerce', dayfirst=True, utc=True, infer_datetime_format=True, cache=True)
    # df[column] = df[column].astype("datetime64[s]")

    print('Preview of converted DataFrame:')
    print(df[[column]].head(5))

    startDate = min(df[column])
    endDate = max(df[column])
    print(f'Data ranges from {startDate} to {endDate}')

    # Determine where the start/end of the data that we graph should be
    if args.start is None:
        chartStart = startDate
    else:
        chartStart = args.start
        df = df.loc[df[column] > chartStart]
    
    if args.end is None:
        chartEnd = endDate
    else:
        chartEnd = args.end
        df = df.loc[df[column] < chartEnd]

    print(f'Chart will range from {chartStart} to {chartEnd}')
    print('Specify a different start/end date by passing -s or -e arguments when running this program')


    # Send the dataframe to our charter function    
    try:
        create_chart(df, column, chartStart, chartEnd)
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