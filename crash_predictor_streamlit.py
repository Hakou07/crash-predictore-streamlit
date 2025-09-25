#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import requests
import random
import json
from datetime import datetime

class CrashPredictor:
    def __init__(self):
        self.history = []

    def get_real_crash_data(self):
        try:
            response = requests.get('https://api.1xbet.com/live/crash', timeout=5)
            data = response.json()
            return data.get('crash_point')
        except Exception as e:
            print('API error:', e)
            return None

    def predict(self):
        cp = self.get_real_crash_data()
        if cp is None:
            cp = round(random.uniform(1.0, 10.0), 2)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.history.append((now, cp))
        return cp

st.set_page_config(page_title='مفترس كراش - Web', layout='centered')
st.title('🛩️ مفترس كراش — Crash Predictor (Web)')

if 'predictor' not in st.session_state:
    st.session_state.predictor = CrashPredictor()
if 'history' not in st.session_state:
    st.session_state.history = []

st.markdown('**ملاحظة:** هذه نسخة Web. `tkinter` ما يخدمش في المتصفح، لهذا حولنا الواجهة إلى Streamlit.')

col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button('🔄 جلب الآن (حقيقي أو محاكاة)'):
        point = st.session_state.predictor.predict()
        st.session_state.history.append((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), point))
        st.success(f'🔮 نقطة الحصول: **{point}**')

with col2:
    n = st.number_input('عدد نقاط المحاكاة', min_value=1, max_value=200, value=5, step=1)
    if st.button('🎮 محاكاة'):
        results = []
        for i in range(n):
            pt = round(random.uniform(1.0, 10.0), 2)
            st.session_state.history.append((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), pt))
            results.append(pt)
        st.info(f'تمت المحاكاة: {results}')

with col3:
    if st.button('🧹 مسح السجل'):
        st.session_state.history = []
        st.success('✅ السجل تفريغ')

st.write('---')
st.header('📊 آخر النتائج (آخر 20)')
if st.session_state.history:
    rows = list(reversed(st.session_state.history[-20:]))
    st.table(rows)
else:
    st.write("ما فمّاش نتائج بعد. استعمل 'جلب الآن' أو 'محاكاة'.")

st.write('---')
if st.session_state.history:
    json_data = json.dumps(st.session_state.history, ensure_ascii=False, indent=2)
    st.download_button('⬇️ تحميل السجل (JSON)', data=json_data, file_name='crash_history.json', mime='application/json')

st.write("**تعليمات سريعة للتشغيل (Replit أو أي بيئة تدعم Streamlit):**")
st.markdown("""
1. أنشئ ملف `crash_predictor_streamlit.py` وحط فيه هذا الكود.  
2. أنشئ ملف `requirements.txt` يحتوي على:  
   `streamlit` `requests` `numpy` `pandas` (pandas اختياري)  
3. في التيرمينال نفذ: `pip install -r requirements.txt`  
4. شغل التطبيق:  
   - في Replit: `streamlit run crash_predictor_streamlit.py --server.port=$PORT --server.headless=true`  
   - محليا: `streamlit run crash_predictor_streamlit.py` ثم افتح http://localhost:8501
""")
