import pycurl,random
import json as devil
while True:
 rnd=random.randint(100,9999)
 email=f'whisper{rnd}@whisper.vip'
 psw='whisper666'
 bd=random.randint(1,27)
 by=random.randint(1996,2003)
 bm=random.randint(1,12)
 data = f'platform=Android-ARM&gender=male&password_repeat={psw}&birth_month={bm}&email={email}&password={psw}&birth_day={bd}&app_version=883600521&iagree=true&birth_year={by}&key=142b583129b2df829de3656f9eb484e6&creation_point=client_mobile'
 whisper = pycurl.Curl()
 whisper.setopt(pycurl.URL, 'https://spclient.wg.spotify.com/signup/public/v1/account/')
 whisper.setopt(pycurl.POST, 1)
 whisper.setopt(pycurl.POSTFIELDS, data)
 whisper.setopt(pycurl.HTTPHEADER,["Host:spclient.wg.spotify.com","user-agent:Spotify/8.8.36.521 Android/26 (Plume L2)","accept-language:en-US","content-type:application/x-www-form-urlencoded",f"content-length:{len(data)}","accept-encoding:gzip"])
 whisper.setopt(pycurl.SSL_VERIFYPEER, False)
 whisper.setopt(pycurl.ENCODING, 'gzip')
 res =str(whisper.perform_rs())
 whisper.close()
 json=devil.loads(res)
 if json['status'] == 1:
  user=json['username']
  spotify=f'''[√] Status : True
[√] UserName : {user}
[√] E-mail : {email}
[√] PassWord : {psw}
[√] BirthDate : {bd} - {bm} - {by}'''
  print(spotify)
  print('='*30)
  with open('Spotify-Create.txt','a+') as whisper:
   whisper.write(f'{email}:{psw}\n')
 else:
  print(json)