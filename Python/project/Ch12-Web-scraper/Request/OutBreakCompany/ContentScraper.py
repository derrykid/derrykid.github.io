import pathlib

import requests, bs4, webbrowser, time

targetURL = 'https://www.wenku8.net/novel/1/1361/'
res = requests.get(targetURL)

try:
    res.raise_for_status()
    homeSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    allLinks = homeSoup.select('table a')

    # for index in range(len(allLinks)):
    for index in range(15):
        # get the individual page URL and its soup
        pageURL = targetURL + allLinks[index].get('href')
        pageResponse = requests.get(pageURL)
        # If the target encoding is different, change the value. e.g. big-5, etc. default utf-8
        pageResponse.encoding = 'gbk'
        pageSoup = bs4.BeautifulSoup(pageResponse.text, 'html.parser')

        # get the page title, and make it the file name
        title = pageSoup.select('title')[0].getText()
        filePath = pathlib.Path.cwd() / 'Product'

        fileToWrite = open(f"{filePath}/{title}.html", 'wb')
        for data in pageResponse.iter_content(100000):
            fileToWrite.write(data)
        fileToWrite.close()
        time.sleep(0.3)

except Exception as err:
    print("Error: " + err)
