
import bs4
from bs4 import BeautifulSoup as soup         #Web Scrapper
from urllib.request import urlopen            #To read url pages
#from nltk.chat.util import Chat, reflections  #Fo the Chatbot
from utils import Chat, reflections

from flask import Flask, render_template, request

#For the ones using A link description
def news_gather1(news_url,typo):
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()
    
    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    # Print news title, url and publish date
    news_str='Today\'s '+typo+' are:'
    for i in range(0,4):
        
      news_str=news_str+'<br>'+news_list[i].title.text
      #print(news.link.text)
# =============================================================================
#       if news_list[i].description.text.find('</a>'):  
#            arry=[]
#            arry=news_list[i].description.text.split('</a>')
#            news_str=news_str+'\n'+arry[1]
#       else:
#           news_str=news_str+'\n'+news_list[i].description.text
# =============================================================================
      #news_str=news_str+'\n'+arry[1]
      news_str=news_str+'\n'+news_list[i].pubDate.text
      news_str=news_str+'<br>'+"-"*40
    return news_str


#for the ones not using a link in description
def news_gather2(news_url,typo):
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()
    
    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    # Print news title, url and publish date
    news_str='Today\'s '+typo+' are:'
    for news in news_list:
        
      news_str=news_str+'<br>'+news.title.text
      #print(news.link.text)
# =============================================================================
#       news_str=news_str+'\n'+news.description.text
# =============================================================================
      news_str=news_str+'<br>'+news.pubDate.text
      news_str=news_str+'<br>'+"-"*40
    return news_str

#NEWS CATEGORIES
sports_news = news_gather1("https://timesofindia.indiatimes.com/rssfeeds/4719148.cms","Sports News")
Indian_news=news_gather1("https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms","Political News")
international_news=news_gather2("https://timesofindia.indiatimes.com/rssfeeds/296589292.cms","International News")
Gossips_news=news_gather1("https://www.cosmopolitan.com/rss","Gossips")
health_news=news_gather1("https://timesofindia.indiatimes.com/rssfeeds/3908999.cms","Lifestyle trends")
headlines_news=news_gather1("https://timesofindia.indiatimes.com/rssfeedstopstories.cms","Top Stories")
#food_news=news_gather(,"Culinary trends")
#hollywood_news=news_gather(,"Hollywood Gossips")
lifestyle_news=news_gather1("https://timesofindia.indiatimes.com/rssfeeds/2886704.cms","Lifestyle Trends")
bollywood_news=news_gather1("https://timesofindia.indiatimes.com/rssfeedstopstories.cms","Bollywood Gossips")
environment_news=news_gather1("https://timesofindia.indiatimes.com/rssfeeds/2647163.cms","Environment News")
Tech_news=news_gather2("https://timesofindia.indiatimes.com/rssfeeds/5880659.cms","Tech Updates")

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
  }


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"thank you|thanks",
        ["You are welcome.",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*) (sports news|Sports news|Sports|sports|Athletics|athletic)",
        [sports_news,]
    ],
    [
        r"(.*) (National news|Local news|national news|national|National|Indian News|Indian)",
        [Indian_news,]
    ],
    [
        r"(.*) (International News|International|Global News|Global)",
        [international_news,]
    ],
    [
        r"(.*) (Gossips|Bollywood Gossips|Bollywood News)",
        [bollywood_news,]
    ],
    [
        r"(.*) (Health|Health News|Hygiene|hygiene)",
        [health_news,]
    ],
    [
        r"(.*) (Environment|Nature|Environmental news|Nature news)",
        [environment_news,]
    ],
    [
        r"(.*) (Headlines|Top News)",
        [headlines_news,]
    ],
    [
        r"(.*) (tech news|Technology|Tech news)",
        [Tech_news,]
    ],
]


#def chatty():
    
#print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
chat = Chat(pairs, reflections)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def process():
    user_input=request.args.get('msg')
    bot_response=chat.converse(user_input)
    bot_response=str(bot_response)
    if bot_response == "None":
        bot_response = "I am sorry, I can't help you :("
    print("Friend: "+bot_response)
    return bot_response


app.run(debug=True)