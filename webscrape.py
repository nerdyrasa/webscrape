import csv
import sys
import urllib.request, urllib.parse

from bs4 import BeautifulSoup


_URL = 'http://espn.go.com/college-football/team/roster/_/id/2132/cincinnati-bearcats'
_HDR = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

def urls_for_teams(url):

    #create a request object
    req = urllib.request.Request(url, headers=_HDR)


    """Return a list of tuples containing team name and its associated url"""
    page = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    url_list = soup.find(class_='select-box').find_all('option')
    return [(element.text, element['value']) for element in url_list][2:]


def player_list_from_url_map(team_urls):
    """Return a list of lists of each of the players statistics"""

    player_list = []
    for (team_name, url) in team_urls[92:93]:

        url = urllib.parse.urlsplit(url)
        url = urllib.parse.urlunsplit(url._replace(path=urllib.parse.quote(url.path)))
        print(url)
        #create a request object
        req = urllib.request.Request(url, headers=_HDR)

        team_page = urllib.request.urlopen(req).read()

        for row in BeautifulSoup(team_page, 'html.parser').find_all('tr'):
            current_row = row.find_all('td')
            player_list.append([e.text for e in current_row])

    return player_list


def write_players_to_csv(player_list):
    """Write player_list to football_player.csv file"""
    with open("football_player.csv", "w",encoding="utf-8", newline='') as players_csv:
        writer = csv.writer(players_csv)
        for each_player in player_list:
            writer.writerow(each_player)


def main():
    """Main entry point for the script"""
    team_urls = urls_for_teams(_URL)
    player_list = player_list_from_url_map(team_urls)
    write_players_to_csv(player_list)


if __name__ == '__main__':
    sys.exit(main())