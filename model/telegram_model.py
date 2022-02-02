from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model.database import Base


class TelegramUser(Base):
    __tablename__ = "telegram_users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    telegram_id = Column(String)
    message = relationship("TelegramMessage", back_populates="user")


class TelegramMessage(Base):
    __tablename__ = "telegram_messages"

    id = Column(Integer, primary_key=True)
    message = Column(String)
    user_id = Column(Integer, ForeignKey("telegram_users.id"))
    user = relationship("TelegramUser", back_populates="message")
