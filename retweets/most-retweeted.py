import csv, argparse
from datetime import datetime
import pandas as pd

# Setup command line arguments:
argParser = argparse.ArgumentParser(description='''
**Twitter Top Retweets **


This silly little program takes an input CSV file containing tweets.
It outputs a secondary CSV file with details of what RTs appear most frequently appear in the dataset.
It's a great way to understand trends of Twitter activity
    
Created by Ben Pettis''',
    usage='''%(prog)s -i [input file] -o [output file]
run "%(prog)s --help" to view more information''',
    formatter_class=argparse.RawTextHelpFormatter
)
argParser.add_argument("-i", "--input", required=True, help="Path to the CSV file to read from")
argParser.add_argument("-o", "--output", required=True, help="Path to output the CSV file to")
argParser.add_argument("-t", "--tweet-column", type=int, default=2, help="Index of column in CSV which contains the Tweet Text. Start counting at 0! - (default value is 2)")
argParser.add_argument("-c", "--rt-count", type=int, default=10, help="How many top RTs should be recorded. Default is top 10.")

args = argParser.parse_args()


def main():
    print(f'Reading data from {args.input}')

    # Get the CSV file and load it into a pandas dataframe
    df = pd.read_csv(args.input)
    print(f'Loaded dataframe with {df.size} rows')

    print(df)

    # Use arguments to determine which columns to read from:
    tweetColumn = df.columns[args.tweet_column]
    print(f'Reading tweets from column {args.tweet_column} - which is labelled "{tweetColumn}"')
    retweetCount = args.rt_count


    
    # Find the rewteets
    retweet_prefix = "RT @"
    boolean_mask = df[tweetColumn].str.startswith(retweet_prefix, na=False)
    filtered_df = df.loc[boolean_mask]
    times_retweeted = len(filtered_df.index)

    print(f'{args.input} contains {str(times_retweeted)} RTs')

    #  Find the most common RTs
    top_rts = filtered_df[tweetColumn].value_counts().nlargest(retweetCount)
    if len(top_rts) > 0:
        print(top_rts)
    #   Write all that information into the CSV file
        top_rts.columns = ['tweet_text', 'retweet_count']
        top_rts.to_csv(args.output)
    else:
        print(f'There are no RTs in this dataset!')






if __name__ == '__main__':
    startTime = datetime.now()
    print(f'Started execution at {startTime}')
    main()
    endTime = datetime.now()
    totalTime = endTime - startTime
    print(f'Finished at {endTime} - a total of {totalTime}')