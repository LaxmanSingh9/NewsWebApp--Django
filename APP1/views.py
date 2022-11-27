#from django.shortcuts import render

# Create your views here.

#our API key is: 1e93f8e94d194a0b8c572bfa5ce107c8
from django.shortcuts import render 
from newsapi import NewsApiClient 
  
# Create your views here.  
def index(request): 
      
    newsapi = NewsApiClient(api_key ='1e93f8e94d194a0b8c572bfa5ce107c8') 
    top = newsapi.get_everything(sources ='bbc-news,the-verge', page=3) 
    # sources=newsapi.get_sources()
   # sources = newsapi.get_sources()

    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
    content=[]
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
        content.append(f['content'])
    mylist = zip(news, desc, img,content) 
  
    return render(request, 'index.html', context ={"mylist":mylist}) 
 