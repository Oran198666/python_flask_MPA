from flask import Blueprint as Router, render_template, redirect, url_for, request
from models.product_model import ProductModel
from services.product_service import ProductService

router = Router("product_view", __name__)

@router.get("/products")
def products():
    with ProductService() as service:
        products = service.get_all_products()
        return render_template("products.html", products=products)

@router.get("/products/<int:id>")
def product_details(id: int):
    with ProductService() as service:
        product = service.get_one_product(id)
        return render_template("product_details.html", product=product)

@router.post("/products/<int:id>/delete")
def delete_product(id: int):
    with ProductService() as service:
        service.delete_product(id)
    return redirect(url_for("product_view.products"))

@router.get("/products/new")
def add_product_page():
    return render_template("add_product.html")

@router.post("/products/new")
def add_product():
    product = ProductModel(
        name=request.form["name"],
        price=float(request.form["price"]),
        stock=int(request.form.get("stock") or 0),
    )
    image = request.files.get("image")
    with ProductService() as service:
        service.add_product(product, image)
    return redirect(url_for("product_view.products"))