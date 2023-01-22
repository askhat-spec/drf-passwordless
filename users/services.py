from twilio.rest import Client
from django.conf import settings


class TwilioService:
    ACCOUNT_SID = settings.TWILIO_ACCOUNT_SID
    AUTH_TOKEN = settings.TWILIO_AUTH_TOKEN
    VERIFY_SID = settings.TWILIO_VERIFY_SID
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def __init__(self, recipient:str, otp:str=None):
        self.recipient = recipient
        self.otp = otp

    def send_code(self) -> bool:
        verification = self.client.verify.v2.services(self.VERIFY_SID) \
        .verifications \
        .create(to=self.recipient, channel="sms")
        return verification.valid

    def check_code(self, otp:str=None) -> bool:
        if otp:
            self.otp = otp
        verification_check = self.client.verify.v2.services(self.VERIFY_SID) \
        .verification_checks \
        .create(to=self.recipient, code=self.otp)
        return verification_check.valid
