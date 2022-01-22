from sqlalchemy import Integer, String, DATE, DateTime, Float, Boolean, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
import sys
#Here the root path of the project needs to be informed
sys.path.append("/home/alonsoehlert/Documentos/APCODERS/condo-backend/")
from src.infra.sqlalchemy.config.database import Base

#Creating a many to many relationship between classes Tenant and Unit

association_table_1 = Table('unit_tenant', Base.metadata,
    Column('unit_id', ForeignKey('unit.id', name='fk_unit'), primary_key=True),
    Column('tenant_id', ForeignKey('tenant.id', name='fk_tenant'), primary_key=True)
)

class Unit(Base):
    __tablename__ = 'unit'

    id = Column(String, primary_key=True, index=True, nullable=False)
    owner = Column(String)
    condo_name = Column(String)
    address = Column(String)
    tenants = relationship(
        "Tenant",
        secondary=association_table_1,
        back_populates="units")
    unitexpenses = relationship("UnitExpenses", back_populates="unit")

class Tenant(Base):
    __tablename__ = 'tenant'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone = Column(Integer)
    email = Column(String)
    units = relationship(
        "Unit",
        secondary=association_table_1,
        back_populates="tenants")


#The following class has a MANY TO ONE relationship with the Unit class. 
class UnitExpenses(Base):
    __tablename__ = 'unit_expenses'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    type_expense = Column(String)
    amount = Column(Float)
    due_date = Column(DateTime)
    payment_status = Column(String)
    unit_id = Column(Integer, ForeignKey('unit.id', name='fk_unit_unit_expenses'))
    unit = relationship("Unit", back_populates="unitexpenses")
  


