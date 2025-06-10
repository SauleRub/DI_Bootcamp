import psycopg2

conn = psycopg2.connect(
    dbname='restaurant_menu',
    user='saulerub',
    password='1717',  
    host='localhost',
    port='5432'
)

cur = conn.cursor()

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        try:
            cur.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s);",
                (self.name, self.price)
            )
            conn.commit()
            print(f"{self.name} added successfully.")
        except Exception as e:
            print("Error adding item:", e)

    def delete(self):
        try:
            cur.execute(
                "DELETE FROM Menu_Items WHERE item_name = %s;",
                (self.name,)
            )
            conn.commit()
            print(f"{self.name} deleted successfully.")
        except Exception as e:
            print("Error deleting item:", e)

    def update(self, new_name, new_price):
        try:
            cur.execute(
                "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s;",
                (new_name, new_price, self.name)
            )
            conn.commit()
            print(f"{self.name} updated to {new_name} with price {new_price}.")
        except Exception as e:
            print("Error updating item:", e)

if __name__ == "__main__":
    burger = MenuItem("Burger", 35)
    burger.save()
    burger.update("Cheese Burger", 40)
    burger.delete()