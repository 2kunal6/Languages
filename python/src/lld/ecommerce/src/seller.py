from person import Person

class Seller(Person):
    def __init__(self, name, seller_id):
        super().__init__(name)
        self.seller_id = seller_id

    def sell(self):
        pass

    def add_or_update_item(self, item_id, quantity, inventory):
        if(item_id in inventory.item_map):
            inventory.item_map[item_id] += quantity
        else:
            inventory.item_map[item_id] = quantity
