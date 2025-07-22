from flask import Flask, render_template, request, redirect
import os, uuid, subprocess, threading

app = Flask(__name__)
TASKS = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run():
    if request.form.get("password") != "manixrana1":
        return "❌ Incorrect password"

    tid = uuid.uuid4().hex[:8]
    open("token.txt", "w").write(request.form.get("token"))
    open("convo.txt", "w").write(request.form.get("convo"))
    open("time.txt", "w").write(request.form.get("time"))
    open("hatersname.txt", "w").write(request.form.get("haters"))
    file = request.files["npfile"]
    file.save("np.txt")

    def task():
        with open(f"{tid}.log", "w") as log:
            p = subprocess.Popen(["python3", "main.py"], stdout=log, stderr=log)
            TASKS[tid] = p
            p.wait()

    threading.Thread(target=task).start()
    return redirect(f"/logs/{tid}")

@app.route("/logs/<tid>")
def logs(tid):
    if not os.path.exists(f"{tid}.log"):
        return "No such task"
    with open(f"{tid}.log", "r") as f:
        return f"<pre>{f.read()}</pre>"

@app.route("/stop", methods=["POST"])
def stop():
    tid = request.form.get("stopid")
    proc = TASKS.get(tid)
    if proc:
        proc.terminate()
        return f"🛑 Task {tid} stopped."
    return "Task not found."

@app.route("/check", methods=["POST"])
def check():
    tid = request.form.get("checkid")
    return redirect(f"/logs/{tid}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
