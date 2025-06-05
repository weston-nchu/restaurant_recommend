from typing import List
from pyfk import AbstractTable
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Restaurant(AbstractTable):

    __tablename__ = "restaurant"

    name = Column(String(length=32), nullable=False)

    code = Column(String(length=32), nullable=False)
    
    desc = Column(String(length=4000), nullable=False)
    
    address = Column(String(length=100), nullable=False)
    
    url = Column(String(length=200), nullable=False)

    img1 = Column(String(length=200), nullable=True)

    img2 = Column(String(length=200), nullable=True)

    img3 = Column(String(length=200), nullable=True)

    img4 = Column(String(length=200), nullable=True)

    img5 = Column(String(length=200), nullable=True)

    tags = relationship("RestaurantTags", cascade="all", lazy="joined")

    def __init__(self, name: str, code: str, desc: str, address: str, url: str,
            img1: str, img2: str, img3: str, img4: str, img5: str,  lm_user="system"):
        super().__init__(lm_user)
        self.name = name
        self.code = code
        self.desc = desc
        self.address = address
        self.url = url
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        self.img4 = img4
        self.img5 = img5

    def get_img_url_list(self) -> List[str]:
        img_url_list = []
        if self.img1:
            img_url_list.append(self.__img_id_to_url(self.img1))
        
        if self.img2:
            img_url_list.append(self.__img_id_to_url(self.img2))

        if self.img3:
            img_url_list.append(self.__img_id_to_url(self.img3))

        if self.img4:
            img_url_list.append(self.__img_id_to_url(self.img4))

        if self.img5:
            img_url_list.append(self.__img_id_to_url(self.img5))

        return img_url_list
    
    def __img_id_to_url(self, img_id: str):
        return f"https://axwwgrkdco.cloudimg.io/v7/__gmpics3__/{img_id}?w=224&h=224&org_if_sml=1"
    
    def get_tag_list(self) -> List[str]:
        tags = self.tags[0]

        result = []
        if tags.restaurant_style:
            result.append(tags.restaurant_style)
        
        if tags.restaurant_type:
            result.append(tags.restaurant_type)
        
        if tags.occasion:
            result.append(tags.occasion)

        if tags.cuisine_style:
            result.append(tags.cuisine_style)
        
        if tags.atmosphere:
            result.append(tags.atmosphere)
        
        if tags.special:
            result.append(tags.special)
            
        return result
