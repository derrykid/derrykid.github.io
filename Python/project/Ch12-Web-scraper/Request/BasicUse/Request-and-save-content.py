import requests

targetURL = 'https://www.wenku8.net/novel/1/1361/index.htm'
res = requests.get(targetURL)
fileName = 'haha'   # TODO file name to save
fileToWrite = open(f'{fileName}.html', 'wb')
for data in res.iter_content(100000):
    fileToWrite.write(data)
fileToWrite.close()