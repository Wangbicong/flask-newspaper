USE newspaper;

-- newspaper demo data
INSERT INTO newspapers(jou_id, sub_jou_id, name, pub_date)
    VALUES (1, 1, '人民日报', '1998-01-01');
INSERT INTO newspapers(jou_id, sub_jou_id, name, pub_date)
    VALUES (1, 1, '光明日报', '2001-01-01');
INSERT INTO newspapers(jou_id, sub_jou_id, name, pub_date)
    VALUES (2, 2, '人民日报', '2014-08-01');
INSERT INTO newspapers(jou_id, sub_jou_id, name, pub_date)
    VALUES (2, 2, '光明日报', '2000-08-01');
INSERT INTO newspapers(jou_id, sub_jou_id, name, pub_date)
    VALUES (1, 1, '华尔街日报', '2013-01-08');

-- user demo data
INSERT INTO users(phone_num, name, sex, age, address)
    VALUES (13845924571, '刘二', 1, 18, '华尔街');
INSERT INTO users(phone_num, name, sex, age, address)
    VALUES (13789211278, '杜三', 1, 45, '哈尔滨');
INSERT INTO users(phone_num, name, sex, age, address)
    VALUES (18245782014, '杜圣哲', 0, 88, '哈工大一区五公寓');
INSERT INTO users(phone_num, name, sex, age, address)
    VALUES (14577824571, '杜笑着', 0, 72, '不详');
INSERT INTO users(phone_num, name, sex, age, address)
    VALUES (12579014579, '杜子疼', 1, 16, '不想说');

-- record demo data
INSERT INTO records(news_id, user_id, station)
    VALUES (1, 1, '哈尔滨');
INSERT INTO records(news_id, user_id, station)
    VALUES (1, 2, '七天');
INSERT INTO records(news_id, user_id, station)
    VALUES (2, 3, '华盛顿');
INSERT INTO records(news_id, user_id, station)
    VALUES (1, 5, '杜圣哲家');
INSERT INTO records(news_id, user_id, station)
    VALUES (2, 1, '四平');
INSERT INTO records(news_id, user_id, station)
    VALUES (4, 2, '哈尔滨');
INSERT INTO records(news_id, user_id, station)
    VALUES (1, 4, '新乡');
INSERT INTO records(news_id, user_id, station)
    VALUES (3, 4, '北京');

-- subscription demo data
INSERT INTO subscriptions(news_id, user_id)
    VALUES (1, 1);
INSERT INTO subscriptions(news_id, user_id)
    VALUES (1, 2);
INSERT INTO subscriptions(news_id, user_id)
    VALUES (3, 3);
INSERT INTO subscriptions(news_id, user_id)
    VALUES (2, 4);