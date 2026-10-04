#!/usr/bin/env python3
import sys, zipfile, re, pathlib

SRC = "assets/minecraft/shaders/include/light.glsl"
OUT = pathlib.Path(__file__).parent / "src/main/resources" / SRC

if len(sys.argv) != 2:
    sys.exit("usage: patch_light.py <jar>")

with zipfile.ZipFile(sys.argv[1]) as z:
    try:
        text = z.read(SRC).decode("utf-8")
    except KeyError:
        sys.exit(f"В jar нет {SRC}")

def patch(text, name):
    m = re.search(r"vec4\s+" + name + r"\s*\([^)]*\)\s*\{", text)
    if not m:
        return text, False
    depth, i = 1, m.end()
    while depth:
        c = text[i]
        depth += (c == "{") - (c == "}")
        i += 1
    sig = text[m.start():m.end()]
    return text[:m.start()] + sig + "\n    return color;\n}" + text[i:], True

found = []
for name in ("minecraft_mix_light", "minecraft_mix_light_separate"):
    text, ok = patch(text, name)
    found.append((name, ok))
    print(("пропатчено: " if ok else "НЕ НАЙДЕНО: ") + name)

if not any(ok for _, ok in found):
    print(text)
    sys.exit("Ни одна функция не найдена")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(text, encoding="utf-8")
print("Готово:", OUT)
print(text)
