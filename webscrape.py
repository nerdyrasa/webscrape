import sys
from bs4 import BeautifulSoup
import urllib2

_URL = 'http://espn.go.com/college-football/team/roster/_/id/2132/cincinnati-bearcats'


def urls_for_teams(url):
    """Return a list of tuples containing team name and its associated url"""
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    url_list = soup.find(class_='select-box').find_all('option')
    return [(element.text, element['value']) for element in url_list][2:5]


def player_list_from_url_map(team_urls):
    """Return a list of lists of each of the players statistics"""
    player_list = []
    for (team_name, url) in team_urls:

        team_page = urllib2.urlopen(url).read()

        for row in BeautifulSoup(team_page, 'html.parser').find_all('tr')[2:]:
            current_row = row.find_all('td')
            player_list.append([e.text for e in current_row])

    return player_list


def main():
    """Main entry point for the script"""
    team_urls = urls_for_teams(_URL)
    player_list = player_list_from_url_map(team_urls)


if __name__ == '__main__':
    sys.exit(main())
