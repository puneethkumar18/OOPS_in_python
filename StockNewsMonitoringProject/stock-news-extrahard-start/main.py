import requests
from bs4 import BeautifulSoup
from datetime import datetime
import lxml


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

Stock_api = "R9MMHCCBXGAX9GRE"
News_api = "f851e009dfd2428586d048fa7326da52"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
Url = 'https://www.alphavantage.co/query'
stock_parameter = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol":f'{COMPANY_NAME}',
    'apikey':f'{Stock_api}',
    
}



#response = requests.get(url=Url,params=stock_parameter)
#stock_data = response.json()["Time Series (Daily)"][f"{datetime.now().date()}"]["4.close"]



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
News_endpoint = "https://newsapi.org/v2/everything"
news_parameter = {
    "q":f"{COMPANY_NAME}",
    "from" :"2023-09-28",
    "sortBy":"publishedAt",
    "apiKey":f"{News_api}"
}
response1 = requests.get(url=News_endpoint,params=news_parameter)
r = requests.get(url= "https://www.google.com")
print(r.text)
#soup = BeautifulSoup(r.text, "lxml.parser")
#print(soup.a)
articles = response1.json()["articles"]
three_article = articles[:3]
format_article = [f"Headline:\n{article['title']} \n\nDesciption:\n{article['description']}" for article in three_article]
#for arti in format_article:
 #   print(arti)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

