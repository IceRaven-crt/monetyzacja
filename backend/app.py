#!/usr/bin/env python3
# 🚀 Agent Handlowy SaaS - Backend
from flask import Flask, request, jsonify, render_template_string
import json
from pathlib import Path
from datetime import datetime
import random

app = Flask(__name__)
DANE = Path.home() / "monetyzacja" / "dane"
DANE.mkdir(parents=True, exist_ok=True)
SUBS_FILE = DANE / "subskrybenci.json"

def load_subs():
    if SUBS_FILE.exists():
        return json.loads(SUBS_FILE.read_text())
    return []

def save_subs(subs):
    SUBS_FILE.write_text(json.dumps(subs, indent=2, ensure_ascii=False))

@app.route("/")
def index():
    return render_template_string("""
    <h1 style="font-family:Arial;background:#0a0a0a;color:#0f0;padding:40px;min-height:100vh">
    🛒 Agent Handlowy SaaS<br><br>
    <a href="/api/health" style="color:#0f0">/api/health</a><br>
    <a href="/api/analiza" style="color:#0f0">/api/analiza</a><br>
    <a href="/api/subskrybenci" style="color:#0f0">/api/subskrybenci</a>
    </h1>
    """)

@app.route("/api/health")
def health():
    return jsonify({"status": "online", "timestamp": datetime.now().isoformat()})

@app.route("/api/analiza")
def analiza():
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "amazon": {"cena": round(random.uniform(50,500),2), "popyt": round(random.uniform(.3,.9),2)},
        "allegro": {"cena": round(random.uniform(50,500),2), "popyt": round(random.uniform(.3,.9),2)},
        "rekomendacja": random.choice(["KUP","TRZYMAJ","ODRZUĆ"])
    })

@app.route("/api/subskrybenci", methods=["GET","POST"])
def subskrybenci():
    subs = load_subs()
    if request.method == "POST":
        data = request.json or {}
        subs.append({"email": data.get("email"), "plan": data.get("plan","pro"), "ts": datetime.now().isoformat()})
        save_subs(subs)
        return jsonify({"status":"ok","count":len(subs)})
    return jsonify(subs)

if __name__ == "__main__":
    print("🚀 SaaS backend: http://0.0.0.0:8000")
    app.run(host="0.0.0.0", port=8000, debug=False)
