# this is a challenge by Kenneth Love 
# challenge: create a script that accepts a month and day date that returns a link to wikipedia of that date
# below is my solution to this challenge

import datetime
import webbrowser

def create_wiki_link(date):
    date_formatted = date.strftime('%B_%d')  # needs to be in the format of December_11
    wiki_link = "https://en.wikipedia.org/wiki/"
    wiki_link_date = wiki_link + date_formatted
    return wiki_link_date

webbrowser.open(create_wiki_link(datetime.datetime.now()))
