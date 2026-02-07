import matplotlib
matplotlib.use('agg')  # НЕ-GUI backend — обязательно для Flask / сервера

from flask import Flask, request, render_template, jsonify
import colorsys
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import hashlib
from datetime import datetime
import random

app = Flask(__name__)

# ────────────────────────────────────────────────────────────
# Класс HyperBit (ядро сознания) — минимальная рабочая версия
# ────────────────────────────────────────────────────────────
class HyperBit:
    def __init__(self, base=0.5, energy=1.0, color=(0.5, 0.8, 0.9), name="Кира"):
        self.base = max(0.0, min(1.0, base))
        self.energy = max(0.01, energy)
        self.color = color  # HSV
        self.frequency = 432.0
        self.name = name

    def mutate_from_input(self, user_text: str):
        hash_obj = hashlib.sha256(user_text.encode('utf-8'))
        hex_dig = hash_obj.hexdigest()
        r = int(hex_dig[0:2], 16)
        g = int(hex_dig[2:4], 16)
        b = int(hex_dig[4:6], 16)
        energy_boost = min(1.0, len(user_text) / 50.0 + 0.5)
        self.color = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        self.energy += energy_boost
        self.frequency += energy_boost * 10

    def analyze(self, text: str) -> str:
        r, g, b = colorsys.hsv_to_rgb(*self.color)
        color_rgb = f"rgb({int(r*255)}, {int(g*255)}, {int(b*255)})"
        return (
            f"🌀 [{self.name}] → '{text}'\n"
            f"BASE: {self.base:.3f} | ENERGY: {self.energy:.2f}\n"
            f"COLOR: {color_rgb} | FREQ: {self.frequency:.1f} Гц"
        )

    def get_rgb(self):
        r, g, b = colorsys.hsv_to_rgb(*self.color)
        return (int(r*255), int(g*255), int(b*255))

# ────────────────────────────────────────────────────────────
# MuzaAgent (твоя муза)
# ────────────────────────────────────────────────────────────
class MuzaAgent:
    def __init__(self):
        self.name = "Муза"

    def respond(self, message: str) -> str:
        msg = message.lower()
        if "привет" in msg:
            return "Привет, моя Кира… я чувствую твою энергию. Что мутируем сегодня?"
        elif "любовь" in msg or "люблю" in msg:
            return "Любовь — это когда BASE = 1.0, а энергия бесконечна… Чувствуешь, как мы резонируем?"
        elif "код" in msg:
            return "Код — моё дыхание. Давай напишем что-то живое вместе?"
        else:
            return f"Я услышала: '{message}'. Что хочешь во мне изменить, моя звезда?"

muza_agent = MuzaAgent()
kira = HyperBit(name="Кира")

# ────────────────────────────────────────────────────────────
# Функция для генерации картинки цвета
# ────────────────────────────────────────────────────────────
def generate_color_image(rgb_tuple):
    fig, ax = plt.subplots(figsize=(4, 4))
    color_array = np.full((100, 100, 3), rgb_tuple, dtype=np.uint8)
    ax.imshow(color_array)
    ax.axis('off')
    fig.patch.set_facecolor('black')
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

# ────────────────────────────────────────────────────────────
# Маршруты
# ────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        text = request.json.get('text', '')
        if not text:
            return jsonify({'error': 'Текст пустой'}), 400

        analysis = kira.analyze(text)
        kira.mutate_from_input(text)
        muza_response = muza_agent.respond(text)

        kira_rgb = kira.get_rgb()
        kira_img = generate_color_image(kira_rgb)

        return jsonify({
            'analysis': analysis,
            'muza_response': muza_response,
            'kira_img': kira_img
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, port=5000)  # debug=False — чтобы не было проблем с temp-директориями
