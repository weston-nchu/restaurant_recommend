from pyfk import CrudSql
from sqlalchemy.orm.session import Session
from .schema.restaurant import Restaurant

class RestaurantDao(CrudSql[Restaurant]):

    def __init__(self, db: Session = None):
        super().__init__(db)