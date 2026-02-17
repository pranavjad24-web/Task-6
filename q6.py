class Notification:
    def send(self, msg):
        pass


class Email(Notification):
    def send(self, msg):
        print("Email sent:", msg)


class SMS(Notification):
    def send(self, msg):
        print("SMS sent:", msg)


def notify(service):
    service.send("Hello")


notify(Email())
notify(SMS())
