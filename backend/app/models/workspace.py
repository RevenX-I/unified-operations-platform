from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from .base import Base

class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    timezone = Column(String, default="UTC")
    contact_email = Column(String, nullable=True)
    
    # Settings store active integrations, working hours, etc.
    settings = Column(JSON, default={})

    # Relationships
    users = relationship("User", backref="workspace")
    contacts = relationship("Contact", back_populates="workspace")
    services = relationship("Service", back_populates="workspace")
    inventory_items = relationship("InventoryItem", back_populates="workspace")
