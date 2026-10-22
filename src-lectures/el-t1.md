---
title: 'المحاضرة 1 نظري: أشباه الموصلات ومستويات الطاقة — Semiconductors & Energy Levels'
---

<callout icon="📘" color="blue_bg">
	**المحاضرة الأولى — نظري**
	Introduction, Semiconductor Materials, Energy Levels, n- and p-Type Extrinsic Materials
	*د. أكرم محمد حاتم — المرحلة الثانية*
</callout>
## 📑 فهرس المحاضرة
1. المقدمة — الإلكترونيات والأمن السيبراني
2. المواد شبه الموصلة — التصنيف الثلاثي
3. مستويات الطاقة وحزم الطاقة
4. المواد المشوبة: n-Type و p-Type
5. أهمية فيزياء أشباه الموصلات في الأمن السيبراني
---
## 📝 الشرح التفصيلي
### 1️⃣ المقدمة
🌱 **الأساس:** الإلكترونيات هي الطبقة المادية الأساسية (Hardware Layer) لبنية الأمن السيبراني الحديثة، وفي صميمها تكمن **فيزياء أشباه الموصلات** — دراسة مواد يمكن التحكم بخصائصها الكهربائية بدقة لتصنيع مكونات جوهرية: الثنائيات (Diodes)، الترانزستورات، والدوائر المتكاملة (ICs).
🌿 **الربط:** لمختص الأمن السيبراني، فهم هذه المكونات على المستوى المادي بالغ الأهمية — الثغرات المرتبطة بالعتاد، هجمات القنوات الجانبية، وتقنيات التشفير القائمة على السيليكون تعتمد كلها بشكل مباشر على سلوك أشباه الموصلات.
🌳 **الخلاصة:** الإلمام بأساسيات الإلكترونيات حيوي لتأمين الأنظمة بدءاً من الطبقة المادية وصولاً إلى المستويات العليا.
---
### 2️⃣ المواد شبه الموصلة
🌱 في فيزياء الحالة الصلبة تُصنَّف المواد إلى ثلاث فئات حسب قدرتها على توصيل الكهرباء:
- **الموصلات** (النحاس، الألمنيوم): موصلية كهربائية عالية بسبب وفرة الإلكترونات الحرة
- **العوازل** (الزجاج، المطاط): تقاوم سريان التيار بشدة بسبب الارتباط القوي لإلكترونات التكافؤ
- **أشباه الموصلات** (السيليكون Si، الجرمانيوم Ge، زرنيخيد الغاليوم GaAs): مستويات توصيل تقع بين الموصلات والعوازل
🌿 في حالتها النقية — **أشباه الموصلات الذاتية (Intrinsic)** — تكون موصليتها منخفضة نسبياً عند درجة حرارة الغرفة.
🌳 خصائصها المميزة: **الحساسية لتغيرات درجة الحرارة**، وقدرتها على **زيادة الموصلية بشكل كبير** عند خلطها بكميات ضئيلة من شوائب محددة.
---
### 3️⃣ مستويات الطاقة وحزم الطاقة
🌱 الإلكترونات داخل الذرة المعزولة تشغل **مستويات طاقة محددة ومنفصلة**؛ وعندما تتحد الذرات لتشكّل شبكة بلورية صلبة، تتسع هذه المستويات لتصبح **حزماً من الطاقة** — وهذا جوهر نظرية حزم الطاقة.
🌿 الحزم الثلاث:
1. **حزمة التكافؤ (Valence Band):** أعلى نطاق لطاقات الإلكترونات التي تتواجد فيها عادةً عند درجة حرارة الصفر المطلق (0 كلفن)
2. **حزمة التوصيل (Conduction Band):** نطاق مستويات الطاقة الذي يعلو حزمة التكافؤ؛ الإلكترونات فيه حرة الحركة داخل المادة وتساهم في التوصيل الكهربائي
3. **فجوة الطاقة (**$`E_g`$** — الفجوة الممنوعة):** فرق الطاقة بين قمة حزمة التكافؤ وقاع حزمة التوصيل
🌳 قيمة الفجوة تحدد سلوك المادة:
- **الموصلات:** الحزمتان متداخلتان ($`E_g \approx 0`$ eV)
- **العوازل:** فجوة واسعة جداً ($`E_g > 5`$ eV) تمنع الإلكترونات من الانتقال في الظروف العادية
- **أشباه الموصلات:** فجوة صغيرة نسبياً — السيليكون $`E_g \approx 1.1`$ eV والجرمانيوم $`E_g \approx 0.67`$ eV عند درجة حرارة الغرفة
الطاقة الحرارية عند درجة حرارة الغرفة تسمح لعدد قليل من إلكترونات التكافؤ بعبور الفجوة إلى حزمة التوصيل → تتولد **إلكترونات حرة** وتُترك خلفها فراغات موجبة الشحنة تُسمى **الفجوات (Holes)**.
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/53cfd98f-d9bc-4ed3-bf2a-3c0f61aa794a/l1-energy-bands.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRHLTJCL%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXC52%2BLWii08QUQvwqQ5Y8IWpyf8B8gS%2FwqO9ReL4yzQIhALlgxVFYBG4cTZNfZ%2BkLrCpZt2AXEmskQzEbFbQCdylKKv8DCHoQABoMNjM3NDIzMTgzODA1IgyzpuZ6P4e1T4Jbq9Eq3APUOoemjOFpNuO0mXadwm3mQ%2FatjmFaRtkNlQRuztalu1nXdqmf16SC9dYAuKaiotOl2JLTLqU4vkWdd%2BAdevUZWRPtmOX7xbPtpM1yY7UTuEAzgqTe6rqOF833iX%2FKh6lsElpWfZ8HN%2BrRj1LhKcjRb3zulbVPnV%2FkpdKhqVNM%2F4Yiy3dU1NcuPuvLA%2B27DAOdCxT3R%2B%2F24a%2BUY4fOG6vv5BcFr953nKxZYRG6V%2B2mKAyFSCvMd26EjrpWY4b7GiJnvAWmU0FPyc4b2k3AudbqlX1FS4XV8%2Fkx5k%2F0Rl0Q6VcWp5vatGVifbYqbf1ZP0Ad7M6UuHD7yjv0MdJChdp%2Bewd3ExZsUxOBWtgORvE9KSuGbFNzfNW08jRvokCmNsC7L6%2F11KjeYRDDyGgIK3YNPHEP0PpPmqOGZTvfWPPLQk4hqrgJJoM0v5oHD1SXMznwPMiSgSSG%2Bw8obJPfzi4T9na25YrPvvbCBDxhkDgklnyntGyJiuj29pUfTLPuqIKWIlrb0PjC6q99LBMd377oSIutYGnAyW0MbLZ4Z%2FT7DmK6n%2BYwQxIxiMOjnyCxOkquwpoVc2%2FyXpv9ESIoeKxTElV1PtyFJ55BKrD4ZJA5ibFjqfyID9iKjsX0GDDchOnWBjqkAZ4Km%2BQP0VD%2BNJdGEH0b0nDWVpoToXSbMq8sKQRHjIFDpMQiEloWCgAITyDytAPq4X4oTPSqWDPwOm%2F1BsQy9rP8YWq8XkbTIAx2EPCEqV8mkiKL%2B5%2FjTckmMzx4Ggz2QD%2FenHt2fc%2F5PXkWsw5k6wFB53mi7QbTgLSATH4NSAgiNYroCCcY7ZvH01k2R7QAigTOdUFfnxAPG%2Ba%2BgWw4UQ59DGDZ&X-Amz-Signature=afce469a6504fc08e6fd3ce54e094d10309ed5199170aa0dc4a60b0dbc5292f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.de003ca3-10a4-4326-809c-3a7a0cdeeaa6.b9748648-8d0b-81de-9e07-0003235c1886)
حزم الطاقة في العازل وشبه الموصل والمعدن — من ملزمة المحاضرة
---
### 4️⃣ المواد المشوبة (Extrinsic): النوع السالب n-Type والنوع الموجب p-Type
🌱 أشباه الموصلات النقية تطبيقاتها العملية محدودة لأن موصليتها منخفضة وتعتمد بشدة على الحرارة → الحل: **التطعيم (Doping)** — إدخال متعمد لذرات شوائب محددة في البنية البلورية. الناتج يُسمى **مواد غير ذاتية (Extrinsic Materials)** وتنقسم لفئتين رئيسيتين.
#### 🔵 أشباه الموصلات n-Type (النوع السالب)
🌱 **التكوين:**
- تطعيم السيليكون أو الجرمانيوم النقي بذرات **خماسية التكافؤ** (تمتلك 5 إلكترونات تكافؤ): الفسفور، الزرنيخ، الأنتيمون
- أربعة من إلكترونات تكافؤ الشائبة تكوّن روابط تساهمية مع ذرات السيليكون المجاورة، بينما **الإلكترون الخامس** يبقى مرتبطاً بضعف → يتحول بسهولة إلى إلكترون حر في حزمة التوصيل
- لأن هذه الشوائب **تمنح** إلكترونات حرة → تُسمى **شوائب مانحة (Donor Impurities)**
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/efe76e74-7181-4ab0-8a46-39ecbc1ce1db/l1-ntype.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRHLTJCL%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXC52%2BLWii08QUQvwqQ5Y8IWpyf8B8gS%2FwqO9ReL4yzQIhALlgxVFYBG4cTZNfZ%2BkLrCpZt2AXEmskQzEbFbQCdylKKv8DCHoQABoMNjM3NDIzMTgzODA1IgyzpuZ6P4e1T4Jbq9Eq3APUOoemjOFpNuO0mXadwm3mQ%2FatjmFaRtkNlQRuztalu1nXdqmf16SC9dYAuKaiotOl2JLTLqU4vkWdd%2BAdevUZWRPtmOX7xbPtpM1yY7UTuEAzgqTe6rqOF833iX%2FKh6lsElpWfZ8HN%2BrRj1LhKcjRb3zulbVPnV%2FkpdKhqVNM%2F4Yiy3dU1NcuPuvLA%2B27DAOdCxT3R%2B%2F24a%2BUY4fOG6vv5BcFr953nKxZYRG6V%2B2mKAyFSCvMd26EjrpWY4b7GiJnvAWmU0FPyc4b2k3AudbqlX1FS4XV8%2Fkx5k%2F0Rl0Q6VcWp5vatGVifbYqbf1ZP0Ad7M6UuHD7yjv0MdJChdp%2Bewd3ExZsUxOBWtgORvE9KSuGbFNzfNW08jRvokCmNsC7L6%2F11KjeYRDDyGgIK3YNPHEP0PpPmqOGZTvfWPPLQk4hqrgJJoM0v5oHD1SXMznwPMiSgSSG%2Bw8obJPfzi4T9na25YrPvvbCBDxhkDgklnyntGyJiuj29pUfTLPuqIKWIlrb0PjC6q99LBMd377oSIutYGnAyW0MbLZ4Z%2FT7DmK6n%2BYwQxIxiMOjnyCxOkquwpoVc2%2FyXpv9ESIoeKxTElV1PtyFJ55BKrD4ZJA5ibFjqfyID9iKjsX0GDDchOnWBjqkAZ4Km%2BQP0VD%2BNJdGEH0b0nDWVpoToXSbMq8sKQRHjIFDpMQiEloWCgAITyDytAPq4X4oTPSqWDPwOm%2F1BsQy9rP8YWq8XkbTIAx2EPCEqV8mkiKL%2B5%2FjTckmMzx4Ggz2QD%2FenHt2fc%2F5PXkWsw5k6wFB53mi7QbTgLSATH4NSAgiNYroCCcY7ZvH01k2R7QAigTOdUFfnxAPG%2Ba%2BgWw4UQ59DGDZ&X-Amz-Signature=ebbd7d380d5cc44dacc55f027a2f06f3caad28f5c2ecea898e0589ae787375f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.988edc14-9739-4bb3-9b67-133665041dab.b9748648-8d0b-81de-9e07-0003235c1886)
شبكة سيليكون مطعّمة بذرة أنتيمون (Sb) — الإلكترون الخامس حر — من الملزمة
🌿 **التوصيل عند تطبيق جهد خارجي:**
- الإلكترونات الحرة تتحرك نحو **القطب الموجب**
- تدفق الإلكترونات يشكّل التيار الكهربائي
- التوصيل يحدث رئيسياً بالإلكترونات؛ ونظراً لتركيزها المرتفع جداً → **تيار الإلكترونات يسود** على تيار الفجوات
- الإلكترونات = حاملات الشحنة السائدة (الأغلبية)؛ الفجوات = حاملات الأقلية
🌳 **المعادلة والخصائص:**
$$
\sigma = q\,(n\mu_n + p\mu_p)
$$
حيث $`n \gg p`$ في النوع السالب. الرموز: $`\sigma`$ الموصلية، $`q`$ شحنة الإلكترون، $`n`$ تركيز الإلكترونات، $`p`$ تركيز الفجوات، $`\mu_n`$ و $`\mu_p`$ قابلية حركة الإلكترونات والفجوات.
**المزايا:** موصلية عالية لكثرة الإلكترونات الحرة • الإلكترونات أسرع من الفجوات ← تدفق تيار أفضل • تحتاج طاقة أقل للتوصيل • أداء أفضل عند درجات الحرارة المنخفضة • مناسبة للأجهزة الإلكترونية عالية السرعة • مقاومة أقل مقارنة بأشباه الموصلات الذاتية
**الخصائص:** تركيز إلكترونات عالٍ • تركيز فجوات منخفض • التوصيل رئيسياً بالإلكترونات • تحتوي ذرات شوائب مانحة • **محايدة كهربائياً بشكل إجمالي** • مقاومية أقل من شبه الموصل الذاتي
#### 🔴 أشباه الموصلات p-Type (النوع الموجب)
🌱 **التكوين:**
- تطعيم بذرات **ثلاثية التكافؤ** (3 إلكترونات تكافؤ): البورون، الغاليوم، الإنديوم
- الإلكترونات الثلاثة تكوّن روابط تساهمية مع ثلاث ذرات سيليكون مجاورة → **نقص إلكترون واحد في الرابطة الرابعة** → فراغ موجب يُعرف بـ**الفجوة (Hole)**
- لأن هذه الشوائب **تقبل** إلكترونات من الروابط المجاورة → تُسمى **شوائب قابلة (Acceptor Impurities)**
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/b9748648-8d0b-81de-9e07-0003235c1886/45563785-038b-471f-b54e-379be40173bf/l1-ptype.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRHLTJCL%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T193642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXC52%2BLWii08QUQvwqQ5Y8IWpyf8B8gS%2FwqO9ReL4yzQIhALlgxVFYBG4cTZNfZ%2BkLrCpZt2AXEmskQzEbFbQCdylKKv8DCHoQABoMNjM3NDIzMTgzODA1IgyzpuZ6P4e1T4Jbq9Eq3APUOoemjOFpNuO0mXadwm3mQ%2FatjmFaRtkNlQRuztalu1nXdqmf16SC9dYAuKaiotOl2JLTLqU4vkWdd%2BAdevUZWRPtmOX7xbPtpM1yY7UTuEAzgqTe6rqOF833iX%2FKh6lsElpWfZ8HN%2BrRj1LhKcjRb3zulbVPnV%2FkpdKhqVNM%2F4Yiy3dU1NcuPuvLA%2B27DAOdCxT3R%2B%2F24a%2BUY4fOG6vv5BcFr953nKxZYRG6V%2B2mKAyFSCvMd26EjrpWY4b7GiJnvAWmU0FPyc4b2k3AudbqlX1FS4XV8%2Fkx5k%2F0Rl0Q6VcWp5vatGVifbYqbf1ZP0Ad7M6UuHD7yjv0MdJChdp%2Bewd3ExZsUxOBWtgORvE9KSuGbFNzfNW08jRvokCmNsC7L6%2F11KjeYRDDyGgIK3YNPHEP0PpPmqOGZTvfWPPLQk4hqrgJJoM0v5oHD1SXMznwPMiSgSSG%2Bw8obJPfzi4T9na25YrPvvbCBDxhkDgklnyntGyJiuj29pUfTLPuqIKWIlrb0PjC6q99LBMd377oSIutYGnAyW0MbLZ4Z%2FT7DmK6n%2BYwQxIxiMOjnyCxOkquwpoVc2%2FyXpv9ESIoeKxTElV1PtyFJ55BKrD4ZJA5ibFjqfyID9iKjsX0GDDchOnWBjqkAZ4Km%2BQP0VD%2BNJdGEH0b0nDWVpoToXSbMq8sKQRHjIFDpMQiEloWCgAITyDytAPq4X4oTPSqWDPwOm%2F1BsQy9rP8YWq8XkbTIAx2EPCEqV8mkiKL%2B5%2FjTckmMzx4Ggz2QD%2FenHt2fc%2F5PXkWsw5k6wFB53mi7QbTgLSATH4NSAgiNYroCCcY7ZvH01k2R7QAigTOdUFfnxAPG%2Ba%2BgWw4UQ59DGDZ&X-Amz-Signature=01296b3a5735c40b681db5975f6129103c270131526cb419dac61c3d843e19b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.37026608-66d7-4ff4-a8dc-b670356ac9f5.b9748648-8d0b-81de-9e07-0003235c1886)
شبكة سيليكون مطعّمة بذرة إنديوم (In) — فجوة في الرابطة الرابعة — من الملزمة
🌿 **التوصيل عند تطبيق جهد:**
- الفجوات تتحرك نحو **القطب السالب**
- الإلكترونات تتحرك بالاتجاه المعاكس
- **تيار الفجوات يسود** عملية التوصيل
🌳 **المعادلة والخصائص:**
في p-Type حيث $`p \gg n`$ تنطبق:
$$
\sigma \approx q\,p\,\mu_p
$$
**المزايا:** موصلية جيدة بوجود الفجوات كحاملات أغلبية • مفيدة لتشكيل وصلات PN • تحتاج طاقة منخفضة نسبياً لتوصيل الفجوات • دور مهم في التحكم بتدفق التيار • مناسبة للمكبرات ودوائر التبديل • سهولة الدمج مع n-Type لتصنيع مكونات متنوعة
**الخصائص:** تركيز فجوات عالٍ • تركيز إلكترونات منخفض • التوصيل رئيسياً بالفجوات • تحتوي ذرات شوائب قابلة • مقاومية أقل من شبه الموصل الذاتي
🌳 **الصورة الكبرى:** القدرة على إنتاج النوعين عبر التطعيم المتحكم به = حجر الأساس لإلكترونيات الحالة الصلبة الحديثة؛ وبدمج النوعين تتشكل **وصلة p-n** ← الثنائيات، الترانزستورات، الخلايا الشمسية، والمعالجات الدقيقة المتطورة.
---
### 5️⃣ لماذا تهم فيزياء أشباه الموصلات في الأمن السيبراني؟
- **برامج التجسس على العتاد (Hardware Trojans):** يستطيع المهاجمون تعديل تركيز الشوائب (مناطق n أو p) بدقة أثناء تصنيع الرقائق لإنشاء أبواب خلفية مخفية أو تغيير سلوك العتاد دون اكتشافه
- **هجمات القنوات الجانبية (Side-Channel Attacks):** عند انتقال الإلكترونات والفجوات عبر أشباه الموصلات تتولد حرارة وتقلبات في الطاقة؛ يقيس المهاجمون هذه الإشارات الفيزيائية الدقيقة (كاستهلاك الطاقة) لاستخراج مفاتيح التشفير
- **حقن الأعطال الفيزيائية (Physical Fault Injection):** تعريض أشباه الموصلات لأشعة الليزر أو درجات حرارة قصوى يولّد إلكترونات أو فجوات حرة غير متوقعة ← أعطال مؤقتة (glitches) تتجاوز فحوصات الأمان في المعالجات
---
## 📊 الجداول المقارنة
### ⚖️ الموصلات vs العوازل vs أشباه الموصلات
<table header-row="true">
<tr color="blue_bg">
<td>**المعيار**</td>
<td>**الموصلات**</td>
<td>**العوازل**</td>
<td>**أشباه الموصلات**</td>
</tr>
<tr>
<td>أمثلة</td>
<td>نحاس، ألمنيوم</td>
<td>زجاج، مطاط</td>
<td>سيليكون Si، جرمانيوم Ge، GaAs</td>
</tr>
<tr>
<td>السلوك الكهربائي</td>
<td>موصلية عالية</td>
<td>مقاومة شديدة للتيار</td>
<td>توصيل بين الفئتين</td>
</tr>
<tr>
<td>السبب الفيزيائي</td>
<td>وفرة الإلكترونات الحرة</td>
<td>إلكترونات التكافؤ مرتبطة بقوة</td>
<td>فجوة طاقة صغيرة تُعبَر حرارياً</td>
</tr>
<tr>
<td>فجوة الطاقة $`E_g`$</td>
<td>≈ 0 eV (تداخل)</td>
<td>\> 5 eV</td>
<td>Si ≈ 1.1 eV / Ge ≈ 0.67 eV</td>
</tr>
</table>
### ⚖️ n-Type vs p-Type
<table header-row="true">
<tr color="red_bg">
<td>**المعيار**</td>
<td>**n-Type (سالب)**</td>
<td>**p-Type (موجب)**</td>
</tr>
<tr>
<td>الشوائب المستخدمة</td>
<td>خماسية التكافؤ: فسفور، زرنيخ، أنتيمون</td>
<td>ثلاثية التكافؤ: بورون، غاليوم، إنديوم</td>
</tr>
<tr>
<td>نوع الشائبة</td>
<td>مانحة Donor</td>
<td>قابلة Acceptor</td>
</tr>
<tr>
<td>آلية التكوين</td>
<td>الإلكترون الخامس يبقى حراً</td>
<td>نقص إلكترون بالرابطة الرابعة = فجوة</td>
</tr>
<tr>
<td>حاملات الأغلبية</td>
<td>الإلكترونات</td>
<td>الفجوات</td>
</tr>
<tr>
<td>حاملات الأقلية</td>
<td>الفجوات</td>
<td>الإلكترونات</td>
</tr>
<tr>
<td>الحركة عند جهد خارجي</td>
<td>الإلكترونات نحو القطب الموجب</td>
<td>الفجوات نحو القطب السالب</td>
</tr>
<tr>
<td>التيار السائد</td>
<td>تيار الإلكترونات</td>
<td>تيار الفجوات</td>
</tr>
<tr>
<td>العلاقة بين التركيزين</td>
<td>$`n \gg p`$</td>
<td>$`p \gg n`$</td>
</tr>
</table>
---
## 🗺️ الخريطة الذهنية
<details color="purple_bg">
<summary>⚡ أشباه الموصلات — المحور المركزي</summary>
	<details color="gray_bg">
	<summary>🧱 تصنيف المواد</summary>
		- موصلات: نحاس/ألمنيوم — إلكترونات حرة وفيرة — $`E_g \approx 0`$
		- عوازل: زجاج/مطاط — تكافؤ مرتبط بقوة — $`E_g > 5`$ eV
		- أشباه موصلات: Si / Ge / GaAs — فجوة صغيرة (1.1 / 0.67 eV)
	</details>
	<details color="gray_bg">
	<summary>🔋 حزم الطاقة</summary>
		- حزمة التكافؤ ← فجوة الطاقة $`E_g`$ ← حزمة التوصيل
		- الحرارة تعبّر إلكترونات قليلة ← إلكترون حر + فجوة
	</details>
	<details color="gray_bg">
	<summary>🧪 التطعيم Doping</summary>
		- خماسي (P, As, Sb) ← n-Type ← شوائب مانحة ← إلكترونات أغلبية
		- ثلاثي (B, Ga, In) ← p-Type ← شوائب قابلة ← فجوات أغلبية
	</details>
	<details color="gray_bg">
	<summary>🔀 الدمج والتطبيق</summary>
		- n + p ← وصلة p-n ← دايود ← ترانزستور ← خلايا شمسية ← معالجات
	</details>
	<details color="gray_bg">
	<summary>🛡️ الأمن السيبراني</summary>
		- Hardware Trojans: تعديل التطعيم أثناء التصنيع
		- Side-Channel: قياس الطاقة لاستخراج مفاتيح التشفير
		- Fault Injection: ليزر/حرارة ← أعطال تتجاوز فحوصات الأمان
	</details>
</details>
---
## ❓ أسئلة متوقعة
1. صنّف المواد كهربائياً مع مثالين لكل فئة، واذكر السبب الفيزيائي لسلوك كل منها.
2. عرّف كلاً من: حزمة التكافؤ، حزمة التوصيل، فجوة الطاقة — وما قيمة $`E_g`$ للسيليكون والجرمانيوم عند درجة حرارة الغرفة؟
3. ما المقصود بعملية التطعيم؟ ولماذا تُعد أشباه الموصلات الذاتية محدودة التطبيق العملي؟
4. قارن بين الشوائب المانحة والشوائب القابلة مع ذكر أمثلة لكل منهما.
5. اشرح آلية التوصيل في أشباه الموصلات n-Type و p-Type عند تطبيق جهد خارجي.
6. اكتب معادلة موصلية أشباه الموصلات واشرح كل رمز فيها، ثم بسّطها لحالة p-Type.
7. اذكر ثلاثة أسباب تجعل فيزياء أشباه الموصلات مهمة في مجال الأمن السيبراني، شارحاً آلية كل منها.