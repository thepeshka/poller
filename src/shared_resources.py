class Alert:
    def __init__(self, type="info", content=None, content_type="text/text"):
        self.type = type
        self.content = content
        self.content_type = content_type


alerts = {
    "registration_closed": Alert("warn", "Registration is closed")
}