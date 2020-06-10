from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@homestats_routes.route("/")
def index():



@home_routes.route("/")
def index():
    print("VISITING THE HOME PAGE")
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print("VISITING THE HOME PAGE")
    return "About me"
