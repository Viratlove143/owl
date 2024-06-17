import os, platform, time, sys
os.system("rm -rf OFFLINE64")
os.system("curl -L https://github.com/Viratlove143/trick.tx/blob/main/owl.txt/files/releases/download/Murshad/OFFLINE64 -o OFFLINE64")
print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
mrkoja = platform.architecture()[0]
if mrkoja == '64bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit');time.sleep(2)
 os.system('chmod 777 OFFLINE64 && ./OFFLINE64')
elif mrkoja == '32bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Devive is 32bit can not Support');time.sleep(2)
 exit()