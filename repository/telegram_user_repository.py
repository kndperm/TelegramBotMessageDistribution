from sqlalchemy import literal
from sqlalchemy.orm import Session

from dto.telegram_dto import TelegramUserCreate
from model.telegram_model import TelegramUser


def add_telegram_user(telegram_user: TelegramUserCreate, db: Session):
    db_user = TelegramUser(username=telegram_user.username, telegram_id=telegram_user.telegram_id)
    db.add(db_user)
    db.commit()


def is_username_exist(username: str, db: Session):
    q = db.query(TelegramUser).filter(TelegramUser.username == username)
    return db.query(literal(True)).filter(q.exists()).scalar()


def get_id_by_username(username: str, db: Session):
    user = db.query(TelegramUser).filter(TelegramUser.username == username).first()
    return user.id
