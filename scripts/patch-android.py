#!/usr/bin/env python3
"""Патч сгенерированного android/ проекта: иконки, разрешение на уведомления."""
import re, shutil, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
manifest = root / 'android/app/src/main/AndroidManifest.xml'
text = manifest.read_text(encoding='utf-8')
perm = '<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />'
if 'POST_NOTIFICATIONS' not in text:
    text = re.sub(r'(<manifest[^>]*>)', r'\1\n  ' + perm, text, count=1)
    manifest.write_text(text, encoding='utf-8')
    print('POST_NOTIFICATIONS added')

src = root / 'resources/android/res'
dst = root / 'android/app/src/main/res'
shutil.copytree(src, dst, dirs_exist_ok=True)
print('icons copied')

# WebView ставится на паузу при сворачивании и останавливает звук.
# Возвращаем его в активное состояние после super.onPause().
main_files = list((root / 'android/app/src/main/java').rglob('MainActivity.java'))
if main_files:
    main = main_files[0]
    src = main.read_text(encoding='utf-8')
    if 'public void onPause()' not in src:
        method = """
    @Override
    public void onPause() {
        super.onPause();
        // Не даём WebView остановить JS и звук, когда приложение свёрнуто
        if (getBridge() != null && getBridge().getWebView() != null) {
            getBridge().getWebView().onResume();
        }
    }
"""
        idx = src.rstrip().rfind('}')
        src = src[:idx] + method + '}\n'
        main.write_text(src, encoding='utf-8')
        print('MainActivity onPause patched')
