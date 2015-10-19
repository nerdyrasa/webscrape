import sys
from bs4 import BeautifulSoup
import urllib2

_URL = 'http://espn.go.com/college-football/team/roster/_/id/2132/cincinnati-bearcats'


def urls_for_teams(url):
    """Return a list of tuples containing team name and its associated url"""
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    url_list = soup.find(class_='select-box').find_all('option')
    return [(element.text, element['value']) for element in url_list][2:]


def main():
    """Main entry point for the script"""
    team_urls = urls_for_teams(_URL)


if __name__ == '__main__':
    sys.exit(main())
