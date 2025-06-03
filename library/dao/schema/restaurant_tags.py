from pyfk import AbstractTable
from sqlalchemy import *

class RestaurantTags(AbstractTable):

    __tablename__ = "restaurant_tags"

    restaurant_uid = Column(String(length=32), ForeignKey("restaurant.uid"), nullable=False)

    # 餐廳風格
    restaurant_style = Column(String(length=32))

    # 餐廳種類
    restaurant_type = Column(String(length=32))

    # 場合
    occasion = Column(String(length=32))

    # 料理風格
    cuisine_style = Column(String(length=32))
    
    # 餐廳氛圍
    atmosphere = Column(String(length=32))
    
    # 招牌亮點
    special = Column(String(length=32))

    def __init__(self, restaurant_uid: str, restaurant_style: str, restaurant_type: str, occasion: str,
            cuisine_style: str, atmosphere: str, special: str, lm_user="system"):
        super().__init__(lm_user)
        self.restaurant_uid = restaurant_uid
        self.restaurant_style = restaurant_style
        self.restaurant_type = restaurant_type
        self.occasion = occasion
        self.cuisine_style = cuisine_style
        self.atmosphere = atmosphere
        self.special = special