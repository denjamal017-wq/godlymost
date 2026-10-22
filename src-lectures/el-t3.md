---
title: 'المحاضرة 3 نظري: شوكلي وتحليل خط الحمل — Shockley & Load-Line Analysis'
---

<callout icon="📙" color="orange_bg">
	**المحاضرة الثالثة — نظري**
	Shockley Equation, Load-Line Analysis, Operating Point
	*د. أكرم محمد حاتم — المرحلة الثانية*
</callout>
## 📑 فهرس المحاضرة
1. معادلة شوكلي (Shockley Equation)
2. أنماط التشغيل — تبسيطات المعادلة
3. خط الحمل (Load Line)
4. نقطتا التشبع والقطع
5. نقطة التشغيل (Q-Point)
---
## 📝 الشرح التفصيلي
### 1️⃣ معادلة شوكلي (Shockley Equation)
🌱 **التعريف:** صيغة رياضية عامة مُشتقة استناداً إلى مفاهيم فيزياء الحالة الصلبة، تُستخدم لوصف **المنحنى المميز للدايود شبه الموصل** في حالتي التحيز الأمامي والعكسي معاً. يُعطى التيار المار عبر الدايود بالصيغة:
$$
I = I_S \left( e^{\frac{V_D}{n V_T}} - 1 \right)
$$
🌿 **الرموز:**
- $`I`$ — التيار المار عبر الدايود
- $`I_S`$ — تيار الإشباع للدايود
- $`V_D`$ — جهد الدايود
- $`n`$ — معامل المثالية للدايود، تتراوح قيمته عادة بين 1 و 2
- $`V_T`$ — الجهد الحراري، يُحسب بالعلاقة $`V_T = \frac{KT}{q}`$ حيث $`K`$ ثابت بولتزمان، $`T`$ درجة الحرارة بالكلفن، $`q`$ شحنة الإلكترون
---
### 2️⃣ أنماط التشغيل — تبسيط المعادلة
🌿 **التحيز الأمامي (**$`V_D > 0`$**):** الحد الأسي $`e^{V_D / nV_T}`$ يزداد بسرعة ويصبح أكبر بكثير من 1 ← تُبسَّط المعادلة إلى:
$$
I \approx I_S \, e^{\frac{V_D}{n V_T}}
$$
🌿 **التحيز العكسي (**$`V_D < 0`$**):** الحد الأسي يقترب بسرعة من الصفر ← تُبسَّط المعادلة إلى:
$$
I \approx -I_S
$$
🌳 **المعنى الفيزيائي:** في الأمامي التيار ينمو أُسّياً مع الجهد، وفي العكسي يثبت عند تيار التشبع العكسي الضئيل — وهذا يطابق تماماً سلوك منحنى I-V من المحاضرة الثانية.
---
### 3️⃣ خط الحمل ونقطة التشغيل (Load Line)
🌱 خط الحمل أداة تُستخدم لتحديد **التيار المار عبر جهاز شبه موصل** و**فرق الجهد بين طرفيه** بدقة — أي تحديد القيم الممكنة للتيار والجهد عند طرفي الدايود في دائرة محددة. الفائدة الكبرى ستظهر لاحقاً مع أجهزة أكثر تعقيداً كالترانزستورات.
🌿 في حالة الدايود، خط الحمل يمثل **المحل الهندسي لجميع قيم التيار والجهد** التي يمكن أن يتخذها الدايود في دائرة معينة. ولرسمه يجب أولاً إيجاد العلاقة بين فرق الجهد بين طرفي الدايود والتيار المار فيه — عبر تطبيق **قانون كيرشوف للجهد (KVL):** المجموع الجبري لفروق الجهد حول أي دائرة كهربائية مغلقة يساوي صفراً.
🌳 بتطبيق KVL على دائرة (مصدر $`V_S`$ + مقاومة $`R_S`$ + دايود على التوالي):
$$
V_S - I_D R_S - V_D = 0
$$
ومنها **معادلة خط الحمل:**
$$
I_D = \frac{V_S - V_D}{R_S}
$$
**مثال عددي من المحاضرة:** إذا كان $`V_S = 2`$ فولت و $`R_S = 100\,\Omega`$:
$$
I_D = \frac{2 - V_D}{100}
$$
---
### 4️⃣ نقطتا التشبع والقطع
🌱 بما أن معادلة خط الحمل تمثل خطاً مستقيماً ← يكفي تحديد نقطتين لرسمه (المحور العمودي = تيار الدايود $`I_D`$، والمحور الأفقي = جهد الدايود $`V_D`$):
- **نقطة التشبع (Saturation Point):** ‏($`V_D = 0`$ V ، $`I_D = 20`$ mA) — تمثل **أقصى تيار** يمكن أن يمر عبر الدايود في هذا التكوين للدائرة
- **نقطة القطع (Cutoff Point):** ‏($`V_D = 2`$ V ، $`I_D = 0`$ mA) — تمثل **أقل تيار (صفر)** يمكن أن يمر عبر الدايود
🌳 بعد تحديد النقطتين، يُرسم خط الحمل مباشرة فوق **منحنى خصائص الدايود** — وهو منحنى يمثل خاصية ذاتية للدايود بغض النظر عن الدائرة التي يعمل فيها.
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/2d5445e6-0af1-4022-b402-7eb5cdb595f1/l3-loadline.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GCI22W2%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBeHR6HSCQPimlEA9gC3yYOCTNLKT6rONgsXDugwG%2BFXAiAVqpka5i2PWmuk6WsfHO2qrccdn0958sz4G8ma7bxxQyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMFtPEqAwbLXKY%2BsApKtwDIPYkEhdHYdw3S24J%2Bl8ruEhJjAtRIAO17iqtdjxvl9VzHtoQ%2Fg5jqtqJvtP%2BOrjG9XCUBnxYlaXvc9jwGlASmyH%2BWaHc%2BkrXPoDJhTCAvSabE%2BgkDwAFPsJzCu%2F7uDnHvX%2FB12uOtKz30ZkhE7FdEIw9%2FoOjwsjeHCEtS6TU4efsAXKIMPLvjpTfhJIrSHeecVtSl%2B%2BuKtbjltk5o5JXmsaUbNEkEgvBh%2BR5ORFR%2FWl7HmbyX2h3wjEqoz7AnvjFDxRy1eNC5dd%2Fi5sdB7aq5KxfVMOeph9jeLOMw5iY1IUUCKbXrSK6i9xxBaia98XvGjN9Pv896l9FZQ1wXFFRMEzA22Ta7brNzioE9utK9dMiN1%2BT%2F%2FtXx2Ix72Kpls8D5P9Rc6F1q5k02UugzyEK4iiUV8ZcHsX6LPaLZvOTQok%2BR0qmIjjqXg0D0iuen8g9LCqpVjdgRDkmhExkUzb8Ubs4Ukl49hpqmwVgdYFgX9Kbc8n3DeX0M7hH2Cg6jt%2BKB6L%2B1%2F9AbfftFUEDQBow7KLSWryIpyZYYfx0v9gemh72VLLEMjUfeROb%2BZKDPtvmcQ%2B1zy3rNvXdCZpI81A%2BpoHYEXL2EbUC8h6UnXBZa2Rom1B1%2FKleBv7ZKskw%2Bobp1gY6pgGeEKCALRfniPeCZVdOfF0N662Fvt6w6WKuKLvgNvzNJtr34vhLgkihaxE9BVNT6t7bBR952Csqci%2FqlqQ%2FFvsTdiiOuQ6q4%2B%2BaF2cmkP2vgktKT8F%2B2cqjB1YdlsDIt5MsI5KOiD9BPtcb74racxSJNFBEhXXX0aYIgYZ2C%2Bsvrtz5PHmmwcKRvKaxs%2FeEmJFOCZYi0tZiw8pzZCp99D6KWPcqO9f3&X-Amz-Signature=52feaa0dc6d040d8b1f43406366829518816b517b0bef05c830176375c69f9bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.857ea827-d6e7-4e10-82b8-5786af5dba49.b9748648-8d0b-81de-9e07-0003235c1886)
خط الحمل مرسوماً على منحنى خصائص الدايود — نقطة التشبع أعلى اليسار، نقطة القطع أسفل اليمين، ونقطة التشغيل Q عند التقاطع — من الملزمة
---
### 5️⃣ نقطة التشغيل (Q-Point)
🌱 نقطة التشغيل عموماً تمثل نقطة محددة على خط الحمل تتحدد بناءً على قيم التيار والجهد عند حالة تشغيل معينة.
🌳 في حالة الدايود البلوري، نقطة التشغيل هي **نقطة التقاطع المشتركة بين خط الحمل ومنحنى خصائص الدايود**؛ وبإسقاط أعمدة على كلا المحورين نجد أن نقطة التشغيل في هذا المثال هي:
<callout icon="🎯" color="green_bg">
	$`V_D = 0.75`$ V ، $`I_D = 12.5`$ mA
