USE newspaper;

-- newspaper demo data
INSERT INTO newspaper(jou_id, sub_jou_id, name, pub_date)
    VALUES (141, 6, '人民日报', '2014-01-01');
INSERT INTO newspaper(jou_id, sub_jou_id, name, pub_date)
    VALUES (2787, 17, '光明日报', '2017-01-01');
INSERT INTO newspaper(jou_id, sub_jou_id, name, pub_date)
    VALUES (387, 9, '人民日报', '2014-08-01');
INSERT INTO newspaper(jou_id, sub_jou_id, name, pub_date)
    VALUES (2214, 56, '英语周报', '2000-08-01');
INSERT INTO newspaper(jou_id, sub_jou_id, name, pub_date)
    VALUES (157, 12, '华尔街日报', '2013-01-08');

-- user demo data
INSERT INTO user(phone_num, name, sex, age, address)
    VALUES (13845924571, '刘二', 1, 18, '华尔街');
INSERT INTO user(phone_num, name, sex, age, address)
    VALUES (13789211278, '杜三', 1, 45, '哈尔滨');
INSERT INTO user(phone_num, name, sex, age, address)
    VALUES (18245782014, '杜圣哲', 0, 88, '哈工大一区五公寓');
INSERT INTO user(phone_num, name, sex, age, address)
    VALUES (14577824571, '杜笑着', 0, 72, '不详');
INSERT INTO user(phone_num, name, sex, age, address)
    VALUES (12579014579, '杜子疼', 1, 16, '不想说');

-- record demo data
INSERT INTO record(news_id, user_id, station)
    VALUES (1, 1, '哈尔滨');
INSERT INTO record(news_id, user_id, station)
    VALUES (1, 2, '七天');
INSERT INTO record(news_id, user_id, station)
    VALUES (2, 3, '华盛顿');
INSERT INTO record(news_id, user_id, station)
    VALUES (1, 5, '杜圣哲家');
INSERT INTO record(news_id, user_id, station)
    VALUES (2, 1, '四平');
INSERT INTO record(news_id, user_id, station)
    VALUES (4, 2, '哈尔滨');
INSERT INTO record(news_id, user_id, station)
    VALUES (1, 4, '新乡');
INSERT INTO record(news_id, user_id, station)
    VALUES (3, 4, '北京');