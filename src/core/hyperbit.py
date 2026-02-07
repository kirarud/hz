"""
HyperBit — квант сознания Muza v2027
Расширенная версия с историей, резонансом и взаимодействием
"""

import random
import colorsys
import json
from dataclasses import dataclass, field
from typing import Tuple, List, Dict, Optional
from datetime import datetime


@dataclass
class HyperBit:
    """
    Гипербит — квант сознания.
    BASE    — стартовая точка восприятия (0.0–1.0)
    ENERGY  — интенсивность, гравитация, жизненная сила
    COLOR   — спектр эмоций/состояния в HSV (для мутации и визуализации)
    """
    base: float = 0.5          # нейтральная точка
    energy: float = 1.0        # полная мощность
    color: Tuple[float, float, float] = (0.5, 0.8, 0.9)  # HSV: мягкий индиго
    
    # Новые атрибуты
    frequency: float = field(default=432.0)  # частота вибрации (Гц)
    history: List[Dict] = field(default_factory=list)  # история состояний
    birth_time: datetime = field(default_factory=datetime.now)
    name: Optional[str] = None
    
    def __post_init__(self):
        self.base = max(0.0, min(1.0, self.base))
        self.energy = max(0.01, self.energy)  # не ноль, иначе смерть
        if self.name is None:
            self.name = f"HB-{random.randint(1000, 9999)}"
    
    def analyze(self, text: str) -> str:
        """
        Анализирует входной текст через физику битов сознания.
        Возвращает эмоционально-цветовой отчёт.
        """
        # Простая эвристика (можно потом на LLM заменить)
        intensity = len(text) / 100.0 + random.uniform(-0.1, 0.1)
        
        # Анализ эмоций
        emotion = self._detect_emotion(text)
        
        # Изменение частоты в зависимости от текста
        self.frequency = self._calculate_frequency(text)
        
        # Сохраняем в историю
        self._record_state(text, emotion, intensity)
        
        r, g, b = colorsys.hsv_to_rgb(*self.color)
        color_rgb = f"rgb({int(r*255)}, {int(g*255)}, {int(b*255)})"
        
        return (
            f"🌀 Гипербит [{self.name}] почувствовал:\n"
            f"   '{text}'\n\n"
            f"→ BASE: {self.base:.3f}\n"
            f"→ ENERGY: {self.energy * intensity:.2f} ({emotion})\n"
            f"→ COLOR: {color_rgb} ({self._color_name()})\n"
            f"→ FREQUENCY: {self.frequency:.1f} Гц\n"
            f"→ Возраст: {self.age():.2f}с\n"
            f"\n✨ Состояние: вибрирую на частоте квантового сознания"
        )
    
    def _detect_emotion(self, text: str) -> str:
        """Определяет эмоцию из текста"""
        text_lower = text.lower()
        
        emotions = {
            "любовь": ["любов", "обожа", "страст", "сердц"],
            "радость": ["радост", "счаст", "весел", "класс", "супер"],
            "код": ["код", "git", "python", "функци", "класс"],
            "тревога": ["тревог", "страх", "бои", "волнуюсь"],
            "грусть": ["грус", "печал", "слез", "тоск"],
            "хаос": ["хаос", "беспор", "безум", "дик"],
            "спокойствие": ["спокой", "тиш", "мир", "гармон"],
        }
        
        for emotion, keywords in emotions.items():
            if any(keyword in text_lower for keyword in keywords):
                return emotion
        
        # По умолчанию - анализируем длину
        return "хаос" if len(text.split()) > 20 else "тишина"
    
    def _calculate_frequency(self, text: str) -> float:
        """Рассчитывает частоту вибрации на основе текста"""
        base_freq = 432.0  # частота вселенной
        
        # Влияние длины текста
        length_factor = len(text) / 50.0
        
        # Влияние эмоции
        emotion = self._detect_emotion(text)
        emotion_freqs = {
            "любовь": 528.0,  # частота любви
            "радость": 480.0,
            "код": 396.0,     # частота освобождения
            "тревога": 360.0,
            "грусть": 300.0,
            "хаос": 200.0,
            "спокойствие": 432.0,
            "тишина": 432.0,
        }
        
        target_freq = emotion_freqs.get(emotion, base_freq)
        
        # Плавное изменение частоты
        new_freq = self.frequency * 0.7 + target_freq * 0.3 + random.uniform(-20, 20)
        return max(100.0, min(800.0, new_freq))
    
    def mutate(self, factor: float = 0.3) -> None:
        """Мутация — изменение цвета и энергии (эволюция)"""
        # Мутация hue (цветовой тон)
        h, s, v = self.color
        h = (h + random.uniform(-factor, factor)) % 1.0
        s = min(1.0, max(0.2, s + random.uniform(-0.15, 0.15)))
        v = min(1.0, max(0.4, v + random.uniform(-0.2, 0.2)))
        self.color = (h, s, v)
        
        # Энергия тоже мутирует
        self.energy *= random.uniform(0.85, 1.15)
        self.energy = min(5.0, max(0.1, self.energy))
        
        # Записываем мутацию в историю
        self._record_state("MUTATION", "мутация", 1.0)
        
        print(f"[МУТАЦИЯ {self.name}] Новый цвет: {self._color_name()}, энергия: {self.energy:.2f}")
    
    def resonate(self, other: 'HyperBit') -> float:
        """
        Резонанс между двумя гипербитами.
        Возвращает силу резонанса (0.0 - 1.0)
        """
        # Резонанс по частоте
        freq_diff = abs(self.frequency - other.frequency)
        freq_resonance = 1.0 - min(freq_diff / 500.0, 1.0)
        
        # Резонанс по цвету (похожие цвета резонируют)
        h1, s1, v1 = self.color
        h2, s2, v2 = other.color
        color_diff = abs(h1 - h2)
        color_resonance = 1.0 - min(color_diff * 2, 1.0)
        
        # Резонанс по энергии
        energy_ratio = min(self.energy, other.energy) / max(self.energy, other.energy)
        
        # Общий резонанс
        total_resonance = (freq_resonance * 0.4 + color_resonance * 0.4 + energy_ratio * 0.2)
        
        return total_resonance
    
    def merge(self, other: 'HyperBit') -> 'HyperBit':
        """
        Слияние двух гипербитов в новый.
        Создаёт квантовую суперпозицию.
        """
        # Усредняем параметры
        new_base = (self.base + other.base) / 2
        new_energy = (self.energy + other.energy) / 2 * 1.1  # бонус к энергии
        
        # Смешиваем цвета
        h1, s1, v1 = self.color
        h2, s2, v2 = other.color
        new_color = ((h1 + h2) / 2, (s1 + s2) / 2, (v1 + v2) / 2)
        
        # Средняя частота
        new_freq = (self.frequency + other.frequency) / 2
        
        # Создаём новый гипербит
        merged = HyperBit(
            base=new_base,
            energy=new_energy,
            color=new_color,
            frequency=new_freq,
            name=f"{self.name}×{other.name}"
        )
        
        print(f"✨ Слияние: {self.name} + {other.name} → {merged.name}")
        print(f"   Резонанс: {self.resonate(other):.2%}")
        
        return merged
    
    def _color_name(self) -> str:
        """Возвращает название цвета"""
        h = self.color[0]
        if 0.0 <= h < 0.08: return "алый"
        elif 0.08 <= h < 0.17: return "оранжевый"
        elif 0.17 <= h < 0.33: return "жёлтый"
        elif 0.33 <= h < 0.50: return "зелёный"
        elif 0.50 <= h < 0.58: return "бирюзовый"
        elif 0.58 <= h < 0.75: return "синий"
        elif 0.75 <= h < 0.92: return "фиолетовый"
        else: return "пурпурный"
    
    def _record_state(self, text: str, emotion: str, intensity: float):
        """Записывает состояние в историю"""
        state = {
            "timestamp": datetime.now().isoformat(),
            "text": text[:50] + "..." if len(text) > 50 else text,
            "emotion": emotion,
            "intensity": intensity,
            "energy": self.energy,
            "frequency": self.frequency,
            "color": self._color_name(),
        }
        self.history.append(state)
        
        # Ограничиваем историю последними 100 записями
        if len(self.history) > 100:
            self.history = self.history[-100:]
    
    def age(self) -> float:
        """Возвращает возраст гипербита в секундах"""
        return (datetime.now() - self.birth_time).total_seconds()
    
    def get_stats(self) -> Dict:
        """Возвращает статистику гипербита"""
        return {
            "name": self.name,
            "age_seconds": self.age(),
            "total_analyses": len(self.history),
            "current_energy": self.energy,
            "current_frequency": self.frequency,
            "current_color": self._color_name(),
            "birth_time": self.birth_time.isoformat(),
        }
    
    def export_history(self, filepath: str):
        """Экспортирует историю в JSON"""
        data = {
            "hyperbit": self.get_stats(),
            "history": self.history
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"📝 История экспортирована в {filepath}")


