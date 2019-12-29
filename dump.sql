DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `django_migrations` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `app` varchar(255) NOT NULL, `name` varchar(255) NOT NULL, `applied` datetime NOT NULL);

INSERT INTO django_migrations VALUES(1,`allUsers`,`0001_initial`,`2019-12-28 13:44:15.482915`);

INSERT INTO django_migrations VALUES(2,'account','0001_initial','2019-12-28 13:44:15.510961');

INSERT INTO django_migrations VALUES(3,'account','0002_email_max_length','2019-12-28 13:44:15.541058');

INSERT INTO django_migrations VALUES(4,'contenttypes','0001_initial','2019-12-28 13:44:15.562297');

INSERT INTO django_migrations VALUES(5,'admin','0001_initial','2019-12-28 13:44:15.591395');

INSERT INTO django_migrations VALUES(6,'admin','0002_logentry_remove_auto_add','2019-12-28 13:44:15.619059');

INSERT INTO django_migrations VALUES(7,'admin','0003_logentry_add_action_flag_choices','2019-12-28 13:44:15.643260');

INSERT INTO django_migrations VALUES(8,'allUsers','0002_auto_20191226_1212','2019-12-28 13:44:15.666534');

INSERT INTO django_migrations VALUES(9,'allUsers','0003_auto_20191226_1213','2019-12-28 13:44:15.689988');

INSERT INTO django_migrations VALUES(10,'allUsers','0004_auto_20191227_1318','2019-12-28 13:44:15.717227');

INSERT INTO django_migrations VALUES(11,'allUsers','0005_auto_20191228_0736','2019-12-28 13:44:15.738415');

INSERT INTO django_migrations VALUES(12,'allUsers','0006_auto_20191228_0917','2019-12-28 13:44:15.762636');

INSERT INTO django_migrations VALUES(13,'allUsers','0007_auto_20191228_1344','2019-12-28 13:44:15.800334');

INSERT INTO django_migrations VALUES(14,'contenttypes','0002_remove_content_type_name','2019-12-28 13:44:15.840121');

INSERT INTO django_migrations VALUES(15,'auth','0001_initial','2019-12-28 13:44:15.889722');

INSERT INTO django_migrations VALUES(16,'auth','0002_alter_permission_name_max_length','2019-12-28 13:44:15.919365');

INSERT INTO django_migrations VALUES(17,'auth','0003_alter_user_email_max_length','2019-12-28 13:44:15.935730');

INSERT INTO django_migrations VALUES(18,'auth','0004_alter_user_username_opts','2019-12-28 13:44:15.949351');

INSERT INTO django_migrations VALUES(19,'auth','0005_alter_user_last_login_null','2019-12-28 13:44:15.964909');

INSERT INTO django_migrations VALUES(20,'auth','0006_require_contenttypes_0002','2019-12-28 13:44:15.970405');

INSERT INTO django_migrations VALUES(21,'auth','0007_alter_validators_add_error_messages','2019-12-28 13:44:15.987659');

INSERT INTO django_migrations VALUES(22,'auth','0008_alter_user_username_max_length','2019-12-28 13:44:16.006245');

INSERT INTO django_migrations VALUES(23,'auth','0009_alter_user_last_name_max_length','2019-12-28 13:44:16.021392');

INSERT INTO django_migrations VALUES(24,'authtoken','0001_initial','2019-12-28 13:44:16.049299');

INSERT INTO django_migrations VALUES(25,'authtoken','0002_auto_20160226_1747','2019-12-28 13:44:16.118243');

INSERT INTO django_migrations VALUES(26,'category','0001_initial','2019-12-28 13:44:16.138958');

INSERT INTO django_migrations VALUES(27,'products','0001_initial','2019-12-28 13:44:16.210755');

INSERT INTO django_migrations VALUES(28,'cart','0001_initial','2019-12-28 13:44:16.248403');

INSERT INTO django_migrations VALUES(29,'cart','0002_auto_20191226_1344','2019-12-28 13:44:16.281562');

INSERT INTO django_migrations VALUES(30,'category','0002_auto_20191226_1344','2019-12-28 13:44:16.311519');

INSERT INTO django_migrations VALUES(31,'products','0002_auto_20191226_1344','2019-12-28 13:44:16.349085');

