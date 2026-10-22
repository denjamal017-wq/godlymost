/* ============================================================
   GODLY MOST — app.js
   data-driven subjects · accordion · reveals · counters · clock
   ============================================================ */

/* ---------- البيانات ---------- */
const SUBJECTS = [
  {
    num: "01",
    title: "أسس الإلكترونيك",
    en: "ELECTRONICS FUNDAMENTALS",
    status: "مكتملة ✅",
    count: "٦ محاضرات",
    desc: "فيزياء أشباه الموصلات، الدايود، ودوائر التقويم — الأساس اللي يشرح شلون الرقائق والعتاد يشتغلون فعلياً، وليش يهمّك بالأمن السيبراني.",
    teach: "نظري: د. أكرم محمد حاتم · مختبر: م. زهراء عبد المهدي + م. عقيل علي",
    tags: ["Semiconductors", "Diode", "Zener", "Rectifiers"],
    lectures: [
      { code: "نظري 01", title: "أشباه الموصلات ومستويات الطاقة", en: "Semiconductors & Energy Levels", type: "نظري" },
      { code: "نظري 02", title: "بناء الدايود والتحيز ومنطقة زينر", en: "Diode, Biasing & Zener Region", type: "نظري" },
      { code: "نظري 03", title: "شوكلي وتحليل خط الحمل", en: "Shockley & Load-Line Analysis", type: "نظري" },
      { code: "عملي 01", title: "خصائص الدايود", en: "Diode Characteristics", type: "مختبر" },
      { code: "عملي 02", title: "خصائص دايود زينر", en: "Zener Diode Characteristics", type: "مختبر" },
      { code: "عملي 03", title: "مقوم نصف الموجة", en: "Half-Wave Rectifier", type: "مختبر" },
    ],
  },
  {
    num: "02",
    title: "هياكل البيانات",
    en: "DATA STRUCTURES & ALGORITHMS",
    status: "مكتملة ✅",
    count: "٥ محاضرات",
    desc: "قلب البرمجة — شلون ترتّب البيانات وتكتب خوارزميات أسرع وأخف على الذاكرة، وياها مختبر OOP بالجافا من الصفر.",
    teach: "نظري + مختبر: م.م عباس كامل + ب. صبا صباح",
    tags: ["Algorithms", "Python", "OOP", "Java"],
    lectures: [
      { code: "نظري 01", title: "مدخل إلى هياكل البيانات والخوارزميات", en: "Overview", type: "نظري" },
      { code: "نظري 02", title: "الخوارزميات: الخصائص والفئات والتصميم", en: "Algorithmics", type: "نظري" },
      { code: "نظري 03", title: "مراجعة بايثون", en: "Python Review", type: "نظري" },
      { code: "عملي 01", title: "مدخل إلى البرمجة كائنية التوجه", en: "OOP Lab 1", type: "مختبر" },
      { code: "عملي 02", title: "البنّاءات ومعدّلات الوصول", en: "Constructors & Access Modifiers", type: "مختبر" },
    ],
  },
];

const SOON = [
  { icon: "⌨️", title: "أساسيات البرمجة", en: "PROGRAMMING BASICS", pri: "أولوية ⭐⭐⭐⭐⭐" },
  { icon: "💻", title: "نظم المعلومات", en: "INFORMATION SYSTEMS", pri: "أولوية ⭐⭐⭐⭐⭐" },
  { icon: "🔌", title: "مبادئ الهندسة الكهربائية", en: "ELECTRICAL ENGINEERING", pri: "أولوية ⭐⭐⭐⭐" },
  { icon: "🔢", title: "الرياضيات", en: "MATHEMATICS", pri: "أولوية ⭐⭐⭐⭐" },
  { icon: "📐", title: "الرسم الهندسي", en: "ENGINEERING DRAWING", pri: "أولوية ⭐⭐⭐" },
  { icon: "🏛️", title: "الديمقراطية وحقوق الإنسان", en: "DEMOCRACY & HUMAN RIGHTS", pri: "مادة إنسانية" },
];

