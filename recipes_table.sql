-- MySQL dump 10.13  Distrib 5.7.24, for osx11.1 (x86_64)
--
-- Host: localhost    Database: recipes_table
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes` (
  `recipeid` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `genre` varchar(255) NOT NULL,
  `description` text,
  `ingredients` text,
  `steps` text,
  `points` text,
  `img` varchar(255) DEFAULT NULL,
  `onCalendar` tinyint(1) DEFAULT '0',
  `calendarDate` int DEFAULT NULL,
  `onCandidate` tinyint(1) DEFAULT '0',
  `onFavorite` tinyint(1) DEFAULT '0',
  `onSuggestion` tinyint(1) DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`recipeid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (1,'ふわっととろける！牛肉と玉ねぎのオムレツ炒め','和食','とろり卵が牛肉とたまねぎを包み込み、まるでオムレツのような満足感。仕上げに醤油をひとたらしで香ばしさアップ！','キ\nャ\nベ\nツ\n:\n \n1\n/\n4\n玉\n,\n牛\n肉\n \n(\n薄\n切\nり\n)\n:\n \n2\n0\n0\ng\n,\n玉\nね\nぎ\n:\n \n1\n/\n2\n個\n,\nピ\nー\nマ\nン\n:\n \n2\n個\n,\n卵\n:\n \n2\n個\n,\n醤\n油\n:\n \n大\nさ\nじ\n2\n,\nサ\nラ\nダ\n油\n:\n \n大\nさ\nじ\n1\n,\n塩\n:\n \n適\n量\n,\n胡\n椒\n:\n \n適\n量','キャベツはざく切り、玉ねぎは薄切りにする。\nフライパンにサラダ油を熱し、牛肉を炒める。\n野菜を加え、調味料で味付けする。\n卵を溶いて加え、炒め合わせる。\n仕上げにごま油を少量加える。','卵を入れることで、オムレツのような触感が楽しめます。醤油ベースの味付けが、野菜と牛肉のうまみを引き出します。','/public/images/dishes/dish1.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(2,'シャキシャキ食感！香ばしいきんぴらごぼう','和食','シャキシャキしたごぼうと甘辛い味付けが絶品！お弁当や副菜にもぴったりです。','ご\nぼ\nう\n:\n \n1\n本\n,\nに\nん\nじ\nん\n:\n \n1\n/\n2\n本\n,\n醤\n油\n:\n \n大\nさ\nじ\n2\n,\nみ\nり\nん\n:\n \n大\nさ\nじ\n1\n,\n砂\n糖\n:\n \n大\nさ\nじ\n1\n,\nご\nま\n油\n:\n \n大\nさ\nじ\n1\n,\nい\nり\nご\nま\n:\n \n適\n量','ごぼうとにんじんを千切りにする。\nフライパンにごま油を熱し、ごぼうとにんじんを炒める。\n醤油、みりん、砂糖を加え、汁気がなくなるまで炒める。\n仕上げにいりごまを振る。','ごぼうのアクを抜くため、切ったらすぐに水にさらしましょう。','/public/images/dishes/dish2.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(3,'ほっこり幸せ！おふくろの味・肉じゃが','和食','ほっこり甘辛い味付けで、ごはんが進む家庭の定番料理。','牛\n肉\n:\n \n2\n0\n0\ng\n,\nじ\nゃ\nが\nい\nも\n:\n \n3\n個\n,\nに\nん\nじ\nん\n:\n \n1\n本\n,\n玉\nね\nぎ\n:\n \n1\n個\n,\n醤\n油\n:\n \n大\nさ\nじ\n3\n,\nみ\nり\nん\n:\n \n大\nさ\nじ\n2\n,\n砂\n糖\n:\n \n大\nさ\nじ\n2\n,\nだ\nし\n汁\n:\n \n3\n0\n0\nm\nl','材料を一口大に切る。\n鍋で牛肉と玉ねぎを炒める。\nじゃがいもとにんじんを加え、だし汁を入れて煮る。\n醤油、みりん、砂糖で味付けし、煮汁が少なくなるまで煮る。','煮る際に落し蓋をすると、味が均一に染み込みます。','/public/images/dishes/dish3.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(4,'とろふわ卵がたまらない！絶品親子丼','和食','ふわふわの卵と鶏肉の組み合わせが絶妙な丼ぶり。','鶏\n肉\n:\n \n1\n5\n0\ng\n,\n卵\n:\n \n2\n個\n,\n玉\nね\nぎ\n:\n \n1\n/\n2\n個\n,\n醤\n油\n:\n \n大\nさ\nじ\n2\n,\nみ\nり\nん\n:\n \n大\nさ\nじ\n2\n,\n砂\n糖\n:\n \n大\nさ\nじ\n1\n,\nだ\nし\n汁\n:\n \n1\n0\n0\nm\nl\n,\nご\nは\nん\n:\n \n2\n膳','鶏肉と玉ねぎを一口大に切る。\n鍋にだし汁、醤油、みりん、砂糖を入れて煮立てる。\n鶏肉と玉ねぎを煮て、卵でとじる。\nごはんに乗せて完成。','卵を2回に分けて入れると、ふんわり仕上がります。','/public/images/dishes/dish4.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(5,'寒い12月でも体ポカポカビーフシチュー','洋食','牛肉がほろほろになるまで煮込んだ、濃厚なデミグラスソースのビーフシチュー。','牛\n肉\n \n(\nシ\nチ\nュ\nー\n用\n)\n:\n \n3\n0\n0\ng\n,\nじ\nゃ\nが\nい\nも\n:\n \n2\n個\n,\nに\nん\nじ\nん\n:\n \n1\n本\n,\n玉\nね\nぎ\n:\n \n1\n個\n,\nデ\nミ\nグ\nラ\nス\nソ\nー\nス\n:\n \n3\n0\n0\nm\nl\n,\n赤\nワ\nイ\nン\n:\n \n1\n0\n0\nm\nl\n,\nバ\nタ\nー\n:\n \n大\nさ\nじ\n2\n,\n小\n麦\n粉\n:\n \n大\nさ\nじ\n1\n,\n塩\n:\n \n適\n量\n,\n胡\n椒\n:\n \n適\n量','牛肉に塩・胡椒をし、小麦粉をまぶす。\n鍋でバターを溶かし、牛肉を焼き色がつくまで焼く。\n玉ねぎ、にんじん、じゃがいもを加えて炒める。\n赤ワインを加え、アルコールを飛ばしたらデミグラスソースを加え、弱火で煮込む。\n牛肉が柔らかくなったら完成。','赤ワインで煮込むことで、コクが深まります。','/public/images/dishes/dish5.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(6,'ふわとろ卵の魔法！絶品オムライス','洋食','ふわふわ卵で包んだケチャップライスが絶品！大人も子供も大好きな一品。','ご\nは\nん\n:\n \n2\n膳\n分\n,\n鶏\n肉\n:\n \n1\n0\n0\ng\n,\n玉\nね\nぎ\n:\n \n1\n/\n2\n個\n,\nケ\nチ\nャ\nッ\nプ\n:\n \n大\nさ\nじ\n4\n,\n卵\n:\n \n2\n個\n,\nバ\nタ\nー\n:\n \n大\nさ\nじ\n1\n,\n塩\n:\n \n適\n量\n,\n胡\n椒\n:\n \n適\n量','鶏肉と玉ねぎを一口大に切る。\nフライパンでバターを溶かし、鶏肉と玉ねぎを炒める。\nごはんとケチャップを加え、炒め合わせる。\n別のフライパンで卵を焼き、ごはんを包む。\nお好みでケチャップをかける。','卵は半熟に仕上げるとふんわり感がアップします。','/public/images/dishes/dish6.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(7,'ジュワッと肉汁あふれる！王道ハンバーグ','洋食','ジューシーでふっくらとした定番ハンバーグ。特製ソースでさらに美味しく！','合\nい\n挽\nき\n肉\n:\n \n3\n0\n0\ng\n,\n玉\nね\nぎ\n:\n \n1\n個\n,\n卵\n:\n \n1\n個\n,\nパ\nン\n粉\n:\n \n大\nさ\nじ\n4\n,\n牛\n乳\n:\n \n大\nさ\nじ\n2\n,\n塩\n:\n \n適\n量\n,\n胡\n椒\n:\n \n適\n量\n,\nナ\nツ\nメ\nグ\n:\n \n少\n々\n,\nサ\nラ\nダ\n油\n:\n \n大\nさ\nじ\n1','玉ねぎをみじん切りにし、炒めて冷ます。\n合い挽き肉、玉ねぎ、卵、パン粉、牛乳、調味料を混ぜる。\n小判型に成形し、真ん中をくぼませる。\nフライパンで両面を焼き、中まで火を通す。\nお好みのソースで仕上げる。','肉ダネは冷蔵庫で少し寝かせると、味が馴染みます。','/public/images/dishes/dish7.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(8,'濃厚クリーミー！本格カルボナーラ','洋食','濃厚なチーズとベーコンの旨味が絡む、クリーミーなパスタ。','パ\nス\nタ\n:\n \n2\n0\n0\ng\n,\nベ\nー\nコ\nン\n:\n \n1\n0\n0\ng\n,\n卵\n:\n \n2\n個\n,\n生\nク\nリ\nー\nム\n:\n \n1\n0\n0\nm\nl\n,\n粉\nチ\nー\nズ\n:\n \n大\nさ\nじ\n4\n,\n塩\n:\n \n適\n量\n,\n胡\n椒\n:\n \n適\n量\n,\nオ\nリ\nー\nブ\nオ\nイ\nル\n:\n \n大\nさ\nじ\n1','ベーコンを細切りにし、オリーブオイルで炒める。\nパスタを茹でる。\nボウルで卵、生クリーム、粉チーズ、塩・胡椒を混ぜる。\n茹で上がったパスタをベーコンと和え、卵液を加える。\n手早く混ぜ、余熱でとろりと仕上げる。','余熱で卵液を固めることで、クリーミーに仕上がります。','/public/images/dishes/dish8.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(9,'しびれる辛さ！本格四川麻婆豆腐','中華','ピリッと辛くてごはんが進む定番中華料理。豆腐とひき肉の旨味がたっぷり！','木\n綿\n豆\n腐\n:\n \n1\n丁\n,\n豚\nひ\nき\n肉\n:\n \n1\n5\n0\ng\n,\n長\nね\nぎ\n:\n \n1\n/\n2\n本\n,\n豆\n板\n醤\n:\n \n大\nさ\nじ\n1\n,\n甜\n麺\n醤\n:\n \n大\nさ\nじ\n1\n,\nし\nょ\nう\nゆ\n:\n \n大\nさ\nじ\n2\n,\n酒\n:\n \n大\nさ\nじ\n1\n,\n水\n:\n \n1\n5\n0\nm\nl\n,\n鶏\nが\nら\nス\nー\nプ\nの\n素\n:\n \n小\nさ\nじ\n1\n,\n片\n栗\n粉\n:\n \n大\nさ\nじ\n1\n,\nご\nま\n油\n:\n \n大\nさ\nじ\n1\n,\n花\n椒\n:\n \n適\n量','豆腐を一口大に切り、熱湯で軽く茹でて水気を切る。\nフライパンにごま油を熱し、豚ひき肉を炒める。\n豆板醤と甜麺醤を加えてさらに炒める。\n水、しょうゆ、酒、鶏がらスープの素を加え、豆腐を入れる。\n水溶き片栗粉でとろみをつけ、花椒を振る。','花椒を加えることで本格的な痺れる辛さが楽しめます。','/public/images/dishes/dish9.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(10,'シャキッと旨い！ピーマンたっぷり青椒肉絲','中華','シャキシャキのピーマンと細切り豚肉の絶妙な組み合わせ。ごはんにぴったりの炒め物。','豚\n肉\n \n(\n細\n切\nり\n)\n:\n \n2\n0\n0\ng\n,\nピ\nー\nマ\nン\n:\n \n3\n個\n,\nた\nけ\nの\nこ\n \n(\n細\n切\nり\n)\n:\n \n1\n0\n0\ng\n,\nし\nょ\nう\nゆ\n:\n \n大\nさ\nじ\n2\n,\n酒\n:\n \n大\nさ\nじ\n1\n,\nオ\nイ\nス\nタ\nー\nソ\nー\nス\n:\n \n大\nさ\nじ\n1\n,\n片\n栗\n粉\n:\n \n大\nさ\nじ\n1\n,\nサ\nラ\nダ\n油\n:\n \n大\nさ\nじ\n2\n,\n塩\n:\n \n少\n々\n,\n胡\n椒\n:\n \n少\n々','豚肉に塩、胡椒、片栗粉をまぶす。\nピーマンとたけのこを細切りにする。\nフライパンにサラダ油を熱し、豚肉を炒める。\nピーマンとたけのこを加え、しょうゆ、酒、オイスターソースで味付けする。\n全体に味がなじんだら完成。','具材は手早く炒めてシャキシャキ感を残しましょう。','/public/images/dishes/dish10.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(11,'甘酸っぱさがやみつき！彩り酢豚','中華','甘酸っぱいタレが絡む、ジューシーな豚肉と野菜の炒め物。','豚\n肩\nロ\nー\nス\n肉\n:\n \n2\n0\n0\ng\n,\n玉\nね\nぎ\n:\n \n1\n/\n2\n個\n,\nピ\nー\nマ\nン\n:\n \n2\n個\n,\nに\nん\nじ\nん\n:\n \n1\n/\n2\n本\n,\nパ\nイ\nナ\nッ\nプ\nル\n:\n \n5\n0\ng\n,\n片\n栗\n粉\n:\n \n大\nさ\nじ\n2\n,\n酢\n:\n \n大\nさ\nじ\n2\n,\nし\nょ\nう\nゆ\n:\n \n大\nさ\nじ\n2\n,\n砂\n糖\n:\n \n大\nさ\nじ\n3\n,\nケ\nチ\nャ\nッ\nプ\n:\n \n大\nさ\nじ\n2\n,\nサ\nラ\nダ\n油\n:\n \n大\nさ\nじ\n2','豚肉を一口大に切り、片栗粉をまぶす。\n野菜とパイナップルを食べやすい大きさに切る。\nフライパンで豚肉を揚げ焼きにする。\n野菜を加えて炒め、酢、しょうゆ、砂糖、ケチャップを混ぜたタレを加える。\n全体を炒め合わせて完成。','パイナップルを入れると甘みと酸味が引き立ちます。','public/images/dishes/dish11.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(12,'コク旨ピリ辛！クセになる担々麺','中華','ピリ辛ごまスープが癖になる本格的な担々麺。','中\n華\n麺\n:\n \n1\n玉\n,\n豚\nひ\nき\n肉\n:\n \n1\n0\n0\ng\n,\n長\nね\nぎ\n:\n \n1\n/\n2\n本\n,\nに\nん\nに\nく\n:\n \n1\n片\n,\nし\nょ\nう\nが\n:\n \n1\n片\n,\n豆\n板\n醤\n:\n \n小\nさ\nじ\n1\n,\n練\nり\nご\nま\n:\n \n大\nさ\nじ\n2\n,\nし\nょ\nう\nゆ\n:\n \n大\nさ\nじ\n2\n,\n鶏\nが\nら\nス\nー\nプ\n:\n \n3\n0\n0\nm\nl\n,\nラ\nー\n油\n:\n \n適\n量\n,\nご\nま\n油\n:\n \n大\nさ\nじ\n1','にんにく、しょうが、長ねぎをみじん切りにする。\nフライパンでごま油を熱し、豚ひき肉、にんにく、しょうがを炒める。\n豆板醤、しょうゆ、練りごまを加えて炒める。\n鶏がらスープを加え、ひと煮立ちさせる。\n茹でた中華麺にスープを注ぎ、長ねぎとラー油を加える。','仕上げにラー油をたっぷり加えると、辛さと香りが際立ちます。','/public/images/dishes/dish12.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(13,'香り立つバジル！本格ガパオライス','その他','タイの定番料理！バジルの香りとピリ辛のひき肉炒めがごはんと相性抜群。','鶏\nひ\nき\n肉\n:\n \n2\n0\n0\ng\n,\nパ\nプ\nリ\nカ\n:\n \n1\n/\n2\n個\n,\nピ\nー\nマ\nン\n:\n \n1\n個\n,\nに\nん\nに\nく\n:\n \n1\n片\n,\n赤\n唐\n辛\n子\n:\n \n1\n本\n,\nバ\nジ\nル\n:\n \n一\n掴\nみ\n,\nナ\nン\nプ\nラ\nー\n:\n \n大\nさ\nじ\n2\n,\nオ\nイ\nス\nタ\nー\nソ\nー\nス\n:\n \n大\nさ\nじ\n1\n,\n砂\n糖\n:\n \n小\nさ\nじ\n1\n,\nサ\nラ\nダ\n油\n:\n \n大\nさ\nじ\n1\n,\n卵\n:\n \n1\n個\n,\nご\nは\nん\n:\n \n1\n膳\n分','にんにくと赤唐辛子をみじん切りにする。\nフライパンにサラダ油を熱し、にんにくと唐辛子を炒める。\n鶏ひき肉を加え、パプリカとピーマンも炒める。\nナンプラー、オイスターソース、砂糖で味付けし、バジルを加える。\n目玉焼きを作り、ごはんと一緒に盛り付ける。','バジルはたっぷり加えると風味が引き立ちます。辛さはお好みで調整してください。','/public/images/dishes/dish13.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(14,'スパイス香る！ジューシータンドリーチキン','その他','スパイスとヨーグルトで漬け込んだ、香ばしく焼き上げるインド風チキン。','鶏\nも\nも\n肉\n:\n \n2\n枚\n,\nプ\nレ\nー\nン\nヨ\nー\nグ\nル\nト\n:\n \n1\n0\n0\ng\n,\nに\nん\nに\nく\n:\n \n1\n片\n,\nし\nょ\nう\nが\n:\n \n1\n片\n,\nカ\nレ\nー\n粉\n:\n \n大\nさ\nじ\n1\n,\nパ\nプ\nリ\nカ\nパ\nウ\nダ\nー\n:\n \n小\nさ\nじ\n1\n,\n塩\n:\n \n小\nさ\nじ\n1\n,\nレ\nモ\nン\n汁\n:\n \n大\nさ\nじ\n1\n,\nサ\nラ\nダ\n油\n:\n \n大\nさ\nじ\n1','にんにく、しょうがをすりおろす。\nヨーグルト、カレー粉、パプリカパウダー、塩、レモン汁、にんにく、しょうがを混ぜる。\n鶏肉を漬け込み、冷蔵庫で2時間寝かせる。\nオーブンで200℃で20分焼く。\n焼き色がついたら完成。','しっかり漬け込むことで、風味豊かな仕上がりになります。','/public/images/dishes/dish14.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(15,'香り豊か！あっさり鶏だしフォー','その他','あっさりした鶏だしが効いた、ベトナムの定番ライスヌードルスープ。','フ\nォ\nー\n麺\n:\n \n1\n0\n0\ng\n,\n鶏\nむ\nね\n肉\n:\n \n1\n5\n0\ng\n,\nも\nや\nし\n:\n \n5\n0\ng\n,\n青\nね\nぎ\n:\n \n2\n本\n,\nパ\nク\nチ\nー\n:\n \n適\n量\n,\n鶏\nが\nら\nス\nー\nプ\n:\n \n5\n0\n0\nm\nl\n,\nナ\nン\nプ\nラ\nー\n:\n \n大\nさ\nじ\n1\n,\n塩\n:\n \n小\nさ\nじ\n1\n,\nラ\nイ\nム\n:\n \n1\n/\n2\n個\n,\n赤\n唐\n辛\n子\n:\n \n1\n本','鶏むね肉を茹で、細かく裂く。\n鶏がらスープにナンプラーと塩を加えて温める。\nフォー麺を茹で、器に盛る。\n鶏肉、もやし、青ねぎ、パクチーをトッピングする。\nスープを注ぎ、ライムを添える。','お好みでライムや唐辛子を加えて、さっぱりとした味わいを楽しんでください。','public/images/dishes/dish15.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01'),(16,'カリッとあなたも包み込む！?メキシカン風タコス','その他','スパイス香るひき肉とフレッシュな野菜をトルティーヤで包んだ、メキシコの人気料理。','ト\nル\nテ\nィ\nー\nヤ\n:\n \n4\n枚\n,\n牛\nひ\nき\n肉\n:\n \n2\n0\n0\ng\n,\n玉\nね\nぎ\n:\n \n1\n/\n2\n個\n,\nト\nマ\nト\n:\n \n1\n個\n,\nレ\nタ\nス\n:\n \n2\n枚\n,\nチ\nー\nズ\n:\n \n5\n0\ng\n,\nサ\nル\nサ\nソ\nー\nス\n:\n \n大\nさ\nじ\n2\n,\nタ\nコ\nミ\nー\nト\nシ\nー\nズ\nニ\nン\nグ\n:\n \n大\nさ\nじ\n1\n,\nサ\nラ\nダ\n油\n:\n \n大\nさ\nじ\n1','玉ねぎとトマトをみじん切りにし、レタスは千切りにする。\nフライパンにサラダ油を熱し、牛ひき肉とタコミートシーズニングを炒める。\nトルティーヤを軽く温める。\nひき肉、野菜、チーズをトルティーヤに乗せ、サルサソースをかける。\nトルティーヤで包んで完成。','具材はお好みでアボカドやハラペーニョを加えても美味しいです。','/public/images/dishes/dish16.jpg',NULL,NULL,NULL,NULL,0,'2024-12-08 12:51:01','2024-12-08 12:51:01');
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-08 13:05:54
