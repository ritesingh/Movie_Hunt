import re
from requests import get
from bs4 import BeautifulSoup

years=[str(i) for i in range(2000,2018)]
for page in years:
    #movies from the year 2018-2019 with all pages 
    val=str(page)
    response=get("http://www.imdb.com/search/title?release_date="+val+"&sort=num_votes,desc&page=1")
    html=BeautifulSoup(response.text,'html.parser')

    #to contain all movies on page
    movies=html.find_all('div',class_='lister-item mode-advanced')

    for i in range(len(movies)):
        #to access movies sequentially
        first_movie=movies[i]

        #movie name 
        print("name= "+first_movie.h3.a.text)

        #movie year
        print("Releasing Year= "+first_movie.h3.find('span','lister-item-year text-muted unbold').text)

        #movie rating
        print("Movie Rating: "+first_movie.strong.text)

        #metascore rating
        print("Metascore Rating: ",end="")
        if(first_movie.find('span',class_=['metascore favorable','metascore mixed','metascore unfavorable'])!=None):
            print(first_movie.find('span',class_=['metascore favorable','metascore mixed','metascore unfavorable']).text)

        #cast names
        dicta=html.find(class_='lister-item-content')
        dictb=dicta.findAll('a',href=True)
        name={a.next:a.next.next for a in dictb}
        key=name.keys()
        print("Cast Name: ")
        for i in key:
            i=str(i)
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')     
            if(regex.search(i) == None): 
                print(i) 

        print("\n\n")
