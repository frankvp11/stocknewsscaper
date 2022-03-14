import requests
import datetime
from twilio.rest import Client

#variables
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key_stock_price = "RYFQ1LEVDV456LSP"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
api_key_news = "68380789dd2349b582ed334721c7c39e"



#getting data
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=RYFQ1LEVDV456LS")
data = response.json()
todays_data = float(data["Time Series (Daily)"]["2021-12-23"]["4. close"])
day_before_data = float(data["Time Series (Daily)"]["2021-12-22"]["4. close"])
difference_between_days = todays_data - day_before_data
percentage_difference = (difference_between_days / todays_data) * 100
#checking the percent difference
if percentage_difference >= 5 or percentage_difference <= -5:
    news_params = {
        "apiKey": api_key_news,
        "qInTitle": COMPANY_NAME,
    }
    #getting relevant news
    response_news = requests.get(NEWS_ENDPOINT, params=news_params)
    article = response_news.json()["articles"]
    
    three_articles = article[:3]    
    
    formatted_articles_list = [f'Headling: {article["title"]}. \nBrief: {article["description"]}' for article in three_articles]
    #Sending said news to me via twilio
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles_list:
        message = client.messages.create(
            body=article,
            from_="+16605383337",
            to="+15196138882",
        )


