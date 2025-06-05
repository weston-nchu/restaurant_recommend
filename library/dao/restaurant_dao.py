from typing import List
from pyfk import CrudSql
from sqlalchemy.orm.session import Session
from .schema.restaurant import Restaurant
from sqlalchemy import select

class RestaurantDao(CrudSql[Restaurant]):

    def __init__(self, db: Session = None):
        super().__init__(db)

    def query_code_by_uid_list(self, uid_list: List[str]) -> List[str]:
        return [obj[0] for obj in self.db.query(Restaurant.code).filter(Restaurant.uid.in_(uid_list)).all()]