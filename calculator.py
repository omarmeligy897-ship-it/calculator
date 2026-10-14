import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="آلة حاسبة تفاعلية", layout="centered")

# إضافة تنسيق CSS لجعل الأزرار متلاصقة وإضافة علامة مائية في الخلفية
st.markdown("""
    <style>
    /* تنسيق حاوية الآلة الحاسبة */
    .calc-container {
        max-width: 400px;
        margin: 0 auto;
        position: relative;
        background-color: #0b0e14;
        padding: 20px;
        border-radius: 10px;
    }
    
    /* إضافة العلامة المائية الشفافة في الخلفية */
    .calc-container::before {
        content: "";
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 200px;
        height: 200px;
        background-image: url('https://imgur.com'); /* ضع رابط صورتك الشفافة هنا */
        background-size: contain;
        background-repeat: no-repeat;
        opacity: 0.15; /* درجة الشفافية */
        pointer-events: none;
    }

    /* إلغاء المسافات بين الأزرار في Streamlit */
    div[data-testid="stHorizontalBlock"] {
        gap: 0px !important;
    }
    
    /* تنسيق أزرار الستريم ليت لتكون متلاصقة ومسطحة */
    button {
        border-radius: 0px !important;
        border: 1px solid #2d3139 !important;
        background-color: #1e222b !important;
        color: white !important;
        width: 100% !important;
        height: 60px !important;
    }
    button:hover {
        background-color: #282c37 !important;
    }
    </style>
""", unsafe_allow_html=True)

# هيكل الآلة الحاسبة
st.markdown('<div class="calc-container">', unsafe_allow_html=True)

# شاشة العرض
st.text_input("", placeholder="0", key="display", label_visibility="collapsed")

# مصفوفة الأزرار المتلاصقة بالتوزيع الشبكي لـ Streamlit
buttons = [
    ['AC', '(', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '⌫', '=']
]

for row in buttons:
    cols = st.columns(4)
    for idx, text in enumerate(row):
        with cols[idx]:
            st.button(text, key=f"btn_{text}_{row.index(text)}")

st.markdown('</div>', unsafe_allow_html=True)
