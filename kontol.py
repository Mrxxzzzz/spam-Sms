import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;       S P A M  S M S      ;
		;---------------------------;
		; Author : FanCyber    ;
		;  YouTube:   https://m.youtube.com/channel/UCS9uQl65oBpuYH5dmX4s_yw ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
1. Spam telnyet
2. Spam kontol
3. Spam memex
4. Spam telnyet2
5. Spam pepek
6. Spam gratis
""")
		pilih=int(input('/Kang-newbie: '))
		if pilih == 1:
			import src.sms
		elif pilih == 2:
			import src.grab
		elif pilih == 3:
			import src.hooq
		elif pilih == 4:
			import src.oyo
		elif pilih == 5:
			print("""
		;;;;;;;;;;;;;;;;;;;
		; Spam TelkomNyet ;
		;;;;;;;;;;;;;;;;;;;
1. Spam TelkomNyet-v1
2. Spam TelkomNyet-v2
""")
			pilihlagi=int(input('/Kang-newbie: '))
			if pilihlagi == 1:
				import src.telnyet
			elif pilihlagi == 2:
				import src.telnyet2
			else: print("[!] lihat menu dong(o)");self.menu()
		elif pilih == 6:
			import src.gratis
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))