from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Integer, String
# from pydantic import BaseModel, Field

# class ProductSchema(BaseModel):
#     id: int | None = None
#     name: str = Field()
#     price: float = Field()
#     stock: int = Field()


class ProductModel(declarative_base()):

    # Exact database table:
    __tablename__ = "products"

    # Table columns:
    id = Column(Integer, primary_key = True)
    name = Column(String(40), nullable = False)
    price = Column(Float, nullable = False)
    stock = Column(Integer, default = 0)
    imgUrl = Column(String(50))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}