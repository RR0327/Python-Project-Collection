from notifications.email import EmailNotification
from notifications.sms import SMSNotification
from order.entity import Order
from order.service import OrderService


def main():
    # Email notification
    email_notifier = EmailNotification()
    order_service = OrderService(email_notifier)

    order1 = Order(order_id=101, amount=249.99)
    order_service.process_order(order1)

    # SMS notification
    sms_notifier = SMSNotification()
    order_service = OrderService(sms_notifier)

    order2 = Order(order_id=102, amount=99.99)
    order_service.process_order(order2)


if __name__ == "__main__":
    main()
