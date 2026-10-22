---
title: 'عملي 1: خصائص الدايود — Exp 1: Diode Characteristics'
---

<callout icon="🔬" color="blue_bg">
	**التجربة الأولى — مختبر**
	Exp 1: Diode Characteristics — دراسة خصائص الدايود وظروف التحيز
	*د. أكرم محمد حاتم + م. زهراء عبد المهدي + م. عقيل علي*
</callout>
## 📑 فهرس التجربة
1. الهدف والأجهزة
2. النظرية: بنية الدايود ورمزه
3. التحيز الأمامي (Forward Bias)
4. التحيز العكسي (Reverse Bias)
5. الدائرة المكافئة للدايود — النموذج الكامل
6. التطبيق العملي
---
## 📝 الشرح التفصيلي
### 1️⃣ الهدف والأجهزة
🎯 **الهدف:** دراسة خصائص الدايود وظروف التحيز (Biasing Conditions).
🛠️ **الأجهزة:**
- مصدر طاقة تيار مستمر (DC Power Supply)
- أجهزة قياس (فولتميتر وأميتر)
- مقاومات
- أسلاك توصيل ولوحة تجارب (Breadboard)
---
### 2️⃣ النظرية: بنية الدايود ورمزه
🌱 الدايود جهاز شبه موصل يسمح بمرور التيار **باتجاه واحد فقط**. يتكون من قطعة سيليكون يُطعَّم أحد جزأيها بشوائب **ثلاثية التكافؤ** لتكوين منطقة p، والجزء الآخر بشوائب **خماسية التكافؤ** لتكوين منطقة n. الحد الفاصل بينهما = **وصلة p-n**، والتطعيم هو إضافة شوائب لزيادة عدد حاملات الشحنة (إلكترونات أو فجوات).
🌿 **البنية والرمز:**
- الجزء p يُسمى **المصعد / الأنود (Anode — A)**
- الجزء n يُسمى **المهبط / الكاثود (Cathode — K)**
- السهم في الرمز يشير إلى اتجاه **التيار الاصطلاحي** (المعاكس لتدفق الإلكترونات)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/b1f67c64-fa63-4937-9b80-24006092ae61/p1-diode.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWAUNLM6%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm9rZSzZqCX3A2496aw3Ru1cipD9L7dtzT0aK8eT%2B3UwIhAMlS91Bdtw7HnfdSRaT8tA%2Fii%2FcF5IT6ExpydeKr5HNxKv8DCHoQABoMNjM3NDIzMTgzODA1IgwKhJdFzb5UE5Ffm9Iq3AMG2lnvaf1bqRzJz2JJ74WQcy%2B4OifNhhOn5li%2B3eKAv4gn8aJr3bOGFHdXSBXrbJyWFRYNtzaQ3%2BcVwD%2FjwiwDVbWoki9XXOdP6Ayv780Yx6QmsYiJXeyrQ7f3BZRiYpZmoIl75otTvq45HNgoawphk9AjP6NFYNznj5DAKdD7UEykzcMz1qrlI8aCAyi59mdWyii68P4ZKiTiTzKjdY7%2BgMTorgvtaniwyfKSqSs4Cj5W95TsY90zB%2FexKfYyUwuK42l2rdnoOSYBME%2FcGVN0BdVhn6Un9Ns3F9snPADPPLsD0TcuuYYiNDZWrUnEUT18%2BEerrAeC6kFTXf4tkuKljgoLEbxg1AZD%2BPTD2i%2BG8s0tUCJtxrFBZ8xjQMjsjsWf0BpNCTRcYptLHLQI8YcQH04%2FXQ85DDswGVzVMyxH1hNdaB6qdoI0KrtWjPXrK4jHvcWh8UE5stiN8dm5A94%2BiZFZN%2F1nrhoW6DLb8w5EFehzV65F4SrwntmXbeJd8TPaBcPJrfVuppgNTFOHH3XZIaghvFqeu%2F6KCozdBdA1OikoNdtpVSjn3uBX0PNdx%2FBXJ42deOEikY0Qbeq1abzBaxvHL501T%2BZl%2FxUnA5QwqxGpHf3bczmS6K6HzjDPhunWBjqkARQECAzqXr%2Bjadrn3QXOlRM%2BRtbVO%2Fy6AtDcKXK6AzI%2FKhkqVgRSakOg9Flmcre6tZcC6OKo2TUsObboKi4eY1F7n0kzHKHsl%2FMLmG%2FztfWaIlwgazzn%2FwH9qRzTFK7QvjIEpsLJKZceVdDFaotE1Dh1ucQuoES4BymCF24wRSlcXjGm02wpJlFYhHKD1QPUsGyIZ3W53081mBCivDcyAsqa%2BEg9&X-Amz-Signature=9ed062431d0eb8dbdfbbf36dce807df59328654984d2928e30886aa03a78741a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.c054b41a-f5ab-45b4-9524-c6462590b463.b9748648-8d0b-81de-9e07-0003235c1886)
رمز الدايود وبنيته — من ملزمة التجربة
---
### 3️⃣ التحيز الأمامي (Forward Bias)
🌱 مصطلح "التحيز/الإزاحة" يعني تطبيق جهد DC لتهيئة ظروف تشغيل محددة لجهاز إلكتروني.
🌿 التحيز الأمامي يسمح بمرور التيار عبر وصلة p-n، ويتحقق بتوصيل:
- **الطرف الموجب** لمصدر $`V_{BIAS}`$ ← منطقة p (الأنود)
- **الطرف السالب** ← منطقة n (الكاثود)
🌳 شرط التوصيل: يجب أن تتجاوز قيمة $`V_{BIAS}`$ جهد الحاجز (**0.7 فولت للسيليكون** و **0.3 فولت للجرمانيوم**). وتُضاف دائماً **مقاومة على التوالي (R)** للحد من التيار الأمامي وحماية الدايود من التلف الحراري.
---
### 4️⃣ التحيز العكسي (Reverse Bias)
🌿 التحيز العكسي هو الحالة التي تمنع مرور التيار عبر الدايود بشكل أساسي، وتتحقق بتوصيل:
- **الطرف الموجب** لـ $`V_{BIAS}`$ ← المنطقة السالبة n (الكاثود)
- **الطرف السالب** ← المنطقة الموجبة p (الأنود)
🌳 في هذه الحالة: الجهد المطبق **يسحب حاملات الشحنة السائدة بعيداً عن الوصلة** ← تتسع منطقة الاستنفاذ ← يعمل الدايود كـ**مفتاح مفتوح**، ولا يسمح إلا بمرور تيار تسرب ضئيل جداً (يتراوح بين nA و µA).
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/0a7553f0-3404-4feb-98af-08d600c04f54/p1-bias.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWAUNLM6%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm9rZSzZqCX3A2496aw3Ru1cipD9L7dtzT0aK8eT%2B3UwIhAMlS91Bdtw7HnfdSRaT8tA%2Fii%2FcF5IT6ExpydeKr5HNxKv8DCHoQABoMNjM3NDIzMTgzODA1IgwKhJdFzb5UE5Ffm9Iq3AMG2lnvaf1bqRzJz2JJ74WQcy%2B4OifNhhOn5li%2B3eKAv4gn8aJr3bOGFHdXSBXrbJyWFRYNtzaQ3%2BcVwD%2FjwiwDVbWoki9XXOdP6Ayv780Yx6QmsYiJXeyrQ7f3BZRiYpZmoIl75otTvq45HNgoawphk9AjP6NFYNznj5DAKdD7UEykzcMz1qrlI8aCAyi59mdWyii68P4ZKiTiTzKjdY7%2BgMTorgvtaniwyfKSqSs4Cj5W95TsY90zB%2FexKfYyUwuK42l2rdnoOSYBME%2FcGVN0BdVhn6Un9Ns3F9snPADPPLsD0TcuuYYiNDZWrUnEUT18%2BEerrAeC6kFTXf4tkuKljgoLEbxg1AZD%2BPTD2i%2BG8s0tUCJtxrFBZ8xjQMjsjsWf0BpNCTRcYptLHLQI8YcQH04%2FXQ85DDswGVzVMyxH1hNdaB6qdoI0KrtWjPXrK4jHvcWh8UE5stiN8dm5A94%2BiZFZN%2F1nrhoW6DLb8w5EFehzV65F4SrwntmXbeJd8TPaBcPJrfVuppgNTFOHH3XZIaghvFqeu%2F6KCozdBdA1OikoNdtpVSjn3uBX0PNdx%2FBXJ42deOEikY0Qbeq1abzBaxvHL501T%2BZl%2FxUnA5QwqxGpHf3bczmS6K6HzjDPhunWBjqkARQECAzqXr%2Bjadrn3QXOlRM%2BRtbVO%2Fy6AtDcKXK6AzI%2FKhkqVgRSakOg9Flmcre6tZcC6OKo2TUsObboKi4eY1F7n0kzHKHsl%2FMLmG%2FztfWaIlwgazzn%2FwH9qRzTFK7QvjIEpsLJKZceVdDFaotE1Dh1ucQuoES4BymCF24wRSlcXjGm02wpJlFYhHKD1QPUsGyIZ3W53081mBCivDcyAsqa%2BEg9&X-Amz-Signature=76aad6483dbdedd1d874dc9268b1cca85818ef8f09ae355fbb5304cccbfdd990&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.ed72b11d-6dc2-41bf-8ef0-be8f731ffd41.b9748648-8d0b-81de-9e07-0003235c1886)
دوائر التحيز الأمامي والعكسي — من ملزمة التجربة
---
### 5️⃣ الدائرة المكافئة للدايود — النموذج الكامل (Complete Model)
🌳 في الدوائر العملية يُستخدم النموذج الكامل للتحليل الدقيق؛ إذ يأخذ بالاعتبار: **جهد الحاجز** + **المقاومة الديناميكية** + **المقاومة الداخلية للتحيز العكسي**:
- **حالة التحيز الأمامي:** يُمثَّل الدايود بمفتاح مغلق موصول على التوالي مع مصدر جهد يمثل جهد الحاجز (0.7 فولت) ومقاومة ديناميكية أمامية صغيرة ($`r'_d`$)
- **حالة التحيز العكسي:** يُمثَّل الدايود بمفتاح مفتوح موصول على التوازي مع مقاومة عكسية عالية جداً ($`r'_R`$) تسمح بمرور تيار تسرب عكسي ضئيل للغاية ($`I_R`$)
---
### 6️⃣ التطبيق العملي
<callout icon="💻" color="purple_bg">
	الصفحة الأخيرة من المحاضرة تحتوي تطبيقاً عملياً لدائرة كهربائية تحتوي على دايود بنوعي التحيز (أمامي وعكسي) على برنامج **NI Multisim** — يُرجى الاطلاع عليها في الملزمة الأساسية
