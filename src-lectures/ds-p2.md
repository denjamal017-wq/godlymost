---
title: 'عملي 2: البنّاءات ومعدّلات الوصول — Constructors & Access Modifiers'
---

<callout icon="🧪" color="red_bg">
	**التجربة الثانية — مختبر**
	OOP Lab 2: Constructors & Access Modifiers — البنّاءات ومعدّلات الوصول
	*م.م عباس كامل + ب. صبا صباح — المرحلة الثانية — قسم الأمن السيبراني*
</callout>
## 📑 فهرس التجربة
1. مراجعة سريعة: ما هو الصنف؟
2. ما هو البنّاء (Constructor)؟
3. أنواع البنّاءات الأربعة
4. مؤشر this
5. معدّلات الوصول: public / private / protected
6. لماذا نستخدم معدّلات الوصول + Getters & Setters
7. أمثلة عملية شاملة
8. التمارين المطلوبة
---
## 📝 الشرح التفصيلي
### 1️⃣ مراجعة: ما هو الصنف؟
🌱 الصنف **مخطط (Blueprint)** يجمع البيانات والدوال معاً في وحدة واحدة:
```c++
class Student {
    string name;            // بيانات
    int age;
    void display_info();    // دوال
    bool is_adult();
};
```
---
### 2️⃣ ما هو البنّاء (Constructor)؟
🌱 البنّاء **دالة عضو خاصة تُستدعى تلقائياً عند إنشاء كائن جديد** — وظيفتها تهيئة بيانات الكائن الأولية.
🌿 قواعده: اسمه = **نفس اسم الصنف** تماماً • **بدون نوع إرجاع** • يُنفَّذ مرة واحدة عند الإنشاء.
🌳 **تشبيه المحاضرة:** البنّاء = **خط الإنتاج في مصنع السيارات** الذي يجمع الأجزاء ويجهّز السيارة ← الكائن = السيارة الجاهزة الخارجة من المصنع.
---
### 3️⃣ أنواع البنّاءات
#### 🔹 البنّاء الافتراضي (Default Constructor)
🌱 بدون معاملات — يعطي قيماً أولية ثابتة:
```c++
class Student {
    string name;
    int age;
public:
    Student() {            // بنّاء افتراضي
        name = "Unknown";
        age = 0;
    }
};
```
#### 🔹 البنّاء المُعامَلاتي (Parameterized Constructor)
🌿 يستقبل معاملات لتهيئة الكائن بقيم مخصصة:
```c++
class Student {
    string name;
    int age;
public:
    Student(string n, int a) {   // بنّاء بمعاملات
        name = n;
        age = a;
    }
};
```
#### 🔹 التحميل الزائد للبنّاءات (Constructor Overloading)
🌳 تعريف **عدة بنّاءات بنفس الاسم بمعاملات مختلفة** — والمترجم يختار المناسب حسب الاستدعاء. **تشبيه المحاضرة:** ماكينة القهوة ← زر افتراضي يعطي قهوة سادة، وأزرار مخصصة تحدد الحجم والسكر والحليب:
```c++
class Student {
    string name;
    int age;
public:
    Student() { name = "Unknown"; age = 0; }         // افتراضي
    Student(string n, int a) { name = n; age = a; }  // بمعاملات
};
```
#### 🔹 بنّاء بمعاملات افتراضية (Default Parameters)
🌿 قيم افتراضية للمعاملات تُستخدم عند عدم تمريرها:
```c++
class TemperatureConverter {
    double fahrenheit;
public:
    TemperatureConverter(double f = 32) {   // 32 قيمة افتراضية
        fahrenheit = f;
    }
};
```
---
### 4️⃣ مؤشر this
🌱 المؤشر this **يشير إلى الكائن الحالي** — يُستخدم للتمييز بين بيانات العضو ومعاملات الدالة عند تشابه الأسماء:
```c++
class BankAccount {
    double balance;
public:
    void setBalance(double balance) {
        this->balance = balance;   // this->balance هو عضو الصنف
    }
};
```
---
### 5️⃣ معدّلات الوصول (Access Modifiers)
🌱 تتحكم بمن يستطيع الوصول إلى بيانات الصنف ودواله — ثلاثة أنواع:
- **public (عام):** متاح للجميع — من داخل الصنف وخارجه وأي مكان بالبرنامج
- **private (خاص):** داخل الصنف فقط — للبيانات الحساسة (كلمات المرور، الأرصدة)
- **protected (محمي):** داخل الصنف والأصناف المشتقة منه فقط (مع الوراثة)
🌿 **تشبيه المنزل من المحاضرة:** النوع public = باب الشارع الذي يستخدمه الجميع • والنوع private = غرفة نومك الخاصة بك وحدك • والنوع protected = غرف مخصصة لأفراد العائلة فقط
🌳 **جدول الوصول:**
<table header-row="true">
<tr color="red_bg">
<td>**المعدّل**</td>
<td>**نفس الصنف**</td>
<td>**الصنف المشتق**</td>
<td>**خارج الصنف**</td>
</tr>
<tr>
<td>public</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>protected</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>private</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
</tr>
</table>
---
### 6️⃣ لماذا نستخدم معدّلات الوصول؟ + نمط Getters & Setters
🌿 **الأسباب الأربعة من المحاضرة:** الحماية (Security) • التحكم (Control) • منع سوء الاستخدام • سهولة الصيانة
🌳 **نمط Getters & Setters:** البيانات private + دوال عامة للقراءة والكتابة مع التحقق:
```c++
class BankAccount {
    double balance;                  // خاص — محمي
public:
    double getBalance() {            // Getter
        return balance;
    }
    void setBalance(double amount) { // Setter مع تحقق
        if (amount > 0)
            balance = amount;
    }
};
```
---
### 7️⃣ أمثلة عملية شاملة من المحاضرة
- **نظام قاعدة بيانات الطلاب (Student Database System):** يجمع أنواع البنّاءات مع التغليف
- **نظام إدارة المكتبة (Library Management System):** صنف Book مع دوال borrow/return تتحكم بحالة الكتاب
- **محلل الحرارة (Temperature Analyzer):** وصول للقراءة فقط مع تحقق من صحة القيم
---
### 8️⃣ التمارين المطلوبة
1. صنف **Rectangle** لحساب المساحة
2. صنف **Circle**
3. صنف **Employee** لكشف الرواتب (Payroll)
4. صنف **ATM** مع حماية رمز PIN
---
## 📊 الجداول المقارنة
### ⚖️ أنواع البنّاءات الأربعة
<table header-row="true">
<tr color="green_bg">
<td>**النوع**</td>
<td>**الوصف**</td>
<td>**مثال الاستدعاء**</td>
</tr>
<tr>
<td>افتراضي Default</td>
<td>بلا معاملات — قيم أولية ثابتة</td>
<td>Student s;</td>
</tr>
<tr>
<td>بمعاملات Parameterized</td>
<td>معاملات لتهيئة مخصصة</td>
<td>Student s("Ali", 20);</td>
</tr>
<tr>
<td>تحميل زائد Overloading</td>
<td>عدة بنّاءات بمعاملات مختلفة بالصنف الواحد</td>
<td>الافتراضي + المُعامَلاتي معاً</td>
</tr>
<tr>
<td>معاملات افتراضية</td>
<td>قيم تُستخدم عند غياب المعامل</td>
<td>TemperatureConverter t; ← f = 32</td>
</tr>
</table>
### ⚖️ public vs private vs protected
<table header-row="true">
<tr color="orange_bg">
<td>**المعيار**</td>
<td>**public**</td>
<td>**protected**</td>
<td>**private**</td>
</tr>
<tr>
<td>نفس الصنف</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>الصنف المشتق</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>خارج الصنف</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>الاستخدام</td>
<td>واجهات للجميع</td>
<td>وراثة فقط</td>
<td>بيانات حساسة</td>
</tr>
<tr>
<td>تشبيه المنزل</td>
<td>باب الشارع</td>
<td>غرف العائلة</td>
<td>غرفة نومك</td>
</tr>
</table>
---
## 🗺️ الخريطة الذهنية
<details color="red_bg">
<summary>🧪 البنّاءات ومعدّلات الوصول — المحور المركزي</summary>
	<details color="gray_bg">
	<summary>🏭 البنّاء Constructor</summary>
		- استدعاء تلقائي عند إنشاء الكائن ← تهيئة البيانات
		- اسمه = اسم الصنف • بلا نوع إرجاع • مرة واحدة
		- التشبيه: خط إنتاج المصنع ← السيارة الجاهزة
	</details>
	<details color="gray_bg">
	<summary>🔢 الأنواع الأربعة</summary>
		- افتراضي: بلا معاملات ← Unknown / 0
		- بمعاملات: قيم مخصصة ← Student("Ali", 20)
		- تحميل زائد: عدة بنّاءات ← ماكينة القهوة
		- معاملات افتراضية: f = 32
	</details>
	<details color="gray_bg">
	<summary>👉 مؤشر this</summary>
		- يشير للكائن الحالي
		- يميز عضو الصنف عن معامل الدالة
	</details>
	<details color="gray_bg">
	<summary>🔐 معدّلات الوصول</summary>
		- public: للجميع (باب الشارع)
		- private: الصنف فقط (غرفة نومك) ← Getters/Setters مع تحقق
		- protected: الصنف + المشتقات (غرف العائلة)
		- لماذا؟ حماية • تحكم • منع سوء استخدام • صيانة
	</details>
</details>
---
## ❓ أسئلة متوقعة
1. ما هو البنّاء؟ واذكر قواعده الثلاث (الاسم، الإرجاع، التنفيذ).
2. قارن بين البنّاء الافتراضي والمُعامَلاتي مع مثال كود لكل منهما.
3. ما التحميل الزائد للبنّاءات؟ واشرحه بتشبيه ماكينة القهوة.
4. ما فائدة المعاملات الافتراضية في البنّاء؟ (مثال TemperatureConverter)
5. ما مؤشر this ومتى نحتاجه؟ اكتب مثال BankAccount.
6. املأ جدول الوصول: أي معدّل يسمح بالوصول من خارج الصنف؟ وأيها يسمح للمشتقات فقط؟
7. لماذا نجعل البيانات private ونوفّر Getters و Setters؟ اكتب مثالاً بكود.
8. صمّم صنف ATM يحمي رمز PIN (تمرين المحاضرة) — حدد البيانات الخاصة والدوال العامة المطلوبة.