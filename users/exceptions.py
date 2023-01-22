from rest_framework.exceptions import APIException
from django.utils.translation import gettext as _


class AccountDoesntExistException(APIException):
    status_code = 404
    default_detail = _("Couldn't find an account with this phone number.")
    default_code = 'account-doesnt-exist'


class InvalidSecurityCodeException(APIException):
    status_code = 400
    default_detail = _('Invalid code.')
    default_code = 'invalid-security-code'


class ExpiredSecurityCodeException(APIException):
    status_code = 400
    default_detail = _('Security code is expired.')
    default_code = 'expired-security-code'