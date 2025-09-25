
\f0\i\fs28 \cf2 #!/usr/bin/env python3
\f1\i0 \cf3 \

\f0\i \cf2 # -*- coding: utf-8 -*-
\f1\i0 \cf3 \
\cf4 import\cf3  streamlit \cf4 as\cf3  st\
\cf4 import\cf3  requests\
\cf4 import\cf3  random\
\cf4 import\cf3  json\
\cf4 from\cf3  datetime \cf4 import\cf3  datetime\
\
\cf4 class\cf3  CrashPredictor:\
    \cf4 def\cf3  __init__(self):\
        self.history = []\
\
    \cf4 def\cf3  get_real_crash_data(self):\
        \cf4 try\cf3 :\
            response = requests.get(\cf5 'https://api.1xbet.com/live/crash'\cf3 , timeout=\cf6 5\cf3 )\
            data = response.json()\
            \cf4 return\cf3  data.get(\cf5 'crash_point'\cf3 )\
        \cf4 except\cf3  Exception \cf4 as\cf3  e:\
            print(\cf5 'API error:'\cf3 , e)\
            \cf4 return\cf3  \cf7 None\cf3 \
\
    \cf4 def\cf3  predict(self):\
        cp = self.get_real_crash_data()\
        \cf4 if\cf3  cp \cf4 is\cf3  \cf7 None\cf3 :\
            cp = round(random.uniform(\cf6 1.0\cf3 , \cf6 10.0\cf3 ), \cf6 2\cf3 )\
        now = datetime.now().strftime(\cf5 '%Y-%m-%d %H:%M:%S'\cf3 )\
        self.history.append((now, cp))\
        \cf4 return\cf3  cp\
\
st.set_page_config(page_title=\cf5 '\uc0\u1605 \u1601 \u1578 \u1585 \u1587  \u1603 \u1585 \u1575 \u1588  - Web'\cf3 , layout=\cf5 'centered'\cf3 )\
st.title(\cf5 '\uc0\u55357 \u57065 \u65039  \u1605 \u1601 \u1578 \u1585 \u1587  \u1603 \u1585 \u1575 \u1588  \'97 Crash Predictor (Web)'\cf3 )\
\
\cf4 if\cf3  \cf5 'predictor'\cf3  \cf4 not\cf3  \cf4 in\cf3  st.session_state:\
    st.session_state.predictor = CrashPredictor()\
\cf4 if\cf3  \cf5 'history'\cf3  \cf4 not\cf3  \cf4 in\cf3  st.session_state:\
    st.session_state.history = []\
\
st.markdown(\cf5 '**\uc0\u1605 \u1604 \u1575 \u1581 \u1592 \u1577 :** \u1607 \u1584 \u1607  \u1606 \u1587 \u1582 \u1577  Web. `tkinter` \u1605 \u1575  \u1610 \u1582 \u1583 \u1605 \u1588  \u1601 \u1610  \u1575 \u1604 \u1605 \u1578 \u1589 \u1601 \u1581 \u1548  \u1604 \u1607 \u1584 \u1575  \u1581 \u1608 \u1604 \u1606 \u1575  \u1575 \u1604 \u1608 \u1575 \u1580 \u1607 \u1577  \u1573 \u1604 \u1609  Streamlit.'\cf3 )\
\
col1, col2, col3 = st.columns([\cf6 1\cf3 ,\cf6 1\cf3 ,\cf6 1\cf3 ])\
\
\cf4 with\cf3  col1:\
    \cf4 if\cf3  st.button(\cf5 '\uc0\u55357 \u56580  \u1580 \u1604 \u1576  \u1575 \u1604 \u1570 \u1606  (\u1581 \u1602 \u1610 \u1602 \u1610  \u1571 \u1608  \u1605 \u1581 \u1575 \u1603 \u1575 \u1577 )'\cf3 ):\
        point = st.session_state.predictor.predict()\
        st.session_state.history.append((datetime.now().strftime(\cf5 '%Y-%m-%d %H:%M:%S'\cf3 ), point))\
        st.success(\cf5 f'\uc0\u55357 \u56622  \u1606 \u1602 \u1591 \u1577  \u1575 \u1604 \u1581 \u1589 \u1608 \u1604 : **\cf8 \{point\}\cf5 **'\cf3 )\
