[app]

# (str) Title of your application
title = PoiExporter

# (str) Package name
package.name = poiexporter

# (str) Package domain (needed for android packaging)
package.domain = org.poiexporter

# (str) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,csv,json,txt

# (list) Source files to include (let it empty to include all files)
source.include_patterns = assets/*,images/*

# (str) Application versioning
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# ملاحظة: تأكد من أن shapely و pandas تدعم البناء لـ Android (قد تحتاج إلى recipes خاصة)
requirements = python3,kivy,pandas,shapely

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (str) Supported orientations (landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Prerender icon glyph (deprecated)
#icon.filename = %(source.dir)s/data/icon.png

# (string) Presplash background color
#presplash.color = #FFFFFF

# (list) Clear application data on launch
#android.clear_app_data_on_launch = False

# --- إعدادات الأندرويد ---

# (str) The android specific target API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android build tools version to use
# تم توحيدها مع android.api لتجنب مشاكل التحميل
android.build_tools_version = 33.0.2

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (list) The format used to package the app for each architecture
android.archs = arm64-v8a

# (bool) Enables AndroidX support
android.androidx = True

# 🔴 هذا هو السطر الأهم لحل مشكلة الخطأ في GitHub Actions
# يقبل تراخيص Android SDK تلقائياً دون الحاجة لتدخل يدوي
android.accept_sdk_license = True
