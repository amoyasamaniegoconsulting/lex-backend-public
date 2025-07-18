from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from  database import Base
from  models.origin import Origin
from  models.frequency  import Frequency

class DailyBalance(Base):
    __tablename__ = "DailyBalance"
    
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    accountCode = Column(Integer, default=0)
    accountName = Column(String, default="")
    thirdParty = Column(String, default="")
    openingBalance = Column(Float, default=0)
    debits = Column(Float, default=0)
    credits = Column(Float, default=0)
    closingBalance = Column(Float, default=0)

    originId = Column(String, ForeignKey("Origin.id"))  # Mantener "Origin" con mayúscula
    frequencyId = Column(Integer, ForeignKey("Frequency.id"), nullable=True)

    createdDate = Column(DateTime, server_default=func.now())
    userId = Column(String, default="bot")
    lastModified = Column(DateTime, server_default=func.now(), onupdate=func.now())
    cutOffDate = Column(DateTime, nullable=True)
    version = Column(Integer, default=1)

    origin = relationship("Origin", foreign_keys=[originId], back_populates="dailyBalances")  # Relación con "Origin"
    frequency = relationship("Frequency",foreign_keys=[frequencyId],  back_populates="dailyBalances")
