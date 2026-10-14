import customtkinter as ctk
from PIL import Image  # تأكد من تثبيتها عبر: pip install pillow

# إعداد المظهر العام للمكتبة (داكن)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("400x550")
root.title("آلة حاسبة تفاعلية")
root.configure(fg_color="#0b0e14") # لون الخلفية الداكن

# 1. تحميل الصورة الشفافة (PNG) وتحديد حجمها كعلامة مائية
# تحكم في أبعاد الصورة (مثلاً 200x200) لتناسب نافذتك
bg_image = ctk.CTkImage(
    light_image=Image.open("your_logo.png"), # ضع مسار صورتك الشفافة هنا
    dark_image=Image.open("your_logo.png"),
    size=(200, 200)
)

# 2. وضع الصورة كعلامة مائية في خلفية التطبيق باستخدام CTkLabel
watermark = ctk.CTkLabel(root, image=bg_image, text="")
watermark.place(relx=0.5, rely=0.5, anchor="center") 

# 3. إنشاء حاوية الأزرار (Frame) 
# جعل خلفية الحاوية شفافة تماماً ("transparent") لتظهر العلامة المائية من خلفها
grid_frame = ctk.CTkFrame(root, fg_color="transparent")
grid_frame.place(relx=0.5, rely=0.6, anchor="center") # وضعها فوق العلامة المائية

# مصفوفة الأزرار
buttons = [
    ['AC', '(', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '⌫', '=']
]

# 4. توزيع الأزرار بشكل متلاصق تماماً
for row_idx, row in enumerate(buttons):
    for col_idx, text in enumerate(row):
        btn = ctk.CTkButton(
            master=grid_frame, 
            text=text, 
            width=70,
            height=60,
            font=("Arial", 16, "bold"),
            fg_color="#1e222b",       # لون الأزرار الداكن
            hover_color="#282c37",    # لون الزر عند تمرير الماوس
            text_color="white",
            corner_radius=0,          # 💡 السر هنا: الحواف حادة تماماً لتتلاحم الأزرار بدون أي فراغات دائرية
            border_width=1,           # فاصل خفيف جداً بعرض 1 بكسل لحجم جمالي (اجعله 0 للاتصال المطلق)
            border_color="#2d3139"    # لون خط الفاصل بين الأزرار المتلاصقة
        )
        # تصفير الهوامش الخارجية تماماً لضمان الالتصاق
        btn.grid(row=row_idx, column=col_idx, padx=0, pady=0, sticky="nsew")

root.mainloop()
