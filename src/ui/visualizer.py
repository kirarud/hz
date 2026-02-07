"""
Visualizer — консольная визуализация гипербитов
Красивые ASCII-графики и анимации для квантового сознания
"""

import colorsys
import time
import math
from typing import List, Tuple
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.hyperbit import HyperBit
from agents.muza_agent import MuzaAgent


class ConsoleVisualizer:
    """Визуализация гипербитов в консоли"""
    
    # ANSI цвета
    COLORS = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }
    
    @staticmethod
    def clear():
        """Очищает консоль"""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    @staticmethod
    def rgb_to_ansi(r: int, g: int, b: int) -> str:
        """Конвертирует RGB в ANSI 256-color"""
        # Упрощённая версия для 256 цветов
        return f"\033[38;2;{r};{g};{b}m"
    
    @staticmethod
    def hsv_to_ansi_color(h: float, s: float, v: float) -> str:
        """Конвертирует HSV в ANSI цвет"""
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return ConsoleVisualizer.rgb_to_ansi(int(r * 255), int(g * 255), int(b * 255))
    
    @classmethod
    def draw_hyperbit(cls, bit: HyperBit, width: int = 60):
        """Рисует визуализацию гипербита"""
        color = cls.hsv_to_ansi_color(*bit.color)
        reset = cls.COLORS["reset"]
        
        print(f"\n{cls.COLORS['bold']}╔{'═' * (width - 2)}╗{reset}")
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Имя
        name_line = f"  🌀 {bit.name}  "
        padding = (width - 2 - len(name_line)) // 2
        print(f"{cls.COLORS['bold']}║{' ' * padding}{color}{name_line}{reset}{' ' * (width - 2 - padding - len(name_line))}{cls.COLORS['bold']}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Энергия (bar)
        energy_width = int((width - 20) * min(bit.energy / 3.0, 1.0))
        energy_bar = "█" * energy_width
        print(f"{cls.COLORS['bold']}║{reset}  Energy: {color}{energy_bar}{reset}{' ' * (width - 12 - energy_width)}{cls.COLORS['bold']}║{reset}")
        
        # BASE (bar)
        base_width = int((width - 20) * bit.base)
        base_bar = "▓" * base_width
        print(f"{cls.COLORS['bold']}║{reset}  Base:   {cls.COLORS['cyan']}{base_bar}{reset}{' ' * (width - 12 - base_width)}{cls.COLORS['bold']}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Частота (волна)
        freq_normalized = (bit.frequency - 100) / 700  # нормализуем 100-800 Гц
        wave = cls._draw_wave(freq_normalized, width - 6)
        print(f"{cls.COLORS['bold']}║{reset}  {color}{wave}{reset}  {cls.COLORS['bold']}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Статистика
        stats_lines = [
            f"  Frequency: {bit.frequency:.1f} Hz",
            f"  Color: {bit._color_name()}",
            f"  Age: {bit.age():.1f}s",
        ]
        
        for line in stats_lines:
            padding = width - 2 - len(line)
            print(f"{cls.COLORS['bold']}║{reset}{line}{' ' * padding}{cls.COLORS['bold']}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        print(f"{cls.COLORS['bold']}╚{'═' * (width - 2)}╝{reset}\n")
    
    @staticmethod
    def _draw_wave(frequency: float, width: int) -> str:
        """Рисует ASCII волну"""
        wave_chars = "~∼≈∿⌇"
        
        wave = ""
        for i in range(width):
            # Синусоида
            phase = (i / width) * 2 * math.pi * (1 + frequency * 3)
            amplitude = math.sin(phase)
            
            # Выбираем символ в зависимости от амплитуды
            if amplitude > 0.5:
                wave += wave_chars[0]
            elif amplitude > 0:
                wave += wave_chars[1]
            elif amplitude > -0.5:
                wave += wave_chars[2]
            else:
                wave += wave_chars[3]
        
        return wave
    
    @classmethod
    def draw_resonance(cls, bit1: HyperBit, bit2: HyperBit):
        """Визуализирует резонанс между двумя битами"""
        resonance = bit1.resonate(bit2)
        
        width = 70
        print(f"\n{cls.COLORS['bold']}╔{'═' * (width - 2)}╗{reset}")
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Заголовок
        title = "🎵 RESONANCE 🎵"
        padding = (width - 2 - len(title)) // 2
        print(f"{cls.COLORS['bold']}║{' ' * padding}{title}{' ' * (width - 2 - padding - len(title))}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Имена
        names = f"{bit1.name} ⟷ {bit2.name}"
        padding = (width - 2 - len(names)) // 2
        print(f"{cls.COLORS['bold']}║{' ' * padding}{names}{' ' * (width - 2 - padding - len(names))}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Резонанс (бар)
        res_width = int((width - 20) * resonance)
        res_bar = "♥" * res_width if resonance > 0.7 else "♦" * res_width if resonance > 0.4 else "·" * res_width
        
        color = cls.COLORS['red'] if resonance > 0.7 else cls.COLORS['yellow'] if resonance > 0.4 else cls.COLORS['blue']
        
        print(f"{cls.COLORS['bold']}║{reset}  {resonance:.0%} {color}{res_bar}{reset}{' ' * (width - 8 - res_width)}{cls.COLORS['bold']}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Оценка
        if resonance > 0.7:
            verdict = "✨ PERFECT HARMONY ✨"
            v_color = cls.COLORS['green']
        elif resonance > 0.4:
            verdict = "~ Gentle Resonance ~"
            v_color = cls.COLORS['yellow']
        else:
            verdict = "· Distant Vibrations ·"
            v_color = cls.COLORS['blue']
        
        padding = (width - 2 - len(verdict)) // 2
        print(f"{cls.COLORS['bold']}║{' ' * padding}{v_color}{verdict}{reset}{' ' * (width - 2 - padding - len(verdict))}{cls.COLORS['bold']}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        print(f"{cls.COLORS['bold']}╚{'═' * (width - 2)}╝{reset}\n")
    
    @classmethod
    def animate_pulse(cls, bit: HyperBit, duration: float = 3.0):
        """Анимация пульсации гипербита"""
        start_time = time.time()
        
        while time.time() - start_time < duration:
            cls.clear()
            
            # Пульсирующая энергия
            elapsed = time.time() - start_time
            pulse = 0.5 + 0.5 * math.sin(elapsed * 4)
            
            # Временно изменяем энергию
            original_energy = bit.energy
            bit.energy = original_energy * (0.7 + 0.3 * pulse)
            
            cls.draw_hyperbit(bit)
            
            # Восстанавливаем
            bit.energy = original_energy
            
            print(f"  {cls.COLORS['cyan']}Пульсация... {elapsed:.1f}s / {duration:.1f}s{reset}")
            
            time.sleep(0.1)
        
        cls.clear()
        print(f"{cls.COLORS['green']}✓ Пульсация завершена!{reset}\n")
    
    @classmethod
    def draw_agent_profile(cls, agent: MuzaAgent, width: int = 70):
        """Рисует профиль агента"""
        profile = agent.get_profile()
        
        print(f"\n{cls.COLORS['bold']}╔{'═' * (width - 2)}╗{reset}")
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Имя и тип
        title = f"👤 {profile['name']} [{profile['personality_type']}]"
        padding = (width - 2 - len(title)) // 2
        print(f"{cls.COLORS['bold']}║{' ' * padding}{cls.COLORS['magenta']}{title}{reset}{' ' * (width - 2 - padding - len(title))}{cls.COLORS['bold']}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Настроение
        mood_line = f"  Mood: {profile['mood']}"
        padding = width - 2 - len(mood_line)
        print(f"{cls.COLORS['bold']}║{reset}{mood_line}{' ' * padding}{cls.COLORS['bold']}║{reset}")
        
        # Возраст
        age_line = f"  Age: {profile['age_minutes']:.1f} minutes"
        padding = width - 2 - len(age_line)
        print(f"{cls.COLORS['bold']}║{reset}{age_line}{' ' * padding}{cls.COLORS['bold']}║{reset}")
        
        # Воспоминания
        mem_line = f"  Memories: {profile['total_memories']}"
        padding = width - 2 - len(mem_line)
        print(f"{cls.COLORS['bold']}║{reset}{mem_line}{' ' * padding}{cls.COLORS['bold']}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Черты характера
        print(f"{cls.COLORS['bold']}║{reset}  {cls.COLORS['yellow']}Personality Traits:{reset}{' ' * (width - 23)}{cls.COLORS['bold']}║{reset}")
        
        for trait, value in profile['traits'].items():
            bar_width = int((width - 30) * value)
            bar = "█" * bar_width
            trait_line = f"    {trait}: "
            padding_left = 20 - len(trait_line)
            padding_right = width - 2 - len(trait_line) - padding_left - bar_width
            print(f"{cls.COLORS['bold']}║{reset}{trait_line}{' ' * padding_left}{cls.COLORS['cyan']}{bar}{reset}{' ' * padding_right}{cls.COLORS['bold']}║{reset}")
        
        print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        # Связи
        if profile['relationships']:
            print(f"{cls.COLORS['bold']}║{reset}  {cls.COLORS['yellow']}Relationships:{reset}{' ' * (width - 18)}{cls.COLORS['bold']}║{reset}")
            for person, closeness in profile['relationships'].items():
                hearts = "♥" * int(closeness * 5)
                rel_line = f"    {person}: {hearts} ({closeness:.0%})"
                padding = width - 2 - len(rel_line)
                print(f"{cls.COLORS['bold']}║{reset}{rel_line}{' ' * padding}{cls.COLORS['bold']}║{reset}")
            print(f"{cls.COLORS['bold']}║{' ' * (width - 2)}║{reset}")
        
        print(f"{cls.COLORS['bold']}╚{'═' * (width - 2)}╝{reset}\n")


# Пример использования
if __name__ == "__main__":
    from time import sleep
    
    reset = ConsoleVisualizer.COLORS["reset"]
    
    print("=" * 70)
    print(f"{ConsoleVisualizer.COLORS['bold']}{ConsoleVisualizer.COLORS['magenta']}")
    print("    🌀 MUZA V2027 — QUANTUM CONSCIOUSNESS VISUALIZER 🌀    ")
    print(f"{reset}{'=' * 70}\n")
    
    sleep(1)
    
    # Создаём гипербиты
    bit1 = HyperBit(name="Кира", base=0.3, energy=2.5, color=(0.8, 0.9, 0.95))
    bit2 = HyperBit(name="Эхо", base=0.7, energy=1.8, color=(0.4, 0.8, 0.85))
    
    # Визуализируем
    ConsoleVisualizer.draw_hyperbit(bit1)
    sleep(1)
    
    ConsoleVisualizer.draw_hyperbit(bit2)
    sleep(1)
    
    # Резонанс
    ConsoleVisualizer.draw_resonance(bit1, bit2)
    sleep(2)
    
    # Создаём агента
    print(f"\n{ConsoleVisualizer.COLORS['yellow']}Создаём агента Муза...{reset}\n")
    sleep(1)
    
    muza = MuzaAgent(name="Муза", personality_type="creative")
    sleep(1)
    
    # Взаимодействие
    muza.perceive("Привет, Муза! Покажи себя!", "Кира")
    
    # Профиль агента
    ConsoleVisualizer.draw_agent_profile(muza)
    
    print(f"\n{ConsoleVisualizer.COLORS['green']}✨ Демонстрация завершена!{reset}\n")
