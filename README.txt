СБОРКА
1) Установите JDK 21.
2) Положите оригинальный light.glsl с правкой для сущностей:
     python patch_light.py "путь/к/.minecraft/versions/1.21.11/1.21.11.jar"
   (Windows: python -> py)
3) Соберите:   gradlew build        (Windows: gradlew.bat build)
4) Готовый мод: build/libs/nolight-1.0.0.jar  (НЕ файл с -sources)
5) Положите jar в папку mods. Нужен только Fabric Loader 0.19.5+ (Fabric API не нужен).

Отдельно в настройках игры: Графика -> Тени сущностей -> выкл.
Если игра падает на запуске, пришлите мне latest.log.
