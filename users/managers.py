from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone):
        if not phone:
            raise ValueError('User must have a phone number!')
        user = self.model(phone=phone)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        if not password:
            raise ValueError('Password is required!')
        user = self.create_user(phone=phone)
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user
