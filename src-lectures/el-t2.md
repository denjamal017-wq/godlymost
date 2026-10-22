---
title: 'المحاضرة 2 نظري: بناء الدايود والتحيز ومنطقة زينر — Diode, Biasing & Zener Region'
---

<callout icon="📗" color="green_bg">
	**المحاضرة الثانية — نظري**
	Semiconductor Diode Construction, Biasing Characteristics, Zener Region
	*د. أكرم محمد حاتم — المرحلة الثانية*
</callout>
## 📑 فهرس المحاضرة
1. تطبيقات الثنائيات (Diodes)
2. ثنائي الوصلة PN وحالة الاتزان
3. التحيز (Biasing) وحالاته الثلاث
4. التحيز الأمامي (Forward Bias)
5. التحيز العكسي (Reverse Bias)
6. منطقة زينر (Zener Region) وآلية عملها
7. منحنى الخصائص I-V: زينر vs الانهيار الإنهيماري
---
## 📝 الشرح التفصيلي
### 1️⃣ تطبيقات الثنائيات
🌱 الثنائيات من أبسط أجهزة أشباه الموصلات وأكثرها فائدة. تطبيقاتها المذكورة في المحاضرة:
- **ثنائيات التقويم (Rectifier Diodes):** مكوّن حيوي في وحدات التغذية — تحويل جهد التيار المتردد AC القادم من الشبكة إلى تيار مستمر DC
- **ثنائيات زينر (Zener Diodes):** تثبيت الجهد ومنع التغيرات غير المرغوبة في مصادر DC، وتوفير جهود مرجعية دقيقة للدوائر
- **حماية القطبية المعكوسة:** منع أضرار جسيمة بالمعدات العاملة بالبطاريات عند توصيلها بقطبية خاطئة
- **ثنائيات الإشارة (Signal Diodes):** استخلاص إشارات الصوت والصورة من إشارات التردد الراديوي (كشف التضمين Demodulation)، وتشكيل وتعديل أشكال الموجات (القص Clipping، الحد Limiting، استعادة مستوى DC)
- **الحماية داخل الدوائر المتكاملة:** تُدمج في الدوائر الرقمية لحمايتها من ارتفاعات الجهد الكبيرة (النبضات المفاجئة)
---
### 2️⃣ ثنائي الوصلة PN — حالة الاتزان (تحيز صفري)
🌱 يتشكل ثنائي الوصلة عند دمج شبه موصل p-Type مع شبه موصل n-Type ضمن شبكة بلورية واحدة ← ينشأ **جهد حاجز (Potential Barrier)** عند الوصلة.
🌿 عند الدمج تحدث ثلاث عمليات تلقائياً:
**أولاً — عملية الانتشار (Diffusion):**
- منطقة N: تحتوي تركيزاً عالياً من الإلكترونات الحرة (حاملات الأغلبية)
- منطقة P: تحتوي تركيزاً عالياً من الفجوات (حالات إلكترونية شاغرة تعمل كحاملات شحنة موجبة)
- بسبب التدرج الحاد في التركيز عبر الحد الفاصل ← تنتشر الإلكترونات الحرة القريبة من الوصلة من جانب N إلى جانب P لتلتحم مع الفجوات
**ثانياً — تشكيل منطقة الاستنفاذ (Depletion Region):**
- عندما يغادر إلكترون حر جانب N ← يترك خلفه **أيوناً موجباً ثابتاً مانحاً** (ذرة فقدت إلكتروناً)
- عندما يعيد الإلكترون الارتباط بفجوة في جانب P ← يتشكل **أيون سالب ثابت قابل** (ذرة اكتسبت إلكتروناً)
- تتراكم هذه الأيونات غير المتحركة على طول الحد الفاصل ← **منطقة خالية من حاملات الشحنة المتحركة = منطقة الاستنفاذ**
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/d52800ec-d8a9-4e98-9d40-07b5cc878b36/l2-depletion.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKI4ZZRU%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEN9fqdOci2ZftG6bhs95bZGkaef7v1BA4QQq8rYELvnAiEA0RmEkg8TSDtzIl6OI1Mdolxqc45S5tvlruDheLPyUKMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLrxm%2BoR8Mr0Q7Vt2ircA50EzvVGnO6u46f1vbSbG7O6DbNPgLdDL88bMmNP699K4H%2F8b7p9xWtUdk%2F5aetnQkkU5QJU6SBYp4dcRzjPm2znEGI4k92AUw7wEuTqVAvHFQd2J2n8eCMs72s%2Bxg%2BCknKe5i%2By4S2rFQ2xR7NNZ8gCSS3T7pkVUrB6lz9wyLlC0RMvl0qUJH%2FLYgnDyDW9fbN%2B6j2N9xvgSLeqPp5p1xcgDMrLJKqMRTh6xJpTMYAUN950mNp4GY0dy%2FTRUg5mS6pNhBRgXIzg7BatW8WaKZvUGLb%2Fwuz3fw9aNFNKb2vTIlosPf3otfBB%2Bmb72qW%2Fb726STI5h2n2K%2F3ESBiUmzRsIyFo%2FNZWtOnBnXxohzcXcInHPz7uS82eslz%2BMNYruwcpRNiqgxX4DX7Q4zl2kpED4ZppCFrW7ovSnuMXOxQPw%2Fv3zAY2DMvdEu17jlCKBwv1bHSdrmheeRBNcTvH3Ekoi44V5jdTkOGi8EY8lv7tb1Z3I6cXAKg7ANAKxmDB0MLIYqO%2BdvQfzSs3ASX5j0RVj0tJJA7d9SYyw1DCDqhxcdZCG2U4nThn7ZTT%2BPOr3O5K8Wl9dwBH2xckt11umyOBRbeNcpMoy%2BlJ1%2FtUjbbsjH5%2FCu1iG2rRAgI5MKiE6dYGOqUBT4gl4tC4N0PeJARNsHPkpRvJC9lYcpp4hsw2OmMB1MmxV%2BU%2BKdWTDr9wL69sbqsdsMXoy8M0rbg8AHqmIqrgy1UkJYISEAOVCP1uJybsZKYWF7jB1Xgu6pTpRtOOUnkrwP3ygQXvVeXGjU4n1h%2BALz8UP8kawPrnEKG6dO3g9dDiwdXcRNCjMO2YJeFUdD0797l0mawWr%2BbBZTkDP0KD1mO1YkSI&X-Amz-Signature=60527a4dd9ede2db9fb17116a9500ccfa7652e87c9f20cd1b71f79ef0b1b8bab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.6dd35293-9b20-4de4-897f-ed89dbb8022d.b9748648-8d0b-81de-9e07-0003235c1886)
تشكل منطقة الاستنفاذ وجهد الحاجز عند وصلة PN — من الملزمة
**ثالثاً — نشوء جهد الحاجز (Barrier Potential):**
- الأيونات الثابتة المتراكمة تولّد **مجالاً كهربائياً داخلياً** يتجه من الأيونات الموجبة (جانب N) إلى الأيونات السالبة (جانب P)
- هذا المجال الداخلي يقاوم استمرار انتشار الإلكترونات حتى الوصول إلى **اتزان ديناميكي**
- فرق الجهد الناتج عبر منطقة الاستنفاذ = **جهد الحاجز **$`V_\gamma`$ ≈ **0.7 فولت للسيليكون** و **0.3 فولت للجرمانيوم**
---
### 3️⃣ التحيز (Biasing) وحالاته الثلاث
🌱 **التعريف:** التحيز في الإلكترونيات هو تطبيق جهد مستمر DC خارجي عبر أطراف عنصر شبه موصل (كالدايود) لتهيئة ظروف تشغيل محددة والتحكم في تدفق التيار الكهربائي عبره.
🌿 للتغلب على جهد الحاجز والسماح بمرور التيار، يُوصَل مصدر DC خارجي (بطارية) بالطرفين P و N — ويختلف سلوك الدايود باختلاف طريقة التوصيل. الحالات الرئيسية الثلاث:
<table header-row="true">
<tr color="green_bg">
<td>**الحالة**</td>
<td>**الشرط**</td>
</tr>
<tr>
<td>A. عدم التحيز (No Bias)</td>
<td>$`V_D = 0`$ V</td>
</tr>
<tr>
<td>B. التحيز الأمامي (Forward Bias)</td>
<td>$`V_D > 0`$ V</td>
</tr>
<tr>
<td>C. التحيز العكسي (Reverse Bias)</td>
<td>$`V_D < 0`$ V</td>
</tr>
</table>
<callout icon="⚠️" color="orange_bg">
	ملاحظة من الملزمة: **مخططات حالات التحيز مطلوبة ومهمة** — راجعها في الملف الأصلي
