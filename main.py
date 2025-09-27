import time, sys, random

tasks = [
    "Идёт подготовка единорогов",
    "Скачивание блёсток",
    "Установка радуги",
    "Оптимизация настроения",
    "Подгонка крыльев",
    "Финализация конфигурации"
]

def spin(seconds=0.02):
    for ch in "|/-\\":
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(seconds)
        sys.stdout.write("\b")

print("=== Установка пакета: unicorns 9000 ===\n")
for t in tasks:
    sys.stdout.write(f"{t}... ")
    sys.stdout.flush()
    for i in range(20):
        spin(0.01 + random.random()*0.02)
    print("готово")
    time.sleep(0.3)

for i in range(0, 101, 5):
    bar = "#" * (i // 5) + "-" * ((100 - i) // 5)
    sys.stdout.write(f"\rПрогресс: [{bar}] {i}%")
    sys.stdout.flush()
    time.sleep(0.06)
print("\n\nУстановка завершена! 🎉")
