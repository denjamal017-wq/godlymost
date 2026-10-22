---
title: 'المحاضرة 3 نظري: مراجعة بايثون — Python Review'
---

<callout icon="📙" color="orange_bg">
	**المحاضرة الثالثة — نظري**
	Python Review — مراجعة بايثون
	*م.م عباس كامل — المرحلة الثانية*
</callout>
## 📑 فهرس المحاضرة
1. مميزات بايثون واستخداماتها
2. المتغيرات وأنواع البيانات + قواعد التسمية
3. التعليقات (Comments)
4. الجمل الشرطية if / elif / else
5. حلقات for + break / continue
6. حلقات while
7. الحلقات المتداخلة (الأعداد الأولية)
8. السلاسل النصية ودوالها
9. إدخال المستخدم
<callout icon="📌" color="yellow_bg">
	**ملاحظة من الملزمة:** الدوال (Functions) ستُشرح في المحاضرة القادمة
</callout>
---
## 📝 الشرح التفصيلي
### 1️⃣ مميزات بايثون واستخداماتها
🌱 **المميزات:**
- لغة سهلة التعلم وكائنية التوجه (OOP)
- صياغة واضحة ومقروءة (Readable Syntax)
- مكتبة قياسية غنية
- تعمل على أنظمة تشغيل متعددة (Cross-Platform)
🌿 **الاستخدامات:** تطبيقات الويب • تطوير الألعاب • تعلم الآلة وتحليل البيانات • **أدوات الاختراق والأمن**
---
### 2️⃣ المتغيرات وأنواع البيانات
🌱 **الأنواع الأساسية:**
```python
x = 5            # int   — عدد صحيح
y = 3.14         # float — عدد عشري
name = "Ali"     # str   — نص
is_valid = True  # bool  — منطقي (صح/خطأ)
```
🌿 **قواعد تسمية المتغيرات:**
- يمكن أن تحتوي أحرفاً وأرقاماً وشرطة سفلية (_)
- **لا يمكن أن تبدأ برقم**
- حساسة لحالة الأحرف (case-sensitive): الاسم Name ≠ name
🌳 **أمثلة التعيين — بايثون ديناميكية الأنواع:**
```python
x = 10
name = "Ali"
total = 20.5
x = "Ali"   # مسموح — نوع المتغير يتغير حسب القيمة
```
---
### 3️⃣ التعليقات (Comments)
```python
# This is a comment   — تعليق بسطر واحد يبدأ بـ #

"""
This is a
multiline comment
"""                    — تعليق متعدد الأسطر (docstring)
```
---
### 4️⃣ الجمل الشرطية
🌱 **if / else — فحص الزوجي والفردي:**
```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
🌿 **elif والشروط المتداخلة — مصنّف الدرجات:**
```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```
🌳 عند score = 85 ← الشرط الأول لا يتحقق، الثاني يتحقق ← الناتج: **Grade: B**
---
### 5️⃣ حلقات for
🌱 **جمع الأعداد من 1 إلى 100:**
```python
total = 0
for i in range(1, 101):
    total += i
print(total)
```
🌿 **break / continue — طباعة الأعداد الزوجية فقط من 1 إلى 10:**
```python
for i in range(1, 11):
    if i % 2 != 0:
        continue   # تخطَّ الفردي
    print(i)
```
🌳 continue يتخطى التكرار الحالي ويكمل التالي؛ break يكسر الحلقة كلياً.
---
### 6️⃣ حلقات while
🌱 **حساب مضروب العدد 5:**
```python
n = 5
fact = 1
i = 1
while i <= 5:
    fact *= i
    i += 1
