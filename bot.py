#US: 'www.amazon.com',
##AU: 'www.amazon.com.au',
##BR: 'www.amazon.com.br',
##CA: 'www.amazon.ca',
##CN: 'www.amazon.cn',
##FR: 'www.amazon.fr',
##DE: 'www.amazon.de',
##IN: 'www.amazon.in',
##IT: 'www.amazon.it',
##MX: 'www.amazon.com.mx',
##NL: 'www.amazon.nl',
##SG: 'www.amazon.sg',
##ES: 'www.amazon.es',
##TR: 'www.amazon.com.tr',
##AE: 'www.amazon.ae',
##GB: 'www.amazon.co.uk',
#JP:   'www.amazon.jp',

import requests
import json
from settings import *
import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import time

kw = input("Cosa vuoi cercare?: ")

url = "https://amazon-product-reviews-keywords.p.rapidapi.com/product/search"

querystring = {"keyword":kw,"country":"IT","category":"aps"}

headers = {
    'x-rapidapi-key': "ee4e30a694msh18cfae15ec78eebp1528d5jsn523f18ad7d7a",
    'x-rapidapi-host': "amazon-product-reviews-keywords.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

json_pack = json.loads(response.text)

products = json_pack["products"]


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)
    
    if content_type == 'text':
        text = msg['text']
    

bot = telepot.Bot(BOT_TOKEN)
MessageLoop(bot, handle).run_as_thread()
for price in products:
	if(price["price"]["discounted"] == True):
		if(price["price"]["savings_percent"] >= 10):
			if(price["price"]["savings_percent"] >= 30):
				if(price["amazonPrime"] == True):
					if(price["reviews"]["rating"] <= 1):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ✅" +"\n\n🔗 URL: " + price["url"])	
					elif(price["reviews"]["rating"] <= 2):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ✅" +"\n\n🔗 URL: " + price["url"])	
					elif(price["reviews"]["rating"] <= 3):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ✅" +"\n\n🔗 URL: " + price["url"])	
					elif(price["reviews"]["rating"] <= 4):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ✅" +"\n\n🔗 URL: " + price["url"])	
					elif(price["reviews"]["rating"] == 5):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️⭐️⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ✅" +"\n\n🔗 URL: " + price["url"])
					else:
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ❓❓❓❓❓ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n\n🔗 URL: " + price["url"])	
				elif(price["amazonPrime"] == False):	
					if(price["reviews"]["rating"] <= 1):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ❌" +"\n\n🔗 URL: " + price["url"])	
					elif(price["reviews"]["rating"] <= 2):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ❌" +"\n\n🔗 URL: " + price["url"])	
					elif(price["reviews"]["rating"] <= 3):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ❌" +"\n\n🔗 URL: " + price["url"])	
					elif(price["reviews"]["rating"] <= 4):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ❌" +"\n\n🔗 URL: " + price["url"])	
					elif(price["reviews"]["rating"] == 5):
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️⭐️⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n🔺 Amazon Prime: ❌" +"\n\n🔗 URL: " + price["url"])	
					else:
						bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ❓❓❓❓❓ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n\n🔗 URL: " + price["url"])
				#print("Title: "+str(price["title"])+" | Price: "+str(price["price"]["current_price"])+"€ | Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " OFFERTONA !")
			else:
				print("Title: "+str(price["title"])+" | Price: "+str(price["price"]["current_price"])+"€ | Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )")
				time.sleep(2)