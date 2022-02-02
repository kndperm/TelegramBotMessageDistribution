from sqlalchemy.orm import Session

from dto.telegram_dto import TelegramMessageCreate
from model.telegram_model import TelegramMessage


def add_telegram_message(message: TelegramMessageCreate, db: Session):
    db_message = TelegramMessage(user_id=message.user_id, message=message.text)
    db.add(db_message)
    db.commit()
