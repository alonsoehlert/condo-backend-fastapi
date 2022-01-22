from sqlalchemy import select, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class UnitExpensesRepository():
    def __init__(self, db : Session):
        self.session = db

    def create(self, unitexpense: schemas.UnitExpense):
        db_unitexpense = models.UnitExpenses(id=unitexpense.id, description=unitexpense.description,
        type_expense=unitexpense.type_expense, amount=unitexpense.amount, due_date=unitexpense.due_date,
        payment_status=unitexpense.payment_status, unit_id=unitexpense.unit_id)

        self.session.add(db_unitexpense)
        self.session.commit()
        self.session.refresh(db_unitexpense)
        return db_unitexpense


    def edit(self, id: int, unitexpense: schemas.UnitExpense):
        update_stmt = update(models.UnitExpenses).where(
            models.UnitExpenses.id == id).values(description=unitexpense.description,
            type_expense=unitexpense.type_expense, amount=unitexpense.amount,
            due_date=unitexpense.due_date, payment_status=unitexpense.payment_status

                                            )
        self.session.execute(update_stmt)
        self.session.commit()

    def get_by_unit(self, unit_id: int):
        query = select(models.UnitExpenses).where(models.UnitExpenses.unit_id == unit_id)
        expense = self.session.execute(query).first()
        return expense

  
    def get_by_overdue(self):
        query = select(models.UnitExpenses).where(models.UnitExpenses.payment_status == 'Overdue')
        overdue = self.session.execute(query).scalars().all()
        return overdue

