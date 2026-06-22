import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import io

st.set_page_config(page_title="تقرير دورية", layout="centered", page_icon="🛡️")

st.title("🛡️ توليد تقرير دورية سوري")

with st.sidebar:
    st.header("📋 إعدادات التقرير")
    date_day = st.text_input("اليوم (مثال: الأحد 19)", value="الأحد 19")
    month = st.number_input("الشهر", value=6, step=1)
    year = st.number_input("السنة", value=2026, step=1)
    report_number = st.text_input("رقم الدورية", value="11631")
    official_name = st.text_input("مسؤول الدورية", value="رامي يونس")
    section = st.text_input("القسم", value="قسم الطرق الدولية")
    start_time = st.text_input("ساعة البدء", value="(014560)3:43")
    hours = st.text_input("عدد الساعات", value="لا يوجد")
    incidents = st.text_input("عدد الحوادث", value="(014590)4:03")
    stops = st.text_input("عدد التوقيف", value="لا يوجد")
    reports_count = st.number_input("عدد البلاغات", value=1)
    human_status = st.text_input("الحالة الإنسانية", value="رقم الضبط")
    phone = st.text_input("الإيصاءي", value="375 267591 3841218")
    
    submit = st.button("🖼️ توليد التقرير", type="primary", use_container_width=True)

if submit:
    with st.spinner("جاري إنشاء الصورة الرسمية..."):
        fig = plt.figure(figsize=(10, 12), facecolor='#003d1e')
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 12)
        ax.axis('off')
        
        # الإطار الخارجي
        outer = Rectangle((0.1, 0.1), 9.8, 11.8, linewidth=4, edgecolor='#D4AF37', facecolor='none')
        ax.add_patch(outer)
        
        # الشعار النصي
        ax.text(0.4, 11.2, '🦅', fontsize=80, ha='center', va='center', color='#FFD700', zorder=2)
        ax.text(5, 11.3, 'تقرير دورية', fontsize=32, fontweight='bold', ha='center', va='center', color='#FFD700', zorder=3)
        
        data = [
            ('اليوم', date_day),
            ('الشهر', str(month)),
            ('السنة', str(year)),
            ('رقم الدورية', report_number),
            ('مسؤول الدورية', official_name),
            ('القسم', section),
            ('ساعة البدء', start_time),
            ('عدد الساعات', hours),
            ('عدد الحوادث', incidents),
            ('عدد التوقيف', stops),
            ('عدد البلاغات', str(reports_count)),
            ('الحالة الإنسانية', human_status),
            ('الإيصاءي', phone)
        ]
        
        y = 10.0
        for label, value in data:
            ax.text(0.8, y, label + ':', fontsize=13, color='#FFD700', ha='left', va='top', fontweight='bold')
            ax.text(4.2, y, value, fontsize=13, ha='right', va='top')
            y -= 0.68
        
        # النبذة
        ax.text(0.8, 1.3, 'النبذة', fontsize=16, fontweight='bold', color='#FFD700')
        ax.text(0.8, 0.95, 'تم إعداد هذا التقرير بواسطة نظام Manus AI', fontsize=11, ha='left')
        
        # حفظ الصورة
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=300, bbox_inches='tight', facecolor='#003d1e', edgecolor='#D4AF37')
        img_buffer.seek(0)
        plt.close()
        
        st.image(img_buffer, caption="تقرير دوري جاهز", use_column_width=True)
        st.download_button(
            label="⬇️ تحميل الصورة (PNG)",
            data=img_buffer,
            file_name="تقرير_دورية.png",
            mime="image/png",
            use_container_width=True
        )
        st.success("✅ تم إنشاء التقرير بنجاح!")