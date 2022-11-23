###########################################
# Garz Menfess Telegram Bot
# Tegar Prayuda | Hak Cipta
# Tolong Hargai Pembuat Script Ini
# Recode ? Cantumin Source
# join t.me/GarzProject
# contact : t.me/tegarprayuda
# Jual Source  Code Menfess Bot Full Fitur 
# github.com/GarzProject/MenfessTelegramBot
###########################################

try:
	import telebot
	import time
	import os
	import json
	from dotenv import load_dotenv
	from telebot import types
except:
	print("error! install dulu pytelegrambotapi dengan cara 'pip install pytelegrambotapi'")

load_dotenv()





token = os.getenv("BOT_TOKEN")
ch = os.getenv("CHANNEL")
link = os.getenv("LINK")
admin = json.loads(os.getenv("ADMIN"))
trigger = json.loads(os.getenv("TAG"))
delay = os.getenv("DELAY")
mulai = '''
Selamat Datang Di *Garz Menfess*

kamu bebas mengirim menfess pada channel garzmenfess, jika ingin memposting menfess silahkan kirim pesan teks beserta tag dibawah ini :
	
*{}*

''' # edit pesan mulai ubah sesuka hati


# pake markdown? ubah jadi >> telebot.TeleBot(token, parse_mode="markdown")
bot = telebot.TeleBot(token)
kirim = bot.send_message 
kopi = bot.copy_message 
lanjut = bot.register_next_step_handler 
ma = types.InlineKeyboardMarkup
bb = types.InlineKeyboardButton



apaantuh = []
def diam(id):
	data = int(id)
	apaantuh.append(data)
	time.sleep(delay)
	apaantuh.remove(data)
	
	
# handling pesan command cuyy kembangin sesuka hati mu
@bot.message_handler(commands=["start", "broadcast", "ping"], chat_types=["private"])
def garz(message):
	id = message.chat.id 
	teks = message.text 
	
	# kebutuhan broadcast
	with open("member.db", "a+") as file:
		file.seek(0)
		value = str(id)
		lines = file.read().splitlines()
		if value in lines:
			pass
		else:
			file.write(value + "\n")
			
	# command start
	if "/start" in teks:
		nggih = '\n'.join(map(str, trigger))
		yamete = ma(row_width=2)
		rawr = bb(text="Channel Menfess", url=link)
		yamete.add(rawr)
		kirim(id, mulai.format(nggih), parse_mode="markdown", reply_markup=yamete)
	# ping
	elif "/ping" in teks:
		total = len(open("member.db", "r").readlines())
		pong = f"Bot Aktif !!!!\nTotal Pengguna Bot : {total}"
		kirim(id, pong)
	# command broadcast untuk admin
	elif "/broadcast" in teks:
		if id in admin:
			anjim = kirim(id, "Masukan Pesan Broadcast : ")
			lanjut(anjim, broadcast)



# handling teks menfess cuy
@bot.message_handler(content_types=["text"])
def menfessin(message):
	id = message.chat.id
	teks = message.text
	ah = tegar(teks)
	ih = len(teks.split(" "))
	if id in apaantuh:
		kirim(id, f"gagal mengirim!!\n\nkamu baru saja mengirim menfess, beri jarak {delay} detik untuk memposting kembali!")
	elif ih < 3:
		kirim(id, "gagal mengirim!!\n\ntidak boleh kurang dari 3 kata!!")
	elif ah == False:
		tag = '\n'.join(map(str, trigger))
		kirim(id, f"gagal mengirim!!\n\nharap gunakan tag dibawah ini : \n{tag}")
	elif ah == True:
		pesan = kirim(ch, teks)
		links = link + "/" + str(pesan.id)
		linksk = links + "?comment=" + str(pesan.id)
		kirim(id, f"*Menfess Berhasil Diposting!!*", parse_mode="markdown", reply_markup=awikwokbanget(links, linksk))
		diam(id)
		
# aninuneno tcih mendoksai
def tegar(data):
	for x in data.split(" "):
		yow = x
		for i in trigger:
			yaw = i
			if yaw in yow:
				data = 1
	if data == 1:
		return True
	else:
		return False

def broadcast(message):
	id = message.chat.id 
	pesans = message.message_id
	with open("member.db", "r") as file:
				lines = file.read().splitlines()
				for x in lines:
					try:
						yy = int(x)
						kopi(yy, id, pesans)
					except:
						print(f"gagal mengirim pesan kepada pengguna *{x}*\nmungkin bot telah diblok.")
	kirim(id, "Pesan broadcast berhasil dikirim.")




def awikwokbanget(cek, cekin):
	miaw = ma(row_width=2)
	b1 = bb(text="Cek Postingan", url=cek)
	b2 = bb(text="Cek Komentar", url=cekin)
	miaw.add(b1, b2)
	return miaw
print("\n\nBOT TELAH AKTIF!!! @GARZPROJECT")
bot.infinity_polling()









