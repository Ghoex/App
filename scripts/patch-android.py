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
