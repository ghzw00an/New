[app]

# (str) Title of your application
title = PoiExporter

# (str) Package name
package.name = poiexporter

# (str) Package domain (needed for android packaging)
package.domain = org.poiexporter

# 🔴 هذا هو السطر الناقص الذي تسبب في الخطأ
source.dir = .

# (str) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,csv,json,txt

# (list) Source files to include (let it empty to include all files)
source.include_patterns = assets/*,images/*

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,pandas,shapely

# (str) Supported orientations (landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# --- إعدادات الأندرويد ---

# (str) The android specific target API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android build tools version to use
android.build_tools_version = 33.0.2

# (list) The format used to package the app for each architecture
android.archs = arm64-v8a

# (bool) Enables AndroidX support
android.androidx = True

# 🔴 هذا السطر لحل مشكلة التراخيص (من الرد السابق)
android.accept_sdk_license = True