INSERT INTO django_migrations VALUES(32,'sessions','0001_initial','2019-12-28 13:44:16.361930');

INSERT INTO django_migrations VALUES(33,'sites','0001_initial','2019-12-28 13:44:16.380614');

INSERT INTO django_migrations VALUES(34,'sites','0002_alter_domain_unique','2019-12-28 13:44:16.402172');

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `account_emailconfirmation` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `created` datetime NOT NULL, `sent` datetime NULL, `key` varchar(64) NOT NULL UNIQUE, `email_address_id` integer NOT NULL REFERENCES `account_emailaddress` (`id`) DEFERRABLE INITIALLY DEFERRED);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `account_emailaddress` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `verified` bool NOT NULL, `primary` bool NOT NULL, `user_id` integer NOT NULL REFERENCES `allUsers_account` (`id`) DEFERRABLE INITIALLY DEFERRED, `email` varchar(254) NOT NULL UNIQUE);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `django_admin_log` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `action_time` datetime NOT NULL, `object_id` text NULL, `object_repr` varchar(200) NOT NULL, `change_message` text NOT NULL, `content_type_id` integer NULL REFERENCES `django_content_type` (`id`) DEFERRABLE INITIALLY DEFERRED, `user_id` integer NOT NULL REFERENCES `allUsers_account` (`id`) DEFERRABLE INITIALLY DEFERRED, `action_flag` smallint unsigned NOT NULL);

INSERT INTO django_admin_log VALUES(1,`2019-12-28 16:43:11.131964`,`7`,`7 - 3 - budikarya@buildup.com - budikarya - 3 - Pasir Abu Batu`,``,13,1,3);