</callout>
---
## 📊 الجداول المقارنة
### ⚖️ أنماط تشغيل معادلة شوكلي
<table header-row="true">
<tr color="orange_bg">
<td>**النمط**</td>
<td>**الشرط**</td>
<td>**سلوك الحد الأسي**</td>
<td>**المعادلة المبسطة**</td>
</tr>
<tr>
<td>تحيز أمامي</td>
<td>$`V_D > 0`$</td>
<td>ينمو بسرعة ويتجاوز 1 بكثير</td>
<td>$`I \approx I_S \, e^{V_D / nV_T}`$</td>
</tr>
<tr>
<td>تحيز عكسي</td>
<td>$`V_D < 0`$</td>
<td>يقترب من الصفر</td>
<td>$`I \approx -I_S`$</td>
</tr>
</table>
### ⚖️ نقطتا خط الحمل (مثال: $`V_S = 2`$V ، $`R_S = 100\Omega`$)
<table header-row="true">
<tr color="blue_bg">
<td>**النقطة**</td>
<td>**الإحداثيات**</td>
<td>**المعنى الفيزيائي**</td>
</tr>
<tr>
<td>التشبع Saturation</td>
<td>$`V_D = 0`$ ، $`I_D = 20`$ mA</td>
<td>أقصى تيار ممكن في الدائرة</td>
</tr>
<tr>
<td>القطع Cutoff</td>
<td>$`V_D = 2`$ V ، $`I_D = 0`$</td>
<td>أقل تيار ممكن (صفر)</td>
</tr>
<tr>
<td>التشغيل Q-Point</td>
<td>$`V_D = 0.75`$ V ، $`I_D = 12.5`$ mA</td>
<td>تقاطع خط الحمل مع منحنى الدايود</td>
</tr>
</table>
---
## 🗺️ الخريطة الذهنية
<details color="orange_bg">
<summary>📈 تحليل الدايود رياضياً — المحور المركزي</summary>
	<details color="gray_bg">
	<summary>🧮 معادلة شوكلي</summary>
		- $`I = I_S(e^{V_D/nV_T} - 1)`$
		- $`V_T = KT/q`$ — معامل المثالية $`n`$ بين 1 و 2
		- أمامي ← $`I \approx I_S e^{V_D/nV_T}`$ \| عكسي ← $`I \approx -I_S`$
	</details>
	<details color="gray_bg">
	<summary>📏 خط الحمل</summary>
		- الأداة: KVL ← $`V_S - I_D R_S - V_D = 0`$
		- المعادلة: $`I_D = (V_S - V_D)/R_S`$
		- نقطة التشبع (أقصى تيار) + نقطة القطع (صفر تيار) ← يُرسم الخط بينهما
	</details>
	<details color="gray_bg">
	<summary>🎯 نقطة التشغيل Q</summary>
		- تقاطع خط الحمل مع منحنى خصائص الدايود
		- مثال المحاضرة: 0.75V و 12.5mA
		- المنحنى خاصية ذاتية للدايود بغض النظر عن الدائرة
	</details>
</details>
---
## ❓ أسئلة متوقعة
1. اكتب معادلة شوكلي واشرح كل رمز فيها بالتفصيل (بما فيه $`V_T`$ ومكوناته).
2. بسّط معادلة شوكلي لحالتي التحيز الأمامي والعكسي مع تبرير كل تبسيط.
3. ما فائدة خط الحمل؟ ولماذا تكمن فائدته الكبرى في الترانزستورات؟
4. اشتق معادلة خط الحمل انطلاقاً من قانون كيرشوف للجهد لدائرة فيها مصدر ومقاومة ودايود على التوالي.
5. لدائرة فيها $`V_S = 2`$V و $`R_S = 100\Omega`$: احسب نقطتي التشبع والقطع، وعرّف كلاً منهما.
6. عرّف نقطة التشغيل Q-point وكيف تُحدد هندسياً في حالة الدايود البلوري.