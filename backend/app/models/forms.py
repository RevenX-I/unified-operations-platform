from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class FormTemplate(Base):
    __tablename__ = "form_templates"

    id = Column(Integer, primary_key=True, index=True)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))
    name = Column(String, nullable=False)
    schema = Column(JSON, nullable=False) # JSON schema for the form fields
    
    workspace = relationship("Workspace", backref="form_templates")
    submissions = relationship("FormSubmission", back_populates="template")

class FormSubmission(Base):
    __tablename__ = "form_submissions"

    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("form_templates.id"))
    contact_id = Column(Integer, ForeignKey("contacts.id"))
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=True)
    
    data = Column(JSON, nullable=False) # The filled form data
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())

    template = relationship("FormTemplate", back_populates="submissions")
    contact = relationship("Contact", back_populates="form_submissions")
    booking = relationship("Booking", back_populates="forms")
