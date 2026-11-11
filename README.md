# MusicFlow (Android APK)

Android-приложение MusicFlow. Внутри — веб-версия плеера с https://burmolda.ru/music
(загрузки, сборники, вход и стриминг работают через сервер).

## Как получить APK без ПК

1. Откройте вкладку **Actions** репозитория → **Build APK** → **Run workflow**
   (или просто сделайте любой push в `main`).
2. Когда сборка зелёная, откройте запуск и скачайте артефакт **MusicFlow-apk** (файл `MusicFlow.apk`).
3. Перенесите APK на телефон, разрешите установку из неизвестных источников и установите.

Для постоянной ссылки на скачивание создайте тег `v1.0.0` — APK прикрепится к релизу.

## Структура

- `www/index.html` — страница-заглушка (актуальная `music.html`), используется Capacitor при сборке.
- `capacitor.config.json` — адрес сервера (`server.url`) и id приложения.
- `.github/workflows/build-apk.yml` — сборка APK в GitHub Actions.
