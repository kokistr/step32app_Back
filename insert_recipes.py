import mysql.connector
import json

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
         "ingredients": [
            {"name": "キャベツ", "quantity": "1/4玉"},
            {"name": "牛肉 (薄切り)", "quantity": "200g"},
            {"name": "玉ねぎ", "quantity": "1/2個"},
            {"name": "ピーマン", "quantity": "2個"},
            {"name": "卵", "quantity": "2個"},
            {"name": "醤油", "quantity": "大さじ2"},
            {"name": "サラダ油", "quantity": "大さじ1"},
            {"name": "塩", "quantity": "適量"},
            {"name": "胡椒", "quantity": "適量"}
        ],
        "steps": [
            "キャベツはざく切り、玉ねぎは薄切りにする。",
            "フライパンにサラダ油を熱し、牛肉を炒める。",
            "野菜を加え、調味料で味付けする。",
            "卵を溶いて加え、炒め合わせる。",
            "仕上げにごま油を少量加える。"
        ],
        "points": "卵を入れることで、オムレツのような触感が楽しめます。醤油ベースの味付けが、野菜と牛肉のうまみを引き出します。",
        "img": "/public/images/dishes/dish1.jpg",
        "onCalendar": True,
        "calendarDate": 12,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },
# サンプルデータ２
    {
        "title": "シャキシャキ食感！香ばしいきんぴらごぼう",
        "genre": "和食",
        "description": "シャキシャキしたごぼうと甘辛い味付けが絶品！お弁当や副菜にもぴったりです。",
        "ingredients": [
            {"name": "ごぼう", "quantity": "1本"},
            {"name": "にんじん", "quantity": "1/2本"},
            {"name": "醤油", "quantity": "大さじ2"},
            {"name": "みりん", "quantity": "大さじ1"},
            {"name": "砂糖", "quantity": "大さじ1"},
            {"name": "ごま油", "quantity": "大さじ1"},
            {"name": "いりごま", "quantity": "適量"}
        ],
        "steps": [
            "ごぼうとにんじんを千切りにする。",
            "フライパンにごま油を熱し、ごぼうとにんじんを炒める。",
            "醤油、みりん、砂糖を加え、汁気がなくなるまで炒める。",
            "仕上げにいりごまを振る。"
        ],
        "points": "ごぼうのアクを抜くため、切ったらすぐに水にさらしましょう。",
        "img": "/public/images/dishes/dish2.jpg",
        "onCalendar": True,
        "calendarDate": 13,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ3
    {
        "title": "ほっこり幸せ！おふくろの味・肉じゃが",
        "genre": "和食",
        "description": "ほっこり甘辛い味付けで、ごはんが進む家庭の定番料理。",
        "ingredients": [
            {"name": "牛肉", "quantity": "200g"},
            {"name": "じゃがいも", "quantity": "3個"},
            {"name": "にんじん", "quantity": "1本"},
            {"name": "玉ねぎ", "quantity": "1個"},
            {"name": "醤油", "quantity": "大さじ3"},
            {"name": "みりん", "quantity": "大さじ2"},
            {"name": "砂糖", "quantity": "大さじ2"},
            {"name": "だし汁", "quantity": "300ml"}
        ],
        "steps": [
            "材料を一口大に切る。",
            "鍋で牛肉と玉ねぎを炒める。",
            "じゃがいもとにんじんを加え、だし汁を入れて煮る。",
            "醤油、みりん、砂糖で味付けし、煮汁が少なくなるまで煮る。"
        ],
        "points": "煮る際に落し蓋をすると、味が均一に染み込みます。",
        "img": "/public/images/dishes/dish3.jpg",
        "onCalendar": True,
        "calendarDate": 1,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ4
    {
        "title": "とろふわ卵がたまらない！絶品親子丼",
        "genre": "和食",
        "description": "ふわふわの卵と鶏肉の組み合わせが絶妙な丼ぶり。",
        "ingredients": [
            {"name": "鶏肉", "quantity": "150g"},
            {"name": "卵", "quantity": "2個"},
            {"name": "玉ねぎ", "quantity": "1/2個"},
            {"name": "醤油", "quantity": "大さじ2"},
            {"name": "みりん", "quantity": "大さじ2"},
            {"name": "砂糖", "quantity": "大さじ1"},
            {"name": "だし汁", "quantity": "100ml"},
            {"name": "ごはん", "quantity": "2膳"}
        ],
        "steps": [
            "鶏肉と玉ねぎを一口大に切る。",
            "鍋にだし汁、醤油、みりん、砂糖を入れて煮立てる。",
            "鶏肉と玉ねぎを煮て、卵でとじる。",
            "ごはんに乗せて完成。"
        ],
        "points": "卵を2回に分けて入れると、ふんわり仕上がります。",
        "img": "/public/images/dishes/dish4.jpg",
        "onCalendar": True,
        "calendarDate": 2,
        "onCandidate": True,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ5
    {
        "title": "寒い12月でも体ポカポカビーフシチュー",
        "genre": "洋食",
        "description": "牛肉がほろほろになるまで煮込んだ、濃厚なデミグラスソースのビーフシチュー。",
        "ingredients": [
            {"name": "合い挽き肉", "quantity": "300g"},
            {"name": "玉ねぎ", "quantity": "1個"},
            {"name": "卵", "quantity": "1個"},
            {"name": "パン粉", "quantity": "大さじ4"},
            {"name": "牛乳", "quantity": "大さじ2"},
            {"name": "塩", "quantity": "適量"},
            {"name": "胡椒", "quantity": "適量"},
            {"name": "ナツメグ", "quantity": "少々"},
            {"name": "サラダ油", "quantity": "大さじ1"}
        ],
        "steps": [
            "牛肉に塩・胡椒をし、小麦粉をまぶす。",
            "鍋でバターを溶かし、牛肉を焼き色がつくまで焼く。",
            "玉ねぎ、にんじん、じゃがいもを加えて炒める。",
            "赤ワインを加え、アルコールを飛ばしたらデミグラスソースを加え、弱火で煮込む。",
            "牛肉が柔らかくなったら完成。"
        ],
        "points": "赤ワインで煮込むことで、コクが深まります。",
        "img": "/public/images/dishes/dish5.jpg",
        "onCalendar": True,
        "calendarDate": 5,
        "onCandidate": True,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ6
    {
        "title": "ふわとろ卵の魔法！絶品オムライス",
        "genre": "洋食",
        "description": "ふわふわ卵で包んだケチャップライスが絶品！大人も子供も大好きな一品。",
        "ingredients": [
            {"name": "パスタ", "quantity": "200g"},
            {"name": "ベーコン", "quantity": "100g"},
            {"name": "卵", "quantity": "2個"},
            {"name": "生クリーム", "quantity": "100ml"},
            {"name": "粉チーズ", "quantity": "大さじ4"},
            {"name": "塩", "quantity": "適量"},
            {"name": "胡椒", "quantity": "適量"},
            {"name": "オリーブオイル", "quantity": "大さじ1"}
        ],
        "steps": [
            "鶏肉と玉ねぎを一口大に切る。",
            "フライパンでバターを溶かし、鶏肉と玉ねぎを炒める。",
            "ごはんとケチャップを加え、炒め合わせる。",
            "別のフライパンで卵を焼き、ごはんを包む。",
            "お好みでケチャップをかける。"
        ],
        "points": "卵は半熟に仕上げるとふんわり感がアップします。",
        "img": "/public/images/dishes/dish6.jpg",
        "onCalendar": True,
        "calendarDate": 3,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ7
    {
        "title": "ジュワッと肉汁あふれる！王道ハンバーグ",
        "genre": "洋食",
        "description": "ジューシーでふっくらとした定番ハンバーグ。特製ソースでさらに美味しく！",
        "ingredients": [
            {"name": "木綿豆腐", "quantity": "1丁"},
            {"name": "豚ひき肉", "quantity": "150g"},
            {"name": "長ねぎ", "quantity": "1/2本"},
            {"name": "豆板醤", "quantity": "大さじ1"},
            {"name": "甜麺醤", "quantity": "大さじ1"},
            {"name": "しょうゆ", "quantity": "大さじ2"},
            {"name": "酒", "quantity": "大さじ1"},
            {"name": "水", "quantity": "150ml"},
            {"name": "鶏がらスープの素", "quantity": "小さじ1"},
            {"name": "片栗粉", "quantity": "大さじ1"},
            {"name": "ごま油", "quantity": "大さじ1"},
            {"name": "花椒", "quantity": "適量"}
        ],
        "steps": [
            "玉ねぎをみじん切りにし、炒めて冷ます。",
            "合い挽き肉、玉ねぎ、卵、パン粉、牛乳、調味料を混ぜる。",
            "小判型に成形し、真ん中をくぼませる。",
            "フライパンで両面を焼き、中まで火を通す。",
            "お好みのソースで仕上げる。"
        ],
        "points": "肉ダネは冷蔵庫で少し寝かせると、味が馴染みます。",
        "img": "/public/images/dishes/dish7.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ8
    {
        "title": "濃厚クリーミー！本格カルボナーラ",
        "genre": "洋食",
        "description": "濃厚なチーズとベーコンの旨味が絡む、クリーミーなパスタ。",
        "ingredients": [
            {"name": "パスタ", "quantity": "200g"},
            {"name": "ベーコン", "quantity": "100g"},
            {"name": "卵", "quantity": "2個"},
            {"name": "生クリーム", "quantity": "100ml"},
            {"name": "粉チーズ", "quantity": "大さじ4"},
            {"name": "塩", "quantity": "適量"},
            {"name": "胡椒", "quantity": "適量"},
            {"name": "オリーブオイル", "quantity": "大さじ1"}
        ],
        "steps": [
            "ベーコンを細切りにし、オリーブオイルで炒める。",
            "パスタを茹でる。",
            "ボウルで卵、生クリーム、粉チーズ、塩・胡椒を混ぜる。",
            "茹で上がったパスタをベーコンと和え、卵液を加える。",
            "手早く混ぜ、余熱でとろりと仕上げる。"
        ],
        "points": "余熱で卵液を固めることで、クリーミーに仕上がります。",
        "img": "/public/images/dishes/dish8.jpg",
        "onCalendar": True,
        "calendarDate": 8,
        "onCandidate": True,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ9
    {
        "title": "しびれる辛さ！本格四川麻婆豆腐",
        "genre": "中華",
        "description": "ピリッと辛くてごはんが進む定番中華料理。豆腐とひき肉の旨味がたっぷり！",
        "ingredients": [
            {"name": "木綿豆腐", "quantity": "1丁"},
            {"name": "豚ひき肉", "quantity": "150g"},
            {"name": "長ねぎ", "quantity": "1/2本"},
            {"name": "豆板醤", "quantity": "大さじ1"},
            {"name": "甜麺醤", "quantity": "大さじ1"},
            {"name": "しょうゆ", "quantity": "大さじ2"},
            {"name": "酒", "quantity": "大さじ1"},
            {"name": "水", "quantity": "150ml"},
            {"name": "鶏がらスープの素", "quantity": "小さじ1"},
            {"name": "片栗粉", "quantity": "大さじ1"},
            {"name": "ごま油", "quantity": "大さじ1"},
            {"name": "花椒", "quantity": "適量"}
        ],
        "steps": [
            "豆腐を一口大に切り、熱湯で軽く茹でて水気を切る。",
            "フライパンにごま油を熱し、豚ひき肉を炒める。",
            "豆板醤と甜麺醤を加えてさらに炒める。",
            "水、しょうゆ、酒、鶏がらスープの素を加え、豆腐を入れる。",
            "水溶き片栗粉でとろみをつけ、花椒を振る。"
        ],
        "points": "花椒を加えることで本格的な痺れる辛さが楽しめます。",
        "img": "/public/images/dishes/dish9.jpg",
        "onCalendar": True,
        "calendarDate": 28,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ10
    {
        "title": "シャキッと旨い！ピーマンたっぷり青椒肉絲",
        "genre": "中華",
        "description": "シャキシャキのピーマンと細切り豚肉の絶妙な組み合わせ。ごはんにぴったりの炒め物。",
        "ingredients": [
            {"name": "豚肉 (細切り)", "quantity": "200g"},
            {"name": "ピーマン", "quantity": "3個"},
            {"name": "たけのこ (細切り)", "quantity": "100g"},
            {"name": "しょうゆ", "quantity": "大さじ2"},
            {"name": "酒", "quantity": "大さじ1"},
            {"name": "オイスターソース", "quantity": "大さじ1"},
            {"name": "片栗粉", "quantity": "大さじ1"},
            {"name": "サラダ油", "quantity": "大さじ2"},
            {"name": "塩", "quantity": "少々"},
            {"name": "胡椒", "quantity": "少々"}
        ],
        "steps": [
            "豚肉に塩、胡椒、片栗粉をまぶす。",
            "ピーマンとたけのこを細切りにする。",
            "フライパンにサラダ油を熱し、豚肉を炒める。",
            "ピーマンとたけのこを加え、しょうゆ、酒、オイスターソースで味付けする。",
            "全体に味がなじんだら完成。"
        ],
        "points": "具材は手早く炒めてシャキシャキ感を残しましょう。",
        "img": "/public/images/dishes/dish10.jpg",
        "onCalendar": True,
        "calendarDate": 9,
        "onCandidate": True,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ11
    {
        "title": "甘酸っぱさがやみつき！彩り酢豚",
        "genre": "中華",
        "description": "甘酸っぱいタレが絡む、ジューシーな豚肉と野菜の炒め物。",
        "ingredients": [
            {"name": "豚肩ロース肉", "quantity": "200g"},
            {"name": "玉ねぎ", "quantity": "1/2個"},
            {"name": "ピーマン", "quantity": "2個"},
            {"name": "にんじん", "quantity": "1/2本"},
            {"name": "パイナップル", "quantity": "50g"},
            {"name": "片栗粉", "quantity": "大さじ2"},
            {"name": "酢", "quantity": "大さじ2"},
            {"name": "しょうゆ", "quantity": "大さじ2"},
            {"name": "砂糖", "quantity": "大さじ3"},
            {"name": "ケチャップ", "quantity": "大さじ2"},
            {"name": "サラダ油", "quantity": "大さじ2"}
        ],
        "steps": [
            "豚肉を一口大に切り、片栗粉をまぶす。",
            "野菜とパイナップルを食べやすい大きさに切る。",
            "フライパンで豚肉を揚げ焼きにする。",
            "野菜を加えて炒め、酢、しょうゆ、砂糖、ケチャップを混ぜたタレを加える。",
            "全体を炒め合わせて完成。"
        ],
        "points": "パイナップルを入れると甘みと酸味が引き立ちます。",
        "img": "/public/images/dishes/dish11.jpg",
        "onCalendar": True,
        "calendarDate": 10,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ12
    {
        "title": "コク旨ピリ辛！クセになる担々麺",
        "genre": "中華",
        "description": "ピリ辛ごまスープが癖になる本格的な担々麺。",
        "ingredients": [
            {"name": "中華麺", "quantity": "1玉"},
            {"name": "豚ひき肉", "quantity": "100g"},
            {"name": "長ねぎ", "quantity": "1/2本"},
            {"name": "にんにく", "quantity": "1片"},
            {"name": "しょうが", "quantity": "1片"},
            {"name": "豆板醤", "quantity": "小さじ1"},
            {"name": "練りごま", "quantity": "大さじ2"},
            {"name": "しょうゆ", "quantity": "大さじ2"},
            {"name": "鶏がらスープ", "quantity": "300ml"},
            {"name": "ラー油", "quantity": "適量"},
            {"name": "ごま油", "quantity": "大さじ1"}
        ],
        "steps": [
            "にんにく、しょうが、長ねぎをみじん切りにする。",
            "フライパンでごま油を熱し、豚ひき肉、にんにく、しょうがを炒める。",
            "豆板醤、しょうゆ、練りごまを加えて炒める。",
            "鶏がらスープを加え、ひと煮立ちさせる。",
            "茹でた中華麺にスープを注ぎ、長ねぎとラー油を加える。"
        ],
        "points": "仕上げにラー油をたっぷり加えると、辛さと香りが際立ちます。",
        "img": "/public/images/dishes/dish12.jpg",
        "onCalendar": True,
        "calendarDate": 4,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ13
    {
        "title": "香り立つバジル！本格ガパオライス",
        "genre": "その他",
        "description": "タイの定番料理！バジルの香りとピリ辛のひき肉炒めがごはんと相性抜群。",
        "ingredients": [
            {"name": "鶏ひき肉", "quantity": "200g"},
            {"name": "パプリカ", "quantity": "1/2個"},
            {"name": "ピーマン", "quantity": "1個"},
            {"name": "にんにく", "quantity": "1片"},
            {"name": "赤唐辛子", "quantity": "1本"},
            {"name": "バジル", "quantity": "一掴み"},
            {"name": "ナンプラー", "quantity": "大さじ2"},
            {"name": "オイスターソース", "quantity": "大さじ1"},
            {"name": "砂糖", "quantity": "小さじ1"},
            {"name": "サラダ油", "quantity": "大さじ1"},
            {"name": "卵", "quantity": "1個"},
            {"name": "ごはん", "quantity": "1膳分"}
        ],
        "steps": [
            "にんにくと赤唐辛子をみじん切りにする。",
            "フライパンにサラダ油を熱し、にんにくと唐辛子を炒める。",
            "鶏ひき肉を加え、パプリカとピーマンも炒める。",
            "ナンプラー、オイスターソース、砂糖で味付けし、バジルを加える。",
            "目玉焼きを作り、ごはんと一緒に盛り付ける。"
        ],
        "points": "バジルはたっぷり加えると風味が引き立ちます。辛さはお好みで調整してください。",
        "img": "/public/images/dishes/dish13.jpg",
        "onCalendar": True,
        "calendarDate": 11,
        "onCandidate": True,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ14
    {
        "title": "スパイス香る！ジューシータンドリーチキン",
        "genre": "その他",
        "description": "スパイスとヨーグルトで漬け込んだ、香ばしく焼き上げるインド風チキン。",
        "ingredients": [
            {"name": "鶏もも肉", "quantity": "2枚"},
            {"name": "プレーンヨーグルト", "quantity": "100g"},
            {"name": "にんにく", "quantity": "1片"},
            {"name": "しょうが", "quantity": "1片"},
            {"name": "カレー粉", "quantity": "大さじ1"},
            {"name": "パプリカパウダー", "quantity": "小さじ1"},
            {"name": "塩", "quantity": "小さじ1"},
            {"name": "レモン汁", "quantity": "大さじ1"},
            {"name": "サラダ油", "quantity": "大さじ1"}
        ],
        "steps": [
            "にんにく、しょうがをすりおろす。",
            "ヨーグルト、カレー粉、パプリカパウダー、塩、レモン汁、にんにく、しょうがを混ぜる。",
            "鶏肉を漬け込み、冷蔵庫で2時間寝かせる。",
            "オーブンで200℃で20分焼く。",
            "焼き色がついたら完成。"
        ],
        "points": "しっかり漬け込むことで、風味豊かな仕上がりになります。",
        "img": "/public/images/dishes/dish14.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ15
    {
        "title": "香り豊か！あっさり鶏だしフォー",
        "genre": "その他",
        "description": "あっさりした鶏だしが効いた、ベトナムの定番ライスヌードルスープ。",
        "ingredients": [
            {"name": "フォー麺", "quantity": "100g"},
            {"name": "鶏むね肉", "quantity": "150g"},
            {"name": "もやし", "quantity": "50g"},
            {"name": "青ねぎ", "quantity": "2本"},
            {"name": "パクチー", "quantity": "適量"},
            {"name": "鶏がらスープ", "quantity": "500ml"},
            {"name": "ナンプラー", "quantity": "大さじ1"},
            {"name": "塩", "quantity": "小さじ1"},
            {"name": "ライム", "quantity": "1/2個"},
            {"name": "赤唐辛子", "quantity": "1本"}
        ],
        "steps": [
            "鶏むね肉を茹で、細かく裂く。",
            "鶏がらスープにナンプラーと塩を加えて温める。",
            "フォー麺を茹で、器に盛る。",
            "鶏肉、もやし、青ねぎ、パクチーをトッピングする。",
            "スープを注ぎ、ライムを添える。"
        ],
        "points": "お好みでライムや唐辛子を加えて、さっぱりとした味わいを楽しんでください。",
        "img": "/public/images/dishes/dish15.jpg",
        "onCalendar": True,
        "calendarDate": 15,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ16
    {
        "title": "カリッとあなたも包み込む！?メキシカン風タコス",
        "genre": "その他",
        "description": "スパイス香るひき肉とフレッシュな野菜をトルティーヤで包んだ、メキシコの人気料理。",
        "ingredients": [
            {"name": "トルティーヤ", "quantity": "4枚"},
            {"name": "牛ひき肉", "quantity": "200g"},
            {"name": "玉ねぎ", "quantity": "1/2個"},
            {"name": "トマト", "quantity": "1個"},
            {"name": "レタス", "quantity": "2枚"},
            {"name": "チーズ", "quantity": "50g"},
            {"name": "サルサソース", "quantity": "大さじ2"},
            {"name": "タコミートシーズニング", "quantity": "大さじ1"},
            {"name": "サラダ油", "quantity": "大さじ1"}
        ],
        "steps": [
            "玉ねぎとトマトをみじん切りにし、レタスは千切りにする。",
            "フライパンにサラダ油を熱し、牛ひき肉とタコミートシーズニングを炒める。",
            "トルティーヤを軽く温める。",
            "ひき肉、野菜、チーズをトルティーヤに乗せ、サルサソースをかける。",
            "トルティーヤで包んで完成。"
        ],
        "points": "具材はお好みでアボカドやハラペーニョを加えても美味しいです。",
        "img": "/public/images/dishes/dish16.jpg",
        "onCalendar": True,
        "calendarDate": 14,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ1７
    {
        "title": "ごはんが進む！サバ味噌煮",
        "genre": "和食",
        "description": "甘辛い味噌ダレで煮込んだサバがふっくら仕上がります。",
        "ingredients": [
            {"name": "サバ", "quantity": "2切れ"},
            {"name": "味噌", "quantity": "大さじ3"},
            {"name": "みりん", "quantity": "大さじ2"},
            {"name": "砂糖", "quantity": "大さじ2"},
            {"name": "生姜", "quantity": "1片"},
            {"name": "酒", "quantity": "大さじ2"},
            {"name": "水", "quantity": "200ml"}
        ],
        "steps": [
            "サバは食べやすい大きさに切る。",
            "鍋に水、酒、みりん、砂糖、味噌を入れて煮立てる。",
            "サバと生姜を加え、中火で煮る。",
            "煮汁が少なくなるまで煮詰める。"
        ],
        "points": "生姜を加えると臭みが取れて風味が良くなります。",
        "img": "/public/images/dishes/dish17.jpg",
        "onCalendar": True,
        "calendarDate": 6,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ18
    {
        "title": "香り豊か！きのこの炊き込みご飯",
        "genre": "和食",
        "description": "きのこの旨味が染み込んだ秋の味覚。",
        "ingredients": [
            {"name": "米", "quantity": "2合"},
            {"name": "しめじ", "quantity": "1パック"},
            {"name": "えのき", "quantity": "1パック"},
            {"name": "醤油", "quantity": "大さじ2"},
            {"name": "みりん", "quantity": "大さじ1"},
            {"name": "酒", "quantity": "大さじ1"},
            {"name": "だし汁", "quantity": "400ml"}
        ],
        "steps": [
            "米を研ぎ、炊飯器にセットする。",
            "しめじとえのきを小分けにする。",
            "炊飯器に醤油、みりん、酒、だし汁を加える。",
            "具材をのせて炊飯し、炊き上がったら混ぜる。"
        ],
        "points": "きのこは数種類使うと旨味が増します。",
        "img": "/public/images/dishes/dish18.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ19
    {
        "title": "だしが決め手！コク旨肉うどん",
        "genre": "和食",
        "description": "甘辛い牛肉と旨味たっぷりのだしが絡む、満足感のあるうどん。",
        "ingredients": [
            {"name": "うどん", "quantity": "2玉"},
            {"name": "牛肉", "quantity": "150g"},
            {"name": "だし汁", "quantity": "500ml"},
            {"name": "醤油", "quantity": "大さじ2"},
            {"name": "みりん", "quantity": "大さじ2"},
            {"name": "砂糖", "quantity": "大さじ1"},
            {"name": "長ねぎ", "quantity": "1本"}
        ],
        "steps": [
            "牛肉を食べやすい大きさに切る。",
            "鍋にだし汁、醤油、みりん、砂糖を入れ煮立てる。",
            "牛肉を加えて煮込み、アクを取る。",
            "茹でたうどんに牛肉と汁をかけ、長ねぎを添える。"
        ],
        "points": "牛肉は薄切りを使うと柔らかく仕上がります。",
        "img": "/public/images/dishes/dish19.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ20
    {
        "title": "なめらか食感！定番茶碗蒸し",
        "genre": "和食",
        "description": "ふんわり滑らかな茶碗蒸し。おもてなしにも最適です。",
        "ingredients": [
            {"name": "卵", "quantity": "2個"},
            {"name": "だし汁", "quantity": "300ml"},
            {"name": "醤油", "quantity": "小さじ1"},
            {"name": "塩", "quantity": "小さじ1/2"},
            {"name": "みりん", "quantity": "小さじ1"},
            {"name": "しいたけ", "quantity": "2枚"},
            {"name": "かまぼこ", "quantity": "2切れ"},
            {"name": "鶏肉", "quantity": "50g"}
        ],
        "steps": [
            "卵を溶き、だし汁、醤油、塩、みりんを加えて混ぜる。",
            "器に具材を入れ、卵液を注ぐ。",
            "蒸し器で中火で15分蒸す。",
            "竹串で確認し、透明な汁が出たら完成。"
        ],
        "points": "卵液はこすと滑らかな仕上がりになります。",
        "img": "/public/images/dishes/dish20.jpg",
        "onCalendar": True,
        "calendarDate": 16,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ21
    {
        "title": "懐かしの味！喫茶店風ナポリタン",
        "genre": "洋食",
        "description": "ケチャップの甘みと酸味が絶妙！どこか懐かしい喫茶店風のナポリタンです。",
        "ingredients": [
            {"name": "スパゲッティ", "quantity": "200g"},
            {"name": "玉ねぎ", "quantity": "1/2個"},
            {"name": "ピーマン", "quantity": "2個"},
            {"name": "ソーセージ", "quantity": "4本"},
            {"name": "ケチャップ", "quantity": "大さじ4"},
            {"name": "バター", "quantity": "大さじ1"},
            {"name": "塩", "quantity": "少々"},
            {"name": "胡椒", "quantity": "少々"},
            {"name": "粉チーズ", "quantity": "適量"}
        ],
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
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ22
    {
        "title": "とろけるチーズ！ジューシーハンバーグ",
        "genre": "洋食",
        "description": "ジューシーなハンバーグにチーズがとろりと溶けた一品。",
        "ingredients": [
            {"name": "合い挽き肉", "quantity": "300g"},
            {"name": "玉ねぎ", "quantity": "1個"},
            {"name": "卵", "quantity": "1個"},
            {"name": "パン粉", "quantity": "大さじ4"},
            {"name": "牛乳", "quantity": "大さじ2"},
            {"name": "塩", "quantity": "適量"},
            {"name": "胡椒", "quantity": "適量"},
            {"name": "スライスチーズ", "quantity": "2枚"},
            {"name": "サラダ油", "quantity": "大さじ1"}
        ],
        "steps": [
            "玉ねぎをみじん切りにし、炒めて冷ます。",
            "合い挽き肉、玉ねぎ、卵、パン粉、牛乳、調味料を混ぜる。",
            "小判型に成形し、真ん中をくぼませる。",
            "フライパンで両面を焼き、火が通ったらチーズを乗せて溶かす。",
            "お好みのソースで仕上げる。"
        ],
        "points": "チーズは最後に乗せて、余熱でとろりと溶かしましょう。",
        "img": "/public/images/dishes/dish22.jpg",
        "onCalendar": True,
        "calendarDate": 7,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ23
    {
        "title": "おうちで簡単！ミートソースパスタ",
        "genre": "洋食",
        "description": "トマトとひき肉の旨味がたっぷり詰まったミートソース。",
        "ingredients": [
            {"name": "スパゲッティ", "quantity": "200g"},
            {"name": "牛ひき肉", "quantity": "150g"},
            {"name": "玉ねぎ", "quantity": "1/2個"},
            {"name": "トマト缶", "quantity": "1缶"},
            {"name": "にんにく", "quantity": "1片"},
            {"name": "オリーブオイル", "quantity": "大さじ2"},
            {"name": "塩", "quantity": "適量"},
            {"name": "胡椒", "quantity": "適量"}
        ],
        "steps": [
            "玉ねぎとにんにくをみじん切りにする。",
            "フライパンにオリーブオイルを熱し、にんにくを炒める。",
            "牛ひき肉と玉ねぎを加え、炒める。",
            "トマト缶を加え、煮詰める。",
            "茹でたスパゲッティにソースをかけて完成。"
        ],
        "points": "トマト缶はしっかり煮詰めることで、旨味が凝縮されます。",
        "img": "/public/images/dishes/dish23.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ24
    {
        "title": "プリプリ海老のエビチリ",
        "genre": "中華",
        "description": "ピリ辛のチリソースが海老に絡んだ絶品中華。",
        "ingredients": [
            {"name": "むきエビ", "quantity": "200g"},
            {"name": "ねぎ", "quantity": "1/2本"},
            {"name": "にんにく", "quantity": "1片"},
            {"name": "しょうが", "quantity": "1片"},
            {"name": "ケチャップ", "quantity": "大さじ4"},
            {"name": "豆板醤", "quantity": "大さじ1"},
            {"name": "片栗粉", "quantity": "大さじ1"},
            {"name": "ごま油", "quantity": "大さじ1"}
        ],
        "steps": [
            "エビに片栗粉をまぶし、下茹でする。",
            "フライパンでにんにく、しょうが、ねぎを炒める。",
            "豆板醤、ケチャップを加え、エビを絡める。",
            "とろみがついたら完成。"
        ],
        "points": "エビは片栗粉で下処理するとプリプリになります。",
        "img": "/public/images/dishes/dish24.jpg",
        "onCalendar": True,
        "calendarDate": 18,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ25
    {
        "title": "ふわとろ卵の天津飯",
        "genre": "中華",
        "description": "ふわふわ卵とあんが絶妙な中華風ごはん。",
        "ingredients": [
            {"name": "卵", "quantity": "2個"},
            {"name": "カニカマ", "quantity": "4本"},
            {"name": "ごはん", "quantity": "1膳分"},
            {"name": "だし汁", "quantity": "100ml"},
            {"name": "醤油", "quantity": "大さじ1"},
            {"name": "片栗粉", "quantity": "大さじ1"}
        ],
        "steps": [
            "卵を溶き、カニカマを加える。",
            "フライパンで卵を焼き、ごはんに乗せる。",
            "あんを作り、卵にかける。"
        ],
        "points": "卵は半熟に仕上げましょう。",
        "img": "/public/images/dishes/dish25.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ26
    {
        "title": "香ばしさ満点！鶏肉とカシューナッツ炒め",
        "genre": "中華",
        "description": "カリッとしたカシューナッツとジューシーな鶏肉の相性抜群な一品。",
        "ingredients": [
            {"name": "鶏もも肉", "quantity": "200g"},
            {"name": "カシューナッツ", "quantity": "50g"},
            {"name": "ピーマン", "quantity": "2個"},
            {"name": "赤パプリカ", "quantity": "1/2個"},
            {"name": "にんにく", "quantity": "1片"},
            {"name": "しょうゆ", "quantity": "大さじ2"},
            {"name": "オイスターソース", "quantity": "大さじ1"},
            {"name": "片栗粉", "quantity": "大さじ1"},
            {"name": "サラダ油", "quantity": "大さじ1"}
        ],
        "steps": [
            "鶏肉を一口大に切り、片栗粉をまぶす。",
            "フライパンに油を熱し、鶏肉を炒める。",
            "カシューナッツと野菜を加え、さらに炒める。",
            "しょうゆとオイスターソースで味付けする。"
        ],
        "points": "カシューナッツは最後に加えて、食感を残しましょう。",
        "img": "/public/images/dishes/dish26.jpg",
        "onCalendar": True,
        "calendarDate": 17,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ27
    {
        "title": "パリッとジューシー！春巻き",
        "genre": "中華",
        "description": "パリパリの皮と中のジューシーな具がたまらない定番中華。",
        "ingredients": [
            {"name": "春巻きの皮", "quantity": "10枚"},
            {"name": "豚ひき肉", "quantity": "200g"},
            {"name": "たけのこ", "quantity": "50g"},
            {"name": "干ししいたけ", "quantity": "2枚"},
            {"name": "にんじん", "quantity": "1/2本"},
            {"name": "春雨", "quantity": "50g"},
            {"name": "しょうゆ", "quantity": "大さじ2"},
            {"name": "オイスターソース", "quantity": "大さじ1"},
            {"name": "片栗粉", "quantity": "大さじ1"},
            {"name": "サラダ油", "quantity": "適量"}
        ],
        "steps": [
            "春雨を戻し、野菜としいたけを細切りにする。",
            "ひき肉と野菜を炒め、調味料で味付けする。",
            "具を春巻きの皮で包む。",
            "油できつね色になるまで揚げる。"
        ],
        "points": "揚げる前に包み終わりをしっかり閉じると、油が入らずきれいに揚がります。",
        "img": "/public/images/dishes/dish27.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ28
    {
        "title": "スパイス香る！簡単キーマカレー",
        "genre": "その他",
        "description": "ひき肉と野菜がたっぷり入った、スパイシーで旨味たっぷりのカレー。",
        "ingredients": [
            {"name": "合い挽き肉", "quantity": "200g"},
            {"name": "玉ねぎ", "quantity": "1個"},
            {"name": "にんじん", "quantity": "1/2本"},
            {"name": "ピーマン", "quantity": "1個"},
            {"name": "カレー粉", "quantity": "大さじ2"},
            {"name": "トマト缶", "quantity": "1/2缶"},
            {"name": "にんにく", "quantity": "1片"},
            {"name": "しょうが", "quantity": "1片"},
            {"name": "塩", "quantity": "適量"},
            {"name": "胡椒", "quantity": "適量"},
            {"name": "サラダ油", "quantity": "大さじ1"}
        ],
        "steps": [
            "野菜をみじん切りにする。",
            "フライパンに油を熱し、にんにくとしょうがを炒める。",
            "ひき肉と野菜を加え、炒める。",
            "カレー粉とトマト缶を加え、水分がなくなるまで煮る。",
            "塩と胡椒で味を調える。"
        ],
        "points": "カレー粉はしっかり炒めて香りを立たせましょう。",
        "img": "/public/images/dishes/dish28.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ29
    {
        "title": "ココナッツ香る！タイ風グリーンカレー",
        "genre": "その他",
        "description": "ココナッツミルクの甘さとスパイシーさが絶妙にマッチしたタイの定番カレー。",
        "ingredients": [
            {"name": "鶏肉", "quantity": "200g"},
            {"name": "ナス", "quantity": "2本"},
            {"name": "パプリカ", "quantity": "1個"},
            {"name": "グリーンカレーペースト", "quantity": "大さじ2"},
            {"name": "ココナッツミルク", "quantity": "400ml"},
            {"name": "ナンプラー", "quantity": "大さじ2"},
            {"name": "砂糖", "quantity": "大さじ1"},
            {"name": "バジル", "quantity": "適量"},
            {"name": "サラダ油", "quantity": "大さじ1"}
        ],
        "steps": [
            "鶏肉と野菜を食べやすい大きさに切る。",
            "フライパンに油を熱し、グリーンカレーペーストを炒める。",
            "鶏肉と野菜を加えて炒める。",
            "ココナッツミルクを加え、煮込む。",
            "ナンプラーと砂糖で味を調え、バジルを加える。"
        ],
        "points": "辛さはペーストの量で調整できます。",
        "img": "/public/images/dishes/dish29.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ30
    {
        "title": "野菜たっぷり！彩りビビンバ",
        "genre": "その他",
        "description": "彩り豊かな野菜とお肉を混ぜて食べる韓国の定番ごはん。",
        "ingredients":  [
            {"name": "ごはん", "quantity": "1膳分"},
            {"name": "牛肉", "quantity": "100g"},
            {"name": "ほうれん草", "quantity": "50g"},
            {"name": "もやし", "quantity": "50g"},
            {"name": "にんじん", "quantity": "1/2本"},
            {"name": "卵", "quantity": "1個"},
            {"name": "コチュジャン", "quantity": "大さじ1"},
            {"name": "ごま油", "quantity": "大さじ1"},
            {"name": "しょうゆ", "quantity": "大さじ2"},
            {"name": "砂糖", "quantity": "大さじ1"}
        ],
        "steps": [
            "牛肉をしょうゆと砂糖で炒める。",
            "ほうれん草、もやし、にんじんをそれぞれ茹で、ごま油と塩で和える。",
            "ごはんに具材を盛り付け、卵を乗せる。",
            "コチュジャンを加え、混ぜて食べる。"
        ],
        "points": "卵は半熟に仕上げると、全体がまろやかになります。",
        "img": "/public/images/dishes/dish30.jpg",
        "onCalendar": False,
        "calendarDate": None,
        "onCandidate": False,
        "onFavorite": False,
        "onSuggestion": True
    },

# サンプルデータ31
    {
        "title": "トシさん激推し!絶品納豆ご飯",
        "genre": "和食",
        "description": "シンプルながらも深い味わい。納豆のネバネバと卵黄が絡み合う究極のご飯。",
        "ingredients": [
            {"name": "ごはん", "quantity": "1膳分"},
            {"name": "納豆", "quantity": "1パック"},
            {"name": "卵黄", "quantity": "1個"},
            {"name": "醤油", "quantity": "小さじ1"},
            {"name": "青ねぎ", "quantity": "適量"}
        ],
        "steps": [
            "ごはんを茶碗に盛る。",
            "納豆に醤油を混ぜてよくかき混ぜる。",
            "ごはんに納豆をかけ、中央に卵黄をのせる。",
            "青ねぎを散らして完成。"
        ],
        "points": "卵黄を加えることで、まろやかさがアップします。",
        "img": "/public/images/dishes/dish31.jpg",
        "onCalendar": True,
        "calendarDate": 21,
        "onCandidate": False,
        "onFavorite": True,
        "onSuggestion": True
    },

# サンプルデータ32
    {
        "title": "さけさんおすすめトマトのさっぱりサラダ",
        "genre": "その他",
        "description": "みずみずしいトマトと香味野菜が引き立つ、さっぱりとしたサラダ。",
        "ingredients": [
            {"name": "トマト", "quantity": "2個"},
            {"name": "玉ねぎ", "quantity": "1/4個"},
            {"name": "バジル", "quantity": "適量"},
            {"name": "醤油", "quantity": "小さじ2"},
            {"name": "ごま油", "quantity": "小さじ1"}
        ],
        "steps": [
            "トマトを食べやすい大きさに切る。",
            "玉ねぎを薄切りにし、水にさらして辛味を抜く。",
            "トマトと玉ねぎを皿に盛り、バジルを添える。",
            "醤油とごま油をかけて完成。"
        ],
        "points": "冷蔵庫で冷やしてから食べるとさらに美味しいです。",
        "img": "/public/images/dishes/dish32.jpg",
        "onCalendar": True,
        "calendarDate": 18,
        "onCandidate": False,
        "onFavorite": True,
        "onSuggestion": True
    },

# サンプルデータ33
    {
        "title": "こーきさんの定番!熱々羽付き紫蘇餃子",
        "genre": "中華",
        "description": "パリッとした羽と紫蘇の香りが広がるジューシーな餃子。",
        "ingredients": [
            {"name": "豚ひき肉", "quantity": "200g"},
            {"name": "紫蘇の葉", "quantity": "10枚"},
            {"name": "餃子の皮", "quantity": "20枚"},
            {"name": "にんにく", "quantity": "1片"},
            {"name": "しょうが", "quantity": "1片"},
            {"name": "片栗粉", "quantity": "小さじ1"},
            {"name": "しょうゆ", "quantity": "大さじ1"},
            {"name": "ごま油", "quantity": "小さじ1"},
            {"name": "サラダ油", "quantity": "適量"}
        ],
        "steps": [
            "豚ひき肉に刻んだ紫蘇、にんにく、しょうが、調味料を加えて混ぜる。",
            "餃子の皮に具を包む。",
            "フライパンに油を熱し、餃子を並べて焼く。",
            "水を加え蓋をし、蒸し焼きにする。",
            "水がなくなったら羽ができるまで焼き上げる。"
        ],
        "points": "紫蘇の香りがアクセント。羽をしっかり焼くとパリッと仕上がります。",
        "img": "/public/images/dishes/dish33.jpg",
        "onCalendar": True,
        "calendarDate": 23,
        "onCandidate": False,
        "onFavorite": True,
        "onSuggestion": True
    },

# サンプルデータ34
   {
        "title": "ぐっさん秘伝の濃厚辛口カレー!",
        "genre": "和食",
        "description": "濃厚な旨味とスパイスの辛さが絶妙に絡み合う秘伝のカレー。",
        "ingredients": [
            {"name": "牛肉", "quantity": "300g"},
            {"name": "玉ねぎ", "quantity": "2個"},
            {"name": "じゃがいも", "quantity": "2個"},
            {"name": "にんじん", "quantity": "1本"},
            {"name": "カレールー", "quantity": "1箱"},
            {"name": "赤唐辛子", "quantity": "2本"},
            {"name": "にんにく", "quantity": "1片"},
            {"name": "しょうが", "quantity": "1片"},
            {"name": "水", "quantity": "800ml"}
        ],
        "steps": [
            "牛肉を一口大に切り、塩胡椒で下味をつける。",
            "玉ねぎ、じゃがいも、にんじんを食べやすい大きさに切る。",
            "鍋に油を熱し、にんにくとしょうがを炒め、牛肉を加えて焼き色をつける。",
            "野菜を加えて炒め、水を加えて煮込む。",
            "カレールーと赤唐辛子を加えてさらに煮込む。"
        ],
        "points": "煮込む時間が長いほど、牛肉が柔らかくなり旨味が増します。",
        "img": "/public/images/dishes/dish34.jpg",
        "onCalendar": True,
        "calendarDate": 31,
        "onCandidate": False,
        "onFavorite": True,
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
        # ingredientsをJSON文字列に変換
        formatted_ingredients = json.dumps(recipe["ingredients"], ensure_ascii=False)

        cursor.execute(insert_query, (
            recipe["title"],
            recipe["genre"],
            recipe["description"],
            formatted_ingredients,  # JSON形式で格納
            "\n".join(recipe["steps"]),
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
