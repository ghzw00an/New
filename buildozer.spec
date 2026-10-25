[app]

# (str) Title of your application
title = PoiExporter

# (str) Package name
package.name = poiexporter

# (str) Package domain
package.domain = org.poiexporter

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,pandas,shapely

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_FINE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Presplash background color
android.presplash_color = #FFFFFF

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = ./bin
