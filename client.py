import xmlrpc.client

class RestaurantClient:
    def __init__(self):
        self.proxy = xmlrpc.client.ServerProxy("http://localhost:8080/")

    def print_menu(self, department):
        menu = self.proxy.get_menu(department)
        if isinstance(menu, str):
            print(menu)
            return False
        print(f"Menu for {department} department:")
        for item, prep_time in menu.items():
            print(f"{item} (Preparation time: {prep_time} seconds)")
        return True

    def place_order(self, department):
        print(f"Enter the order for the {department} department or 'exit' to stop:")
        order = input()
        if order.lower() == 'exit':
            return False
        print(self.proxy.receive_order(order, department))
        return True

    def interact(self):
        while True:
            print("Enter the department (sandwiches, ready meals, drinks, desserts) or 'exit' to stop:")
            department = input()
            if department.lower() == 'exit':
                break
            if not self.print_menu(department):
                continue
            if not self.place_order(department):
                break

if __name__ == "__main__":
    client = RestaurantClient()
    client.interact()