/* ---------- رسم المواد ---------- */
const subjectsList = document.getElementById("subjects-list");

SUBJECTS.forEach((s, i) => {
  const item = document.createElement("article");
  item.className = "subject";

  const lectures = s.lectures
    .map(
      (l) => `
      <li class="lec">
        <span class="lec__code">${l.code}</span>
        <span>
          <span class="lec__title">${l.title}</span>
          <span class="lec__en" dir="ltr">${l.en}</span>
        </span>
        <span class="lec__type ${l.type === "مختبر" ? "lec__type--lab" : ""}">${l.type}</span>
      </li>`
    )
    .join("");

  item.innerHTML = `
    <button class="subject__head" aria-expanded="false" aria-controls="panel-${i}">
      <span class="subject__num" dir="ltr">/${s.num}</span>
      <span class="subject__name">
        <span class="subject__title">${s.title}</span>
        <span class="subject__en" dir="ltr">${s.en}</span>
      </span>
      <span class="subject__meta">${s.count} · ${s.status}</span>
      <span class="subject__icon">+</span>
    </button>
    <div class="subject__panel" id="panel-${i}">
      <div class="subject__panel-inner">
        <div class="subject__body">
          <div>
            <p class="subject__desc">${s.desc}</p>
            <p class="subject__teach">👤 ${s.teach}</p>
            <div class="subject__tags" dir="ltr">${s.tags.map((t) => `<span class="tag">${t}</span>`).join("")}</div>
          </div>
          <ol class="subject__lectures">${lectures}</ol>
        </div>
      </div>
    </div>`;

  subjectsList.appendChild(item);
});

/* أكورديون — يفتح واحد ويسد الباقي */
subjectsList.addEventListener("click", (e) => {
  const head = e.target.closest(".subject__head");
  if (!head) return;
  const current = head.parentElement;
  const isOpen = current.classList.contains("open");
  subjectsList.querySelectorAll(".subject.open").forEach((el) => {
    el.classList.remove("open");
    el.querySelector(".subject__head").setAttribute("aria-expanded", "false");
  });
  if (!isOpen) {
    current.classList.add("open");
    head.setAttribute("aria-expanded", "true");
  }
});

/* ---------- رسم "قريباً" ---------- */
const soonGrid = document.getElementById("soon-grid");
SOON.forEach((s) => {
  const card = document.createElement("div");
  card.className = "soon__card reveal";
  card.innerHTML = `
    <span class="soon__icon">${s.icon}</span>
    <span class="soon__title">${s.title}</span>
    <span class="soon__en" dir="ltr">${s.en}</span>
    <span class="soon__state">${s.pri} · قيد التحضير ⏳</span>`;
  soonGrid.appendChild(card);
});

/* ---------- الظهور عند التمرير ---------- */
const io = new IntersectionObserver(
  (entries) => entries.forEach((en) => en.isIntersecting && en.target.classList.add("in")),
  { threshold: 0.12 }
);
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

/* ---------- عدّادات الإحصائيات ---------- */
const counters = new IntersectionObserver(
  (entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      const el = en.target;
      counters.unobserve(el);
      const target = +el.dataset.count;
      const suffix = el.dataset.suffix || "";
      const t0 = performance.now();
      const dur = 1200;
      const tick = (t) => {
        const p = Math.min((t - t0) / dur, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = String(Math.round(target * eased)).padStart(2, "0") + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  },
  { threshold: 0.5 }
);
document.querySelectorAll(".stat__num").forEach((el) => counters.observe(el));

/* ---------- ساعة بغداد + السنة ---------- */
const clock = document.getElementById("clock");
const fmt = new Intl.DateTimeFormat("en-GB", {
  timeZone: "Asia/Baghdad",
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
  hour12: false,
});
setInterval(() => (clock.textContent = fmt.format(new Date())), 1000);
clock.textContent = fmt.format(new Date());
document.getElementById("year").textContent = new Date().getFullYear();
