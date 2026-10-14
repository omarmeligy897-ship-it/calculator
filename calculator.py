import streamlit as st

st.set_page_config(page_title="آلة حاسبة تفاعلية", page_icon="🧮")

st.title("🧮 آلة حاسبة تفاعلية متكاملة")

# تهيئة الذاكرة لحفظ العمليات الحسابية
if "display" not in st.session_state:
    st.session_state.display = ""

# عرض شاشة الآلة الحاسبة
display_val = st.text_input("الشاشة", value=st.session_state.display, disabled=True, label_visibility="collapsed")

# وظيفة لإضافة الأرقام أو الرموز للشاشة
def add_to_display(val):
    st.session_state.display += str(val)

# وظيفة مسح الشاشة
def clear_display():
    st.session_state.display = ""

# وظيفة حساب النتيجة
def calculate():
    try:
        # استبدال الرموز لتعمل بلغة بايثون
        expr = st.session_state.display.replace("×", "*").replace("÷", "/")
        result = str(eval(expr))
        st.session_state.display = result
    except Exception:
        st.session_state.display = "خطأ"

# تصميم الأزرار على هيئة شبكة (Grid)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("AC"):
        clear_display()
        st.rerun()
    if st.button("7"):
        add_to_display("7")
        st.rerun()
    if st.button("4"):
        add_to_display("4")
        st.rerun()
    if st.button("1"):
        add_to_display("1")
        st.rerun()
    if st.button("0"):
        add_to_display("0")
        st.rerun()

with col2:
    if st.button("("):
        add_to_display("(")
        st.rerun()
    if st.button("8"):
        add_to_display("8")
        st.rerun()
    if st.button("5"):
        add_to_display("5")
        st.rerun()
    if st.button("2"):
        add_to_display("2")
        st.rerun()
    if st.button("."):
        add_to_display(".")
        st.rerun()

with col3:
    if st.button("%"):
        add_to_display("/100")
        st.rerun()
    if st.button("9"):
        add_to_display("9")
        st.rerun()
    if st.button("6"):
        add_to_display("6")
        st.rerun()
    if st.button("3"):
        add_to_display("3")
        st.rerun()
    if st.button("⌫"):
        st.session_state.display = st.session_state.display[:-1]
        st.rerun()

with col4:
    if st.button("÷"):
        add_to_display("÷")
        st.rerun()
    if st.button("×"):
        add_to_display("×")
        st.rerun()
    if st.button("-"):
        add_to_display("-")
        st.rerun()
    if st.button("+"):
        add_to_display("+")
        st.rerun()
    if st.button("="):
        calculate()
        st.rerun()
