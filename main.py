import re
from requests import get
from bs4 import BeautifulSoup

years=[str(i) for i in range(2000,2018)]
movies=[]
names=[]
rating=[]
metascore=[]
release_year=[]
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
        names.append(first_movie.h3.a.text)

        #movie year
        release_year.append(first_movie.h3.find('span','lister-item-year text-muted unbold').text)

        #movie rating
        rating.append(first_movie.strong.text)

        #metascore rating
       
        if(first_movie.find('span',class_=['metascore favorable','metascore mixed','metascore unfavorable'])!=None):
            metascore.append(first_movie.find('span',class_=['metascore favorable','metascore mixed','metascore unfavorable']).text)
    
         

#cast names
for page in years:
    #movies from the year 2018-2019 with all pages 
    response=get("http://www.imdb.com/search/title?release_date="+val+"&sort=num_votes,desc&page=1")
    html=BeautifulSoup(response.content,'html.parser')
    cast=html.select("div.lister-item-content")
    for i in range(len(cast)):
        x=(cast[i].findAll('p'))
        d=x[2].text
        idx=d.find("Stars:")
        pro=d[idx+6:]
        mlist=pro.split("\n")
        mlist="".join(mlist).strip().split(',')
        org_list=[]
        for i in mlist:
            org_list.append(i.strip())
        movies.append(org_list)


main=[]
for i in range(len(names)):
    jdict={}
    jdict['name']=names[i]
    jdict['rating']=rating[i]
    jdict['cast']=movies[i]
    jdict['metascore']=metascore[i]
    jdict['releasing_year']=release_year[i]
    main.append(jdict)



print(main)
