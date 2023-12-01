Could you please perform sentiment analysis for each item in the following Python language testing data-lists, where there are eight different language-data lists, each containing 24 elements.

In each of these elements, there is a "tweet" key with a value correlating to a random Tweet message in the language of that given language testing data-lists. Using the text data of "tweet" in each of the elements, provide & set a sentiment rating, for each element based on its "tweet" text-data, in the "llama2-sentiment" key.

For each element, please provide sentiment analysis of each element's "tweet" text-data, specifically, by providing a value of  "0" for negative sentiment or a value of "2" for positive sentiment:

```py
parsed_arabic = [
    {
        "tweet": "نوال الزغبي (الشاب خالد ليس عالمي) هههههههه أتفرجي على ها الفيديو يا مبتدئة http vía @user",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": "0"
    },
    {
        "tweet": "نوال الزغبي لطيفه الفنانه الوحيده اللي كل الفيديو كليبات تبعها ماتسبب تلوث بصري ولا سمعي لو صوتها اقل من عادي",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": "2"
    },
    {
        "tweet": "لما قالت نوال الزغبي لابقلها هاللقب فرحوا فانزها 😂😂😂كان لازم ياخدوها اهانة مش ثناء http",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": "2"
    },
    {
        "tweet": "@user تذكرني بأغنية نوال الزغبي \"عينيك كدابين\"",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": "2"
    },
    {
        "tweet": "بلا تشفير- أمل حمادي بتنتقد النجمة نوال الزغبي:\" نتي... http",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": "0"
    },
    {
        "tweet": "فنانة لبنانية كبيرة  صوتها إسطوري ؟! #ماجدة_الرومي   @user #نجوى_كرم  @user #نوال_الزغبي  @user #جوليا_بطرس",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": "2"
    },
    {
        "tweet": "#لبناني_يقيم_دوره_مكياج_بالرياضمانكبنى غير براطم نوال الزغبيونهود اليساومؤخرة هيفاء وهبيقلنالكم كله نفخ وهوابس😉😉 يازين نفخهم يلطش",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": "2"
    },
    {
        "tweet": "سيلفي للفنانة 👇الذهبية #نوال_الزغبي @user باطلالة رقيقة جميلة صباح اليوم 💋❤🌹صباح الخير 😍 http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": "2"
    },
    {
        "tweet": "منافسة كبيرة بين #نوال_الزغبي و #أمل_حجازي  ومشاكل وغيرة متبادلة من هي نجمة شركة #لايف_ستايلز_استوديوز#توقعات2017",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": "0"
    },
    {
        "tweet": "روئيتك #تريح #النظر #سماعك #يريح #الاعصاب #كلماتك #بلسم #الجروح ي #نجمتي #الذهبية #نوال_الزغبي #بحبك @user… http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": "2"
    },
    {
        "tweet": "#star_news@Cheb_Khaled_ رد الشاب خالد على نوال الزغبي مضحك ههههههههههه  نوال لازم ما تتكلمي على اسيادكhttp",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": "0"
    },
    {
        "tweet": "عم بحكي مع حالي #نوال_الزغبي http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": "2"
    },
    {
        "tweet": "لو اشوفه قدامي ذبحته بس طبعا مو قبل التحقيق  😅😅 @user #nadinenassibnjeim #nnn #star #actress… http",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": "0"
    },
    {
        "tweet": "@user - آلعآقل آلآگثر جنونآ بآلذهبیةة #نوآل_آلزغبي ❤😍💗💗 http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "@user هناك لعبة وتبادل ادوار بين ميشال عون وحزب الله لخداع السعوديه حتى يحصلوا على الهبة الماليه فحزب الله في ضائقه ماليه .",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "@user - ﺑﻴﻦ گُل \" ﻧِﻔﺲ ﻓﻴّﻨﻲ \" صُوتگگ\"  #نوآل_آلزغبي #آغلى_آلحبآيب 💙💗💗😍❤ http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "-بيار ربّاط: لا هلّق بدي اسئلك، مين صديقك أكتر \" الرّئيس ميشال عون أو سليمان فرنجية؟\"مش علينا هالحركات. إنّو اعترف بغلطتك #بلا_هبلPart 2",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "@user - علآج ﻟُﻠﻤﺰآﺝ آﻟﻤﺮ ﻓﻲ صُـوتگگ  💛💗💙❤💙#نوآل_آلزغبي #گُل_یوم_جمعةة 💗💛 http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "وداد جابر: ميشال عون لن يكمل ولايته #للنشر",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "I liked a @user video from @user http نوال الزغبي و وائل كفوري مين حبيبي",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "ومن غير #الرئيس_ميشال_عون يستأهل ذلك في وجه الفساد والحراميي  #جهزوا_سواعدكم http",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "نوال الزغبي  صوت الهدوء ❤️❤️",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "رأى الرئيس ميشال عون أن (الرئيس السوري) بشار الأسد لو خسر الحرب، لتحولت سورية إلى ليبيا ثانية\"،",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "نوال الزغبي من الحجات الي هتفضل جميله علي طول...😍😍😍😍 http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    }
]
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, fill in with either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment:

```py
{
        "tweet": "@user هناك لعبة وتبادل ادوار بين ميشال عون وحزب الله لخداع السعوديه حتى يحصلوا على الهبة الماليه فحزب الله في ضائقه ماليه .",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "@user - ﺑﻴﻦ گُل \" ﻧِﻔﺲ ﻓﻴّﻨﻲ \" صُوتگگ\"  #نوآل_آلزغبي #آغلى_آلحبآيب 💙💗💗😍❤ http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "-بيار ربّاط: لا هلّق بدي اسئلك، مين صديقك أكتر \" الرّئيس ميشال عون أو سليمان فرنجية؟\"مش علينا هالحركات. إنّو اعترف بغلطتك #بلا_هبلPart 2",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "@user - علآج ﻟُﻠﻤﺰآﺝ آﻟﻤﺮ ﻓﻲ صُـوتگگ  💛💗💙❤💙#نوآل_آلزغبي #گُل_یوم_جمعةة 💗💛 http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "وداد جابر: ميشال عون لن يكمل ولايته #للنشر",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "I liked a @user video from @user http نوال الزغبي و وائل كفوري مين حبيبي",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "ومن غير #الرئيس_ميشال_عون يستأهل ذلك في وجه الفساد والحراميي  #جهزوا_سواعدكم http",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "نوال الزغبي  صوت الهدوء ❤️❤️",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "رأى الرئيس ميشال عون أن (الرئيس السوري) بشار الأسد لو خسر الحرب، لتحولت سورية إلى ليبيا ثانية\"،",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "نوال الزغبي من الحجات الي هتفضل جميله علي طول...😍😍😍😍 http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    }
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, fill in with either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment:
```py
    {
        "tweet": "@user - ﺑﻴﻦ گُل \" ﻧِﻔﺲ ﻓﻴّﻨﻲ \" صُوتگگ\"  #نوآل_آلزغبي #آغلى_آلحبآيب 💙💗💗😍❤ http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "-بيار ربّاط: لا هلّق بدي اسئلك، مين صديقك أكتر \" الرّئيس ميشال عون أو سليمان فرنجية؟\"مش علينا هالحركات. إنّو اعترف بغلطتك #بلا_هبلPart 2",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "@user - علآج ﻟُﻠﻤﺰآﺝ آﻟﻤﺮ ﻓﻲ صُـوتگگ  💛💗💙❤💙#نوآل_آلزغبي #گُل_یوم_جمعةة 💗💛 http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "وداد جابر: ميشال عون لن يكمل ولايته #للنشر",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "I liked a @user video from @user http نوال الزغبي و وائل كفوري مين حبيبي",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "ومن غير #الرئيس_ميشال_عون يستأهل ذلك في وجه الفساد والحراميي  #جهزوا_سواعدكم http",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "نوال الزغبي  صوت الهدوء ❤️❤️",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    },
    {
        "tweet": "رأى الرئيس ميشال عون أن (الرئيس السوري) بشار الأسد لو خسر الحرب، لتحولت سورية إلى ليبيا ثانية\"،",
        "actual-sentiment": "0",
        "chatgpt-sentiment": "0",
        "llama2-sentiment": ""
    },
    {
        "tweet": "نوال الزغبي من الحجات الي هتفضل جميله علي طول...😍😍😍😍 http",
        "actual-sentiment": "2",
        "chatgpt-sentiment": "2",
        "llama2-sentiment": ""
    }
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, fill in with either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment:
```py
parsed_english = [
    {
        "tweet": "Trying to have a conversation with my dad about vegetarianism is the most pointless infuriating thing ever #caveman ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user You are a stand up guy and a Gentleman Vice President Pence ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user @user Looks like Flynn isn't too pleased with me, he blocked me. You blocked by Flynn too @user ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "i'm not even catholic, but pope francis is my dude. like i just need him to hug me and tell me everything is okay. ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user for al the crying you do about how middle America is left out-they have twice as much voting power ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Samsung to Bring Android 7.0 Nougat to Galaxy S6, S6 edge, Note 5, and Tab S2 - Softpedia News ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Israel deems comatose Gaza man who needs treatment in West Bank  a security threat. #Palestine  via @user ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "I will go so far to say s1 of westworld isn't just good, it's brilliant. A story within a story within a story about storytelling ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Iraqi Forces set to storm 3 areas of #Mosul, #AlQahira, #alMasarif &  #alAmn#MosulOps#mosuloffensive#iraq#ISIS… ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "#NationalFastFoodDay Would love to live there. Chick-fil-A 😍 ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Electoral College must reject Trump #rejecttrump #notmypresident #takingbackdemocracy #blacklivesmatter #nevertrump ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "The Reputation Doctor weighs in on Tony Romo #NFL @user joins @user on #TheMorningRush LISTEN: ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Stop #fracking #Cuadrilla persecuting land defenders through the legal system #BankruptCuadrilla #ECOCIDE ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "So proud of way @user & #trumpTransitionteam are molding strong leadership group for #America #TeamTrump #MakeAmericaGreatAgain ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user Everyone's thinking far too short-termed. When all fossil fuels run out with no substitutes, then the crisis will come. ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user - #ScreamQueens so lucky to get to work with TK. ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user @user Why is it that today society is casually comfortable about being pubicly distasteful?#deplorables ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "This is a big deal and a smart move by Microsoft: ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Ben Carson for Housing & Urban Development?? 😐 I just can't 😒 ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Digesting while watching #ScreamQueens s1 Thanksgiving & Black Friday eps. SO SO GOOD!! ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Israel's New Racism: Persecution of African Migrants in Holy Land #gaza #palestine #israel #BDS ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "I've been listening to Leonard Cohen nonstop for the past month. Only to find out he passed literally weeks ago. Wow my heart is so overwhel ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user She just didn't get them in areas were she needed them. Lots of voter suppression going on. Hacking & tampering💙 ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Listen to #NBAwards Winner @user interview on @user ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    }
]

```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, fill in with either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment:
```py
    {
        "tweet": "I've been listening to Leonard Cohen nonstop for the past month. Only to find out he passed literally weeks ago. Wow my heart is so overwhel ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user She just didn't get them in areas were she needed them. Lots of voter suppression going on. Hacking & tampering💙 ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Listen to #NBAwards Winner @user interview on @user ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    }
```