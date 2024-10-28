from person import Person

class Buyer(Person):
    def __init__(self, name, buyer_id, payment_type):
        super().__init__(name)
        self.buyer_id = buyer_id
        self.payment_type = payment_type

    def buy(self, item_id, quantity, inventory):
        if(item_id in inventory.item_map):
            self.payment_type.pay()
            try:
                inventory.sell_item(item_id, quantity)
            except Exception:
                self.payment_type.return_payment()

