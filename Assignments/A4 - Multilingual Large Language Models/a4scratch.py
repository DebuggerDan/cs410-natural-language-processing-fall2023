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

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment:
```py

    {
        "tweet": "La lutte contre la mosaïque du manioc aux Comores: La sélection variétale pour lutter contre la mosaïque du manioc http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Il nous sort \"J'vais pas allumer la lumière parce que je veux pas faire marcher des centrales électriques.\" Ah.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Cuba: Mesures contre les effets du changement http #Cuba",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user @user Je mets au défis ce député bobo écologiste d'aller au chantier de Saint-Nazaire #chiche",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    }
]
```


Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "La lutte contre la mosaïque du manioc aux Comores: La sélection variétale pour lutter contre la mosaïque du manioc http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Il nous sort \"J'vais pas allumer la lumière parce que je veux pas faire marcher des centrales électriques.\" Ah.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Cuba: Mesures contre les effets du changement http #Cuba",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user @user Je mets au défis ce député bobo écologiste d'aller au chantier de Saint-Nazaire #chiche",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    }
```



Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "@user korrekt! Verstehe sowas nicht...",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Der Dubbletimepart von Julien war ja mal sowas von genial! :D (@user http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "#Instachallenge #Day16 #what #i #am #reading #Fratzensammler #Horror #Wattpad http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user ah. Hatte nur bis radolfzell geschaut wegen ticket. Aber so isses fast normal ;)",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user Überall lauert Gefahr. Unverhofft. #Achtung",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Sonntag ✔ Fitness ✔ Nichts tun✔",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user da werden wir uns wohl nicht einig werden, befürchte ich!",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user Toll. Sehr löblich. Sieht echt klasse aus.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "\"Absurde Unwahrheiten\" -Hoeneß stocksauer auf den \"Stern\" http #Absurde #Nachrichten #N24",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "RT @user: Linda, perfeita, guapa, Wunderschön, Bella, Beautiful !! http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "Dank @user spiele ich jetzt ohne Scheiß Candy Crush Saga ... es regt mich maßlos auf aber aufhören kann ich auch ned -.-",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Andreas Späck aus der Crowd sucht ein originelles Hochzeitgeschenk... ;-) Wer kann helfen? Merci ! Chuy You... http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Nicht nur gg Bürger, sondern auch gg eigene Mitarbeiter mobben die Behörden. Diese Fälle bearbeitet http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user OMG Titanium! Unbelievable Jahmene",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Unnötiger scheiß. Ernsthaft.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Bei http l�uft zur zeit EminemSing For The Moment also schnell einschalten :)",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "RT @user: liebe @user, dein Duschgel schmeckt nicht #tranzparenztweet",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user Aw, na gut, dann schlaf fein, klein Delalein :)",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user kann man viel gelesen haben davon, nona, aber grundsätzlich so natürlich lächerlich, die Liste! ff",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user kale chips= life",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Arschlöcher!!! MOBIL http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "RT @user: Das beste kommt zum Schluss? Ilsö: \"Manchmal kommt der Beste auch erst in den letzten 45min.\"… http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "RT @user: Wach liegen, Gedankenkarussell, unbeantwortete Fragen, Bangen, Hoffen, Zweifeln, Stolz, Verblendung, Leere, Einsamkeit…",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user Mich haben se nach vorne geschickt, konnt ne stille stehen ^^",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    }
```


Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
{
        "tweet": "CONGRESS na ye party kabhi bani hoti na india ka partition hota nd na hi humari country itni khokhli hoti   @ ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "ha ha ha ha ha ha ha .  .  .  .  . :d ye mast tha .  .  .  . cute aur comic .  .  .  . :)",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "kejariwal tum apana soch ka dayra badho ab is misunderstanding se kam nahi chalane wala hai tumhara",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "jai hind",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "result me konsa bc univrsty tope mari ... jo itna wait kr rha h ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "rt @mukhijanidhi: hai teri hasti aisi jo dekhe wo mar mite #msgyouthicon #msgrevolution",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Dhyan rakh ?? ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "aisa school ho to me kabhi ghar hi na jau .  .  . ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "pratiyogita darpan ki spelling mistake hai :)",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "i'll never forget that first girl i was crazy about in 5th grade .  i still got her valentine day card in my secret safe . ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "BC porn site ki tarah advertise karo tum bas ..... !!!! male hoe .. ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "hahaha sai m .  .  ek baar class se nikal jate the to pura school naap ke wapas ate the",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "post of the night: anonymous (id: excv6jkr) 11/02/12(fri)00:52:39 no . 434329650 this thread is like watching a monkey fuck a coconut",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Jaanma main bol rahi hu ki,tum mere twits dekho :/",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Did ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "rt psharma2525: rt komalinsaan: gurmeetramrahim #lovetoseemsg #msgincinemas schi agr duniya ye movi dekh le to yaha swrg bn skta h",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Woh  bhi ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "rare ,  300kg meteorite discovered in poland ,  biggest in eastern europe and may provide clues about earth's core: http/URL",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "band karo ye atyachaar. #indvsuae",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "durdarshan wah wah  .  .  .  . ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Ruk ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Salman bai ap kese hen ma b ap ka fen hun",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "aur jab koi ek excuse maar deta tha toh dusra kehta saale ye maine socha hua tha tune kyun bol diya",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "kiranji ko delhi ka cm ummidwar ghosit karna modiji ki doodarshita wa samghdaari ko darshata hai . ",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    }
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "@user @user Ma Ferrero? il compagno Ferrero? ma il suo partito esiste ancora? allora stiamo proprio frecati !!!",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Non vedi l'ora che venga qui almeno lo sentirò più spesso e potrò finalmente stare con lui alla faccia di chi mi ha friendzonato.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user solo che poi arriva @user e decide sempre tutto lui",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user Tutta la pasticceria! 💏 Grazie amore mio! ❤",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Quanto mi stai cazzo troia",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Perché alla fine siamo una famiglia e la famiglia non va mai abbandonata💕 #WeWillMeetAgain1D http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user @user @user @user calcio è la quintessenza della noia. Sport frenetici come basket o volley no",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user Ciao!Mia sorella ha un canale YouTube che si chiama corinnelife97potresti visitarlo e iscriverti se ti piace?Grazie💚",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "cazzo sono tutti sti tweet in tl di \\\"innocente\\\" \\\"colpevole\\\" ao",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "La bellezza della mie Steve Madden Fringly 💗 http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "@user però ha detto che è collegato positivamente alla pedofilia quindi ci vede qualcosa di buono",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "La più grande prova d'amore è sempre stata togliersi dai coglioni.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user Quando invece riaprii i miei occhi mi accorsi che non era un sogno...Era tutto nitido e reale!Grigio e freddo...",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "– tomlinsik;Profilo molto carino in generale abbinato molto bene.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Io faccio di tutto e lei ha ancora la faccia di ignorarmi perché sono così stupida? L'avrei dovuta mandare a fanculo da tempo.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user @user @user @user @user prima ora e dopo 😍😍😚",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user quanto ti odio da uno a dieci",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user @user ti vogliamo bene anche noi Harry",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Io mi lamento della gente che scrive ancora \\\"freddy mercury\\\" ma anche quella che scrive \\\"jhonny cash\\\" non scherza",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Oggi cominciamo così! Con i nostri saluti per voi di venerdì scorso dopo \\\"Notre Dame de Paris\\\". http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Dal prossimo anno Audi non sarà più uno sponsor del Milan il testimone passerà alla Piaggio...e via con gli Apetti!!",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "IL MIO DIARIO - Pagine d'estate quando ti innamori piano piano dietro uno schermo. Grazie Greta. @user ❤️ http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user il fatto che una persona che vada in discoteca implichi che questa si droghi è una fesseria...",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user che la forza sia con noi",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    }
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "todos os meus favoritos na prova de eliminação #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Augusto Cury é o cara😉 entrevista myito boa do #ConversaComBial",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Mano Vitor, tá muito feio! Decepção. #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Morrendo de amores pelo @user no programa do @user. #TheNoite",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "MIRIAN CHOORANDO PELA PROVA PASSADA #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "a cada episódio q passa Fabrizio continua um gato ne 😏 #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Traz o @user e tira a Mirian Pvr    #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "A maior e melhor cantora que você respeita @user no @user. #SandyLeah #Encontro #SandynoEncontro",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Imagina que insuportável ter de dar de comer pra uma gente que calcula CADA CALORIA que come? Jesus... #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Baixa caloria? Frango desfiado e salada. Tá ótimo  #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Aí que agonia essa Marian, meu Deus do céu, mulher!! #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "\"Eu adoro fazer piquenique no TEMPRO”  haha te amo yuko #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "\"uma mulher mais nova com um homem mais velho é normal\" normal dizer que ela ta com ele por dinheiro né? #Encontro",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Que amor esse @user no #Encontro ❤❤❤",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Vanessa da Mata acabou com a fofurice do parto da mala da Bela Gil kkkkkk #AltasHoras",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "fátima bernardes maravilhosa no #VideoShowAoVivo",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Alô NET, voces tão fora do ar?! Arrumem por favor que eu quero assistir #MasterChefBR hojeeee",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "#MasterChefBR Hummm deu vontade de comer uma sardinha com pãozinho kkk partiu abrir uma latinha! 😁",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Pq o programa não ta ao vivo? @user  #MaisVocê",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Mr Catra dando um show no The Noite ! Falando da política no país 👏 #TheNoite @user @user",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Se alguém me fala que é termogênico, eu devolvo o prato na hora #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Ai eu me derreto todinha com a Paola😭😍 #MasterChefBR",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "#AltasHoras assistindo o programa com uma cx de lenços ao lado! Haja❤😢",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Legal está prova tomara que tenha mais #DomingoLegal",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    }
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "@user jajajaja dale, hacete la boluda vos jajaja igual a vos nunca se te puede tomar en serio te mando un abrazo desde Perú!",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user MAAAAE RAJADO! Pero lo bueno es q uno se va independizando!y logrando metas",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Bueno hoy fui a almorzar a Nanay con otras 3 dras xq la capacitación mal organizada no nos dió almuerzo y encima nos mandan a comer 2pm",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user ¡Hola Tomás! ¿Habéis visto los nuevos #dinos de #TierraMagna? Es normal que haya colas antes de que comience el espectáculo",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user la hijueputa tela se me salió. yo quería volver a quedar acostada.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user pues no está nada mal",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user quizá para profesionales no sea mucho,pero hay no remunerados principalmente femenino para quienes es un sueño, pasa en mi país",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Hora de seguir soñando muy bonito",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Me estoy muriendo. Ojalá mi jefa me haga trabajar viernes y sábado en la mañana. Porque cerrar va a ser fatal",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "La felicidad tiene un nombr #Tailandia  Si es tu PRIMERA VEZ, apunta estos #consejos!   http http",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user justamente ahí es tu equivocada suposición, qxq estudió en 1 colegio ficho será pulcro? La religión le importa mda",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user Alpha suerte y ten un feliz año 2017",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py
    {
        "tweet": "Que viene Nonpa y fijo es para mayores. Ya lloro.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user pues sí, sé lo que se siente. Pero piénselo como el último esfuerzo, que ya ahorita llegan las vacaciones",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user @user @user HAHAHAHHA MMM NOS VAMOS EN 2 semanas y no tenemos ni hotel Pa la primera noche 😂😂😂",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user Que bonito,y yo tengo una sorpresa para Ti ,que te gustara muchísimo!",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "No me sorprende que 2ne1 se haya separado, man. Pero aún así me dio en el cora bc es un grupo legendario y empecé mi era kpop con ellas",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user pero yo te kiero",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user tu te planteas comprar gráfica. Yo si lo planteo tengo que comprar todo, mi pc es un venerable anciano",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Cambiar \"El mejor sistema™\" y la educación médica en España será complicado, pero con gente como vosotros tengo fe  @user @user",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user @user fallecido hace meses. Hay q contrastar.",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "Que haya una planta de tamarindo afuera de la que posiblemente va a ser la casa en la que vivas de vez en cuando, es una buena señal",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "no me deis confianza que luego os digo las cosas muy claras y os jode",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    },
    {
        "tweet": "@user ay, gracias. Lo malo es que ese es solo para primer viaje. Pero mil gracias igualmente",
        "chatgpt-sentiment": None,
        "llama2-sentiment": None
    }
```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py

```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py

```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py

```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py

```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py

```

Please fill in the "llama2-sentiment" key in the following elements, based on your sentiment analysis of each element's text-data from the "tweet" element - specifically, you must only fill in either a value of "0" for a negative sentiment or a value of "2" for a positive sentiment - there cannot be any neutral sentiment scores given:
```py

```