import requests
from bs4 import BeautifulSoup

URL = 'https://www.imdb.com/chart/top/'

res = requests.get(URL)

soup = BeautifulSoup(res.content, 'html.parser')

movie_list = soup.findAll('tbody', { 'class' : 'lister-list' })[0]

#print(movie_list.findAll('td', { 'class' : 'titleColumn' }))

movies = movie_list.findAll('td', { 'class' : 'titleColumn' })

movie_index = 0

for movie in movies:
	movie_index += 1
	print(str(movie_index) + ') ' + movie.find('a').get_text()) 