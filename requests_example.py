import requests
import webbrowser


r = requests.get('https://source.unsplash.com/random/800x600')

webbrowser.open(r.url)
