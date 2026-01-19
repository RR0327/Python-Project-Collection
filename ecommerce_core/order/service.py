from notifications.base import NotificationService
from order.entity import Order


class OrderService:
    def __init__(self, notifier: NotificationService) -> None:
        self.notifier = notifier

    def process_order(self, order: Order) -> None:
        order.mark_paid()

        self.notifier.send(
            f"Order #{order.order_id} has been successfully paid. "
            f"Total amount: ${order.amount}"
        )
