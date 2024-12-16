import sqlite3


def create_db():
    try:
        sql_con = sqlite3.connect("Pizzas.db")
        cursor = sql_con.cursor()

        with open("create_db.sql") as fh:
            query = fh.read()

        cursor.execute(query)
        sql_con.commit()
        cursor.close()
        print("База даних та таблиця успішно створена")

    except sqlite3.Error as error:
        print(f"{error = }")


    def insert_data(
            name: str,
            price: int | None = None,
    ):

        try:
            sql_con = sqlite3.connect("Pizzas.db")
            cursor = sql_con.cursor()

            query = "INSERT INTO Pizzas (name, price) VALUES (?, ?)"
            data = (name, price)

            cursor.execute(query, data)
            sql_con.commit()
            cursor.close()
            print("Дані успішно записані")

        except sqlite3.Error as error:
            print(f"{error = }")

        finally:
            if sql_con:
                sql_con.close()
                print("Робота з базою даних успішно завершена")


# create_db()
    insert_data("Маргарита", "90")
    insert_data("Pizza Hut", "160")
    insert_data("Пепероні", "120")
    insert_data("Сирна", "100")
    insert_data("М'ясна", "110")
    insert_data("Нарізана на шматочки", "80")
    insert_data("Pizza Bianca", "70")
    insert_data("Гавайська", "95")
    insert_data("Капричоза", "100")
    insert_data("Кватро Формаджі", "150")