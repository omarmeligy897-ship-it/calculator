import streamlit as st
import streamlit.components.v1 as components  # استيراد مكتبة المكونات الرسمية

# إعدادات الصفحة
st.set_page_config(page_title="آلة حاسبة تفاعلية", layout="centered")

# كود الواجهة الكامل (HTML + CSS + JavaScript)
calculator_html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: transparent;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
}
.calc-container {
    width: 100%;
    max-width: 360px;
    background-color: #0b0e14;
    padding: 15px;
    border-radius: 12px;
}
.calc-screen {
    width: 100%;
    height: 60px;
    background-color: #131722;
    color: white;
    border: 1px solid #2d3139;
    border-radius: 6px;
    text-align: right;
    font-size: 2rem;
    padding: 10px;
    box-sizing: border-box;
    margin-bottom: 15px;
}
.calculator-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0px;
    border: 1px solid #2d3139;
    border-radius: 8px;
    overflow: hidden;
}
.calc-btn {
    background-color: #1e222b;
    color: white;
    border: 1px solid #2d3139;
    padding: 22px 0;
    font-size: 1.3rem;
    font-weight: bold;
    text-align: center;
    cursor: pointer;
    user-select: none;
    transition: background 0.1s;
}
.calc-btn:hover { background-color: #282c37; }
.calc-btn:active { background-color: #3e4453; }
</style>
</head>
<body>

<div class="calc-container">
    <!-- شاشة العرض المدمجة -->
    <input type="text" class="calc-screen" id="screen" value="0" readonly>

    <!-- شبكة الأزرار المتلاصقة -->
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
</div>

<script>
let screen = document.getElementById('screen');

function press(val) {
    if (val === 'AC') {
        screen.value = '0';
    } else if (val === 'C') {
        if (screen.value.length > 1) {
            screen.value = screen.value.slice(0, -1);
        } else {
            screen.value = '0';
        }
    } else {
        if (screen.value === '0' || screen.value === 'Error') {
            screen.value = val;
        } else {
            screen.value += val;
        }
    }
}

function calculate() {
    try {
        // حساب العملية الرياضية بأمان
        let result = eval(screen.value);
        screen.value = result;
    } catch (e) {
        screen.value = 'Error';
    }
}
</script>

</body>
</html>
"""

# تشغيل المكون بشكل مستقل وآمن داخل تطبيق Streamlit
components.html(calculator_html, height=500, scrolling=False)
