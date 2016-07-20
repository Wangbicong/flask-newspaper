from app import db, create_app


class Newspaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jou_id = db.Column(db.Integer, nullable=False)
    sub_jou_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, jou_id, sub_jou_id, name, pub_date):
        self.jou_id = jou_id
        self.sub_jou_id = sub_jou_id
        self.name = name
        self.pub_date = pub_date

    def __repr__(self):
        return '<Newspaper %r %r>' % (self.name, self.jou_id)


class User(db.Model):
    phone_num = db.Column(db.String(11), primary_key=True)
    name = db.Column(db.String(4), nullable=False)
    sex = db.Column(db.Boolean, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(40), nullable=False)

    def __init__(self, phone_num, name, sex, age, address):
        self.phone_num = phone_num
        self.name = name
        self.sex = sex
        self.age = age
        self.address = address

    def __repr__(self):
        return '<User %r %r>' % (self.name, self.phone_num)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer,
                        db.ForeignKey('newspaper.id'))
    phone_num = db.Column(db.String(11),
                          db.ForeignKey('user.phone_num'))
    station = db.Column(db.String(40), nullable=False)

    def __init__(self, news_id, phone_num, station):
        self.news_id = news_id
        self.phone_num = phone_num
        self.station = station

    def __repr__(self):
        return '<Record news %r user% r>' % \
               (self.news_id, self.phone_num)


def create_database():
    app = create_app()
    db.create_all(app=app)

if __name__ == '__main__':
    create_database()