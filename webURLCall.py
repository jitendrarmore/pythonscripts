from http.client import responses

import requests

def callAPIURL(url, chunk, fileName):
    #downloading large file using chunk
    responses = requests.get(url, stream=True)
    responses.raise_for_status()

    try:

        with open(fileName, 'wb') as file:
            for chunk in responses.iter_content(chunk):
                if chunk:
                    file.write(chunk)

    except:
        print('downloading issue')


callAPIURL('https://dummyjson.com/products', 1024, './mydata')