\
\cf4 with\cf3  col2:\
    n = st.number_input(\cf5 '\uc0\u1593 \u1583 \u1583  \u1606 \u1602 \u1575 \u1591  \u1575 \u1604 \u1605 \u1581 \u1575 \u1603 \u1575 \u1577 '\cf3 , min_value=\cf6 1\cf3 , max_value=\cf6 200\cf3 , value=\cf6 5\cf3 , step=\cf6 1\cf3 )\
    \cf4 if\cf3  st.button(\cf5 '\uc0\u55356 \u57262  \u1605 \u1581 \u1575 \u1603 \u1575 \u1577 '\cf3 ):\
        results = []\
        \cf4 for\cf3  i \cf4 in\cf3  range(n):\
            pt = round(random.uniform(\cf6 1.0\cf3 , \cf6 10.0\cf3 ), \cf6 2\cf3 )\
            st.session_state.history.append((datetime.now().strftime(\cf5 '%Y-%m-%d %H:%M:%S'\cf3 ), pt))\
            results.append(pt)\
        st.info(\cf5 f'\uc0\u1578 \u1605 \u1578  \u1575 \u1604 \u1605 \u1581 \u1575 \u1603 \u1575 \u1577 : \cf8 \{results\}\cf5 '\cf3 )\
\
\cf4 with\cf3  col3:\
    \cf4 if\cf3  st.button(\cf5 '\uc0\u55358 \u56825  \u1605 \u1587 \u1581  \u1575 \u1604 \u1587 \u1580 \u1604 '\cf3 ):\
        st.session_state.history = []\
        st.success(\cf5 '\uc0\u9989  \u1575 \u1604 \u1587 \u1580 \u1604  \u1578 \u1601 \u1585 \u1610 \u1594 '\cf3 )\
\
st.write(\cf5 '---'\cf3 )\
st.header(\cf5 '\uc0\u55357 \u56522  \u1570 \u1582 \u1585  \u1575 \u1604 \u1606 \u1578 \u1575 \u1574 \u1580  (\u1570 \u1582 \u1585  20)'\cf3 )\
\cf4 if\cf3  st.session_state.history:\
    rows = list(reversed(st.session_state.history[-\cf6 20\cf3 :]))\
    st.table(rows)\
\cf4 else\cf3 :\
    st.write(\cf5 "\uc0\u1605 \u1575  \u1601 \u1605 \u1617 \u1575 \u1588  \u1606 \u1578 \u1575 \u1574 \u1580  \u1576 \u1593 \u1583 . \u1575 \u1587 \u1578 \u1593 \u1605 \u1604  '\u1580 \u1604 \u1576  \u1575 \u1604 \u1570 \u1606 ' \u1571 \u1608  '\u1605 \u1581 \u1575 \u1603 \u1575 \u1577 '."\cf3 )\
\
st.write(\cf5 '---'\cf3 )\
\cf4 if\cf3  st.session_state.history:\
    json_data = json.dumps(st.session_state.history, ensure_ascii=\cf7 False\cf3 , indent=\cf6 2\cf3 )\
    st.download_button(\cf5 '\uc0\u11015 \u65039  \u1578 \u1581 \u1605 \u1610 \u1604  \u1575 \u1604 \u1587 \u1580 \u1604  (JSON)'\cf3 , data=json_data, file_name=\cf5 'crash_history.json'\cf3 , mime=\cf5 'application/json'\cf3 )\
\
st.write(\cf5 "**\uc0\u1578 \u1593 \u1604 \u1610 \u1605 \u1575 \u1578  \u1587 \u1585 \u1610 \u1593 \u1577  \u1604 \u1604 \u1578 \u1588 \u1594 \u1610 \u1604  (Replit \u1571 \u1608  \u1571 \u1610  \u1576 \u1610 \u1574 \u1577  \u1578 \u1583 \u1593 \u1605  Streamlit):**"\cf3 )\
st.markdown(\cf5 """\
1. \uc0\u1571 \u1606 \u1588 \u1574  \u1605 \u1604 \u1601  `crash_predictor_streamlit.py` \u1608 \u1581 \u1591  \u1601 \u1610 \u1607  \u1607 \u1584 \u1575  \u1575 \u1604 \u1603 \u1608 \u1583 .  \
2. \uc0\u1571 \u1606 \u1588 \u1574  \u1605 \u1604 \u1601  `requirements.txt` \u1610 \u1581 \u1578 \u1608 \u1610  \u1593 \u1604 \u1609 :  \
   `streamlit` `requests` `numpy` `pandas` (pandas \uc0\u1575 \u1582 \u1578 \u1610 \u1575 \u1585 \u1610 )  \
3. \uc0\u1601 \u1610  \u1575 \u1604 \u1578 \u1610 \u1585 \u1605 \u1610 \u1606 \u1575 \u1604  \u1606 \u1601 \u1584 : `pip install -r requirements.txt`  \
4. \uc0\u1588 \u1594 \u1604  \u1575 \u1604 \u1578 \u1591 \u1576 \u1610 \u1602 :  \
   - \uc0\u1601 \u1610  Replit: `streamlit run crash_predictor_streamlit.py --server.port=$PORT --server.headless=true`  \
   - \uc0\u1605 \u1581 \u1604 \u1610 \u1575 : `streamlit run crash_predictor_streamlit.py` \u1579 \u1605  \u1575 \u1601 \u1578 \u1581  http://localhost:8501\
"""\cf3 )}
