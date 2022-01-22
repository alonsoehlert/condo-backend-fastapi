from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class UnitRepository():
    def __init__(self, db : Session):
        self.db = db

    def create(self, unit: schemas.Unit):
        db_unit = models.Unit(id=unit.id, owner=unit.owner,
        condo_name=unit.condo_name, address=unit.address)

        self.db.add(db_unit)
        self.db.commit()
        self.db.refresh(db_unit)
        return db_unit


    def get_all_units(self):
        units = self.db.query(models.Unit).all()
        return units

        