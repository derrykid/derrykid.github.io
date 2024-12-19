# This program will save the link in a list, and thereafter we can access the link in a for loop
# We can combine the root URL with the link

import requests, bs4, webbrowser

targetURL = 'targetURL'
res = requests.get(targetURL)

try:
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    allLinks = soup.select('table a')

    for index in range(len(allLinks)):
        # The URL going to open:
        print(targetURL + allLinks[index].get('href'))

        # Open in web browser
        webbrowser.open(targetURL + allLinks[index].get('href'))


except Exception as err:
    print("Error: " + err)