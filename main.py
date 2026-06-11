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


class OrderServices:
    def send_email(self, email, total):
        print("Email enviado")

    def generate_invoice(self, name, cpf, total):
        print("NF gerada")

    def update_inventory(self, items):
        print("Estoque atualizado")

    def register_audit(self, name, total):
        print("Auditoria registrada")

    def generate_financial_report(self, total):
        print("Relatório financeiro")

    def save_history(self, name, total):
        print("Histórico salvo")

    def notify_shipping(self, name):
        print("Transportadora notificada")


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

        # cálculo repetido
        total2 = self.calculate_total()

        self.payment.process()

        print(self.customer)

        self.services.send_email(self.customer.email, total)
        self.services.generate_invoice(self.customer.name, self.customer.cpf, total)
        self.services.update_inventory(self.items)
        self.services.register_audit(self.customer.name, total)
        self.services.generate_financial_report(total)
        self.services.save_history(self.customer.name, total)
        self.services.notify_shipping(self.customer.name)