print(fact)   # 120
```
🌿 **while مع continue — تخطي مضاعفات 3 (من 0 إلى 9):**
```python
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
```
---
### 7️⃣ الحلقات المتداخلة — الأعداد الأولية من 2 إلى 50
🌳 حلقة داخل حلقة: الخارجية تمر على كل عدد، والداخلية تختبر قابلية القسمة:
```python
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
```
---
### 8️⃣ السلاسل النصية (Strings)
🌱 **عمليات أساسية:**
```python
text = "Hello" + " " + "World"   # دمج — "Hello World"
print(text.upper())               # HELLO WORLD
print(text.replace("World", "Python"))  # Hello Python
```
🌿 **دوال السلاسل المذكورة بالمحاضرة:**
<table header-row="true">
<tr color="orange_bg">
<td>**الدالة**</td>
<td>**الوظيفة**</td>
<td>**مثال**</td>
<td>**الناتج**</td>
</tr>
<tr>
<td>upper()</td>
<td>تحويل إلى أحرف كبيرة</td>
<td>"hello".upper()</td>
<td>"HELLO"</td>
</tr>
<tr>
<td>lower()</td>
<td>تحويل إلى أحرف صغيرة</td>
<td>"HELLO".lower()</td>
<td>"hello"</td>
</tr>
<tr>
<td>strip()</td>
<td>إزالة الفراغات من الطرفين</td>
<td>"  hi  ".strip()</td>
<td>"hi"</td>
</tr>
<tr>
<td>replace()</td>
<td>استبدال نص بنص</td>
<td>"Hello World".replace("World", "Python")</td>
<td>"Hello Python"</td>
</tr>
<tr>
<td>split()</td>
<td>تقسيم النص إلى قائمة</td>
<td>"a,b,c".split(",")</td>
<td>\['a', 'b', 'c'\]</td>
</tr>
<tr>
<td>find()</td>
<td>إيجاد موضع أول ظهور</td>
<td>"hello".find("e")</td>
<td>1</td>
</tr>
</table>
---
### 9️⃣ إدخال المستخدم (User Input)
🌱 input() تقرأ نصاً دائماً ← للأعداد نحوّلها بـ int():
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```
---
## 📊 الجداول المقارنة
### ⚖️ أنواع البيانات الأساسية
<table header-row="true">
<tr color="blue_bg">
<td>**النوع**</td>
<td>**الوصف**</td>
<td>**مثال**</td>
</tr>
<tr>
<td>int</td>
<td>عدد صحيح</td>
<td>x = 5</td>
</tr>
<tr>
<td>float</td>
<td>عدد عشري</td>
<td>y = 3.14</td>
</tr>
<tr>
<td>str</td>
<td>نص</td>
<td>name = "Ali"</td>
</tr>
<tr>
<td>bool</td>
<td>قيمة منطقية</td>
<td>is_valid = True</td>
</tr>
</table>
### ⚖️ for vs while
<table header-row="true">
<tr color="purple_bg">
<td>**المعيار**</td>
<td>**for**</td>
<td>**while**</td>
</tr>
<tr>
<td>نمط الاستخدام في المحاضرة</td>
<td>عدد تكرارات معلوم عبر range()</td>
<td>تكرار بشرط متحقق</td>
</tr>
<tr>
<td>مثال المحاضرة</td>
<td>جمع 1..100 • الزوجية 1..10 • الأولية 2..50</td>
<td>مضروب 5 • تخطي مضاعفات 3</td>
</tr>
<tr>
<td>أدوات التحكم المشتركة</td>
<td>continue — تخطي التكرار الحالي</td>
<td>break — كسر الحلقة كلياً</td>
</tr>
</table>
---
## 🗺️ الخريطة الذهنية
<details color="orange_bg">
<summary>🐍 مراجعة بايثون — المحور المركزي</summary>
	<details color="gray_bg">
	<summary>✨ المميزات والاستخدامات</summary>
		- سهلة + OOP + صياغة مقروءة + مكتبة غنية + متعددة المنصات
		- ويب • ألعاب • تعلم آلة/بيانات • أدوات اختراق
	</details>
	<details color="gray_bg">
	<summary>📦 المتغيرات</summary>
		- int / float / str / bool — كتابة ديناميكية (x=10 ثم x="Ali")
		- تسمية: أحرف/أرقام/_ • لا تبدأ برقم • حساسة للحالة
	</details>
	<details color="gray_bg">
	<summary>🔀 التحكم بالتدفق</summary>
		- if / elif / else ← مصنف الدرجات A/B/C/F
		- for + range ← جمع 1..100 \| continue للزوجية \| break للكسر
		- while بشرط ← مضروب 5 ← تخطي مضاعفات 3
		- متداخلة ← أعداد أولية 2..50
	</details>
	<details color="gray_bg">
	<summary>🔤 السلاسل والإدخال</summary>
		- دمج + upper + replace
		- دوال: upper • lower • strip • replace • split • find
		- input() ← نص ← int(input()) للأعداد
	</details>
</details>
---
## ❓ أسئلة متوقعة
1. اذكر أربع مميزات للغة بايثون وأربعة من استخداماتها.
2. ما قواعد تسمية المتغيرات في بايثون؟ ولماذا يُعد السطر x = "Ali" بعد x = 10 صحيحاً؟
3. اكتب برنامجاً يفحص هل العدد المُدخل زوجي أم فردي.
4. اكتب مصنّف الدرجات باستخدام elif وحدد ناتجه عند score = 85.
5. اكتب حلقة for تجمع الأعداد من 1 إلى 100.
6. ما الفرق بين break و continue؟ ادعم بمثال من المحاضرة.
7. اكتب حلقة while تحسب مضروب العدد 5.
8. اشرح كيف تعمل الحلقات المتداخلة في برنامج الأعداد الأولية (2..50).
9. املأ: ناتج "hello".find("e")‎ = ؟ وناتج "a,b,c".split(",")‎ = ؟
10. لماذا نستخدم int(input())‎ بدل input()‎ عند قراءة عمر المستخدم؟