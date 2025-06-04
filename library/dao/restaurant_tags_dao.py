from typing import List
from pyfk import CrudSql
from sqlalchemy.orm.session import Session
from .schema.restaurant_tags import RestaurantTags
from sqlalchemy import select, union_all
from sqlalchemy.orm import aliased
from sqlalchemy.sql import literal_column

class RestaurantTagsDao(CrudSql[RestaurantTags]):

    def __init__(self, db: Session = None):
        super().__init__(db)

    def query_all_tags(self) -> List[str]:
        # 各欄位都要 where restaurant_style != ''
        condition = RestaurantTags.restaurant_style != ''

        # 個別 select 查詢
        q1 = select(RestaurantTags.restaurant_style.label("tags")).where(condition).distinct()
        q2 = select(RestaurantTags.restaurant_type.label("tags")).where(condition).distinct()
        q3 = select(RestaurantTags.occasion.label("tags")).where(condition).distinct()
        q4 = select(RestaurantTags.cuisine_style.label("tags")).where(condition).distinct()
        q5 = select(RestaurantTags.atmosphere.label("tags")).where(condition).distinct()
        q6 = select(RestaurantTags.special.label("tags")).where(condition).distinct()

        # 使用 union_all 合併查詢
        union_query = union_all(q1, q2, q3, q4, q5, q6)

        # 使用 session 執行
        result = self.db.execute(union_query).fetchall()

        # 取出 tags 字串
        return [row.tags for row in result]