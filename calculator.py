import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="آلة حاسبة تفاعلية", layout="centered")

# 1. شاشة العرض (نتركها كعنصر Streamlit عادي مع تنسيقها)
st.text_input("", placeholder="0", key="display", label_visibility="collapsed")

# 2. بناء شبكة الأزرار المتلاصقة بالكامل باستخدام HTML و CSS Grid
# هذا الكود يضمن التصاق الأزرار تماماً أفقياً ورأسياً ككتلة واحدة
st.markdown("""
    <style>
    /* تخصيص شاشة العرض العلوية لتناسب الأزرار الملتصقة */
    div[data-testid="stTextInput"] input {
        border-radius: 4px !important;
        background-color: #131722 !important;
        color: white !important;
        border: 1px solid #2d3139 !important;
        text-align: right;
        font-size: 1.5rem;
        margin-bottom: 15px;
    }

    /* حاوية الشبكة الملتحمة */
    .calculator-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr); /* 4 أعمدة متساوية */
        gap: 0px !important;                  /* تصفير الفراغات تماماً */
        border: 1px solid #2d3139;             /* إطار خارجي للمجموعة */
        border-radius: 8px;                    /* انحناء زوايا الشبكة الخارجية */
        overflow: hidden;                      /* لمنع الأزرار من الخروج عن الانحناء */
        max-width: 400px;
        margin: 0 auto;
    }

    /* تنسيق الأزرار داخل الشبكة */
    .calc-btn {
        background-color: #1e222b !important;
        color: white !important;
        border: 1px solid #2d3139 !important; /* فاصل رفيع جداً */
        padding: 20px 0;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        cursor: pointer;
        transition: background 0.2s;
        outline: none;
    }

    /* تأثير عند تمرير الماوس */
    .calc-btn:hover {
        background-color: #282c37 !important;
    }
    </style>

    <!-- هيكل الأزرار المتلاصقة -->
    <div class="calculator-grid">
        <div class="calc-btn">AC</div>
        <div class="calc-btn">(</div>
        <div class="calc-btn">%</div>
        <div class="calc-btn">÷</div>
        
        <div class="calc-btn">7</div>
        <div class="calc-btn">8</div>
        <div class="calc-btn">9</div>
        <div class="calc-btn">×</div>
        
        <div class="calc-btn">4</div>
        <div class="calc-btn">5</div>
        <div class="calc-btn">6</div>
        <div class="calc-btn">-</div>
        
        <div class="calc-btn">1</div>
        <div class="calc-btn">2</div>
        <div class="calc-btn">3</div>
        <div class="calc-btn">+</div>
        
        <div class="calc-btn">0</div>
        <div class="calc-btn">.</div>
        <div class="calc-btn">⌫</div>
        <div class="calc-btn">=</div>
    </div>
""", unsafe_allow_html=True)
