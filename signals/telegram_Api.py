import telegram
#API_TOKEN = '1306512151:AAGpLPqZpUm5VRVeU8t2Lok10_erhYGlao0'
import requests


API_TOKEN = '1306512151:AAGpLPqZpUm5VRVeU8t2Lok10_erhYGlao0'



def send(msg, chat_id, token=API_TOKEN):
	"""
	Send a mensage to a telegram user specified on chatId
	chat_id must be a number!
	"""
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)
    #bot.send_photo(chat_id=chat_id,photo='signals\images\Decred-DCR.png', caption='This is the test photo caption')

url='api.telegram.org/bot1306512151:AAGpLPqZpUm5VRVeU8t2Lok10_erhYGlao0'

def sendp(chat_id,photo,caption,token=API_TOKEN):
    bot = telegram.Bot(token=token)
    bot.sendPhoto(chat_id=chat_id, photo=photo,caption=caption)



path = 'https://thumbs.dreamstime.com/b/pi%C3%A8ce-de-monnaie-bitcoin-btc-avec-le-logo-d-isolement-sur-blanc-117133078.jpg'
path1= 'signals\images\photo_2020-08-13_16-41-40.jpg'
message="💰 : LTC_USDT\n⏳ TF: 1D\n💵 NP: 58.14\n🔫 Tr : 62.53\n⛔️ SL : 51.32\n✅ Tp1 : 71.46   🧮 14.26%\n✅ Tp2 : 83.78   🧮 34.00%\n✅ Tp3 : 101.47   🧮 62.28%\n"
messageText= "💰 : {}\n⏳ TF: {}\n💵 NP: {}\n🔫 Tr : {}\n⛔️ SL : {}\n✅ Tp1 : {}   🧮 {}\n✅ Tp2 : {}   🧮 {}\n✅ Tp3 : {}   🧮 {}\n".format(1,2,3,4,5,6,7,8,9,10,11)


#send(msg=message,chat_id='@crypto_monarch',token=API_TOKEN)
#sendp(chat_id='@crypto_monarch',photo=open(path1,'rb'),caption=messageText)