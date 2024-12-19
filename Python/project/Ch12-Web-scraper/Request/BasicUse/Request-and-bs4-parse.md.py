import requests, bs4

targetURL = 'https://derry.club'
res = requests.get(targetURL)
try:
    res.raise_for_status()
    webContent = bs4.BeautifulSoup(res.text, 'html.parser')

    # this will select only h2 tags and create a list
    h2Content = webContent.select('h2')
    footerContent = webContent.select('#top > main > article:nth-child(2) > footer')

    print('Start of h2 content')
    for index in range(len(h2Content)):
        print(h2Content[index].getText())

    print('Start of footer content')
    for index in range(len(footerContent)):
        print(footerContent[index].getText())
        # get a dict of k-v: attr element with its value
        print(footerContent[index].attrs)

except Exception as err:
    print("Error Occurs: " + err)
