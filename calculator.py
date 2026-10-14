import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="آلة حاسبة تفاعلية", layout="centered")

# التنسيق المتقدم لإلغاء أي فراغات بين الأعمدة والأزرار
st.markdown("""
    <style>
    /* 1. إلغاء الفراغات بين الأعمدة أفقياً */
    div[data-testid="stHorizontalBlock"] {
        gap: 0px !important;
    }
    
    /* 2. إلغاء أي هوامش أو فجوات داخل العمود نفسه */
    div[data-testid="column"] {
        padding: 0px !important;
        margin: 0px !important;
    }

    /* 3. تنسيق الأزرار لتتلاحم بالكامل وتملأ مساحة العمود */
    div.stButton > button {
        border-radius: 0px !important;          /* حواف حادة للالتصاق */
        border: 1px solid #2d3139 !important;   /* فاصل رفيع جداً */
        background-color: #1e222b !important;   /* لون الزر الداكن */
        color: white !important;
        width: 100% !important;                 /* تمدد الزر لملء العمود */
        height: 65px !important;                /* ارتفاع مناسب للزر */
        margin: 0px !important;                 /* إزالة أي هوامش إضافية */
        padding: 0px !important;
        display: block !important;
    }

    /* تأثير عند تمرير الماوس فوق الأزرار */
    div.stButton > button:hover {
        background-color: #282c37 !important;
    }
    
    /* تخصيص شاشة العرض العلوية لتناسب الأزرار الملتصقة */
    div[data-testid="stTextInput"] input {
        border-radius: 4px !important;
        background-color: #131722 !important;
        color: white !important;
        border: 1px solid #2d3139 !important;
        text-align: right;
        font-size: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# شاشة العرض (Input الخاص بالحاسبة)
st.text_input("", placeholder="0", key="display", label_visibility="collapsed")

# مصفوفة الأزرار
buttons = [
    ['AC', '(', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '⌫', '=']
]

# رسم الشبكة الملتصقة
for r_idx, row in enumerate(buttons):
    cols = st.columns(4)  # إنشاء 4 أعمدة متساوية لكل صف
    for c_idx, text in enumerate(row):
        with cols[c_idx]:
            # استخدام مفتاح (key) فريد لكل زر لتجنب الأخطاء في Streamlit
            st.button(text, key=f"btn_{r_idx}_{c_idx}")
