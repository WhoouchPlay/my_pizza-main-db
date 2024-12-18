import creator

from flask import Flask, render_template


app = Flask(__name__)


CONTACT = "+380731570901"


@app.get("/")
def show_pizzas():
    pizzas_db = creator.get_Pizzas()
    pizzas = []

    for pizza in pizzas_db:
        pizzas.append(
            {"name": pizza[1], "price": pizza[2]}
        )

    return render_template("index.html", pizzas=pizzas_db, contact=CONTACT)


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