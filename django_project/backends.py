from django.core.mail.backends.base import BaseEmailBackend

class NoEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        # Do nothing, effectively disabling email sending
        return len(email_messages)
