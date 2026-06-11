from abc import ABC, abstractmethod


class Address:
    def __init__(self, street, number, city, state):
        self.street = street
        self.number = number
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.street}\n{self.number}\n{self.city}\n{self.state}"


class Customer:
    def __init__(self, name, cpf, email, phone, address: Address):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"{self.name}\n{self.cpf}\n{self.email}\n{self.phone}\n{self.address}"


class ReportService:
    def print_customer(self, customer):
        print(customer.name)
        print(customer.cpf)


class NotificationService:
    def send_order_confirmation(self, email, total):
        print("Email enviado")

    def notify_shipping(self, name):
        print("Transportadora notificada")


class BillingService:
    def generate_invoice(self, name, cpf, total):
        print("NF gerada")

    def generate_financial_report(self, total):
        print("Relatório financeiro")


class InventoryService:
    def update_inventory(self, items):
        print("Estoque atualizado")


class OrderRecordService:
    def register_audit(self, name, total):
        print("Auditoria registrada")

    def save_history(self, name, total):
        print("Histórico salvo")


class OrderServices:
    def __init__(
        self,
        notifications=None,
        billing=None,
        inventory=None,
        records=None,
    ):
        self.notifications = notifications or NotificationService()
        self.billing = billing or BillingService()
        self.inventory = inventory or InventoryService()
        self.records = records or OrderRecordService()


class Payment(ABC):
    @abstractmethod
    def process(self):
        pass


class PixPayment(Payment):
    def process(self):
        print("Pagamento PIX")


class CardPayment(Payment):
    def process(self):
        print("Pagamento Cartão")


class BoletoPayment(Payment):
    def process(self):
        print("Pagamento Boleto")


class Order:
    def __init__(
        self, customer: Customer, items, payment: Payment, services: OrderServices
    ):
        self.customer = customer
        self.items = items
        self.payment = payment
        self.services = services

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

    def process_order(self):
        total = self.calculate_total()

        self.payment.process()
        print(self.customer)
        self._complete_order(total)

    def _complete_order(self, total):
        customer = self.customer

        self.services.notifications.send_order_confirmation(customer.email, total)
        self.services.billing.generate_invoice(customer.name, customer.cpf, total)
        self.services.inventory.update_inventory(self.items)
        self.services.records.register_audit(customer.name, total)
        self.services.billing.generate_financial_report(total)
        self.services.records.save_history(customer.name, total)
        self.services.notifications.notify_shipping(customer.name)
