import requests, time

with open('token.txt') as f:
    tokens = [x.strip() for x in f if x.strip()]
with open('convo.txt') as f:
    convo = f.read().strip()
with open('np.txt', encoding='utf-8') as f:
    messages = [x.strip() for x in f if x.strip()]
with open('hatersname.txt', encoding='utf-8') as f:
    hater = f.read().strip()
with open('time.txt') as f:
    delay = int(f.read().strip())

print(f"🔥 STARTED for convo ID: {convo}")
i = 0
while True:
    for token in tokens:
        for msg in messages:
            full = f"{hater} {msg}"
            url = f"https://graph.facebook.com/v18.0/t_{convo}/messages"
            res = requests.post(url, data={
                "access_token": token,
                "message": full
            })
            i += 1
            print(f"[{time.strftime('%H:%M:%S')}] {i}. {full} → {'✅ OK' if res.status_code==200 else '❌ ' + res.text}")
            time.sleep(delay)
