---
title: 'عملي 3: مقوم نصف الموجة — Exp 3: Half-Wave Rectifier'
---

<callout icon="⚗️" color="purple_bg">
	**التجربة الثالثة — مختبر**
	Exp 3: Half-Wave Rectifier — مقوم نصف الموجة
	*د. أكرم محمد حاتم + م. زهراء عبد المهدي + م. عقيل علي*
</callout>
## 📑 فهرس التجربة
1. الهدف والمكونات
2. النظرية: فكرة التقويم
3. عمل الدائرة — النصف الموجب
4. عمل الدائرة — النصف السالب
5. النتيجة: جهد DC نابض
6. خطوات التنفيذ في NI Multisim
---
## 📝 الشرح التفصيلي
### 1️⃣ الهدف والمكونات
🎯 **الأهداف:**
1. بناء دائرة مقوم نصف الموجة (Half-Wave Rectifier)
2. قياس/رسم شكل موجة الدخل والخرج
3. إيجاد القيمة العظمى (Peak) والقيمة المتوسطة (Average) لإشارة الخرج
🛠️ **المكونات والمعدات:**
1. مصدر طاقة AC (مولد إشارة Function Generator) أو محول قياسي
2. راسم إشارة ثنائي القناة (Two-Channel Oscilloscope)
3. لوحة تجارب (Breadboard) + دايود شبه موصل + مقاومة 1KΩ
---
### 2️⃣ النظرية: فكرة التقويم
🌱 بسبب قدرة الدايود على **توصيل التيار باتجاه واحد وحجبه بالاتجاه الآخر**، تُستخدم الدايودات في دوائر تُسمى **المقوّمات (Rectifiers)** تحوّل جهد AC إلى جهد DC.
🌿 المقومات موجودة في **جميع مصادر تغذية DC** التي تعمل من مصدر جهد AC.
🌳 في الدائرة (الشكل 1): دايود موصول بمصدر AC يزوّد جهد الدخل $`V_{in}`$ إلى مقاومة حمل $`R_L`$ — مشكّلاً **مقوّم نصف موجة**.
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/a3ad8508-0f57-4f94-9fb0-d6ab14aafebf/p3-circuit.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CX2HZFC%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BnnJZZAfq%2FjGVpd61UM4mhbRN2hFpIdV8NnTnDtIAKQIgGEJm4kAkmOGBp4kPflw%2BFq3Zng2xzN7DOwABmmFcoIcq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLEfDgVZfcJmKT1NGircA4oAbEgVe8ljgg%2BrLWhfvtzQ8eaDAkdnV8HGLEeLU9b5GRDwFSGFIYlrLXFMJgpHtVEuRa3NwwvJrNn4jJwigbW1GKPOmCnB6kn4Z5xqWPl7VtetYxHAOBhs5WwF90mxiBVVIH4JiyddaPIgM38%2B7qXD3Kh%2BVKNXka30QYGzpi6yxmo9Ec9LPhDbmVtcK06NREAILJ6szGbCkXhVn2cXeD8kPyQdZ0LIqhQ%2BIZCN8ImkIMBjwQ5lAM22%2F4S10nRxKEB2YtfAnm0ObTDiRuLx4GacH2K8%2FFyhgTmLHXO72yegAjeeU4oav0rxUI9fC6I1P5hHJfZ9%2FAI9t0YRYPz8g1nokYMLklpfHViJFH3qh06VtZKW9ZGJ%2BnVFoS%2Bc2yb9%2Bj%2B3kSc%2B0hQKjDMZZs7HsGZ%2FZOTjCful%2FYXd7r%2FRRAdtJuxwtkO8h8htdMqylJFMSHmGW8Vg%2FuK9sKmC9Bk1UkergBHpfxYhEUaaWeJ74wQOTgE5DI5boJ4Ajdm1Ce2Q%2Facmo0Y%2FgFqPEfboWfvIjIe3GB6NF7bk6C%2FwL70vP9wxLdAoA9o2axbc%2Fz3icgOLBN7kKIBjH%2BHw5qXUB3EbITnfIHmRvSKYFyN9oH3q6o8lt2TqpuMD%2FUyojbN9MJ6E6dYGOqUBL11ZQ89bLYaQPBtZUVJ6HLLHxC09%2B628XWT%2FAbd4pVpmpNxlpFSmbvFxvvmwT4JrtpEIo00bdDZqp1MJbZ2rIuMTToq3UNxIf6IlGbL8i8Vcf68%2FZ7GML2Mnv%2FppitcPh0%2B31cYoEiLp9nWienrGFaUWTGAOJ4GyCtDqLEmxgMA0TV2E7%2FHrNhZeP4YWchd9wASll3dGWA2HqCLkWVcbRIzOn%2BFh&X-Amz-Signature=0a9e3fce548bf27c1ce67185d17dfd9d6723d46a8fe02831fd54435b1e499948&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.65c662cd-384d-49f1-8752-db8e2978f61a.b9748648-8d0b-81de-9e07-0003235c1886)
دائرة مقوم نصف الموجة — من ملزمة التجربة
---
### 3️⃣ عمل الدائرة — النصف الموجب من الدورة
🌿 عندما يصبح جهد الدخل الجيبي **موجباً**:
- الدايود D يكون **منحازاً أمامياً** (Forward-Biased)
- يوصّل تياراً عبر مقاومة الحمل $`R_L`$ (شكل 2)
- التيار ينتج **جهد خرج عبر **$`R_L`$ له نفس شكل نصف الموجة الموجبة
---
### 4️⃣ عمل الدائرة — النصف السالب من الدورة
🌿 عندما يصبح جهد الدخل **سالباً** خلال النصف الثاني من دورته:
- الدايود يكون **منحازاً عكسياً** (Reverse-Biased)
- **لا يمر تيار** ← الجهد عبر مقاومة الحمل $`R_L`$ = **صفر** (شكل 3)
---
### 5️⃣ النتيجة: جهد DC نابض
🌳 **الحصيلة:** فقط أنصاف الدورات الموجبة من جهد الدخل AC تظهر عبر الحمل؛ وبما أن الخرج **لا يغيّر قطبيته** ← فهو **جهد DC نابض (Pulsating DC)** كما في شكل 4.
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/ea2daaed-1378-46c0-b22e-1e808b5eec20/p3-waves.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CX2HZFC%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BnnJZZAfq%2FjGVpd61UM4mhbRN2hFpIdV8NnTnDtIAKQIgGEJm4kAkmOGBp4kPflw%2BFq3Zng2xzN7DOwABmmFcoIcq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLEfDgVZfcJmKT1NGircA4oAbEgVe8ljgg%2BrLWhfvtzQ8eaDAkdnV8HGLEeLU9b5GRDwFSGFIYlrLXFMJgpHtVEuRa3NwwvJrNn4jJwigbW1GKPOmCnB6kn4Z5xqWPl7VtetYxHAOBhs5WwF90mxiBVVIH4JiyddaPIgM38%2B7qXD3Kh%2BVKNXka30QYGzpi6yxmo9Ec9LPhDbmVtcK06NREAILJ6szGbCkXhVn2cXeD8kPyQdZ0LIqhQ%2BIZCN8ImkIMBjwQ5lAM22%2F4S10nRxKEB2YtfAnm0ObTDiRuLx4GacH2K8%2FFyhgTmLHXO72yegAjeeU4oav0rxUI9fC6I1P5hHJfZ9%2FAI9t0YRYPz8g1nokYMLklpfHViJFH3qh06VtZKW9ZGJ%2BnVFoS%2Bc2yb9%2Bj%2B3kSc%2B0hQKjDMZZs7HsGZ%2FZOTjCful%2FYXd7r%2FRRAdtJuxwtkO8h8htdMqylJFMSHmGW8Vg%2FuK9sKmC9Bk1UkergBHpfxYhEUaaWeJ74wQOTgE5DI5boJ4Ajdm1Ce2Q%2Facmo0Y%2FgFqPEfboWfvIjIe3GB6NF7bk6C%2FwL70vP9wxLdAoA9o2axbc%2Fz3icgOLBN7kKIBjH%2BHw5qXUB3EbITnfIHmRvSKYFyN9oH3q6o8lt2TqpuMD%2FUyojbN9MJ6E6dYGOqUBL11ZQ89bLYaQPBtZUVJ6HLLHxC09%2B628XWT%2FAbd4pVpmpNxlpFSmbvFxvvmwT4JrtpEIo00bdDZqp1MJbZ2rIuMTToq3UNxIf6IlGbL8i8Vcf68%2FZ7GML2Mnv%2FppitcPh0%2B31cYoEiLp9nWienrGFaUWTGAOJ4GyCtDqLEmxgMA0TV2E7%2FHrNhZeP4YWchd9wASll3dGWA2HqCLkWVcbRIzOn%2BFh&X-Amz-Signature=b6582505981f96bab3fa26f15c1014b6ad4dac1a050e27151752aa1658979d04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.6a22c1c0-1901-41d4-a2cb-299c1a531596.b9748648-8d0b-81de-9e07-0003235c1886)
موجة الدخل (جيبية كاملة) وموجة الخرج (أنصاف موجبة فقط) — من ملزمة التجربة
---
### 6️⃣ خطوات التنفيذ في NI Multisim
1. افتح **NI Multisim 14.2**
2. من (Place Source) اختر **AC_Voltage** وضعه، واختر أيضاً **Ground**
3. اجعل المصدر **5 Vpk** و **50Hz**
4. من (Place Diode) اختر **Diodes_Virtual** ثم **Diode** وضعه
5. من (Place Basic) اختر **Resistor** بقيمة **1.0 KΩ** وضعه
6. صِل جميع الأجزاء بالأسلاك
7. من الجانب الأيمن اختر الجهاز الرابع — **راسم الإشارة (Oscilloscope)**: القناة 1 (Channel 1) على المصدر، والقناة 2 (Channel 2) على طرفي المقاومة
8. غيّر لون أسلاك القناة 1: نقرة يمين ← Segment Color ← اختر اللون الذي تريده
9. شغّل الدائرة، ثم افتح راسم الإشارة واختر **AC** للقناة 1 و **DC** للقناة 2، واختر خيار **Single** في Trigger
10. لاحظ شكل الموجة في الدخل والخرج، ارسمها، حدد قيمة جهد الخرج وسجّلها في الجدول، ثم غيّر جهد المصدر إلى **10** و **15** وسجّل القيم أيضاً
---
## 📊 الجداول المقارنة
### ⚖️ سلوك الدائرة خلال دورة الدخل
<table header-row="true">
<tr color="blue_bg">
<td>**المعيار**</td>
<td>**النصف الموجب**</td>
<td>**النصف السالب**</td>
</tr>
<tr>
<td>حالة الدايود</td>
<td>تحيز أمامي</td>
<td>تحيز عكسي</td>
</tr>
<tr>
<td>التيار عبر $`R_L`$</td>
<td>يسري</td>
<td>صفر</td>
</tr>
<tr>
<td>جهد الخرج عبر $`R_L`$</td>
<td>يتبع شكل نصف الموجة الموجبة</td>
<td>صفر</td>
</tr>
</table>
---
## 🗺️ الخريطة الذهنية
<details color="purple_bg">
<summary>⚗️ Exp 3 — مقوم نصف الموجة</summary>
	<details color="gray_bg">
	<summary>💡 الفكرة</summary>
		- الدايود يوصّل باتجاه ويحجب بالآخر ← أساس المقوّمات
		- كل مصدر DC يعمل من AC فيه مقوّم
	</details>
	<details color="gray_bg">
	<summary>🔄 العمل</summary>
		- نصف موجب ← أمامي ← تيار عبر $`R_L`$ ← خرج يتبع الموجة
		- نصف سالب ← عكسي ← لا تيار ← خرج صفر
		- الناتج: **DC نابض** (أنصاف موجبة فقط، قطبية ثابتة)
	</details>
	<details color="gray_bg">
	<summary>🖥️ Multisim</summary>
		- مصدر 5 Vpk / 50Hz ← ثم 10 و 15
		- دايود + مقاومة 1KΩ
		- راسم إشارة: قناة 1 على المصدر / قناة 2 على المقاومة
		- المطلوب قياسه: القيمة العظمى والمتوسطة للخرج
	</details>
</details>
---
## ❓ أسئلة متوقعة
1. ما أهداف التجربة الثالثة الثلاثة؟ وما المكونات المطلوبة؟
2. لماذا يصلح الدايود لدوائر التقويم؟ (اربط الإجابة بخاصية التحيز)
3. اشرح ما يحدث في دائرة مقوم نصف الموجة خلال النصف الموجب من دورة الدخل.
4. اشرح ما يحدث خلال النصف السالب، ولماذا يكون جهد الخرج صفراً؟
5. لماذا يُسمى خرج هذه الدائرة "جهد DC نابض"؟
6. في خطوات Multisim: أين توصَل قناتا راسم الإشارة؟ ولماذا تُضبط القناة 1 على AC والقناة 2 على DC؟