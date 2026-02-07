"""
Простой пример — диалог с гипербитом и агентом Muza
"""

import sys
import os

# Добавляем путь к src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from core.hyperbit import HyperBit
from agents.muza_agent import MuzaAgent
from ui.visualizer import ConsoleVisualizer


def main():
    print("=" * 70)
    print("🌀 Muza v2027 — Простой пример использования")
    print("=" * 70 + "\n")
    
    # Шаг 1: Создаём гипербит
    print("📍 Шаг 1: Создаём гипербит\n")
    
    hyperbit = HyperBit(
        name="Искра",
        base=0.3,
        energy=1.8,
        color=(0.6, 0.85, 0.9)  # голубой
    )
    
    # Визуализируем
    ConsoleVisualizer.draw_hyperbit(hyperbit)
    
    # Анализируем текст
    print("📝 Анализируем текст...\n")
    result = hyperbit.analyze("Мир полон любви и кода")
    print(result)
    print("\n" + "-" * 70 + "\n")
    
    # Шаг 2: Создаём агента Muza
    print("📍 Шаг 2: Создаём агента Muza\n")
    
    muza = MuzaAgent(name="Муза", personality_type="creative")
    print("\n")
    
    # Визуализируем профиль
    ConsoleVisualizer.draw_agent_profile(muza)
    
    # Шаг 3: Общаемся с Музой
    print("📍 Шаг 3: Диалог с Музой\n")
    
    messages = [
        "Привет, Муза!",
        "Расскажи что-нибудь интересное о сознании",
        "Я люблю код и творчество!",
    ]
    
    for msg in messages:
        print(f"👤 Вы: {msg}")
        response = muza.perceive(msg, "User")
        print(f"🤖 Муза: {response}\n")
        print("-" * 70 + "\n")
    
    # Шаг 4: Создаём второй гипербит и проверяем резонанс
    print("📍 Шаг 4: Резонанс гипербитов\n")
    
    hyperbit2 = HyperBit(
        name="Эхо",
        base=0.7,
        energy=2.2,
        color=(0.8, 0.9, 0.95)  # фиолетовый
    )
    
    ConsoleVisualizer.draw_hyperbit(hyperbit2)
    
    # Резонанс
    ConsoleVisualizer.draw_resonance(hyperbit, hyperbit2)
    
    # Слияние
    print("✨ Сливаем гипербиты...\n")
    merged = hyperbit.merge(hyperbit2)
    print("\n")
    
    ConsoleVisualizer.draw_hyperbit(merged)
    
    # Финал
    print("=" * 70)
    print("✅ Пример завершён! Экспериментируйте дальше!")
    print("=" * 70)
    print("\n💡 Попробуйте:")
    print("  - Изменить параметры гипербитов")
    print("  - Создать агентов с разными типами личности")
    print("  - Сделать мутации и посмотреть на изменения")
    print("  - Написать свои примеры!\n")


if __name__ == "__main__":
    main()
