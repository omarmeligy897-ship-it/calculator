import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="آلة حاسبة تفاعلية", layout="centered")

# شاشة العرض العلوية
st.text_input("", placeholder="0", key="display", label_visibility="collapsed")

# كود الـ HTML والـ CSS مدمجين ومحميّن من أخطاء القراءة النصية
html_code = """
<style>
div[data-testid="stTextInput"] input {
    border-radius: 4px !important;
    background-color: #131722 !important;
    color: white !important;
    border: 1px solid #2d3139 !important;
    text-align: right;
    font-size: 1.5rem;
    margin-bottom: 15px;
}
.calculator-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0px !important;
    border: 1px solid #2d3139;
    border-radius: 8px;
    overflow: hidden;
    max-width: 400px;
    margin: 0 auto;
}
.calc-btn {
    background-color: #1e222b !important;
    color: white !important;
    border: 1px solid #2d3139 !important;
    padding: 20px 0;
    font-size: 1.2rem;
    font-weight: bold;
    text-align: center;
    cursor: pointer;
    transition: background 0.2s;
}
.calc-btn:hover {
    background-color: #282c37 !important;
}
</style>

<div class="calculator-grid">
    <div class="calc-btn">AC</div><div class="calc-btn">(</div><div class="calc-btn">%</div><div class="calc-btn">÷</div>
    <div class="calc-btn">7</div><div class="calc-btn">8</div><div class="calc-btn">9</div><div class="calc-btn">×</div>
    <div class="calc-btn">4</div><div class="calc-btn">5</div><div class="calc-btn">6</div><div class="calc-btn">-</div>
    <div class="calc-btn">1</div><div class="calc-btn">2</div><div class="calc-btn">3</div><div class="calc-btn">+</div>
    <div class="calc-btn">0</div><div class="calc-btn">.</div><div class="calc-btn">⌫</div><div class="calc-btn">=</div>
</div>
"""

# تشغيل الكود مع تفعيل خاصية إتاحة الـ HTML
st.markdown(html_code, unsafe_allow_html=True)
