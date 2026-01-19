class Order:
    def __init__(self, order_id: int, amount: float) -> None:
        self.order_id = order_id
        self.amount = amount
        self.status = "CREATED"

    def mark_paid(self) -> None:
        self.status = "PAID"
