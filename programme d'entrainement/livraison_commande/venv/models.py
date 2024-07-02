from database import Base, engine, SessionLocal
from sqlalchemy import Boolean,Column, Integer, String, ForeignKey, Text
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(25), unique=True)
    email = Column(String(50), unique=True)
    password = Column(Text, nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    orders = relationship("Commande", back_populates="User")
class Commande(Base):
    
    ORDER_STATUS = (("EN_COURS", "en_cours"),( "EN_ATTENTE", "en_attente"),("LIVREE", "livree"))
    
    __tablename__ = 'commande'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    status_commande = Column(ChoiceType(ORDER_STATUS), default="EN_COURS")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    users = relationship("User", back_populates="Commande")