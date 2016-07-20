from app import db
from app.models import Newspaper


def add_newspaper(jou_id, sub_jou_id, name, pub_date):
    newspaper = Newspaper(jou_id, sub_jou_id, name, pub_date)
    db.session.add(newspaper)
    db.session.commit()
    return True


def delete_newspaper(jou_id, sub_jou_id, name, pub_date):
    newspaper = Newspaper(jou_id, sub_jou_id, name, pub_date)
    db.session.delete(newspaper)
    db.session.commit()
    return True


def get_newspapers():
    return Newspaper.query.all()