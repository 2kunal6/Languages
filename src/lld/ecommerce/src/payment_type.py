from abc import ABC, abstractmethod

class PaymentType(ABC):
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def return_payment(self):
        pass