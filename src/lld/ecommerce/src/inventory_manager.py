class InventoryManager:
    def __init__(self):
        self.item_map = {}

    def add_item(self, item_id, quantity):
        if(item_id in self.item_map):
            self.item_map[item_id] += quantity
        else:
            self.item_map[item_id] = quantity

    def sell_item(self, item_id, quantity):
        if (item_id in self.item_map and self.item_map[item_id] >= quantity):
            self.item_map[item_id] -= quantity
        else:
            raise Exception
