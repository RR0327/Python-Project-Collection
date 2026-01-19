from notifications.base import NotificationService


class SMSNotification(NotificationService):

    def send(self, message: str) -> None:
        print(f"[SMS] Order Update: {message}")
