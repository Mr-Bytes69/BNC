#<\>!python3.11
import os,platform,time
os.system('mkdir BNC-OK')
bitt=platform.architecture()[0]

if bitt=="32bit":
    print('[!] Your Device is 32 bit');print('32 Bit is not Sapported ')
    time.sleep(2)


elif bitt=="64bit":
    os.system('clear');print('[!] Your Device is 64 bit');time.sleep(1);print('\n\n[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(2)
    import sayem

else:
    print('\nUNKNOWN DEVICE')
