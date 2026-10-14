import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="آلة حاسبة تفاعلية", layout="centered")

# 1. شاشة العرض العلوية (أعطيناها معرف id من أجل جافا سكريبت)
st.markdown('<div id="calc-display-wrapper">', unsafe_allow_html=True)
st.text_input("", placeholder="0", key="display", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# 2. كود الواجهة والـ JavaScript لتفعيل الحسابات والضغطات فوراً
html_code = """
<style>
/* تنسيق شاشة العرض */
div[data-testid="stTextInput"] input {
    border-radius: 4px !important;
    background-color: #131722 !important;
    color: white !important;
    border: 1px solid #2d3139 !important;
    text-align: right;
    font-size: 1.8rem;
    margin-bottom: 15px;
    padding: 10px !important;
}

/* حاوية الشبكة الملتحمة */
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

/* تنسيق الأزرار */
.calc-btn {
    background-color: #1e222b !important;
    color: white !important;
    border: 1px solid #2d3139 !important;
    padding: 20px 0;
    font-size: 1.2rem;
    font-weight: bold;
    text-align: center;
    cursor: pointer;
    user-select: none;
    transition: background 0.1s;
}

/* تأثير الضغط وتمرير الماوس */
.calc-btn:hover { background-color: #282c37 !important; }
.calc-btn:active { background-color: #3e4453 !important; }
</style>

<!-- هيكل الأزرار المتلاصقة -->
<div class="calculator-grid">
    <div class="calc-btn" onclick="press('AC')">AC</div>
    <div class="calc-btn" onclick="press('(')">(</div>
    <div class="calc-btn" onclick="press('%')">%</div>
    <div class="calc-btn" onclick="press('/')">÷</div>
    
    <div class="calc-btn" onclick="press('7')">7</div>
    <div class="calc-btn" onclick="press('8')">8</div>
    <div class="calc-btn" onclick="press('9')">9</div>
    <div class="calc-btn" onclick="press('*')">×</div>
    
    <div class="calc-btn" onclick="press('4')">4</div>
    <div class="calc-btn" onclick="press('5')">5</div>
    <div class="calc-btn" onclick="press('6')">6</div>
    <div class="calc-btn" onclick="press('-')">-</div>
    
    <div class="calc-btn" onclick="press('1')">1</div>
    <div class="calc-btn" onclick="press('2')">2</div>
    <div class="calc-btn" onclick="press('3')">3</div>
    <div class="calc-btn" onclick="press('+')">+</div>
    
    <div class="calc-btn" onclick="press('0')">0</div>
    <div class="calc-btn" onclick="press('.')">.</div>
    <div class="calc-btn" onclick="press('C')">⌫</div>
    <div class="calc-btn" onclick="calculate()">=</div>
</div>

<script>
// كود الجافا سكريبت للتحكم في الضغطات والحسابات
function press(val) {
    // جلب شاشة الإدخال الخاصة بـ Streamlit
    let input = parent.document.querySelector('div[data-testid="stTextInput"] input');
    if (!input) return;
    
    if (val === 'AC') {
        input.value = '';
    } else if (val === 'C') {
        input.value = input.value.slice(0, -1);
    } else {
        if (input.value === '0' || input.value === 'Error') input.value = '';
        input.value += val;
    }
    
    // إرسال حدث التحديث لتشعر المنصة بالتغيير
    input.dispatchEvent(new Event('input', { bubbles: true }));
}

function calculate() {
    let input = parent.document.querySelector('div[data-testid="stTextInput"] input');
    if (!input || !input.value) return;
    
    try {
        // استبدال الرموز الرسومية بالرموز البرمجية قبل الحساب
        let expression = input.value.replace(/×/g, '*').replace(/÷/g, '/');
        let result = eval(expression);
        input.value = result;
    } catch (e) {
        input.value = 'Error';
    }
    input.dispatchEvent(new Event('input', { bubbles: true }));
}
</script>
"""

# تشغيل الكود البرمجي المتكامل
st.markdown(html_code, unsafe_allow_html=True)
