from notifications.base import NotificationService


class EmailNotification(NotificationService):

    def send(self, message: str) -> None:
        print(f"[EMAIL] Order Update: {message}")
