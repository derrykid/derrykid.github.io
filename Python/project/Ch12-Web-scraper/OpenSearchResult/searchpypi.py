#! python
# This program opens the search result in web browser
import webbrowser

import requests, bs4, sys, bs4
# print('searching')
# res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
# res.raise_for_status()
#
#
# # TODO: Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
# # TODO: Open a browser tab for each result.
# linkElems = soup.select('')

webbrowser.open_new_tab("https://www.google.com/search?q=arab+flat&tbm=isch&ved=2ahUKEwj-14e2pvr2AhVJAd4KHaJfCrQQ2-cCegQIABAA&oq=arab+flat&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgQIABAYMgQIABAYMgYIABAKEBg6BwgjEO8DECc6BAgAEB46BggAEAgQHlCdHVjeLWD-MWgAcAB4AIABkgGIAcUHkgEEMTIuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=7dVKYr6tCcmC-Aaiv6mgCw&bih=876&biw=1605#imgrc=cXnlSiS0zfR8cM")