INSERT INTO django_admin_log VALUES(2,'2019-12-29 05:42:44.588450','1','1 - 2 - anugrah@buildup.com - anugrah - 3 - Asia Tile Alpha Black - Asia_Tile_Alpha_Black_25x25.jpeg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(3,'2019-12-29 05:43:06.192708','2','2 - 3 - budikarya@buildup.com - budikarya - 3 - BlackBull - Black-Bull.png','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(4,'2019-12-29 05:43:33.622985','3','3 - 3 - budikarya@buildup.com - budikarya - 3 - Cat Paragon Putih - catparagon.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(5,'2019-12-29 05:43:46.582360','4','4 - 3 - budikarya@buildup.com - budikarya - 3 - Cat Catylac - CATYLAC_INTERIOR_5KG-500x500.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(6,'2019-12-29 05:44:06.035531','5','5 - 3 - budikarya@buildup.com - budikarya - 3 - Pipa PVC - pipa.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(7,'2019-12-29 05:44:24.482410','6','6 - 3 - budikarya@buildup.com - budikarya - 3 - Bata Merah - batu-bata.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(8,'2019-12-29 05:44:37.233365','7','8 - 3 - budikarya@buildup.com - budikarya - 3 - Pasir Abu Batu - psir_abu_batu.PNG','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(9,'2019-12-29 05:44:53.963670','8','9 - 3 - budikarya@buildup.com - budikarya - 3 - Tang Kombinasi - Tekiro-8-Tang-Kombinasi.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(10,'2019-12-29 05:45:25.693084','9','10 - 4 - warnajaya@buildup.com - warnajaya - 3 - Pasir Abu Batu - abubatu-msk.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(11,'2019-12-29 05:45:39.937766','10','11 - 4 - warnajaya@buildup.com - warnajaya - 3 - Batu Bata Merah - bata-merah2.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(12,'2019-12-29 05:45:53.606098','11','12 - 4 - warnajaya@buildup.com - warnajaya - 3 - Cat Avitex Warna Kuning - avite.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(13,'2019-12-29 05:46:01.817325','12','13 - 4 - warnajaya@buildup.com - warnajaya - 3 - Cat No Drop - no_drop.png','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(14,'2019-12-29 05:46:35.033931','13','14 - 5 - sahabat@buildup.com - sahabat - 3 - Bata Ringan Hebel Bata Putih - bata_putih.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(15,'2019-12-29 05:47:00.061121','14','15 - 5 - sahabat@buildup.com - sahabat - 3 - Semen 3 roda TR30 acian putih - semene_iki.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(16,'2019-12-29 05:47:22.685231','15','16 - 5 - sahabat@buildup.com - sahabat - 3 - Pasir Hitam Cor - pasir_hitam.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(17,'2019-12-29 05:47:36.357176','16','17 - 5 - sahabat@buildup.com - sahabat - 3 - Catut / Tang serbaguna - tang.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(18,'2019-12-29 05:47:48.537006','17','18 - 5 - sahabat@buildup.com - sahabat - 3 - Paragon Warna Putih - paragon_puti.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(19,'2019-12-29 05:48:01.963675','18','19 - 5 - sahabat@buildup.com - sahabat - 3 - Sambungan Pipa PVC - pipa_VoQ8Y5k.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(20,'2019-12-29 05:48:22.934523','19','20 - 6 - matahari@buildup.com - matahari - 3 - Semen Gresik - smen.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(21,'2019-12-29 05:48:33.610284','20','21 - 6 - matahari@buildup.com - matahari - 3 - Cat Avitex warna kuning - cat_tembok_avitex_interior_avian_klikcat.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(22,'2019-12-29 05:48:42.862912','21','22 - 6 - matahari@buildup.com - matahari - 3 - Kayu Kamper - Apa-Kayu-Kamper.jpg','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(23,'2019-12-29 05:48:56.625119','22','23 - 6 - matahari@buildup.com - matahari - 3 - Pasir Batu - 900040_699ab0c3-89af-4083-9b26-2f049f83a899_1080_1080.png','[{"added": {}}]',12,1,1);

INSERT INTO django_admin_log VALUES(24,'2019-12-29 05:49:08.235467','23','24 - 6 - matahari@buildup.com - matahari - 3 - Bata Merah - Bata_Merah_Berkualitas.jpg','[{"added": {}}]',12,1,1);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `allUsers_account` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `password` varchar(128) NOT NULL, `email` varchar(60) NOT NULL UNIQUE, `username` varchar(30) NOT NULL UNIQUE, `date_joined` datetime NOT NULL, `last_login` datetime NOT NULL, `is_admin` bool NOT NULL, `is_active` bool NOT NULL, `is_staff` bool NOT NULL, `is_superuser` bool NOT NULL, `role` integer NULL, `nik` varchar(20) NOT NULL, `name` varchar(50) NOT NULL, `address` varchar(500) NOT NULL, `phone` varchar(50) NOT NULL);

INSERT INTO allUsers_account VALUES(1,`pbkdf2_sha256$120000$SvqNqpaebSMk$ur013sKiaDi8zZSdhnuF4eGPIEYMQIkT1FMEyjJ3U6g=`,`dev@dev.com`,`dev`,`2019-12-28 13:52:55.038255`,`2019-12-29 05:39:37.052023`,1,1,1,1,NULL,``,``,``,``);

INSERT INTO allUsers_account VALUES(2,'pbkdf2_sha256$120000$m0KA39tqedos$uSiUPrzeAp6MdfaqylTfn9KZyIUcvkzCIcH7l3T+0zY=','anugrah@buildup.com','anugrah','2019-12-28 13:59:51.645773','2019-12-28 13:59:51.645846',0,1,0,0,3,'083846617708','Anugrah Bangunan Baliwerti','Jl. Baliwerti No.98, Alun-alun Contong, Kec. Bubutan, Kota SBY, Jawa Timur 60174','(031) 5451819');

INSERT INTO allUsers_account VALUES(3,'pbkdf2_sha256$120000$VGZlpQdudkIP$Oa7UGHKDmeZObOUXTYJ2UXCrGoCNli2Cw9L4wMyGtpk=','budikarya@buildup.com','budikarya','2019-12-28 14:01:19.436406','2019-12-28 14:01:19.436458',0,1,0,0,3,'083846617708','TB Budi Karya','Jl. Keputih Tegal No.16, Keputih, Kec. Sukolilo, Kota SBY, Jawa Timur 60111','(031) 5911691');

INSERT INTO allUsers_account VALUES(4,'pbkdf2_sha256$120000$6I4Bz9HZaEA3$AnkRSnK+1UsyZYxG45fvg6dqlYJRhAAZEki6+kTnDSU=','warnajaya@buildup.com','warnajaya','2019-12-28 14:03:03.532704','2019-12-28 14:03:03.532759',0,1,0,0,3,'08113466898','Toko Warna Jaya','Jl. Keputih Utara No.57, Keputih, Kec. Sukolilo, Kota SBY, Jawa Timur 60111','0811-3466-898');

INSERT INTO allUsers_account VALUES(5,'pbkdf2_sha256$120000$NLnimou1e5Wd$jEt98/P6Tjrb9NKkJ711R/eKw+ewA3U93nypx73z99Y=','sahabat@buildup.com','sahabat','2019-12-28 14:04:47.866125','2019-12-28 14:04:47.866195',0,1,0,0,3,'083846617708','Toko Sahabat','Gebang Putih No.74, Gebang Putih, Kec. Sukolilo, Kota SBY, Jawa Timur 60117','(031) 5943601');

INSERT INTO allUsers_account VALUES(6,'pbkdf2_sha256$120000$pKqO6iaKKyhA$9VvAMtC6WvrRFaoMTGuzGNEoS3tRSEJm3uiU0Xs8LTw=','matahari@buildup.com','matahari','2019-12-28 14:06:47.642736','2019-12-28 14:06:47.642794',0,1,0,0,3,'083846617708','UD. Matahari','Jl. Arif Rahman Hakim No.71, Klampis Ngasem, Kec. Sukolilo, Kota SBY, Jawa Timur  60117','083846617708');

INSERT INTO allUsers_account VALUES(7,'pbkdf2_sha256$120000$WdIdJZeFAKvI$FXsTcH8AfjkaXpimo6XV8gmNZcYT2mcr4EYV5vUE114=','pelanggan@buildup.com','pelanggan','2019-12-28 18:26:34.275104','2019-12-28 18:26:34.275175',0,1,0,0,1,'3515070606980001','Bimo Prasetyo Afif','Gang Buntu, Kebosari, Candi, Sidoarjo','088217667185');

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `allUsers_imageuser` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `Image` varchar(100) NOT NULL, `AccId_id` integer NOT NULL REFERENCES `allUsers_account` (`id`) DEFERRABLE INITIALLY DEFERRED);

INSERT INTO allUsers_imageuser VALUES(1,`Capture_oRrz3g4.PNG`,6);

INSERT INTO allUsers_imageuser VALUES(2,'Capture_oFUBDjm.PNG',2);

INSERT INTO allUsers_imageuser VALUES(3,'gambar_toko_7cwCiHz.jpg',3);

INSERT INTO allUsers_imageuser VALUES(4,'Capture_DYZTMWq.PNG',4);

INSERT INTO allUsers_imageuser VALUES(5,'unnamed.jpg',5);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `django_content_type` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `app_label` varchar(100) NOT NULL, `model` varchar(100) NOT NULL);

INSERT INTO django_content_type VALUES(1,`admin`,`logentry`);

INSERT INTO django_content_type VALUES(2,'auth','permission');

INSERT INTO django_content_type VALUES(3,'auth','group');

INSERT INTO django_content_type VALUES(4,'contenttypes','contenttype');

INSERT INTO django_content_type VALUES(5,'sessions','session');

INSERT INTO django_content_type VALUES(6,'authtoken','token');

INSERT INTO django_content_type VALUES(7,'account','emailaddress');

INSERT INTO django_content_type VALUES(8,'account','emailconfirmation');

INSERT INTO django_content_type VALUES(9,'sites','site');

INSERT INTO django_content_type VALUES(10,'allUsers','account');

INSERT INTO django_content_type VALUES(11,'allUsers','imageuser');

INSERT INTO django_content_type VALUES(12,'products','productimages');

INSERT INTO django_content_type VALUES(13,'products','products');

INSERT INTO django_content_type VALUES(14,'category','categorys');

INSERT INTO django_content_type VALUES(15,'category','categoryshome');

INSERT INTO django_content_type VALUES(16,'cart','cart');

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `auth_group` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `name` varchar(80) NOT NULL UNIQUE);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `auth_group_permissions` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `group_id` integer NOT NULL REFERENCES `auth_group` (`id`) DEFERRABLE INITIALLY DEFERRED, `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`) DEFERRABLE INITIALLY DEFERRED);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `auth_permission` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `content_type_id` integer NOT NULL REFERENCES `django_content_type` (`id`) DEFERRABLE INITIALLY DEFERRED, `codename` varchar(100) NOT NULL, `name` varchar(255) NOT NULL);

INSERT INTO auth_permission VALUES(1,1,`add_logentry`,`Can add log entry`);

INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');

INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');

INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');

INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');

INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');

INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');

INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');

INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');

INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');

INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');

INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');

INSERT INTO auth_permission VALUES(13,4,'add_contenttype','Can add content type');

INSERT INTO auth_permission VALUES(14,4,'change_contenttype','Can change content type');

INSERT INTO auth_permission VALUES(15,4,'delete_contenttype','Can delete content type');

INSERT INTO auth_permission VALUES(16,4,'view_contenttype','Can view content type');

INSERT INTO auth_permission VALUES(17,5,'add_session','Can add session');

INSERT INTO auth_permission VALUES(18,5,'change_session','Can change session');

INSERT INTO auth_permission VALUES(19,5,'delete_session','Can delete session');

INSERT INTO auth_permission VALUES(20,5,'view_session','Can view session');

INSERT INTO auth_permission VALUES(21,6,'add_token','Can add Token');

INSERT INTO auth_permission VALUES(22,6,'change_token','Can change Token');

INSERT INTO auth_permission VALUES(23,6,'delete_token','Can delete Token');

INSERT INTO auth_permission VALUES(24,6,'view_token','Can view Token');

INSERT INTO auth_permission VALUES(25,7,'add_emailaddress','Can add email address');

INSERT INTO auth_permission VALUES(26,7,'change_emailaddress','Can change email address');

INSERT INTO auth_permission VALUES(27,7,'delete_emailaddress','Can delete email address');

INSERT INTO auth_permission VALUES(28,7,'view_emailaddress','Can view email address');

INSERT INTO auth_permission VALUES(29,8,'add_emailconfirmation','Can add email confirmation');

INSERT INTO auth_permission VALUES(30,8,'change_emailconfirmation','Can change email confirmation');

INSERT INTO auth_permission VALUES(31,8,'delete_emailconfirmation','Can delete email confirmation');

INSERT INTO auth_permission VALUES(32,8,'view_emailconfirmation','Can view email confirmation');

INSERT INTO auth_permission VALUES(33,9,'add_site','Can add site');

INSERT INTO auth_permission VALUES(34,9,'change_site','Can change site');

INSERT INTO auth_permission VALUES(35,9,'delete_site','Can delete site');

INSERT INTO auth_permission VALUES(36,9,'view_site','Can view site');

INSERT INTO auth_permission VALUES(37,10,'add_account','Can add account');

INSERT INTO auth_permission VALUES(38,10,'change_account','Can change account');

INSERT INTO auth_permission VALUES(39,10,'delete_account','Can delete account');

INSERT INTO auth_permission VALUES(40,10,'view_account','Can view account');

INSERT INTO auth_permission VALUES(41,11,'add_imageuser','Can add image user');

INSERT INTO auth_permission VALUES(42,11,'change_imageuser','Can change image user');

INSERT INTO auth_permission VALUES(43,11,'delete_imageuser','Can delete image user');

INSERT INTO auth_permission VALUES(44,11,'view_imageuser','Can view image user');

INSERT INTO auth_permission VALUES(45,12,'add_productimages','Can add product images');

INSERT INTO auth_permission VALUES(46,12,'change_productimages','Can change product images');

INSERT INTO auth_permission VALUES(47,12,'delete_productimages','Can delete product images');

INSERT INTO auth_permission VALUES(48,12,'view_productimages','Can view product images');

INSERT INTO auth_permission VALUES(49,13,'add_products','Can add products');

INSERT INTO auth_permission VALUES(50,13,'change_products','Can change products');

INSERT INTO auth_permission VALUES(51,13,'delete_products','Can delete products');

INSERT INTO auth_permission VALUES(52,13,'view_products','Can view products');

INSERT INTO auth_permission VALUES(53,14,'add_categorys','Can add categorys');

INSERT INTO auth_permission VALUES(54,14,'change_categorys','Can change categorys');

INSERT INTO auth_permission VALUES(55,14,'delete_categorys','Can delete categorys');

INSERT INTO auth_permission VALUES(56,14,'view_categorys','Can view categorys');

INSERT INTO auth_permission VALUES(57,15,'add_categoryshome','Can add categorys home');

INSERT INTO auth_permission VALUES(58,15,'change_categoryshome','Can change categorys home');

INSERT INTO auth_permission VALUES(59,15,'delete_categoryshome','Can delete categorys home');

INSERT INTO auth_permission VALUES(60,15,'view_categoryshome','Can view categorys home');

INSERT INTO auth_permission VALUES(61,16,'add_cart','Can add cart');

INSERT INTO auth_permission VALUES(62,16,'change_cart','Can change cart');

INSERT INTO auth_permission VALUES(63,16,'delete_cart','Can delete cart');

INSERT INTO auth_permission VALUES(64,16,'view_cart','Can view cart');

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `authtoken_token` (`key` varchar(40) NOT NULL PRIMARY KEY, `created` datetime NOT NULL, `user_id` integer NOT NULL UNIQUE REFERENCES `allUsers_account` (`id`) DEFERRABLE INITIALLY DEFERRED);

INSERT INTO authtoken_token VALUES(`e793496b225a6ff135c0c1c882260d74567b6a2b`,`2019-12-28 13:52:55.046895`,1);

INSERT INTO authtoken_token VALUES('f11617a61257a40b15a5561624877e3c6b815f41','2019-12-28 13:59:51.655189',2);

INSERT INTO authtoken_token VALUES('a367735a072eb311a59c7460def118d15d70ff3a','2019-12-28 14:01:19.447487',3);

INSERT INTO authtoken_token VALUES('1797b25c1c818d1271963ce4d4c3af97a63c2667','2019-12-28 14:03:03.543124',4);

INSERT INTO authtoken_token VALUES('f3ae9a72be91882e480356145543ebf53be3dc66','2019-12-28 14:04:47.875518',5);

INSERT INTO authtoken_token VALUES('addfe15327bfaf23414de091c48befa87eaae4e6','2019-12-28 14:06:47.652215',6);

INSERT INTO authtoken_token VALUES('de47d48735968608ac9048920e0cdcb7cad7cfe1','2019-12-28 18:26:34.284576',7);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `products_productimages` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `ProductImage` varchar(100) NOT NULL, `ProdId_id` integer NOT NULL REFERENCES `products_products` (`ProductId`) DEFERRABLE INITIALLY DEFERRED);

INSERT INTO products_productimages VALUES(1,`Asia_Tile_Alpha_Black_25x25.jpeg`,1);

INSERT INTO products_productimages VALUES(2,'Black-Bull.png',2);

INSERT INTO products_productimages VALUES(3,'catparagon.jpg',3);

INSERT INTO products_productimages VALUES(4,'CATYLAC_INTERIOR_5KG-500x500.jpg',4);

INSERT INTO products_productimages VALUES(5,'pipa.jpg',5);

INSERT INTO products_productimages VALUES(6,'batu-bata.jpg',6);

INSERT INTO products_productimages VALUES(7,'psir_abu_batu.PNG',8);

INSERT INTO products_productimages VALUES(8,'Tekiro-8-Tang-Kombinasi.jpg',9);

INSERT INTO products_productimages VALUES(9,'abubatu-msk.jpg',10);

INSERT INTO products_productimages VALUES(10,'bata-merah2.jpg',11);

INSERT INTO products_productimages VALUES(11,'avite.jpg',12);

INSERT INTO products_productimages VALUES(12,'no_drop.png',13);

INSERT INTO products_productimages VALUES(13,'bata_putih.jpg',14);

INSERT INTO products_productimages VALUES(14,'semene_iki.jpg',15);

INSERT INTO products_productimages VALUES(15,'pasir_hitam.jpg',16);

INSERT INTO products_productimages VALUES(16,'tang.jpg',17);

INSERT INTO products_productimages VALUES(17,'paragon_puti.jpg',18);

INSERT INTO products_productimages VALUES(18,'pipa_VoQ8Y5k.jpg',19);

INSERT INTO products_productimages VALUES(19,'smen.jpg',20);

INSERT INTO products_productimages VALUES(20,'cat_tembok_avitex_interior_avian_klikcat.jpg',21);

INSERT INTO products_productimages VALUES(21,'Apa-Kayu-Kamper.jpg',22);

INSERT INTO products_productimages VALUES(22,'900040_699ab0c3-89af-4083-9b26-2f049f83a899_1080_1080.png',23);

INSERT INTO products_productimages VALUES(23,'Bata_Merah_Berkualitas.jpg',24);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `cart_cart` (`cartId` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `quantity` integer NOT NULL, `CustomerId_id` integer NOT NULL REFERENCES `allUsers_account` (`id`) DEFERRABLE INITIALLY DEFERRED, `productId_id` integer NOT NULL REFERENCES `products_products` (`ProductId`) DEFERRABLE INITIALLY DEFERRED);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `category_categorys` (`CategoryId` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `CategoryName` varchar(50) NOT NULL);

INSERT INTO category_categorys VALUES(1,`Perkakas`);

INSERT INTO category_categorys VALUES(2,'Semen');

INSERT INTO category_categorys VALUES(3,'Pasir');

INSERT INTO category_categorys VALUES(4,'Pipa');

INSERT INTO category_categorys VALUES(5,'Cat');

INSERT INTO category_categorys VALUES(6,'Keramik');

INSERT INTO category_categorys VALUES(7,'Kayu');

INSERT INTO category_categorys VALUES(8,'Bata');

INSERT INTO category_categorys VALUES(9,'Batu');

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `category_categoryshome` (`CategoryId` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `CategoryName` varchar(50) NOT NULL);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `products_products` (`ProductId` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `ProductName` varchar(50) NOT NULL, `ProductDesc` varchar(500) NOT NULL, `ProductPrice` integer NOT NULL, `ProductStock` integer NOT NULL, `ProductSatuan` integer NOT NULL, `ProductNamaSatuan` varchar(20) NOT NULL, `ProductCategory_id` integer NOT NULL REFERENCES `category_categorys` (`CategoryId`) DEFERRABLE INITIALLY DEFERRED, `creator_id` integer NULL REFERENCES `allUsers_account` (`id`) DEFERRABLE INITIALLY DEFERRED);

INSERT INTO products_products VALUES(1,`Asia Tile Alpha Black`,`Warna Hitam, Ukuran 25 x 25`,55000,50,6,`Dus`,6,2);

INSERT INTO products_products VALUES(2,'BlackBull','Semen Black Bull kualitas terjamin, berat 40 Kg',67000,10,40,'Kg',2,3);

INSERT INTO products_products VALUES(3,'Cat Paragon Putih','Warna putih, Berat 1kg',67000,11,1,'Kg',5,3);

INSERT INTO products_products VALUES(4,'Cat Catylac','Warna putih, hitam, merah bata',109000,11,5,'Kg',5,3);

INSERT INTO products_products VALUES(5,'Pipa PVC','Warna putih,Ukuran 4 inch 40 cm',28000,9,4,'Inch',4,3);

INSERT INTO products_products VALUES(6,'Bata Merah','Batu Bata Merah (biasa)',725,2000,1,'biji',8,3);

INSERT INTO products_products VALUES(8,'Pasir Abu Batu','Pasir Abu-Abu kualitas bagus',175000,9,1,'m3',3,3);

INSERT INTO products_products VALUES(9,'Tang Kombinasi','Berat 0.5 kg,Merek Tekiro, Ukuran 8',55000,5,1,'pcs',1,3);

INSERT INTO products_products VALUES(10,'Pasir Abu Batu','Pasir Abu-Abu Batu biasa',174000,9,1,'m3',3,4);

INSERT INTO products_products VALUES(11,'Batu Bata Merah','Ukuran 10cm',760,600,1,'biji',8,4);

INSERT INTO products_products VALUES(12,'Cat Avitex Warna Kuning','Cat Avitex kualitas umum dengan warna kuning. original',98000,20,5,'Kg',5,4);

INSERT INTO products_products VALUES(13,'Cat No Drop','Cat no drop warna biru',100000,20,5,'Kg',5,4);

INSERT INTO products_products VALUES(14,'Bata Ringan Hebel Bata Putih','Batu bata ringan asli dalam negeri. 7.5cm',750000,200,1,'m3',8,5);

INSERT INTO products_products VALUES(15,'Semen 3 roda TR30 acian putih','Semen 3 roda tipe TR30 dengan warna acian putih',100000,20,40,'kg',2,5);

INSERT INTO products_products VALUES(16,'Pasir Hitam Cor','Pasir hitam stok terbatas',390000,8,1,'m3',3,5);

INSERT INTO products_products VALUES(17,'Catut / Tang serbaguna','Catut PVC Blister 9 / Tang Kakaktua / Tang gegep / Tang Jepit',42000,10,1,'pcs',1,5);

INSERT INTO products_products VALUES(18,'Paragon Warna Putih','Cat Paragon Warna putih.',97000,5,5,'kg',5,5);

INSERT INTO products_products VALUES(19,'Sambungan Pipa PVC','Tee 8 inch',50000,70,1,'pcs',4,5);

INSERT INTO products_products VALUES(20,'Semen Gresik','Berat 40 Kg',45000,10,1,'pcs',2,6);

INSERT INTO products_products VALUES(21,'Cat Avitex warna kuning','Cat merk Avitex kualitas ori',10000,20,5,'kg',5,6);

INSERT INTO products_products VALUES(22,'Kayu Kamper','Ukuran kayu 5x10',95000,15,4,'m',7,6);

INSERT INTO products_products VALUES(23,'Pasir Batu','Pasir Batu import madura',176000,15,1,'m3',3,6);

INSERT INTO products_products VALUES(24,'Bata Merah','Ukuran 10 Cm',600,900,1,'pcs',8,6);

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `django_session` (`session_key` varchar(40) NOT NULL PRIMARY KEY, `session_data` text NOT NULL, `expire_date` datetime NOT NULL);

INSERT INTO django_session VALUES(`v9b5ppvnjt2inmti03kkg3c5t1ank89n`,`ZWU0NmEwOWY1ZjM4YTdhZjgwMTVkYjUxNjFmNjRhODA2NzgxMWE5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5BbGxvd0FsbFVzZXJzTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWI1OWI1M2FiYWY3NTIxMTU1YjU2YmYxOWMxNWNhNzg3NTY0MjhjNiJ9`,`2020-01-11 13:53:06.126205`);

INSERT INTO django_session VALUES('2vylon6aa774apn1y97dp9ype2bd2qpj','ZWU0NmEwOWY1ZjM4YTdhZjgwMTVkYjUxNjFmNjRhODA2NzgxMWE5ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5BbGxvd0FsbFVzZXJzTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWI1OWI1M2FiYWY3NTIxMTU1YjU2YmYxOWMxNWNhNzg3NTY0MjhjNiJ9','2020-01-12 05:39:37.057437');

DROP TABLE IF EXISTS IF;
CREATE TABLE IF NOT EXISTS `IF` NOT EXISTS `django_site` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT AUTOINCREMENT, `name` varchar(50) NOT NULL, `domain` varchar(100) NOT NULL UNIQUE);

INSERT INTO django_site VALUES(1,`example.com`,`example.com`);

CREATE INDEX `account_emailconfirmation_email_address_id_5b7f8c58` ON `account_emailconfirmation` (`email_address_id`);

CREATE INDEX `account_emailaddress_user_id_2c513194` ON `account_emailaddress` (`user_id`);

CREATE INDEX `django_admin_log_content_type_id_c4bce8eb` ON `django_admin_log` (`content_type_id`);

CREATE INDEX `django_admin_log_user_id_c564eba6` ON `django_admin_log` (`user_id`);

CREATE INDEX `allUsers_imageuser_AccId_id_3c37e750` ON `allUsers_imageuser` (`AccId_id`);

CREATE INDEX `auth_group_permissions_group_id_b120cbf9` ON `auth_group_permissions` (`group_id`);

CREATE INDEX `auth_group_permissions_permission_id_84c5c92e` ON `auth_group_permissions` (`permission_id`);

CREATE INDEX `auth_permission_content_type_id_2f476e4b` ON `auth_permission` (`content_type_id`);

CREATE INDEX `products_productimages_ProdId_id_4c67381e` ON `products_productimages` (`ProdId_id`);

CREATE INDEX `cart_cart_CustomerId_id_a6c0f226` ON `cart_cart` (`CustomerId_id`);

CREATE INDEX `cart_cart_productId_id_f48d425a` ON `cart_cart` (`productId_id`);

CREATE INDEX `products_products_ProductCategory_id_462762a0` ON `products_products` (`ProductCategory_id`);

CREATE INDEX `products_products_creator_id_e7eaa191` ON `products_products` (`creator_id`);

CREATE INDEX `django_session_expire_date_a5c62663` ON `django_session` (`expire_date`);

