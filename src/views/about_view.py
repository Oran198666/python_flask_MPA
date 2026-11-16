from flask import Blueprint as Router, render_template

router = Router("about_router", __name__) # Blueprint = Router

@router.route("/about")
def about():
    return render_template("about.html")