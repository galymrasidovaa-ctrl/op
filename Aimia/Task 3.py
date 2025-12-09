# Конкретті хабарламалар кластар
class EmailNotification:
    def send(self, message: str):
        print(f"Email sent: {message}")


class SMSNotification:
    def send(self, message: str):
        print(f"SMS sent: {message}")


class PushNotification:
    def send(self, message: str):
        print(f"Push notification sent: {message}")


# Factory классы
class NotificationFactory:
    # Барлық типтерді сақтайтын dictionary
    _creators = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification
    }

    @classmethod
    def get(cls, notification_type: str):
        notification_type = notification_type.lower()
        if notification_type in cls._creators:
            return cls._creators[notification_type]()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

    @classmethod
    def register(cls, notification_type: str, creator_class):
        """Жаңа хабарламалар типін қосу үшін"""
        cls._creators[notification_type.lower()] = creator_class


# Демонстрация
factory = NotificationFactory()

# Email
email_notification = factory.get("email")
email_notification.send("Hello via Email!")

# SMS
sms_notification = factory.get("sms")
sms_notification.send("Hello via SMS!")

# Push
push_notification = factory.get("push")
push_notification.send("Hello via Push Notification!")

# Жаңа тип қосу (мысалы WhatsApp)
class WhatsAppNotification:
    def send(self, message: str):
        print(f"WhatsApp sent: {message}")


NotificationFactory.register("whatsapp", WhatsAppNotification)
whatsapp_notification = factory.get("whatsapp")
whatsapp_notification.send("Hello via WhatsApp!")
