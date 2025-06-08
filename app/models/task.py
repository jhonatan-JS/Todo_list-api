from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from app.models.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, server_default='False', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    user = relationship("User")