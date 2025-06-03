from pyfk import CrudSql
from sqlalchemy.orm.session import Session
from .schema.restaurant_tags import RestaurantTags

class RestaurantTagsDao(CrudSql[RestaurantTags]):

    def __init__(self, db: Session = None):
        super().__init__(db)