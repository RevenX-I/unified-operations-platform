from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from .base import Base

class UserRole(str, enum.Enum):
    OWNER = "OWNER"
    STAFF = "STAFF"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    role = Column(String, default=UserRole.STAFF) # Stored as string for simplicity with SQLite/PG compat
    is_active = Column(Boolean, default=True)
    
    # Relationships
    workspace_id = Column(Integer, ForeignKey("workspaces.id"), nullable=True)
    # workspace = relationship("Workspace", back_populates="users") 
    # (Commented out until Workspace model exists to avoid circular import errors if run prematurely, 
    # but I will define them together or use string references)
