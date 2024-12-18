import creator

from flask import Flask, render_template


app = Flask(__name__)


CONTACT = "+380731570901"


@app.get("/")
def show_pizzas():
    pizzas = creator.get_Pizzas()
    pizza_name1 = pizzas[0]
    pizza_name2 = pizzas[1]
    context = {
        "title": "Меню",
        "pizzas": pizzas
    }
    return render_template("index.html", **context)


@app.get('/results-ababagalamaga/')
def results():
    context = {
        "max_score": 100,
        "test_name": "Python Challenge",
        "students": [
        {"name": "Vlad", "score": 100},
        {"name": "Vlad", "score": 42},
        {"name": "Sviatoslav", "score": 99},
        {"name": "Юстин", "score": 100},
        {"name": "Viktor", "score": 79},
        {"name": "Ярослав", "score": 93},
        ],
        "title": "Результати тестування",
        "contact": CONTACT
    }

    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)