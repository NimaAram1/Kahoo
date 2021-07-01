from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, username, password):

        if not username:
            raise ValueError("نام کاربری حتما باید وارد شود")

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        
        user = self.create_user(email=email, username=username, password=password) 
        user.is_admin = True
        user.save(using=self._db)
        return user    

    def return_user_instance(self, email, username, password):

        user = self.model(email=email, username=username) 
        user.set_password(password)
        return user   