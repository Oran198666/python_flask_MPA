from utils.dal import Dal
from models.product_model import ProductModel
from sqlalchemy import text
from models.errors import NotFoundError
import os
import uuid

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "images")

class NotFoundError(Exception):
    pass


class ProductService:

    def __init__(self) -> None:
        self.session = Dal.create_session()

    def get_all_products(self):
        products = self.session.query(ProductModel).all()
        return [p.to_dict() for p in products]

    def get_one_product(self, id: int):
        product = self.session.get(ProductModel, id)
        if product is None:
            raise NotFoundError(f"id {id} not found.")
        return product.to_dict()

    def add_product(self, product: ProductModel, image=None):
        if image and image.filename:
            ext = os.path.splitext(image.filename)[1]
            filename = f"{uuid.uuid4()}{ext}"
            image.save(os.path.join(IMAGES_DIR, filename))
            product.imgUrl = filename
        self.session.add(product)
        self.session.commit()
        return product

    def update_product(self, product: ProductModel):
        if self.session.get(ProductModel, product.id) is None:
            raise NotFoundError(f"id {product.id} not found.")
        db_product = self.session.merge(product)
        self.session.commit()
        return db_product

    def delete_product(self, id: int):
        product = self.session.get(ProductModel, id)
        if product is None:
            raise NotFoundError(f"id {id} not found.")

        if product.imgUrl:
            image_path = os.path.join(IMAGES_DIR, product.imgUrl)
            if os.path.exists(image_path):
                os.remove(image_path)

        self.session.delete(product)
        self.session.commit()

    def get_products_by_range(self, min_price: float, max_price: float):
        statement = text("select * from products where price between :minimum and :maximum order by price")
        result = self.session.execute(statement, {"minimum":min_price, "maximum":max_price})
        products = result.mappings().all()
        return products

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()