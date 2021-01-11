import os, time, pyfiglet, termcolor
def banenr(name):
	print (os.system('clear'))
	print (termcolor.colored(pyfiglet.figlet_format('LinuxInstaller'), 'green'))
	print ('==============')
	print ('[*] Installion Complete')
	print ('      [*] OS : ', name)
	print ('      [*] Thanks for using this tool')
	exit()

def fail(name):
	print (os.system('clear'))
	print (termcolor.colored(pyfiglet.figlet_format('LinuxInstaller'), 'yellow'))
	print ('============')
	print ('[*] Installion Fail')
	print ('      [*] OS : ', name)
	print ('      [*] Check your Internet and Disk Space')
	exit()

def kali():
	try:
		os.system('cd $Home && pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh')
		banner('Kali')
	except:
		fail('Kali')

def cent():
	try:
		os.system('cd $Home && pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh')
		banner('CentOS')
	except:
		fail('CentOS')
def ubuntu():
	try:
		os.system('cd $Home && pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh')
		banner('Ubuntu')
	except:
		fail('Ubuntu')

def debian():
	try:
		os.system('cd $Home && pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh')
		banner('Debian')
	except:
		fail('Debian')

def nethunter():
	try:
		os.system('cd $Home && pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh')
		banner('Kali Nethunter')
	except:
		fail('Kali Nethunter')

def msf():
	try:
		os.system('cd $Home && pkg install root-repo && pkg install metasploit')
		banner('Metasploit')
	except:
		fail('Metasploit')
def ferado():
	try:
		os.system('cd $Home && pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh')
		banner('Ferado')
	except:
		fail('Ferado')

def blacbox():
	try:
		os.system('cd $Home && pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh')
		banner('BlackBox')
	except:
		fail('BlackBox')
def linuxinstaler():
	print (os.system('clear'))
	print (termcolor.colored(pyfiglet.figlet_format('LinuxInstaller'), 'red'))
	print ('Author	:	LuciferPy')
	print ('Github	:	github.com/LuciferPy')
	print ('Mail	:	luciferpy60@gmail.com')
	print ('Choice~:')
	print ('		[1] Kali')
	print ('		[2] CentOS')
	print ('		[3] Ubuntu')
	print ('		[4] Debian')
	print ('		[5] Kali Nethunter	==> 	Size = 2GB')
	print ('		[6] Metasploit	==>	Size = 600MB')
	print ('		[7] Ferado')
	print ('		[8] BlackBox')
	print ('		[9] Exit ')
	choice = input('Enter Number you want to Choice:~#  ')
	if choice==str(1):
		time.sleep(2)
		kali()
	elif choice==str(2):
		time.sleep(2)
		cent()
	elif choice==str(3):
		time.sleep(2)
		ubuntu()
	elif choice==str(4):
		time.sleep(3)
		debian()
	elif choice==str(5):
		time.sleep(2)
		nethunter()
	elif choice==str(6):
		time.sleep(3)
		msf()
	elif choice==str(7):
		time.sleep(3)
		ferado()
	elif choice==str(8):
		time.sleep(1)
		blacbox()
	elif choice==str(9):
		print (termcolor.colored('Thanks for using my tool', 'blue'))
		exit()
	else:
		print ('Wrong Number')
		time.sleep(5)
		linuxinstaler()
linuxinstaler()
