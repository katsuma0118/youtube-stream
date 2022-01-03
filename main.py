import streamlit as st
import numpy as np
import pandas as  pd
from PIL import Image
import time

st.write("プログレスバーの表示")
"start!!"

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interatin {i+1}%')
    bar.progress(i + 1)
    time.sleep(0.01)

"Done!!!"

st.title("Streamlit 超入門")
st.write("DataFlame")

df = pd.DataFrame({
    "一列目":[1,2,3,4],
    "二列目":[100,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0),width=1000,height=1000)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as  pd
```
"""

df1 = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)

st.table(df1)
st.line_chart(df1)
st.bar_chart(df1)

df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=["lat","lon"]
)

st.table(df2)
st.map(df2)

img = Image.open("main.jpg")
st.image(img, caption="GIZMO" ,use_column_width=True)

if st.checkbox("want check GOZMO?"):
    img = Image.open("main.jpg")
    st.image(img, caption="GIZMO" ,use_column_width=True)

option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)

"あなたの好きな数字は、",option,"です"

st.write("insteractiv widgets")
option1 = st.text_input("あなたの趣味をおしえてください")
"あなたの趣味は",option1,"です。" 

condition = st.sidebar.slider("あなたの今の調子は？",0,1000,500)
"コンディション:",condition


left_column, middle_column, right_column = st.columns(3)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("うんちとはなんですか？")
expander1.write("うんちはとてもすごいものです")
expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ内容を書く")
expander3 = st.expander("問い合わせ")
expander3.write("問い合わせ内容を書く")