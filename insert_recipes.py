import mysql.connector

# データベース接続設定
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'new_password',  # MySQLのパスワード
    'database': 'recipes_table'   # 使用するデータベース名
}

# 登録したい料理データ（16個のサンプルデータ）
recipes = [
# サンプルデータ1
    {
        "title": "ふわっととろける！牛肉と玉ねぎのオムレツ炒め",
        "genre": "和食",
        "description": "とろり卵が牛肉とたまねぎを包み込み、まるでオムレツのような満足感。仕上げに醤油をひとたらしで香ばしさアップ！",
        "ingredients": "キャベツ: 1/4玉,牛肉 (薄切り): 200g,玉ねぎ: 1/2個,ピーマン: 2個,卵: 2個,醤油: 大さじ2,サラダ油: 大さじ1,塩: 適量,胡椒: 適量",
        "steps": [
            "キャベツはざく切り、玉ねぎは薄切りにする。",
            "フライパンにサラダ油を熱し、牛肉を炒める。",
            "野菜を加え、調味料で味付けする。",
            "卵を溶いて加え、炒め合わせる。",
            "仕上げにごま油を少量加える。"
        ],
        "points": "卵を入れることで、オムレツのような触感が楽しめます。醤油ベースの味付けが、野菜と牛肉のうまみを引き出します。",
        "img": "/public/images/dishes/dish1.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },
# サンプルデータ２
    {
        "title": "シャキシャキ食感！香ばしいきんぴらごぼう",
        "genre": "和食",
        "description": "シャキシャキしたごぼうと甘辛い味付けが絶品！お弁当や副菜にもぴったりです。",
        "ingredients": "ごぼう: 1本,にんじん: 1/2本,醤油: 大さじ2,みりん: 大さじ1,砂糖: 大さじ1,ごま油: 大さじ1,いりごま: 適量",
        "steps": [
            "ごぼうとにんじんを千切りにする。",
            "フライパンにごま油を熱し、ごぼうとにんじんを炒める。",
            "醤油、みりん、砂糖を加え、汁気がなくなるまで炒める。",
            "仕上げにいりごまを振る。"
        ],
        "points": "ごぼうのアクを抜くため、切ったらすぐに水にさらしましょう。",
        "img": "/public/images/dishes/dish2.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ3
    {
        "title": "ほっこり幸せ！おふくろの味・肉じゃが",
        "genre": "和食",
        "description": "ほっこり甘辛い味付けで、ごはんが進む家庭の定番料理。",
        "ingredients": "牛肉: 200g,じゃがいも: 3個,にんじん: 1本,玉ねぎ: 1個,醤油: 大さじ3,みりん: 大さじ2,砂糖: 大さじ2,だし汁: 300ml",
        "steps": [
            "材料を一口大に切る。",
            "鍋で牛肉と玉ねぎを炒める。",
            "じゃがいもとにんじんを加え、だし汁を入れて煮る。",
            "醤油、みりん、砂糖で味付けし、煮汁が少なくなるまで煮る。"
        ],
        "points": "煮る際に落し蓋をすると、味が均一に染み込みます。",
        "img": "/public/images/dishes/dish3.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ4
    {
        "title": "とろふわ卵がたまらない！絶品親子丼",
        "genre": "和食",
        "description": "ふわふわの卵と鶏肉の組み合わせが絶妙な丼ぶり。",
        "ingredients": "鶏肉: 150g,卵: 2個,玉ねぎ: 1/2個,醤油: 大さじ2,みりん: 大さじ2,砂糖: 大さじ1,だし汁: 100ml,ごはん: 2膳",
        "steps": [
            "鶏肉と玉ねぎを一口大に切る。",
            "鍋にだし汁、醤油、みりん、砂糖を入れて煮立てる。",
            "鶏肉と玉ねぎを煮て、卵でとじる。",
            "ごはんに乗せて完成。"
        ],
        "points": "卵を2回に分けて入れると、ふんわり仕上がります。",
        "img": "/public/images/dishes/dish4.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ5
    {
        "title": "寒い12月でも体ポカポカビーフシチュー",
        "genre": "洋食",
        "description": "牛肉がほろほろになるまで煮込んだ、濃厚なデミグラスソースのビーフシチュー。",
        "ingredients": "牛肉 (シチュー用): 300g,じゃがいも: 2個,にんじん: 1本,玉ねぎ: 1個,デミグラスソース: 300ml,赤ワイン: 100ml,バター: 大さじ2,小麦粉: 大さじ1,塩: 適量,胡椒: 適量",
        "steps": [
            "牛肉に塩・胡椒をし、小麦粉をまぶす。",
            "鍋でバターを溶かし、牛肉を焼き色がつくまで焼く。",
            "玉ねぎ、にんじん、じゃがいもを加えて炒める。",
            "赤ワインを加え、アルコールを飛ばしたらデミグラスソースを加え、弱火で煮込む。",
            "牛肉が柔らかくなったら完成。"
        ],
        "points": "赤ワインで煮込むことで、コクが深まります。",
        "img": "/public/images/dishes/dish5.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ6
    {
        "title": "ふわとろ卵の魔法！絶品オムライス",
        "genre": "洋食",
        "description": "ふわふわ卵で包んだケチャップライスが絶品！大人も子供も大好きな一品。",
        "ingredients": "ごはん: 2膳分,鶏肉: 100g,玉ねぎ: 1/2個,ケチャップ: 大さじ4,卵: 2個,バター: 大さじ1,塩: 適量,胡椒: 適量",
        "steps": [
            "鶏肉と玉ねぎを一口大に切る。",
            "フライパンでバターを溶かし、鶏肉と玉ねぎを炒める。",
            "ごはんとケチャップを加え、炒め合わせる。",
            "別のフライパンで卵を焼き、ごはんを包む。",
            "お好みでケチャップをかける。"
        ],
        "points": "卵は半熟に仕上げるとふんわり感がアップします。",
        "img": "/public/images/dishes/dish6.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ7
    {
        "title": "ジュワッと肉汁あふれる！王道ハンバーグ",
        "genre": "洋食",
        "description": "ジューシーでふっくらとした定番ハンバーグ。特製ソースでさらに美味しく！",
        "ingredients": "合い挽き肉: 300g,玉ねぎ: 1個,卵: 1個,パン粉: 大さじ4,牛乳: 大さじ2,塩: 適量,胡椒: 適量,ナツメグ: 少々,サラダ油: 大さじ1",
        "steps": [
            "玉ねぎをみじん切りにし、炒めて冷ます。",
            "合い挽き肉、玉ねぎ、卵、パン粉、牛乳、調味料を混ぜる。",
            "小判型に成形し、真ん中をくぼませる。",
            "フライパンで両面を焼き、中まで火を通す。",
            "お好みのソースで仕上げる。"
        ],
        "points": "肉ダネは冷蔵庫で少し寝かせると、味が馴染みます。",
        "img": "/public/images/dishes/dish7.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ8
    {
        "title": "濃厚クリーミー！本格カルボナーラ",
        "genre": "洋食",
        "description": "濃厚なチーズとベーコンの旨味が絡む、クリーミーなパスタ。",
        "ingredients": "パスタ: 200g,ベーコン: 100g,卵: 2個,生クリーム: 100ml,粉チーズ: 大さじ4,塩: 適量,胡椒: 適量,オリーブオイル: 大さじ1",
        "steps": [
            "ベーコンを細切りにし、オリーブオイルで炒める。",
            "パスタを茹でる。",
            "ボウルで卵、生クリーム、粉チーズ、塩・胡椒を混ぜる。",
            "茹で上がったパスタをベーコンと和え、卵液を加える。",
            "手早く混ぜ、余熱でとろりと仕上げる。"
        ],
        "points": "余熱で卵液を固めることで、クリーミーに仕上がります。",
        "img": "/public/images/dishes/dish8.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ9
    {
        "title": "しびれる辛さ！本格四川麻婆豆腐",
        "genre": "中華",
        "description": "ピリッと辛くてごはんが進む定番中華料理。豆腐とひき肉の旨味がたっぷり！",
        "ingredients": "木綿豆腐: 1丁,豚ひき肉: 150g,長ねぎ: 1/2本,豆板醤: 大さじ1,甜麺醤: 大さじ1,しょうゆ: 大さじ2,酒: 大さじ1,水: 150ml,鶏がらスープの素: 小さじ1,片栗粉: 大さじ1,ごま油: 大さじ1,花椒: 適量",
        "steps": [
            "豆腐を一口大に切り、熱湯で軽く茹でて水気を切る。",
            "フライパンにごま油を熱し、豚ひき肉を炒める。",
            "豆板醤と甜麺醤を加えてさらに炒める。",
            "水、しょうゆ、酒、鶏がらスープの素を加え、豆腐を入れる。",
            "水溶き片栗粉でとろみをつけ、花椒を振る。"
        ],
        "points": "花椒を加えることで本格的な痺れる辛さが楽しめます。",
        "img": "/public/images/dishes/dish9.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ10
    {
        "title": "シャキッと旨い！ピーマンたっぷり青椒肉絲",
        "genre": "中華",
        "description": "シャキシャキのピーマンと細切り豚肉の絶妙な組み合わせ。ごはんにぴったりの炒め物。",
        "ingredients": 
            "豚肉 (細切り): 200g,ピーマン: 3個,たけのこ (細切り): 100g,しょうゆ: 大さじ2,酒: 大さじ1,オイスターソース: 大さじ1,片栗粉: 大さじ1,サラダ油: 大さじ2,塩: 少々,胡椒: 少々",
        "steps": [
            "豚肉に塩、胡椒、片栗粉をまぶす。",
            "ピーマンとたけのこを細切りにする。",
            "フライパンにサラダ油を熱し、豚肉を炒める。",
            "ピーマンとたけのこを加え、しょうゆ、酒、オイスターソースで味付けする。",
            "全体に味がなじんだら完成。"
        ],
        "points": "具材は手早く炒めてシャキシャキ感を残しましょう。",
        "img": "/public/images/dishes/dish10.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ11
    {
        "title": "甘酸っぱさがやみつき！彩り酢豚",
        "genre": "中華",
        "description": "甘酸っぱいタレが絡む、ジューシーな豚肉と野菜の炒め物。",
        "ingredients": "豚肩ロース肉: 200g,玉ねぎ: 1/2個,ピーマン: 2個,にんじん: 1/2本,パイナップル: 50g,片栗粉: 大さじ2,酢: 大さじ2,しょうゆ: 大さじ2,砂糖: 大さじ3,ケチャップ: 大さじ2,サラダ油: 大さじ2",
        "steps": [
            "豚肉を一口大に切り、片栗粉をまぶす。",
            "野菜とパイナップルを食べやすい大きさに切る。",
            "フライパンで豚肉を揚げ焼きにする。",
            "野菜を加えて炒め、酢、しょうゆ、砂糖、ケチャップを混ぜたタレを加える。",
            "全体を炒め合わせて完成。"
        ],
        "points": "パイナップルを入れると甘みと酸味が引き立ちます。",
        "img": "/public/images/dishes/dish11.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ12
    {
        "title": "コク旨ピリ辛！クセになる担々麺",
        "genre": "中華",
        "description": "ピリ辛ごまスープが癖になる本格的な担々麺。",
        "ingredients": "中華麺: 1玉,豚ひき肉: 100g,長ねぎ: 1/2本,にんにく: 1片,しょうが: 1片,豆板醤: 小さじ1,練りごま: 大さじ2,しょうゆ: 大さじ2,鶏がらスープ: 300ml,ラー油: 適量,ごま油: 大さじ1",
        "steps": [
            "にんにく、しょうが、長ねぎをみじん切りにする。",
            "フライパンでごま油を熱し、豚ひき肉、にんにく、しょうがを炒める。",
            "豆板醤、しょうゆ、練りごまを加えて炒める。",
            "鶏がらスープを加え、ひと煮立ちさせる。",
            "茹でた中華麺にスープを注ぎ、長ねぎとラー油を加える。"
        ],
        "points": "仕上げにラー油をたっぷり加えると、辛さと香りが際立ちます。",
        "img": "/public/images/dishes/dish12.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ13
    {
        "title": "香り立つバジル！本格ガパオライス",
        "genre": "その他",
        "description": "タイの定番料理！バジルの香りとピリ辛のひき肉炒めがごはんと相性抜群。",
        "ingredients": "鶏ひき肉: 200g,パプリカ: 1/2個,ピーマン: 1個,にんにく: 1片,赤唐辛子: 1本,バジル: 一掴み,ナンプラー: 大さじ2,オイスターソース: 大さじ1,砂糖: 小さじ1,サラダ油: 大さじ1,卵: 1個,ごはん: 1膳分",
        "steps": [
            "にんにくと赤唐辛子をみじん切りにする。",
            "フライパンにサラダ油を熱し、にんにくと唐辛子を炒める。",
            "鶏ひき肉を加え、パプリカとピーマンも炒める。",
            "ナンプラー、オイスターソース、砂糖で味付けし、バジルを加える。",
            "目玉焼きを作り、ごはんと一緒に盛り付ける。"
        ],
        "points": "バジルはたっぷり加えると風味が引き立ちます。辛さはお好みで調整してください。",
        "img": "/public/images/dishes/dish13.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ14
    {
        "title": "スパイス香る！ジューシータンドリーチキン",
        "genre": "その他",
        "description": "スパイスとヨーグルトで漬け込んだ、香ばしく焼き上げるインド風チキン。",
        "ingredients": "鶏もも肉: 2枚,プレーンヨーグルト: 100g,にんにく: 1片,しょうが: 1片,カレー粉: 大さじ1,パプリカパウダー: 小さじ1,塩: 小さじ1,レモン汁: 大さじ1,サラダ油: 大さじ1",
        "steps": [
            "にんにく、しょうがをすりおろす。",
            "ヨーグルト、カレー粉、パプリカパウダー、塩、レモン汁、にんにく、しょうがを混ぜる。",
            "鶏肉を漬け込み、冷蔵庫で2時間寝かせる。",
            "オーブンで200℃で20分焼く。",
            "焼き色がついたら完成。"
        ],
        "points": "しっかり漬け込むことで、風味豊かな仕上がりになります。",
        "img": "/public/images/dishes/dish14.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ15
    {
        "title": "香り豊か！あっさり鶏だしフォー",
        "genre": "その他",
        "description": "あっさりした鶏だしが効いた、ベトナムの定番ライスヌードルスープ。",
        "ingredients": "フォー麺: 100g,鶏むね肉: 150g,もやし: 50g,青ねぎ: 2本,パクチー: 適量,鶏がらスープ: 500ml,ナンプラー: 大さじ1,塩: 小さじ1,ライム: 1/2個,赤唐辛子: 1本",
        "steps": [
            "鶏むね肉を茹で、細かく裂く。",
            "鶏がらスープにナンプラーと塩を加えて温める。",
            "フォー麺を茹で、器に盛る。",
            "鶏肉、もやし、青ねぎ、パクチーをトッピングする。",
            "スープを注ぎ、ライムを添える。"
        ],
        "points": "お好みでライムや唐辛子を加えて、さっぱりとした味わいを楽しんでください。",
        "img": "/public/images/dishes/dish15.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ16
    {
        "title": "カリッとあなたも包み込む！?メキシカン風タコス",
        "genre": "その他",
        "description": "スパイス香るひき肉とフレッシュな野菜をトルティーヤで包んだ、メキシコの人気料理。",
        "ingredients": "トルティーヤ: 4枚,牛ひき肉: 200g,玉ねぎ: 1/2個,トマト: 1個,レタス: 2枚,チーズ: 50g,サルサソース: 大さじ2,タコミートシーズニング: 大さじ1,サラダ油: 大さじ1",
        "steps": [
            "玉ねぎとトマトをみじん切りにし、レタスは千切りにする。",
            "フライパンにサラダ油を熱し、牛ひき肉とタコミートシーズニングを炒める。",
            "トルティーヤを軽く温める。",
            "ひき肉、野菜、チーズをトルティーヤに乗せ、サルサソースをかける。",
            "トルティーヤで包んで完成。"
        ],
        "points": "具材はお好みでアボカドやハラペーニョを加えても美味しいです。",
        "img": "/public/images/dishes/dish16.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ1７
    {
        "title": "ごはんが進む！サバ味噌煮",
        "genre": "和食",
        "description": "甘辛い味噌ダレで煮込んだサバがふっくら仕上がります。",
        "ingredients": "サバ: 2切れ, 味噌: 大さじ3, みりん: 大さじ2, 砂糖: 大さじ2, 生姜: 1片, 酒: 大さじ2, 水: 200ml",
        "steps": [
            "サバは食べやすい大きさに切る。",
            "鍋に水、酒、みりん、砂糖、味噌を入れて煮立てる。",
            "サバと生姜を加え、中火で煮る。",
            "煮汁が少なくなるまで煮詰める。"
        ],
        "points": "生姜を加えると臭みが取れて風味が良くなります。",
        "img": "/public/images/dishes/dish17.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# ンプルデータ18
    {
        "title": "香り豊か！きのこの炊き込みご飯",
        "genre": "和食",
        "description": "きのこの旨味が染み込んだ秋の味覚。",
        "ingredients": "米: 2合, しめじ: 1パック, えのき: 1パック, 醤油: 大さじ2, みりん: 大さじ1, 酒: 大さじ1, だし汁: 400ml",
        "steps": [
            "米を研ぎ、炊飯器にセットする。",
            "しめじとえのきを小分けにする。",
            "炊飯器に醤油、みりん、酒、だし汁を加える。",
            "具材をのせて炊飯し、炊き上がったら混ぜる。"
        ],
        "points": "きのこは数種類使うと旨味が増します。",
        "img": "/public/images/dishes/dish18.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ19
    {
        "title": "だしが決め手！コク旨肉うどん",
        "genre": "和食",
        "description": "甘辛い牛肉と旨味たっぷりのだしが絡む、満足感のあるうどん。",
        "ingredients": "うどん: 2玉, 牛肉: 150g, だし汁: 500ml, 醤油: 大さじ2, みりん: 大さじ2, 砂糖: 大さじ1, 長ねぎ: 1本",
        "steps": [
            "牛肉を食べやすい大きさに切る。",
            "鍋にだし汁、醤油、みりん、砂糖を入れ煮立てる。",
            "牛肉を加えて煮込み、アクを取る。",
            "茹でたうどんに牛肉と汁をかけ、長ねぎを添える。"
        ],
        "points": "牛肉は薄切りを使うと柔らかく仕上がります。",
        "img": "/public/images/dishes/dish19.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ20
    {
        "title": "なめらか食感！定番茶碗蒸し",
        "genre": "和食",
        "description": "ふんわり滑らかな茶碗蒸し。おもてなしにも最適です。",
        "ingredients": "卵: 2個, だし汁: 300ml, 醤油: 小さじ1, 塩: 小さじ1/2, みりん: 小さじ1, しいたけ: 2枚, かまぼこ: 2切れ, 鶏肉: 50g",
        "steps": [
            "卵を溶き、だし汁、醤油、塩、みりんを加えて混ぜる。",
            "器に具材を入れ、卵液を注ぐ。",
            "蒸し器で中火で15分蒸す。",
            "竹串で確認し、透明な汁が出たら完成。"
        ],
        "points": "卵液はこすと滑らかな仕上がりになります。",
        "img": "/public/images/dishes/dish20.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ21
    {
        "title": "懐かしの味！喫茶店風ナポリタン",
        "genre": "洋食",
        "description": "ケチャップの甘みと酸味が絶妙！どこか懐かしい喫茶店風のナポリタンです。",
        "ingredients": "スパゲッティ: 200g, 玉ねぎ: 1/2個, ピーマン: 2個, ソーセージ: 4本, ケチャップ: 大さじ4, バター: 大さじ1, 塩: 少々, 胡椒: 少々, 粉チーズ: 適量",
        "steps": [
            "スパゲッティを茹でる。",
            "玉ねぎ、ピーマン、ソーセージを食べやすい大きさに切る。",
            "フライパンにバターを溶かし、玉ねぎ、ソーセージを炒める。",
            "ピーマンを加え、さらに炒める。",
            "ケチャップを加えて全体に絡め、茹でたスパゲッティを加えて炒め合わせる。",
            "塩、胡椒で味を整え、粉チーズを振りかけて完成。"
        ],
        "points": "ケチャップはしっかり炒めると甘みと香ばしさが増します。",
        "img": "/public/images/dishes/dish21.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ22
    {
        "title": "とろけるチーズ！ジューシーハンバーグ",
        "genre": "洋食",
        "description": "ジューシーなハンバーグにチーズがとろりと溶けた一品。",
        "ingredients": "合い挽き肉: 300g, 玉ねぎ: 1個, 卵: 1個, パン粉: 大さじ4, 牛乳: 大さじ2, 塩: 適量, 胡椒: 適量, スライスチーズ: 2枚, サラダ油: 大さじ1",
        "steps": [
            "玉ねぎをみじん切りにし、炒めて冷ます。",
            "合い挽き肉、玉ねぎ、卵、パン粉、牛乳、調味料を混ぜる。",
            "小判型に成形し、真ん中をくぼませる。",
            "フライパンで両面を焼き、火が通ったらチーズを乗せて溶かす。",
            "お好みのソースで仕上げる。"
        ],
        "points": "チーズは最後に乗せて、余熱でとろりと溶かしましょう。",
        "img": "/public/images/dishes/dish22.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ23
    {
        "title": "おうちで簡単！ミートソースパスタ",
        "genre": "洋食",
        "description": "トマトとひき肉の旨味がたっぷり詰まったミートソース。",
        "ingredients": "スパゲッティ: 200g, 牛ひき肉: 150g, 玉ねぎ: 1/2個, トマト缶: 1缶, にんにく: 1片, オリーブオイル: 大さじ2, 塩: 適量, 胡椒: 適量",
        "steps": [
            "玉ねぎとにんにくをみじん切りにする。",
            "フライパンにオリーブオイルを熱し、にんにくを炒める。",
            "牛ひき肉と玉ねぎを加え、炒める。",
            "トマト缶を加え、煮詰める。",
            "茹でたスパゲッティにソースをかけて完成。"
        ],
        "points": "トマト缶はしっかり煮詰めることで、旨味が凝縮されます。",
        "img": "/public/images/dishes/dish23.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ24
    {
        "title": "プリプリ海老のエビチリ",
        "genre": "中華",
        "description": "ピリ辛のチリソースが海老に絡んだ絶品中華。",
        "ingredients": "むきエビ: 200g, ねぎ: 1/2本, にんにく: 1片, しょうが: 1片, ケチャップ: 大さじ4, 豆板醤: 大さじ1, 片栗粉: 大さじ1, ごま油: 大さじ1",
        "steps": [
            "エビに片栗粉をまぶし、下茹でする。",
            "フライパンでにんにく、しょうが、ねぎを炒める。",
            "豆板醤、ケチャップを加え、エビを絡める。",
            "とろみがついたら完成。"
        ],
        "points": "エビは片栗粉で下処理するとプリプリになります。",
        "img": "/public/images/dishes/dish24.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ25
    {
        "title": "ふわとろ卵の天津飯",
        "genre": "中華",
        "description": "ふわふわ卵とあんが絶妙な中華風ごはん。",
        "ingredients": "卵: 2個, カニカマ: 4本, ごはん: 1膳分, だし汁: 100ml, 醤油: 大さじ1, 片栗粉: 大さじ1",
        "steps": [
            "卵を溶き、カニカマを加える。",
            "フライパンで卵を焼き、ごはんに乗せる。",
            "あんを作り、卵にかける。"
        ],
        "points": "卵は半熟に仕上げましょう。",
        "img": "/public/images/dishes/dish25.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ26
    {
        "title": "香ばしさ満点！鶏肉とカシューナッツ炒め",
        "genre": "中華",
        "description": "カリッとしたカシューナッツとジューシーな鶏肉の相性抜群な一品。",
        "ingredients": "鶏もも肉: 200g, カシューナッツ: 50g, ピーマン: 2個, 赤パプリカ: 1/2個, にんにく: 1片, しょうゆ: 大さじ2, オイスターソース: 大さじ1, 片栗粉: 大さじ1, サラダ油: 大さじ1",
        "steps": [
            "鶏肉を一口大に切り、片栗粉をまぶす。",
            "フライパンに油を熱し、鶏肉を炒める。",
            "カシューナッツと野菜を加え、さらに炒める。",
            "しょうゆとオイスターソースで味付けする。"
        ],
        "points": "カシューナッツは最後に加えて、食感を残しましょう。",
        "img": "/public/images/dishes/dish26.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ27
    {
        "title": "パリッとジューシー！春巻き",
        "genre": "中華",
        "description": "パリパリの皮と中のジューシーな具がたまらない定番中華。",
        "ingredients": "春巻きの皮: 10枚, 豚ひき肉: 200g, たけのこ: 50g, 干ししいたけ: 2枚, にんじん: 1/2本, 春雨: 50g, しょうゆ: 大さじ2, オイスターソース: 大さじ1, 片栗粉: 大さじ1, サラダ油: 適量",
        "steps": [
            "春雨を戻し、野菜としいたけを細切りにする。",
            "ひき肉と野菜を炒め、調味料で味付けする。",
            "具を春巻きの皮で包む。",
            "油できつね色になるまで揚げる。"
        ],
        "points": "揚げる前に包み終わりをしっかり閉じると、油が入らずきれいに揚がります。",
        "img": "/public/images/dishes/dish27.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ28
    {
        "title": "スパイス香る！簡単キーマカレー",
        "genre": "その他",
        "description": "ひき肉と野菜がたっぷり入った、スパイシーで旨味たっぷりのカレー。",
        "ingredients": "合い挽き肉: 200g, 玉ねぎ: 1個, にんじん: 1/2本, ピーマン: 1個, カレー粉: 大さじ2, トマト缶: 1/2缶, にんにく: 1片, しょうが: 1片, 塩: 適量, 胡椒: 適量, サラダ油: 大さじ1",
        "steps": [
            "野菜をみじん切りにする。",
            "フライパンに油を熱し、にんにくとしょうがを炒める。",
            "ひき肉と野菜を加え、炒める。",
            "カレー粉とトマト缶を加え、水分がなくなるまで煮る。",
            "塩と胡椒で味を調える。"
        ],
        "points": "カレー粉はしっかり炒めて香りを立たせましょう。",
        "img": "/public/images/dishes/dish28.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ29
    {
        "title": "ココナッツ香る！タイ風グリーンカレー",
        "genre": "その他",
        "description": "ココナッツミルクの甘さとスパイシーさが絶妙にマッチしたタイの定番カレー。",
        "ingredients": "鶏肉: 200g, ナス: 2本, パプリカ: 1個, グリーンカレーペースト: 大さじ2, ココナッツミルク: 400ml, ナンプラー: 大さじ2, 砂糖: 大さじ1, バジル: 適量, サラダ油: 大さじ1",
        "steps": [
            "鶏肉と野菜を食べやすい大きさに切る。",
            "フライパンに油を熱し、グリーンカレーペーストを炒める。",
            "鶏肉と野菜を加えて炒める。",
            "ココナッツミルクを加え、煮込む。",
            "ナンプラーと砂糖で味を調え、バジルを加える。"
        ],
        "points": "辛さはペーストの量で調整できます。",
        "img": "/public/images/dishes/dish29.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },

# サンプルデータ30
    {
        "title": "野菜たっぷり！彩りビビンバ",
        "genre": "その他",
        "description": "彩り豊かな野菜とお肉を混ぜて食べる韓国の定番ごはん。",
        "ingredients": "ごはん: 1膳分, 牛肉: 100g, ほうれん草: 50g, もやし: 50g, にんじん: 1/2本, 卵: 1個, コチュジャン: 大さじ1, ごま油: 大さじ1, しょうゆ: 大さじ2, 砂糖: 大さじ1",
        "steps": [
            "牛肉をしょうゆと砂糖で炒める。",
            "ほうれん草、もやし、にんじんをそれぞれ茹で、ごま油と塩で和える。",
            "ごはんに具材を盛り付け、卵を乗せる。",
            "コチュジャンを加え、混ぜて食べる。"
        ],
        "points": "卵は半熟に仕上げると、全体がまろやかになります。",
        "img": "/public/images/dishes/dish30.jpg",
        "onCalendar": None,
        "calendarDate": None,
        "onCandidate": None,
        "onFavorite": None,
        "onSuggestion": True
    },
]

# MySQLに接続してデータを挿入
try:
    # データベース接続
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # SQL挿入クエリ
    insert_query = """
        INSERT INTO recipes (title, genre, description, ingredients, steps, points, img, onCalendar, calendarDate, onCandidate, onFavorite, onSuggestion)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # レシピデータを挿入
    for recipe in recipes:
        cursor.execute(insert_query, (
            recipe["title"],
            recipe["genre"],
            recipe["description"],
            "\n".join(recipe["ingredients"]),  # リストを改行で結合して文字列に変換
            "\n".join(recipe["steps"]),        # リストを改行で結合して文字列に変換
            recipe["points"],
            recipe["img"],
            recipe["onCalendar"],
            recipe["calendarDate"],
            recipe["onCandidate"],
            recipe["onFavorite"],
            recipe["onSuggestion"]
        ))

    # 変更をコミット
    conn.commit()
    print(f"{cursor.rowcount} 件のレシピが正常に挿入されました。")

except mysql.connector.Error as err:
    print(f"エラー: {err}")

finally:
    # connが定義されているか確認してからクローズ処理を実行
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("データベース接続が閉じられました。")
