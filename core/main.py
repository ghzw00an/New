# gis_core.py - محرك التحليل والجودة للبيانات الجغرافية
import pandas as pd

class PoiGisEngine:
    def __init__(self):
        # جدول بيانات المعلم الثابت
        self.columns = ['name', 'type', 'Gategory', 'gathaa', 'Nahia', 'mohafadha', 'x', 'y', 'link']
        self.df = pd.DataFrame(columns=self.columns)

    def add_feature(self, name, f_type, category, x, y, gathaa="", nahia="", mohafadha="", link=""):
        """إضافة معلم جديد وحفظ إحداثيات UTM"""
        new_row = {
            'name': name,
            'type': f_type,
            'Gategory': category,
            'gathaa': gathaa,
            'Nahia': nahia,
            'mohafadha': mohafadha,
            'x': float(x),
            'y': float(y),
            'link': link
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def get_all_features(self):
        """استرجاع كفافة المعالم"""
        return self.df
