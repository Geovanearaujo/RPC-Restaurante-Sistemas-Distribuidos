import xmlrpc.server
import time
import threading 

class RestaurantServer:
    def __init__(self):
        self.menu = {
            'sandwiches': {'ham': 5, 'cheese': 3, 'vegan': 7},
            'ready_meals': {'pasta': 10, 'chicken': 7, 'salad': 5},
            'drinks': {'coffee': 2, 'juice': 1, 'water': 1},
            'desserts': {'cake': 7, 'fruit_salad': 5, 'ice_cream': 3}
        }
        self.orders_status = {}

    def get_menu(self, department):
        return self.menu.get(department, "Department not found.")

    def receive_order(self, order, department):
        if order in self.menu.get(department, {}):
            self.orders_status[(order, department)] = "Order is being prepared."
            threading.Thread(target=self.prepare_food, args=(order, department)).start()
            return f"Received order for {order} in {department}. It's being prepared."
        else:
            return "Order not available."

    def get_order_status(self, order, department):
        return self.orders_status.get((order, department), "Order not found or still being prepared.")

    def prepare_food(self, order, department):
        time.sleep(self.menu[department][order])
        self.orders_status[(order, department)] = f"The {order} from {department} is ready."

    def serve_forever(self):
        server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8080))
        server.register_instance(self)
        print("Listening on port 8080...")
        server.serve_forever()

if __name__ == "__main__":
    RestaurantServer().serve_forever()
