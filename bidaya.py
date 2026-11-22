import streamlit as st
import json
import pandas as pd
import os

# ---------- الإعدادات والتصميم ----------
st.set_page_config(page_title="New Beginning", layout="centered")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&family=Playfair+Display:wght@600&display=swap');

#MainMenu, header, footer {visibility: hidden;}
html, body, [class*="css"], .stApp, p, label, span, div, li, input, textarea {
    font-family: 'Tajawal', sans-serif !important;}
.stApp {direction: rtl; text-align: right; background: #0A0F1C !important;}
p, label, span, div, li, h1, h2, h3 {color: #F5F5F5 !important;}

/* الهيدر */
.header {background: linear-gradient(135deg, #111A2E 0%, #0A0F1C 100%);
         border: 1px solid #2A3550; border-top: 3px solid #C9A227;
         padding: 34px 28px; border-radius: 16px; margin-bottom: 14px;}
.brand {font-family: 'Playfair Display', serif !important; color: #FFFFFF !important;
        font-size: 40px; text-align: left; direction: ltr; letter-spacing: 2px;}
.line {width: 60px; height: 2px; background: #C9A227; margin: 10px 0 12px auto;}
.sub {color: #B8C2D6 !important; font-size: 16px;}
.note {font-size: 13px; color: #7D879C !important; margin-bottom: 14px;}

/* البطاقات */
.card {background: #121A2C; border: 1px solid #24304A; border-right: 3px solid #C9A227;
       border-radius: 12px; padding: 14px 18px; margin-bottom: 10px;}
.card b {color: #FFFFFF !important; font-size: 17px;}
.meta {font-size: 13px; color: #9AA5BC !important;}
.tag {display: inline-block; background: #1C2740; color: #E6C65C !important; border: 1px solid #33415F;
      border-radius: 20px; padding: 2px 10px; font-size: 12px; margin: 6px 0 0 6px;}
.tool {font-size: 13px; color: #E6C65C !important; font-weight: 700; margin-bottom: 8px; letter-spacing: 0.5px;}
.step {background: transparent; color: #E6C65C !important; border-bottom: 1px solid #C9A227;
       padding: 6px 0; margin: 18px 0 10px 0; font-weight: 700; font-size: 17px;}

/* التبويبات */
[data-baseweb="tab-list"] {border-bottom: 1px solid #24304A;}
[data-baseweb="tab"] p {color: #9AA5BC !important; font-size: 16px;}
[aria-selected="true"] p {color: #FFFFFF !important;}
[data-baseweb="tab-highlight"] {background-color: #C9A227 !important;}

/* المحادثة */
[data-testid="stChatMessage"] {background: #121A2C !important; border: 1px solid #24304A; border-radius: 12px;}
[data-testid="stBottom"] > div, [data-testid="stBottomBlockContainer"] {background: #0A0F1C !important;}
[data-testid="stChatInput"] > div {background: #121A2C !important; border: 1px solid #33415F !important;}
[data-testid="stChatInput"] textarea {background: #121A2C !important; color: #FFFFFF !important;}
[data-testid="stChatInput"] textarea::placeholder {color: #7D879C !important;}

/* القوائم والأزرار */
[data-baseweb="select"] > div {background: #121A2C !important; border-color: #33415F !important;}
[data-baseweb="popover"] * {background: #121A2C !important; color: #FFFFFF !important;}
[data-baseweb="tag"] {background: #C9A227 !important;}
.stButton button {background: #C9A227 !important; border: none; border-radius: 10px; padding: 8px 28px;}
.stButton button p {color: #0A0F1C !important; font-weight: 700;}
.stButton button:hover {background: #E6C65C !important;}
[data-testid="stAlert"] {background: #121A2C !important; border: 1px solid #C9A227;}
[data-baseweb="select"] div, [data-baseweb="select"] input {background-color: #121A2C !important; color: #FFFFFF !important;}
[data-baseweb="popover"] ul, [role="listbox"], [role="option"] {background-color: #121A2C !important; color: #FFFFFF !important;}
[role="option"]:hover, [aria-selected="true"][role="option"] {background-color: #1C2740 !important;}
[data-baseweb="select"] svg {fill: #C9A227 !important;}
[data-testid="stCheckbox"] label p {color: #FFFFFF !important;}
[data-testid="stProgress"] div[role="progressbar"] > div > div {background-color: #C9A227 !important;}
[data-testid="stMetric"] {background: #121A2C; border: 1px solid #24304A; border-radius: 12px; padding: 12px 16px;}
[data-testid="stMetricValue"] div {color: #E6C65C !important;}
.score {font-size: 44px; color: #E6C65C !important; font-weight: 700; text-align: center;}
.match {float: left; color: #0A0F1C !important; background: #C9A227; border-radius: 20px;
        padding: 2px 12px; font-size: 13px; font-weight: 700;}
/* إصلاحات: القوائم، الأيقونات، اللون الذهبي */
[data-testid="stMultiSelect"] div {background-color: #121A2C !important; color: #FFFFFF !important;}
[data-testid="stMultiSelect"] [data-baseweb="select"] > div {border: 1px solid #33415F !important;}
[data-testid="stMultiSelect"] [data-baseweb="tag"], [data-testid="stMultiSelect"] [data-baseweb="tag"] * {background-color: #C9A227 !important; color: #0A0F1C !important;}
[data-testid="stIconMaterial"], .material-symbols-rounded {font-family: 'Material Symbols Rounded' !important;}
[data-testid="stChatMessageAvatarAssistant"], [data-testid="stChatMessageAvatarUser"] {background-color: #C9A227 !important;}
[data-testid="stChatMessageAvatarAssistant"] *, [data-testid="stChatMessageAvatarUser"] * {color: #0A0F1C !important;}
button[role="tab"][aria-selected="true"] {box-shadow: inset 0 -3px 0 #C9A227 !important;}
[data-baseweb="tab-highlight"] {display: none !important;}
[data-baseweb="radio"] > div:first-child {background-color: #121A2C !important; border: 2px solid #C9A227 !important;}
[data-baseweb="radio"]:has(input:checked) > div:first-child {background-color: #C9A227 !important;}
.footer {text-align: center; margin-top: 50px; padding: 22px 0 10px 0; border-top: 1px solid #24304A;}
.footer .en {font-family: 'Playfair Display', serif !important; color: #E6C65C !important; font-size: 15px; letter-spacing: 1.5px; direction: ltr;}
.footer .ar {color: #9AA5BC !important; font-size: 14px; margin-top: 4px;}
.cv {background: #121A2C; border: 1px solid #24304A; border-top: 3px solid #C9A227; border-radius: 12px; padding: 22px 26px;}
.cv h3 {color: #FFFFFF !important; margin: 0 0 4px 0;}
.cv .sec {color: #E6C65C !important; font-weight: 700; margin-top: 14px; border-bottom: 1px solid #33415F; padding-bottom: 4px;}
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {background-color: #121A2C !important; color: #FFFFFF !important; border: 1px solid #33415F !important;}
[data-testid="stDownloadButton"] button {background: #C9A227 !important; border: none; border-radius: 10px;}
[data-testid="stDownloadButton"] button p {color: #0A0F1C !important; font-weight: 700;}
[data-testid="stMultiSelect"] label, [data-testid="stMultiSelect"] label * {background-color: transparent !important;}
[data-testid="stMultiSelect"] *, [data-testid="stMultiSelect"] input {color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important; opacity: 1 !important;}
[data-testid="stMultiSelect"] [data-baseweb="tag"] * {color: #0A0F1C !important; -webkit-text-fill-color: #0A0F1C !important;}
input::placeholder, textarea::placeholder {color: #D5DBE6 !important; -webkit-text-fill-color: #D5DBE6 !important; opacity: 1 !important;}
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {-webkit-text-fill-color: #FFFFFF !important;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
  <div class="brand">New Beginning</div>
  <div class="line"></div>
  <div class="sub">منصة إرشادية للمفرج عنهم: الوظائف، والتدريب، والإجراءات الرسمية، والدعم</div>
</div>
<div class="note">نسخة تجريبية لأغراض التدريب، وجميع البيانات المعروضة أمثلة توضيحية.</div>
""", unsafe_allow_html=True)

# ---------- البيانات (أمثلة توضيحية) ----------
SKILLS = ["حاسب", "تواصل", "قيادة", "فني", "طبخ", "يدوي", "إدارة وقت"]

jobs = [
    {"title": "مساعد مستودع", "city": "الرياض", "sector": "قطاع الخدمات اللوجستية",
     "type": "دوام كامل", "skills": ["يدوي", "إدارة وقت"]},
    {"title": "سائق توصيل", "city": "الرياض", "sector": "قطاع النقل والتوصيل",
     "type": "دوام مرن", "skills": ["قيادة", "إدارة وقت", "تواصل"]},
    {"title": "فني صيانة مكيفات", "city": "جدة", "sector": "قطاع الصيانة",
     "type": "دوام كامل", "skills": ["فني", "يدوي"]},
    {"title": "مدخل بيانات", "city": "الرياض", "sector": "قطاع الأعمال الإدارية",
     "type": "دوام كامل", "skills": ["حاسب", "إدارة وقت"]},
    {"title": "مساعد طباخ", "city": "الدمام", "sector": "قطاع الأغذية والضيافة",
     "type": "دوام جزئي", "skills": ["طبخ", "يدوي"]},
    {"title": "موظف خدمة عملاء", "city": "الرياض", "sector": "قطاع الاتصالات",
     "type": "دوام كامل", "skills": ["تواصل", "حاسب"]},
]
courses = [
    {"title": "أساسيات الحاسب", "skill": "حاسب", "hours": "20 ساعة"},
    {"title": "مهارات التواصل وخدمة العملاء", "skill": "تواصل", "hours": "12 ساعة"},
    {"title": "سلامة القيادة", "skill": "قيادة", "hours": "10 ساعات"},
    {"title": "صيانة المكيفات", "skill": "فني", "hours": "40 ساعة"},
    {"title": "فنون الطهي", "skill": "طبخ", "hours": "30 ساعة"},
    {"title": "إدارة الوقت والانضباط المهني", "skill": "إدارة وقت", "hours": "8 ساعات"},
    {"title": "مهارات المقابلة الوظيفية", "skill": "عام", "hours": "6 ساعات"},
]
# قوائم السيرة الذاتية (مرتبة حسب المجال)
CV_SKILLS = {
    "الحاسب": ["مايكروسوفت وورد", "مايكروسوفت إكسل", "مايكروسوفت باوربوينت", "إدخال البيانات",
               "الطباعة السريعة", "البريد الإلكتروني", "البحث في الإنترنت", "أساسيات البرمجة", "التصميم الجرافيكي"],
    "القانون والإدارة": ["الأنظمة واللوائح", "كتابة الخطابات الرسمية", "الأرشفة وحفظ الملفات",
                          "السكرتارية", "إدارة المكاتب", "الموارد البشرية", "المحاسبة الأساسية"],
    "الفني والمهني": ["صيانة المكيفات", "الكهرباء", "السباكة", "النجارة", "الحدادة واللحام",
                       "ميكانيكا السيارات", "الدهانات", "صيانة الجوالات"],
    "التواصل وخدمة العملاء": ["خدمة العملاء", "المبيعات", "التفاوض", "الاستقبال", "التسويق", "اللغة الإنجليزية"],
    "الطبخ والضيافة": ["الطبخ", "إعداد المخبوزات", "تحضير القهوة", "سلامة الغذاء", "الضيافة"],
    "القيادة والنقل": ["رخصة قيادة خاصة", "رخصة قيادة عامة", "التوصيل", "قيادة الرافعة الشوكية", "إدارة المستودعات"],
    "المهارات الشخصية": ["إدارة الوقت", "العمل الجماعي", "حل المشكلات", "القيادة والإشراف",
                          "الالتزام والانضباط", "التعلم السريع"],
}
CV_COURSES = {
    "الحاسب": ["أساسيات الحاسب", "الرخصة الدولية لقيادة الحاسب ICDL", "مهارات إكسل", "مقدمة في البرمجة", "التصميم بالكانفا"],
    "القانون والإدارة": ["مبادئ الأنظمة السعودية", "مهارات السكرتارية", "إدارة المكاتب", "أساسيات الموارد البشرية", "المحاسبة للمبتدئين"],
    "الفني والمهني": ["صيانة المكيفات", "التمديدات الكهربائية", "السباكة", "النجارة", "اللحام", "صيانة السيارات"],
    "التواصل وخدمة العملاء": ["مهارات التواصل وخدمة العملاء", "فن البيع", "اللغة الإنجليزية للمبتدئين"],
    "الطبخ والضيافة": ["فنون الطهي", "سلامة الغذاء", "الباريستا"],
    "القيادة والنقل": ["سلامة القيادة", "قيادة الرافعة الشوكية", "إدارة المستودعات"],
    "المهارات الشخصية": ["إدارة الوقت والانضباط المهني", "مهارات المقابلة الوظيفية", "العمل الجماعي", "حل المشكلات"],
}

def flat(d):
    # يحوّل القوائم لترتيب ثابت: المجال - المهارة
    return [f"{group} - {item}" for group, items in d.items() for item in items]

def clean(items):
    # يشيل اسم المجال عند العرض في السيرة
    return [x.split(" - ", 1)[1] if " - " in x else x for x in items]

def pick_or_type(label, options, key):
    # قائمة فيها خيارات + إمكانية الكتابة في نفس المكان
    try:
        return st.multiselect(label, options, key=key, accept_new_options=True,
                              placeholder="اختر من القائمة، أو اكتب واضغط Enter")
    except TypeError:
        # لو نسخة ستريملت قديمة: قائمة + خانة كتابة
        chosen = st.multiselect(label, options, key=key, placeholder="اختر من القائمة")
        more = st.text_input(f"{label} غير موجودة في القائمة", key=key + "_more",
                             placeholder="اكتبها وافصل بينها بفاصلة")
        return chosen + [x.strip() for x in more.replace("،", ",").split(",") if x.strip()]

# ---------- إنشاء ملف Word للسيرة الذاتية (بدون أي مكتبة إضافية) ----------
def make_word(name, city, goal, skills, course_list, exp):
    sec = "color:#B8861E; font-size:16pt; font-weight:bold; border-bottom:1.5pt solid #C9A227; margin:16pt 0 6pt 0;"
    body = f"<p style='font-size:26pt; font-weight:bold; color:#0A0F1C; margin:0;'>{name}</p>"
    if city:
        body += f"<p style='color:#555E70; font-size:12pt; margin:0 0 8pt 0;'>{city}</p>"
    if goal:
        body += f"<p style='{sec}'>الهدف الوظيفي</p><p>{goal}</p>"
    body += f"<p style='{sec}'>المهارات</p>" + "".join(f"<p style='margin:2pt 0;'>&#8226; {x}</p>" for x in skills)
    if course_list:
        body += f"<p style='{sec}'>الدورات التدريبية</p>" + "".join(f"<p style='margin:2pt 0;'>&#8226; {x}</p>" for x in course_list)
    if exp:
        body += f"<p style='{sec}'>الخبرات</p><p>{exp}</p>"
    html = ("<html dir='rtl'><head><meta charset='utf-8'></head>"
            "<body dir='rtl' style='font-family:Arial; font-size:13pt; text-align:right;'>"
            + body + "</body></html>")
    return html.encode("utf-8")

documents = {
    "هوية": "تجديد الهوية الوطنية: عبر منصة أبشر أو مكتب الأحوال المدنية.",
    "شهادة": "شهادة حسن السيرة والسلوك: تقديم طلب للجهة المختصة مع إثبات الهوية.",
    "رخصة": "تجديد رخصة القيادة: عبر منصة أبشر بعد إجراء الفحص الطبي.",
}
support = [
    "جمعيات رعاية السجناء والمفرج عنهم وأسرهم.",
    "مراكز الإرشاد الأسري والنفسي.",
    "برامج الدعم الاجتماعي للأسر.",
]

# ---------- حفظ الإحصائيات (بدون أي بيانات شخصية) ----------
STATS_FILE = "bidaya_stats.json"

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"tools": {}, "skills": {}, "readiness": [], "cv": 0}

def save_stats(stats):
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

stats = load_stats()
stats.setdefault("cv", 0)

def add_count(group, key):
    stats[group][key] = stats[group].get(key, 0) + 1
    save_stats(stats)

# ---------- عرض البطاقات ----------
def job_card(j, score=None):
    badge = f"<span class='match'>توافق {score}%</span>" if score is not None else ""
    return (f"<div class='card'>{badge}<b>{j['title']}</b><br>"
            f"<span class='meta'>{j['sector']} | {j['city']}</span><br>"
            f"<span class='tag'>{j['type']}</span>"
            f"<span class='tag'>المهارات: {'، '.join(j['skills'])}</span></div>")

def course_card(c):
    return (f"<div class='card'><b>{c['title']}</b><br>"
            f"<span class='tag'>مجانية</span><span class='tag'>{c['hours']}</span></div>")

def text_card(t):
    return f"<div class='card'>{t}</div>"

# ---------- الأدوات ----------
def job_tool():
    return jobs

def match_tool(my_skills):
    # نسبة التوافق = عدد المهارات المشتركة ÷ مهارات الوظيفة
    results = []
    for j in jobs:
        common = len(set(my_skills) & set(j["skills"]))
        score = round(common / len(j["skills"]) * 100)
        if score > 0:
            results.append((score, j))
    results.sort(key=lambda x: x[0], reverse=True)
    return results

def course_tool(my_skills=None):
    if not my_skills:
        return courses
    return [c for c in courses if c["skill"] in my_skills or c["skill"] == "عام"]

def document_tool(msg=""):
    for key in documents:
        if key in msg:
            return [documents[key]]
    return list(documents.values())

# ---------- الوكيل: يفهم الطلب ويختار الأداة ----------
def agent(msg):
    if "وظيف" in msg or "شغل" in msg or "عمل" in msg:
        return "بحث الوظائف", "".join(job_card(j) for j in job_tool())
    if "دور" in msg or "تعلم" in msg or "تدريب" in msg:
        return "بحث الدورات", "".join(course_card(c) for c in course_tool())
    if "هوية" in msg or "أوراق" in msg or "شهادة" in msg or "رخصة" in msg:
        return "الإجراءات الرسمية", "".join(text_card(d) for d in document_tool(msg))
    if "ضغط" in msg or "دعم" in msg or "حزين" in msg or "أسرة" in msg:
        return "الدعم النفسي والاجتماعي", "".join(text_card(s) for s in support)
    return None, "عذراً، لم أفهم طلبك. يمكنك السؤال عن: الوظائف، أو الدورات، أو الإجراءات، أو الدعم."

tab1, tab2, tab3, tab5, tab4, tab6 = st.tabs(["المحادثة", "خطتي الشخصية", "تقييم الجاهزية", "السيرة الذاتية", "لوحة الإحصائيات", "عن المشروع"])

# ---------- 1) المحادثة ----------
with tab1:
    if "chat" not in st.session_state:
        st.session_state.chat = [("assistant", "مرحباً بك. كيف يمكنني مساعدتك اليوم؟")]

    for role, text in st.session_state.chat:
        st.chat_message(role).markdown(text, unsafe_allow_html=True)

    msg = st.chat_input("اكتب طلبك، مثال: أبحث عن وظيفة")
    if msg:
        tool, content = agent(msg)
        if tool:
            add_count("tools", tool)
        reply = (f"<div class='tool'>الأداة المختارة: {tool}</div>" if tool else "") + content
        st.session_state.chat.append(("user", msg))
        st.session_state.chat.append(("assistant", reply))
        st.rerun()

# ---------- 2) الخطة الشخصية + مطابقة الوظائف ----------
with tab2:
    st.subheader("إعداد الخطة الشخصية")
    my_skills = st.multiselect("مهاراتك (اختر أكثر من مهارة)", SKILLS, placeholder="اختر مهاراتك")
    need_docs = st.multiselect("الوثائق المطلوب استخراجها", ["هوية", "شهادة", "رخصة"], placeholder="اختر الوثائق")
    need_support = st.checkbox("أحتاج إلى دعم نفسي أو أسري")

    if st.button("إنشاء الخطة"):
        if not my_skills:
            st.warning("اختر مهارة واحدة على الأقل.")
        else:
            for sk in my_skills:
                add_count("skills", sk)
            step = 1
            if need_docs:
                st.markdown(f"<div class='step'>الخطوة {step}: استكمال الوثائق الرسمية</div>", unsafe_allow_html=True)
                for d in need_docs:
                    st.markdown(text_card(documents[d]), unsafe_allow_html=True)
                step += 1

            st.markdown(f"<div class='step'>الخطوة {step}: التدريب وتطوير المهارات</div>", unsafe_allow_html=True)
            for c in course_tool(my_skills):
                st.markdown(course_card(c), unsafe_allow_html=True)
            step += 1

            st.markdown(f"<div class='step'>الخطوة {step}: الوظائف الأنسب لك (مرتبة حسب التوافق)</div>", unsafe_allow_html=True)
            matches = match_tool(my_skills)
            if matches:
                for score, j in matches:
                    st.markdown(job_card(j, score), unsafe_allow_html=True)
            else:
                st.markdown(text_card("لا توجد وظيفة مطابقة حالياً، ننصحك بالبدء بالدورات المقترحة."), unsafe_allow_html=True)
            step += 1

            if need_support:
                st.markdown(f"<div class='step'>الخطوة {step}: الدعم النفسي والاجتماعي</div>", unsafe_allow_html=True)
                for s in support:
                    st.markdown(text_card(s), unsafe_allow_html=True)

            st.success("تم إعداد خطتك بنجاح.")

# ---------- 3) تقييم الجاهزية ----------
with tab3:
    st.subheader("تقييم الجاهزية لسوق العمل")
    st.markdown("<div class='note'>أجب عن الأسئلة التالية لمعرفة مدى جاهزيتك.</div>", unsafe_allow_html=True)

    questions = {
        "هل لديك هوية وطنية سارية؟": "جدّد هويتك عبر منصة أبشر.",
        "هل لديك سيرة ذاتية جاهزة؟": "جهّز سيرة ذاتية مختصرة توضح مهاراتك.",
        "هل أكملت دورة تدريبية واحدة على الأقل؟": "سجّل في دورة من الدورات المجانية المقترحة.",
        "هل تعرف كيف تقدّم على وظيفة إلكترونياً؟": "تعلّم التقديم عبر منصات التوظيف الرسمية.",
        "هل تدربت على مقابلة العمل؟": "التحق بدورة مهارات المقابلة الوظيفية.",
    }
    answers = {q: st.radio(q, ["نعم", "لا"], horizontal=True, index=1, key=q) for q in questions}

    if st.button("احسب نسبة الجاهزية"):
        yes = sum(1 for a in answers.values() if a == "نعم")
        score = round(yes / len(questions) * 100)
        stats["readiness"].append(score)
        save_stats(stats)

        st.markdown(f"<div class='score'>{score}%</div>", unsafe_allow_html=True)
        st.progress(score / 100)
        if score == 100:
            st.success("أنت جاهز تماماً للتقديم على الوظائف.")
        else:
            st.markdown("<div class='step'>ما يلزمك لإكمال جاهزيتك</div>", unsafe_allow_html=True)
            for q, a in answers.items():
                if a == "لا":
                    st.markdown(text_card(questions[q]), unsafe_allow_html=True)

# ---------- 4) لوحة الإحصائيات ----------
with tab4:
    st.subheader("لوحة الإحصائيات")
    st.markdown("<div class='note'>إحصائيات عامة لمساعدة الجهة في التخطيط، ولا تحتوي على أي بيانات شخصية.</div>",
                unsafe_allow_html=True)

    total_chats = sum(stats["tools"].values())
    avg = round(sum(stats["readiness"]) / len(stats["readiness"])) if stats["readiness"] else 0

    c1, c2 = st.columns(2)
    c1.metric("طلبات المحادثة", total_chats)
    c2.metric("السير الذاتية المنشأة", stats["cv"])
    c3, c4 = st.columns(2)
    c3.metric("تقييمات الجاهزية", len(stats["readiness"]))
    c4.metric("متوسط الجاهزية", f"{avg}%")

    if stats["skills"]:
        st.markdown("<div class='step'>أكثر المهارات اختياراً</div>", unsafe_allow_html=True)
        st.bar_chart(pd.Series(stats["skills"], name="العدد"), color="#C9A227")
    if stats["tools"]:
        st.markdown("<div class='step'>أكثر الخدمات طلباً في المحادثة</div>", unsafe_allow_html=True)
        st.bar_chart(pd.Series(stats["tools"], name="العدد"), color="#C9A227")
    if not stats["skills"] and not stats["tools"]:
        st.markdown(text_card("لا توجد بيانات بعد. جرّب المحادثة والخطة الشخصية لتظهر الإحصائيات."), unsafe_allow_html=True)

# ---------- 5) منشئ السيرة الذاتية ----------
with tab5:
    st.subheader("إنشاء سيرة ذاتية")
    st.markdown("<div class='note'>لا يتم حفظ أي معلومة تكتبها هنا، السيرة تُنشأ للتحميل فقط.</div>", unsafe_allow_html=True)

    cv_name = st.text_input("الاسم الكامل")
    cv_city = st.text_input("المدينة")
    cv_goal = st.text_area("الهدف الوظيفي", placeholder="مثال: أسعى للعمل في مجال خدمة العملاء وتطوير مهاراتي")
    cv_skills = clean(pick_or_type("المهارات", flat(CV_SKILLS), "cv_skills"))
    cv_courses = clean(pick_or_type("الدورات التدريبية", flat(CV_COURSES), "cv_courses"))
    cv_exp = st.text_area("الخبرات السابقة (اختياري)")

    if st.button("إنشاء السيرة الذاتية"):
        if not cv_name or not cv_skills:
            st.warning("اكتب الاسم وأضف مهارة واحدة على الأقل.")
        else:
            stats["cv"] += 1
            save_stats(stats)
            html = f"<div class='cv'><h3>{cv_name}</h3><span class='meta'>{cv_city}</span>"
            if cv_goal:
                html += f"<div class='sec'>الهدف الوظيفي</div><p>{cv_goal}</p>"
            html += "<div class='sec'>المهارات</div>" + "".join(f"<span class='tag'>{s}</span>" for s in cv_skills)
            if cv_courses:
                html += "<div class='sec'>الدورات التدريبية</div>" + "".join(f"<p>- {c}</p>" for c in cv_courses)
            if cv_exp:
                html += f"<div class='sec'>الخبرات</div><p>{cv_exp}</p>"
            html += "</div>"
            st.markdown(html, unsafe_allow_html=True)

            st.download_button("تحميل السيرة الذاتية (Word)", make_word(cv_name, cv_city, cv_goal, cv_skills, cv_courses, cv_exp),
                               file_name="CV.doc", mime="application/msword")

# ---------- 6) عن المشروع ----------
with tab6:
    st.subheader("عن المشروع")
    st.markdown(text_card("<b>المشكلة</b><br>يواجه المفرج عنهم صعوبة في العودة لسوق العمل، ولا يعرفون من أين يبدأون: الوظائف، والتدريب، والوثائق، والدعم."), unsafe_allow_html=True)
    st.markdown(text_card("<b>الحل</b><br>منصة New Beginning تجمع كل ما يحتاجه المستخدم في مكان واحد: مساعد ذكي، وخطة شخصية، ومطابقة للوظائف، وتقييم للجاهزية، ومنشئ للسيرة الذاتية."), unsafe_allow_html=True)
    st.markdown(text_card("<b>الذكاء في المشروع</b><br>وكيل ذكي (AI Agent) يفهم طلب المستخدم ويختار الأداة المناسبة، وخوارزمية تحسب نسبة التوافق بين مهارات المستخدم ومتطلبات كل وظيفة."), unsafe_allow_html=True)
    st.markdown(text_card("<b>التقنيات</b><br><span class='tag'>Python</span><span class='tag'>Streamlit</span><span class='tag'>AI Agent</span><span class='tag'>Skill Matching</span>"), unsafe_allow_html=True)
    st.markdown(text_card("<b>ملاحظة</b><br>مشروع تدريبي شخصي، وجميع البيانات المعروضة أمثلة توضيحية."), unsafe_allow_html=True)

# ---------- التوقيع ----------
st.markdown("""
<div class="footer">
  <div class="en">Designed &amp; Developed by Mieaad Al-Otaibi &copy; 2026</div>
  <div class="ar">تصميم وتطوير: ميعاد العتيبي</div>
</div>
""", unsafe_allow_html=True)