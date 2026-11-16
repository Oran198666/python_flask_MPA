from flask import Blueprint as Router, render_template

router = Router("home_router", __name__) # Blueprint = Router

@router.route("/")
@router.route("/home")
def home():
    return render_template("home.html")