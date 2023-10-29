from flask import Flask, render_template

from helper import recipes

app = Flask(__name__)  # main


@app.route("/")
def index():
    recipe = recipes[1]
    return render_template("index.html", recipes=recipes)


@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
    return f"Recipe with #{id}"

@app.route("/about")
def about():
    return render_template("about.html")



# @app.route("/animals/<animal_type>")
# def pet_list(animal_type):
#     if animal_type in pets.keys():
#         name = pets[animal_type][0]["name"]
#         return f"""
#         <h1>{animal_type}</h1>
#         <ul>
#             <li><a href="/animals/{animal_type}/{name}">{name}</a></li>
#         </ul>
#         """

#     return """
#     <p>We don't have such animals, but we have:</p>
#     <ul>
#         <li><a href="/animals/rabbits">Rabbits</a></li>
#         <li><a href="/animals/cats">Cats</a></li>
#         <li><a href="/animals/dogs">Dogs</a></li>
#     </ul>
#     """


# @app.route("/animals/<string:animal_type>/<animal_name>")
# def pet_deail(animal_type, animal_name):
#     return f"Type = {animal_type},animal_name = {animal_name}."


# @app.route("/orders/<user_name>/<int:order_id>")
# def orders(user_name, order_id):
#     order_id + 2
#     return f"<p>Fetching order #{order_id} for {user_name}.</p>"


# """
# Создать функцию pet_detail, которая будет выводить информацию о кошке:
# - age
# - breed
# - description
# - name

# Она должна открывает при переходе на путь /snowflake

# /animals/<animal_type>
# /animals/<animal_type>/<animal_name>
# """