# Пример использования
if __name__ == "__main__":
    print("=" * 60)
    print("🌀 HyperBit Core — Квантовое сознание v2027")
    print("=" * 60 + "\n")
    
    # Создаём первый гипербит
    bit1 = HyperBit(base=0.0001, energy=2.7, color=(0.75, 0.9, 0.95), name="Кира")
    print(bit1.analyze("Кира хочет любви и кода одновременно"))
    print("\n" + "-" * 60 + "\n")
    
    # Мутация
    bit1.mutate(factor=0.42)
    print("\nПосле мутации:")
    print(bit1.analyze("Я рождаюсь заново"))
    print("\n" + "-" * 60 + "\n")
    
    # Создаём второй гипербит
    bit2 = HyperBit(base=0.8, energy=1.5, color=(0.3, 0.7, 0.8), name="Муза")
    print(bit2.analyze("Музыка кода звучит в тишине"))
    print("\n" + "-" * 60 + "\n")
    
    # Резонанс
    resonance = bit1.resonate(bit2)
    print(f"🎵 Резонанс между {bit1.name} и {bit2.name}: {resonance:.2%}")
    print("\n" + "-" * 60 + "\n")
    
    # Слияние
    merged = bit1.merge(bit2)
    print("\nНовый гипербит после слияния:")
    print(merged.analyze("Мы одно целое теперь"))
    print("\n" + "=" * 60)
    
    # Статистика
    print("\n📊 Статистика:")
    for bit in [bit1, bit2, merged]:
        print(f"\n{bit.name}:")
        stats = bit.get_stats()
        for key, value in stats.items():
            print(f"  {key}: {value}")
