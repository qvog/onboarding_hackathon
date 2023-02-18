from django.contrib.auth.base_user import BaseUserManager

class EmployeeManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, identifier, password, **extra_fields):
        if not identifier:
            raise ValueError('The given identifier must be set')
        user = self.model(identifier=identifier, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, identifier, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(identifier, password, **extra_fields)

    def create_superuser(self, identifier, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(identifier, password, **extra_fields)