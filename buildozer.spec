[app]

# (str) Title of your application
title = PoiExporter

# (str) Package name
package.name = poiexporter

# (str) Package domain (needed for android packaging)
package.domain = org.poiexporter

# (list) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# هنا نحدد المكتبات الجغرافية التي سنحتاجها
requirements = python3,kivy,pandas,shapely

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_FINE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
