from fastapi import FastAPI, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models.models import UnitExpenses
from src.schemas.schemas import Tenant, Unit, UnitExpense
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repositories.tenant import TenantRepository
from src.infra.sqlalchemy.repositories.unit import UnitRepository
from src.infra.sqlalchemy.repositories.unit_expenses import UnitExpensesRepository

create_db()

app = FastAPI()

#Command in terminal to run the server:
#uvicorn src.server:app --reload --reload-dir=src

#Tenants Endpoints

@app.get('/tenants', status_code = status.HTTP_200_OK, response_model= List[Tenant])
def get_all_tenants(db: Session = Depends(get_db)):
    tenants = TenantRepository(db).get_all_tenants()
    return tenants

@app.post('/tenants', status_code = status.HTTP_201_CREATED, response_model=Tenant)
def create_tenants(tenant: Tenant, db: Session = Depends(get_db)):
    created_tenant = TenantRepository(db).create(tenant)
    return created_tenant


#Units Endpoints

@app.post('/units', status_code = status.HTTP_201_CREATED, response_model=Unit)
def create_units(unit: Unit, db: Session = Depends(get_db)):
    created_unit = UnitRepository(db).create(unit)
    return created_unit

@app.get('/units', response_model=List[Unit])
def get_all_units(db: Session = Depends(get_db)):
    units = UnitRepository(db).get_all_units()
    return units


#Unit Expenses endpoints

@app.post('/unitexpenses',
             status_code=status.HTTP_201_CREATED,
             response_model=UnitExpense)
def create_unit_expense(
        unit_expense: UnitExpense,
        session: Session = Depends(get_db)):
    created_unit_expense = UnitExpensesRepository(session).create(unit_expense)
    return created_unit_expense


@app.put('/unitexpenses/{id}', response_model=UnitExpense)
def edit_unit_expense(
        id: int,
        unit_expense: UnitExpense,
        session: Session = Depends(get_db)):
    UnitExpensesRepository(session).edit(id, unit_expense)
    unit_expense.id = id
    return unit_expense


@app.get('/unitexpenses/{unit_id}')
def expense_per_unit(unit_id: int, session: Session = Depends(get_db)):
    unit_found = UnitExpensesRepository(session).get_by_unit(unit_id)
    if not unit_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'There is no expense related to unit id = {unit_id}')
    return unit_found


@app.get('/unitexpenses/overdue/', response_model=List[UnitExpense])
def get_overdue_expenses(session: Session = Depends(get_db)):
    overdue = UnitExpensesRepository(session).get_by_overdue()
    if not overdue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='There is no expense related to Overdue payment status!')
    return overdue

