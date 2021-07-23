from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests
import bs4
# Create a new chat bot named Charlie
chatbot = ChatBot('charlie',database_uri=None)

trainer = ListTrainer(chatbot)

stocks = {
    'Company' : [],
    'Current_Price' : [],
    '%Change' : [],
    'Volume' : [],
    'Equity' : [],
    'Face_value' : [],
    'Market_cap_Cr' : []
}

url = 'https://money.rediff.com/companies/market-capitalisation'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.content,'html.parser')
div = soup.find('table',attrs={'class':'dataTable'})
all_td = div.find_all('td')

for i in range(0,len(all_td),7):
    stocks['Company'].append((all_td[i].text).strip())
    stocks['Current_Price'].append(all_td[i + 1].text)
    stocks['%Change'].append((all_td[i + 2].text).strip())
    stocks['Volume'].append(all_td[i + 3].text)
    stocks['Equity'].append(all_td[i + 4].text)
    stocks['Face_value'].append(all_td[i + 5].text)
    stocks['Market_cap_Cr'].append(all_td[i + 6].text)
print('stocks is', stocks)
trainer.train([
    'hi',
    'Hello, How can i help you ?',
    'hy',
    'Hello, How can i help you ?',
    'hello',
    'Hello, How can i help you ?',
    'what is the current stock price?',
    'for which company you are looking for?',
    'stock price',
    'for which company you are looking for?',
    'price ',
    'for which company you are looking for?',
    'current stock price',
    'for which company you are looking for?',
    'company',
    'for which company you are looking for?',
    'ok',
    'How can i help you ?',
    'thanks',
    'How can i help you ?'

])

print('stocks is ', stocks)
trains = []
for i in range(len(stocks['Company'])):
    trains.append(stocks['Company'][i])
    trains.append(f"Current_Price : {stocks['Current_Price'][i]}\n%Change : {stocks['%Change'][i]}\nVolume : {stocks['Volume'][i]}\nEquity : {stocks['Equity'][i]}\nFace_value : {stocks['Face_value'][i]}\nMarket_cap in Cr : {stocks['Market_cap_Cr'][i]}")

trainer.train(trains)

for i in range(10):
    response = chatbot.get_response(input('You : '))
    print('Bot : '+str(response))

