#!/usr/bin/env python3
"""Берёт оригинальный light.glsl из jar игры и заменяет minecraft_mix_light
так, чтобы затенение сущностей отключилось. Результат кладёт в ресурсы мода.

Использование:  python patch_light.py <путь к 1.21.11.jar>
(jar лежит в .minecraft/versions/1.21.11/1.21.11.jar)
"""
import sys, zipfile, re, pathlib

SRC = "assets/minecraft/shaders/include/light.glsl"
OUT = pathlib.Path(__file__).parent / "src/main/resources" / SRC

if len(sys.argv) != 2:
    sys.exit(__doc__)

with zipfile.ZipFile(sys.argv[1]) as z:
    try:
        text = z.read(SRC).decode("utf-8")
    except KeyError:
        sys.exit(f"В jar нет {SRC}. Пришлите мне список файлов в assets/minecraft/shaders/")

m = re.search(r"vec4\s+minecraft_mix_light\s*\([^)]*\)\s*\{", text)
if not m:
    print("Функция minecraft_mix_light не найдена. Содержимое оригинала:\n")
    print(text)
    sys.exit(1)

depth, i = 1, m.end()
while depth:
    c = text[i]
    depth += (c == "{") - (c == "}")
    i += 1

sig = text[m.start():m.end()]
new = sig + "\n    return color;\n}"
patched = text[:m.start()] + new + text[i:]
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(patched, encoding="utf-8")
print("Готово:", OUT)
print("--- было ---\n" + text[m.start():i] + "\n--- стало ---\n" + new)
