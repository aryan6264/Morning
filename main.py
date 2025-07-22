import requests
import time
import os

print("✅ MAIN.PY STARTED")

try:
    with open('token.txt', 'r') as f:
        tokens = [x.strip() for x in f if x.strip()]
    print(f"✔️ Loaded {len(tokens)} tokens")
except Exception as e:
    print(f"❌ Error reading token.txt: {e}")
    exit()

try:
    with open('convo.txt', 'r') as f:
        convo = f.read().strip()
    print(f"✔️ Convo ID: {convo}")
except Exception as e:
    print(f"❌ Error reading convo.txt: {e}")
    exit()

try:
    with open('np.txt', 'r', encoding='utf-8') as f:
        messages = [x.strip() for x in f if x.strip()]
    print(f"✔️ Loaded {len(messages)} messages from np.txt")
except Exception as e:
    print(f"❌ Error reading np.txt: {e}")
    exit()

try:
    with open('time.txt', 'r') as f:
        delay = int(f.read().strip())
    print(f"✔️ Delay: {delay}s")
except Exception as e:
    print(f"❌ Error reading time.txt: {e}")
    delay = 2

try:
    with open('hatersname.txt', 'r', encoding='utf-8') as f:
        hater = f.read().strip()
    print(f"✔️ Hater Name: {hater}")
except Exception as e:
    print(f"❌ Error reading hatersname.txt: {e}")
    hater = ""

print("🚀 STARTING MESSAGE SEND LOOP")

counter = 0
while True:
    for token in tokens:
        for msg in messages:
            full_msg = f"{hater} {msg}"
            url = f"https://graph.facebook.com/v18.0/t_{convo}/messages"
            res = requests.post(url, data={
                "access_token": token,
                "message": full_msg
            })

            counter += 1
            timestamp = time.strftime('%H:%M:%S')
            if res.status_code == 200:
                print(f"[{timestamp}] ✅ {counter}. SENT: {full_msg}")
            else:
                print(f"[{timestamp}] ❌ {counter}. FAILED: {res.text}")
            time.sleep(delay)