</callout>
---
## 📊 الجداول المقارنة
### ⚖️ التحيز الأمامي vs العكسي في التجربة
<table header-row="true">
<tr color="green_bg">
<td>**المعيار**</td>
<td>**أمامي Forward**</td>
<td>**عكسي Reverse**</td>
</tr>
<tr>
<td>توصيل $`V_{BIAS}`$</td>
<td>الموجب ← p (أنود) / السالب ← n (كاثود)</td>
<td>الموجب ← n (كاثود) / السالب ← p (أنود)</td>
</tr>
<tr>
<td>الشرط</td>
<td>$`V_{BIAS}`$ \> جهد الحاجز (0.7V Si / 0.3V Ge)</td>
<td>—</td>
</tr>
<tr>
<td>منطقة الاستنفاذ</td>
<td>تضيق</td>
<td>تتسع</td>
</tr>
<tr>
<td>التيار</td>
<td>يسري (مع مقاومة توالٍ حامية R)</td>
<td>تسرب ضئيل nA ← µA</td>
</tr>
<tr>
<td>النموذج المكافئ</td>
<td>مفتاح مغلق + 0.7V + $`r'_d`$ على التوالي</td>
<td>مفتاح مفتوح ∥ $`r'_R`$ عالية جداً</td>
</tr>
</table>
---
## 🗺️ الخريطة الذهنية
<details color="blue_bg">
<summary>🔬 Exp 1 — خصائص الدايود</summary>
	<details color="gray_bg">
	<summary>🧱 البنية</summary>
		- سيليكون: جزء ثلاثي التطعيم = p ← وجزء خماسي = n
		- الحد الفاصل = وصلة p-n
		- الرمز: أنود A (سهم باتجاه التيار الاصطلاحي) / كاثود K
	</details>
	<details color="gray_bg">
	<summary>🔋 التحيز</summary>
		- أمامي: موجب←p وسالب←n ← تجاوز 0.7V ← يوصّل (مقاومة حماية R)
		- عكسي: موجب←n وسالب←p ← استنفاذ يتسع ← يحجب (تسرب nA–µA)
	</details>
	<details color="gray_bg">
	<summary>⚙️ النموذج الكامل</summary>
		- أمامي = مفتاح مغلق + 0.7V + $`r'_d`$
		- عكسي = مفتاح مفتوح ∥ $`r'_R`$ + تسرب $`I_R`$
	</details>
</details>
---
## ❓ أسئلة متوقعة
1. ما هدف التجربة؟ واذكر الأجهزة الأربعة المستخدمة فيها.
2. كيف يتكون الدايود من قطعة سيليكون واحدة؟ وما المقصود بالتطعيم؟
3. في رمز الدايود: أي جزء هو الأنود وأيها الكاثود؟ وبأي اتجاه يشير السهم؟
4. اشرح كيف يتحقق التحيز الأمامي، وما شرط التوصيل، ولماذا تُضاف مقاومة على التوالي؟
5. اشرح ما يحدث لمنطقة الاستنفاذ في التحيز العكسي، وما مقدار تيار التسرب؟
6. ارسم/اوصف النموذج الكامل للدايود في حالتي التحيز الأمامي والعكسي.