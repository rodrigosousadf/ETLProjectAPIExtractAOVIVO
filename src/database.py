from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

Base = declarative_base()

class BitcoinPreco(Base):
    __tablename__ = 'bitcoin_precos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(50), nullable=False)
    moeda = Column(String(10), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<BitcoinPreco(valor={self.valor}, criptomoeda={self.criptomoeda}, moeda={self.moeda}, timestamp={self.timestamp})>"

