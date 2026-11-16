# from http import HTTPStatus
# from flask import Blueprint as Router, jsonify, request
# from services.product_service import ProductService
# from models.product_model import ProductModel

# router = Router("product_router", __name__)


# @router.get("/api/products")
# def get_all_products():
#     with ProductService() as service:
#         return jsonify(service.get_all_products()), HTTPStatus.OK


# @router.get("/api/products/<int:id>")
# def get_one_product(id: int):
#     with ProductService() as service:
#         return jsonify(service.get_one_product(id)), HTTPStatus.OK


# @router.post("/api/products")
# def add_product():
#     data = request.get_json()
#     product = ProductModel(**data)
#     with ProductService() as service:
#         added = service.add_product(product)
#         return jsonify(added.to_dict()), HTTPStatus.CREATED


# @router.put("/api/products/<int:id>")
# def update_product(id: int):
#     data = request.get_json()
#     product = ProductModel(**data)
#     product.id = id
#     with ProductService() as service:
#         updated = service.update_product(product)
#         return jsonify(updated.to_dict()), HTTPStatus.OK


# @router.delete("/api/products/<int:id>")
# def delete_product(id: int):
#     with ProductService() as service:
#         service.delete_product(id)
#     return "", HTTPStatus.NO_CONTENT


# @router.get("/api/products-by-range/<min_price>/<max_price>")
# def get_products_by_range(min_price: str, max_price: str):
#     min_price, max_price = float(min_price), float(max_price)
#     with ProductService() as service:
#         products_by_range = service.get_products_by_range(min_price, max_price)
#         return jsonify([dict(row) for row in products_by_range]), HTTPStatus.OK