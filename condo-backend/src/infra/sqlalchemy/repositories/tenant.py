import email
from sqlalchemy.orm import Session
import sys
#Here the root path of the project needs to be informed
sys.path.append("/home/alonsoehlert/Documentos/APCODERS/condo-backend/")
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class TenantRepository():
    def __init__(self, db : Session):
        self.db = db

    def create(self, tenant: schemas.Tenant):
        db_tenant = models.Tenant(name=tenant.name,
        age=tenant.age, gender=tenant.gender, phone=tenant.phone, 
        email=tenant.email)

        self.db.add(db_tenant)
        self.db.commit()
        self.db.refresh(db_tenant)
        return db_tenant

    def get_all_tenants(self):
        tenants = self.db.query(models.Tenant).all()
        return tenants

