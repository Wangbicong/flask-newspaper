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
    VALUES (13845924571, '刘二', '男', 18, '华尔街');
INSERT INTO users(phone_num, name, sex, age, address)
    VALUES (13789211278, '杜三', '女', 45, '哈尔滨');
INSERT INTO users(phone_num, name, sex, age, address)
    VALUES (18245782014, '杜圣哲', '男', 88, '哈工大一区五公寓');
INSERT INTO users(phone_num, name, sex, age, address)
    VALUES (14577824571, '杜笑着', '女', 72, '不详');
INSERT INTO users(phone_num, name, sex, age, address)
    VALUES (12579014579, '杜子疼', '男', 16, '不想说');

-- record demo data
INSERT INTO records(news_id, user_id, station, date)
    VALUES (1, 1, '哈尔滨', '2016-08-20 09:05:23');
INSERT INTO records(news_id, user_id, station, date)
    VALUES (1, 2, '七天', '2016-08-20');
INSERT INTO records(news_id, user_id, station, date)
    VALUES (2, 3, '华盛顿', '2016-07-07');
INSERT INTO records(news_id, user_id, station, date)
    VALUES (1, 5, '杜圣哲家', '2016-02-04');
INSERT INTO records(news_id, user_id, station, date)
    VALUES (2, 1, '四平', '2016-07-08');
INSERT INTO records(news_id, user_id, station, date)
    VALUES (4, 2, '哈尔滨', '2016-08-02');
INSERT INTO records(news_id, user_id, station, date)
    VALUES (1, 4, '新乡', '2016-02-20');
INSERT INTO records(news_id, user_id, station, date)
    VALUES (3, 4, '北京', '2016-06-20');

-- subscription demo data
INSERT INTO subscriptions(news_id, user_id)
    VALUES (1, 1);
INSERT INTO subscriptions(news_id, user_id)
    VALUES (1, 2);
INSERT INTO subscriptions(news_id, user_id)
    VALUES (3, 3);
INSERT INTO subscriptions(news_id, user_id)
    VALUES (2, 4);