from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .services import TwilioService

from .exceptions import AccountDoesntExistException, InvalidSecurityCodeException


User = get_user_model()


class LoginOTPSerializer(serializers.Serializer):
    phone = PhoneNumberField(region=settings.PHONENUMBER_DEFAULT_REGION)
    otp = serializers.CharField(max_length=settings.TOKEN_LENGTH, min_length=settings.TOKEN_LENGTH)

    def validate(self, validated_data):
        phone = validated_data['phone']
        otp = validated_data['otp']

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            raise AccountDoesntExistException()

        verify = TwilioService(recipient=str(phone), otp=otp)
        status = verify.check_code()
        if not status:
            raise InvalidSecurityCodeException()
        validated_data['user'] = user
        return validated_data


class GetOTPSerializer(serializers.Serializer):
    phone = PhoneNumberField(region=settings.PHONENUMBER_DEFAULT_REGION)

    def save(self):
        phone = self.validated_data['phone']

        User.objects.get_or_create(phone=phone)

        verify = TwilioService(recipient=str(phone))
        verify.send_code()
