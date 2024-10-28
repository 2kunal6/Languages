from payment_type import PaymentType

class Gpay(PaymentType):
    def pay(self):
        print('Gpay paying')
    def return_payment(self):
        print('Gpay returning payment')