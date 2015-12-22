## Overview

This is a simple web scraping program using BeautifulSoup4.

## Requirements

Python 3.4.2
BeautifulSoup4 4.4.1

## Usage

Run python webscrape.py.

## Known Issues

Initially, the program generated the following error for the team San Jos&eacute; State:

UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 49: ordinal not in range(128)

This was a great opportunity for me to learn more about Unicode:
http://www.joelonsoftware.com/articles/Unicode.html

Although the code has been updated to handle the non-ascii url, the csv file doesn't seem to be handling it properly.
I still need to handle the write to the csv file. Also, there is an extra unnecessary line between player stats.
This probably has something to do with the fact that my current dev env is Windows 10.


## Attribution ##

Writing Idiomatic Python Video One [youtube video](https://www.youtube.com/watch?v=g0gNWGg2JxM)




