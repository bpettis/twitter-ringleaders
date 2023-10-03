# Twitter Ringleaders

A project to assess the activities of right-wing "culture warriors" on Twitter. This repo will contain some basic scripts for interacting with previously scraped twitter data.

## Data

Scripts will likely expect input data files to be placed in a `data` directory in the project root. This directory is excluded via the `.gitignore` file to avoid committing sensitive info to a public repo

## Output

Similarly, scripts' output directories will be excluded via `.gitignore` to avoid inadvertently committing data. Making data publicly available is a good thing, but I think that it should be done on your terms - rather than happening automatically. It's better to have a chance to review output to make sure PII isn't getting exposed.

---

## Scripts

Simple descriptions/overviews of each script and/or project component.

### Birdwatch Crossreferencing (`birdwatch-xref`)

Compare a list of Tweet IDs and determine which, if any, received notes in Birdwatch/Community Notes, Twitter's crowd-sourced program for fact-checking and community moderation.

Birdwatch data is pulled from the [Birdwatch Archive](https://birdwatcharchive.org/) project, which itself relies on these scripts: https://github.com/bpettis/birdwatch-scraper


More details: [birdwatch-xref/README.md](birdwatch-xref/README.md)

## Check Users (`checkusers`)

Take a CSV file which contains twitter usernames and attempt to determine whether the account is active, suspended, or deleted.

More details: (user-checking/README.md)[user-checking/README.md]
