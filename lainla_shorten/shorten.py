import requests

def shorten_url(url):
    
    data = f'url={url}'
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    
    response = requests.post('https://s.lain.la', headers=headers, data=data)
    
    return response.text