</callout>
---
### 4️⃣ التحيز الأمامي (Forward Bias)
🌱 الموجب إلى P والسالب إلى N ← الدايود يوصّل.
🌿 **التوصيل وسريان التيار:**
- عندما يكون الجهد المطبق أدنى من جهد الحاجز ($`V_D < V_\gamma`$) ← التيار مهمل
- بمجرد تجاوز $`V_\gamma`$ ‏(0.7V للسيليكون) ← حاملات الأغلبية تكتسب طاقة كافية لعبور الوصلة
- يسري **تيار أمامي أُسّي (**$`I_D`$**)** عبر الدايود، وتنخفض المقاومة الديناميكية ($`r_d`$) لقيمة ضئيلة جداً
- منطقة الاستنفاذ **تضيق وتنهار**
🌳 **النتيجة:** الدايود يعمل فعلياً كـ**مفتاح مغلق (موصل)**
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/9ffa6168-f980-4473-9b9e-50e92d6e6bf6/l2-forward.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKI4ZZRU%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEN9fqdOci2ZftG6bhs95bZGkaef7v1BA4QQq8rYELvnAiEA0RmEkg8TSDtzIl6OI1Mdolxqc45S5tvlruDheLPyUKMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLrxm%2BoR8Mr0Q7Vt2ircA50EzvVGnO6u46f1vbSbG7O6DbNPgLdDL88bMmNP699K4H%2F8b7p9xWtUdk%2F5aetnQkkU5QJU6SBYp4dcRzjPm2znEGI4k92AUw7wEuTqVAvHFQd2J2n8eCMs72s%2Bxg%2BCknKe5i%2By4S2rFQ2xR7NNZ8gCSS3T7pkVUrB6lz9wyLlC0RMvl0qUJH%2FLYgnDyDW9fbN%2B6j2N9xvgSLeqPp5p1xcgDMrLJKqMRTh6xJpTMYAUN950mNp4GY0dy%2FTRUg5mS6pNhBRgXIzg7BatW8WaKZvUGLb%2Fwuz3fw9aNFNKb2vTIlosPf3otfBB%2Bmb72qW%2Fb726STI5h2n2K%2F3ESBiUmzRsIyFo%2FNZWtOnBnXxohzcXcInHPz7uS82eslz%2BMNYruwcpRNiqgxX4DX7Q4zl2kpED4ZppCFrW7ovSnuMXOxQPw%2Fv3zAY2DMvdEu17jlCKBwv1bHSdrmheeRBNcTvH3Ekoi44V5jdTkOGi8EY8lv7tb1Z3I6cXAKg7ANAKxmDB0MLIYqO%2BdvQfzSs3ASX5j0RVj0tJJA7d9SYyw1DCDqhxcdZCG2U4nThn7ZTT%2BPOr3O5K8Wl9dwBH2xckt11umyOBRbeNcpMoy%2BlJ1%2FtUjbbsjH5%2FCu1iG2rRAgI5MKiE6dYGOqUBT4gl4tC4N0PeJARNsHPkpRvJC9lYcpp4hsw2OmMB1MmxV%2BU%2BKdWTDr9wL69sbqsdsMXoy8M0rbg8AHqmIqrgy1UkJYISEAOVCP1uJybsZKYWF7jB1Xgu6pTpRtOOUnkrwP3ygQXvVeXGjU4n1h%2BALz8UP8kawPrnEKG6dO3g9dDiwdXcRNCjMO2YJeFUdD0797l0mawWr%2BbBZTkDP0KD1mO1YkSI&X-Amz-Signature=d8ac16a8c2efb236ccb1ae759936b8e2f6651e5c20fe5806e130e19cdb85e011&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.12ed3c90-0d45-4745-91d5-0219a641c46d.b9748648-8d0b-81de-9e07-0003235c1886)
التحيز الأمامي — تضيُّق منطقة الاستنفاذ وسريان تيار الأغلبية — من الملزمة
---
### 5️⃣ التحيز العكسي (Reverse Bias)
🌱 الموجب إلى N والسالب إلى P ← الدايود يحجب.
🌿 **التوصيل وسريان التيار:**
- تيار حاملات الأغلبية **محجوب تماماً** عبر الوصلة
- حاملات الأقلية المتولدة حرارياً تنتج تيار تسرب ضئيلاً يُعرف بـ**تيار التشبع العكسي (**$`I_S`$**)** — يقاس بالنانوأمبير (nA) في ثنائيات السيليكون
- الدايود يبدي **مقاومة عكسية (**$`R_R`$**) عالية للغاية**
🌳 **النتيجة:** الدايود يعمل فعلياً كـ**مفتاح مفتوح (عازل)**
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/69e7fcb1-a32d-4a59-bb0b-cd3aef64a6e8/l2-reverse.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKI4ZZRU%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEN9fqdOci2ZftG6bhs95bZGkaef7v1BA4QQq8rYELvnAiEA0RmEkg8TSDtzIl6OI1Mdolxqc45S5tvlruDheLPyUKMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLrxm%2BoR8Mr0Q7Vt2ircA50EzvVGnO6u46f1vbSbG7O6DbNPgLdDL88bMmNP699K4H%2F8b7p9xWtUdk%2F5aetnQkkU5QJU6SBYp4dcRzjPm2znEGI4k92AUw7wEuTqVAvHFQd2J2n8eCMs72s%2Bxg%2BCknKe5i%2By4S2rFQ2xR7NNZ8gCSS3T7pkVUrB6lz9wyLlC0RMvl0qUJH%2FLYgnDyDW9fbN%2B6j2N9xvgSLeqPp5p1xcgDMrLJKqMRTh6xJpTMYAUN950mNp4GY0dy%2FTRUg5mS6pNhBRgXIzg7BatW8WaKZvUGLb%2Fwuz3fw9aNFNKb2vTIlosPf3otfBB%2Bmb72qW%2Fb726STI5h2n2K%2F3ESBiUmzRsIyFo%2FNZWtOnBnXxohzcXcInHPz7uS82eslz%2BMNYruwcpRNiqgxX4DX7Q4zl2kpED4ZppCFrW7ovSnuMXOxQPw%2Fv3zAY2DMvdEu17jlCKBwv1bHSdrmheeRBNcTvH3Ekoi44V5jdTkOGi8EY8lv7tb1Z3I6cXAKg7ANAKxmDB0MLIYqO%2BdvQfzSs3ASX5j0RVj0tJJA7d9SYyw1DCDqhxcdZCG2U4nThn7ZTT%2BPOr3O5K8Wl9dwBH2xckt11umyOBRbeNcpMoy%2BlJ1%2FtUjbbsjH5%2FCu1iG2rRAgI5MKiE6dYGOqUBT4gl4tC4N0PeJARNsHPkpRvJC9lYcpp4hsw2OmMB1MmxV%2BU%2BKdWTDr9wL69sbqsdsMXoy8M0rbg8AHqmIqrgy1UkJYISEAOVCP1uJybsZKYWF7jB1Xgu6pTpRtOOUnkrwP3ygQXvVeXGjU4n1h%2BALz8UP8kawPrnEKG6dO3g9dDiwdXcRNCjMO2YJeFUdD0797l0mawWr%2BbBZTkDP0KD1mO1YkSI&X-Amz-Signature=fa8a58da5762d168bd2175e8231d23dd9f26fad3e45a9c7711490480a3117e80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.313329c1-373e-43a5-b6e1-cb939d807366.b9748648-8d0b-81de-9e07-0003235c1886)
التحيز العكسي — اتساع منطقة الاستنفاذ وحجب التيار — من الملزمة
---
### 6️⃣ منطقة زينر (Zener Region)
🌱 الدايود العادي يسمح بمرور التيار في التحيز الأمامي فقط ويبدي مقاومة صغيرة له؛ وهو يعمل كـ**صمام أحادي الاتجاه**: يمرّر أمامياً ويمنع عكسياً تماماً.
🌿 **منطقة زينر** هي حالة **متحكم فيها** من التوصيل الكهربائي العكسي — دايود زينر مصمم خصيصاً يمرّر التيار بأمان في التحيز العكسي **دون أن يتلف**.
**رمز دايود زينر:** مشابه لرمز ثنائي الوصلة العادي (طرفان: كاثود وأنود) لكن بانحناءات عند أطراف الخط العمودي.
🌳 **آلية عمل منطقة زينر:**
1. **التطعيم الكثيف (Heavy Doping):** تُصنَّع ثنائيات زينر بإضافة تركيز عالٍ من الشوائب إلى مادة السيليكون
2. **منطقة استنفاذ ضيقة:** التطعيم الكثيف يكوّن منطقة استنفاذ رقيقة للغاية عند وصلة PN
3. **التأين بالمجال (Field Ionization — كسر الروابط):** عندما يصل الجهد العكسي إلى $`V_Z`$ (عادةً أقل من 5V) ← ينشأ مجال كهربائي شديد عبر الطبقة الضيقة ← يكسر الروابط التساهمية مباشرة ← تحرير أعداد هائلة من أزواج إلكترون-فجوة في آن واحد لنقل التيار العكسي
---
### 7️⃣ منحنى خصائص الدايود I-V
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/b782bbbd-ef89-4639-8a43-71912d03bac0/l2-iv-curve.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKI4ZZRU%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEN9fqdOci2ZftG6bhs95bZGkaef7v1BA4QQq8rYELvnAiEA0RmEkg8TSDtzIl6OI1Mdolxqc45S5tvlruDheLPyUKMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLrxm%2BoR8Mr0Q7Vt2ircA50EzvVGnO6u46f1vbSbG7O6DbNPgLdDL88bMmNP699K4H%2F8b7p9xWtUdk%2F5aetnQkkU5QJU6SBYp4dcRzjPm2znEGI4k92AUw7wEuTqVAvHFQd2J2n8eCMs72s%2Bxg%2BCknKe5i%2By4S2rFQ2xR7NNZ8gCSS3T7pkVUrB6lz9wyLlC0RMvl0qUJH%2FLYgnDyDW9fbN%2B6j2N9xvgSLeqPp5p1xcgDMrLJKqMRTh6xJpTMYAUN950mNp4GY0dy%2FTRUg5mS6pNhBRgXIzg7BatW8WaKZvUGLb%2Fwuz3fw9aNFNKb2vTIlosPf3otfBB%2Bmb72qW%2Fb726STI5h2n2K%2F3ESBiUmzRsIyFo%2FNZWtOnBnXxohzcXcInHPz7uS82eslz%2BMNYruwcpRNiqgxX4DX7Q4zl2kpED4ZppCFrW7ovSnuMXOxQPw%2Fv3zAY2DMvdEu17jlCKBwv1bHSdrmheeRBNcTvH3Ekoi44V5jdTkOGi8EY8lv7tb1Z3I6cXAKg7ANAKxmDB0MLIYqO%2BdvQfzSs3ASX5j0RVj0tJJA7d9SYyw1DCDqhxcdZCG2U4nThn7ZTT%2BPOr3O5K8Wl9dwBH2xckt11umyOBRbeNcpMoy%2BlJ1%2FtUjbbsjH5%2FCu1iG2rRAgI5MKiE6dYGOqUBT4gl4tC4N0PeJARNsHPkpRvJC9lYcpp4hsw2OmMB1MmxV%2BU%2BKdWTDr9wL69sbqsdsMXoy8M0rbg8AHqmIqrgy1UkJYISEAOVCP1uJybsZKYWF7jB1Xgu6pTpRtOOUnkrwP3ygQXvVeXGjU4n1h%2BALz8UP8kawPrnEKG6dO3g9dDiwdXcRNCjMO2YJeFUdD0797l0mawWr%2BbBZTkDP0KD1mO1YkSI&X-Amz-Signature=7f250b6d866f1c4850fdc92590d82d590a79c375d1cc020b467ff0e3fbd492c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.e81b4d55-a64b-4f95-b213-5f3de5135a97.b9748648-8d0b-81de-9e07-0003235c1886)
منحنى خصائص الجهد والتيار I-V للدايود — من الملزمة
يوضح المنحنى:
- **توصيل عالٍ في التحيز الأمامي** بعد تجاوز جهد العتبة
- **حجب التيار في التحيز العكسي** حتى الوصول لنقطة الانهيار (الركبة Knee)
- الفرق الجوهري بين **انهيار زينر** (يحدث عند جهود عكسية أقل بسبب التطعيم الكثيف) و**الانهيار الإنهيماري Avalanche** (يحدث عند جهود عكسية أعلى بسبب تسارع حاملات الشحنة وتأين التصادم)
---
## 📊 الجداول المقارنة
### ⚖️ التحيز الأمامي vs التحيز العكسي
<table header-row="true">
<tr color="yellow_bg">
<td>**المعيار**</td>
<td>**تحيز أمامي (**$`V_D > 0`$**)**</td>
<td>**تحيز عكسي (**$`V_D < 0`$**)**</td>
</tr>
<tr>
<td>توصيل البطارية</td>
<td>الموجب ← P والسالب ← N</td>
<td>الموجب ← N والسالب ← P</td>
</tr>
<tr>
<td>تيار الأغلبية</td>
<td>يسري بعد تجاوز $`V_\gamma`$</td>
<td>محجوب تماماً</td>
</tr>
<tr>
<td>التيار الفعلي</td>
<td>أسّي $`I_D`$ كبير</td>
<td>تسرب ضئيل $`I_S`$ بحدود nA</td>
</tr>
<tr>
<td>المقاومة</td>
<td>$`r_d`$ منخفضة جداً</td>
<td>$`R_R`$ عالية للغاية</td>
</tr>
<tr>
<td>منطقة الاستنفاذ</td>
<td>تضيق وتنهار</td>
<td>تتسع</td>
</tr>
<tr>
<td>السلوك المكافئ</td>
<td>مفتاح مغلق (موصل)</td>
<td>مفتاح مفتوح (عازل)</td>
</tr>
</table>
### ⚖️ انهيار زينر vs الانهيار الإنهيماري
<table header-row="true">
<tr color="purple_bg">
<td>**المعيار**</td>
<td>**انهيار زينر**</td>
<td>**الانهيار الإنهيماري (Avalanche)**</td>
</tr>
<tr>
<td>الجهد العكسي</td>
<td>أقل (عادة $`V_Z < 5`$V)</td>
<td>أعلى</td>
</tr>
<tr>
<td>السبب</td>
<td>تطعيم كثيف ← مجال شديد يكسر الروابط التساهمية مباشرة</td>
<td>تسارع حاملات الشحنة وتأين التصادم</td>
</tr>
</table>
### ⚖️ أنواع الثنائيات وتطبيقاتها (من المحاضرة)
<table header-row="true">
<tr color="blue_bg">
<td>**النوع**</td>
<td>**التطبيق**</td>
</tr>
<tr>
<td>تقويم Rectifier</td>
<td>تحويل AC إلى DC في وحدات التغذية</td>
</tr>
<tr>
<td>زينر Zener</td>
<td>تثبيت الجهد + جهود مرجعية دقيقة</td>
</tr>
<tr>
<td>إشارة Signal</td>
<td>كشف التضمين، القص، الحد، استعادة DC</td>
</tr>
<tr>
<td>حماية</td>
<td>حماية من القطبية المعكوسة ونبضات الجهد داخل الدوائر المتكاملة</td>
</tr>
</table>
---
## 🗺️ الخريطة الذهنية
<details color="green_bg">
<summary>🔌 الدايود — المحور المركزي</summary>
	<details color="gray_bg">
	<summary>🧱 البناء — وصلة PN</summary>
		- انتشار إلكترونات N ← P
		- أيونات ثابتة (+ في N / − في P) ← منطقة استنفاذ
		- مجال داخلي ← اتزان ديناميكي ← جهد حاجز $`V_\gamma`$ = 0.7V سيليكون / 0.3V جرمانيوم
	</details>
	<details color="gray_bg">
	<summary>🔋 حالات التحيز</summary>
		- لا تحيز: $`V_D = 0`$
		- أمامي $`V_D > 0`$: استنفاذ يضيق ← تيار أسّي ← مفتاح مغلق
		- عكسي $`V_D < 0`$: استنفاذ يتسع ← $`I_S`$ بحدود nA ← مفتاح مفتوح
	</details>
	<details color="gray_bg">
	<summary>⚡ منطقة زينر</summary>
		- تطعيم كثيف ← استنفاذ ضيق جداً
		- عند $`V_Z`$: تأين بالمجال ← كسر روابط جماعي ← توصيل عكسي آمن
		- زينر (جهد أقل) ≠ أفلانش (جهد أعلى + تأين تصادمي)
	</details>
	<details color="gray_bg">
	<summary>🛠️ التطبيقات</summary>
		- تقويم AC إلى DC • تثبيت جهد • حماية قطبية معكوسة • معالجة إشارات • حماية ICs
	</details>
</details>
---
## ❓ أسئلة متوقعة
1. اذكر أربعة تطبيقات للثنائيات مع وظيفة كل منها.
2. اشرح بالتفصيل كيف تتشكل منطقة الاستنفاذ عند وصلة PN في حالة الاتزان.
3. ما هو جهد الحاجز؟ وما قيمته للسيليكون والجرمانيوم؟ وكيف ينشأ؟
4. عرّف التحيز، وعدّد حالاته الثلاث مع شرط كل حالة.
5. قارن بين التحيز الأمامي والعكسي من حيث: التيار، المقاومة، منطقة الاستنفاذ، والسلوك كمفتاح.
6. ما تيار التشبع العكسي $`I_S`$؟ وما مصدره الفيزيائي؟ وبأي وحدة يقاس للسيليكون؟
7. اشرح آلية عمل منطقة زينر (التطعيم الكثيف ← الاستنفاذ الضيق ← التأين بالمجال).
8. قارن بين انهيار زينر والانهيار الإنهيماري من حيث الجهد والآلية.