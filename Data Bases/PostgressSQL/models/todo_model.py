from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class TodoModel(Base):  # ✅ Corrected class name
    __tablename__ = 'todos_table'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    status = Column(Boolean, default=False)
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))  # ✅ Added ForeignKey for relationship

    user = relationship("Users", back_populates="todos")  # ✅ Defined relationship


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    
    todos = relationship("TodoModel", back_populates="user", cascade="all, delete")  # ✅ Defined relationship
