from flask import Flask

app = Flask(__name__)  # main
pets = {
    "cats": [
        {
            "age": 1,
            "breed": "Tabby",
            "description": "Snowflake is a playful kitten who loves roaming the house and exploring.",
            "name": "Snowflake",
        }
    ],
    "dogs": [
        {
            "age": 2,
            "breed": "Dalmatian",
            "description": "Spot is an energetic puppy who seeks fun and adventure!",
            "name": "Spot",
        },
        {
            "age": 4,
            "breed": "Border Collie",
            "description": "Eager and curious, Shadow enjoys company and can always be found tagging along at your heels!",
            "name": "Shadow",
        },
    ],
    "rabbits": [
        {
            "age": 4,
            "breed": "Mini Rex",
            "description": "Easter is a sweet, gentle rabbit who likes spending most of the day sleeping.",
            "name": "Easter",
        }
    ],
}

@app.route("/")
@app.route("/home")
def index():
    return f"""
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend: </p>
    <ul>
        <li><a href="/animals/dogs"></a>{pets["dogs"][0]["name"]}</li>
        <li><a href="/animals/cats"></a>{pets["cats"][0]["name"]}</li>
        <li><a href="/animals/rabbits"></a>{pets["rabbits"][0]["name"]}</li>
    </ul>
    """


@app.route("/snowflake")
def pet_detail():
    return f"""
    <ul>
        <li><a href="/animals/dogs"></a>{pets["dogs"][0]["age"]}</li>
        <li><a href="/animals/dogs"></a>{pets["dogs"][0]["breed"]}</li>
        <li><a href="/animals/dogs"></a>{pets["dogs"][0]["description"]}</li>
        <li><a href="/animals/dogs"></a>{pets["dogs"][0]["name"]}</li>
    </ul>
    <ul>
        <li><a href="/animals/cats"></a>{pets["cats"][0]["age"]}</li>
        <li><a href="/animals/cats"></a>{pets["cats"][0]["breed"]}</li>
        <li><a href="/animals/cats"></a>{pets["cats"][0]["description"]}</li>
        <li><a href="/animals/cats"></a>{pets["cats"][0]["name"]}</li>
    </ul>
    <ul>
        <li><a href="/animals/rabbits"></a>{pets["rabbits"][0]["age"]}</li>
        <li><a href="/animals/rabbits"></a>{pets["rabbits"][0]["breed"]}</li>
        <li><a href="/animals/rabbits"></a>{pets["rabbits"][0]["description"]}</li>
        <li><a href="/animals/rabbits"></a>{pets["rabbits"][0]["name"]}</li>
    </ul>
    """

    