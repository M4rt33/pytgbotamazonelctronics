BOT_TOKEN = "1517533942:AAHOADnZfbzFoSxJfVKLAuI2VznfAhDi_BA"

CHAT_ID = -1001490455999

API = "https://api.telegram.org"


#	bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n\n🔗 URL: " + price["url"])
#				elif(price["reviews"]["rating"] <=2):
#					bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n\n🔗 URL: " + price["url"])
#				elif(price["reviews"]["rating"] <=3):
#					bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n\n🔗 URL: " + price["url"])
#				elif(price["reviews"]["rating"] <=4):
#					bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n\n🔗 URL: " + price["url"])
#				elif(price["reviews"]["rating"] == 5):
#					bot.sendMessage(CHAT_ID, "📦 Prodotto: "+str(price["title"])+"\n\n💵 Prezzo: "+str(price["price"]["current_price"])+"€ \n📊 Risparmio: "+str(price["price"]["savings_amount"]) + "€ ( "+str(price["price"]["savings_percent"])+"% )" + " \n🛎 Rating: ⭐️⭐️⭐️⭐️⭐️ ( " + str(price["reviews"]["rating"]) + " | " + str(price["reviews"]["total_reviews"]) + " )" + "\n\n🔗 URL: " + price["url"])