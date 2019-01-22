class Alert:
    def __init__(self, type="info", content=None):
        self.type = type
        self.content = content

alerts = {
    "registration_closed": Alert("warn", "Registration is closed")
}