[app]

# (str) Title of your application
title = PoiExporter

# (str) Package name
package.name = poiexporter

# (str) Package domain (needed for android packaging)
package.domain = org.poiexporter

# (str) Source directory where the application lives
source.dir = core

# (str) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,csv,json,txt

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,pandas,shapely

# (str) Supported orientations (landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) The android specific target API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android build tools version to use
android.build_tools_version = 33.0.2

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (list) The format used to package the app for each architecture
android.archs = arm64-v8a

# (bool) Enables AndroidX support
android.androidx = True
