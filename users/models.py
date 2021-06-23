from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

class User(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        ("df", "کاربر عادی"),
        ("pr", "کاربر حرفه ای"),
        ("te", "معلم"),
        ("ad", "ادمین")
    )
    username = models.CharField(max_length=190, verbose_name="نام کاربری", unique=True, help_text="در اینجا نام کاربری خود را وارد نمایید")
    email = models.EmailField(max_length=200, verbose_name="ایمیل", unique=True, help_text="ایمیل خود را وارد نمایید")
    birth_date = models.DateField(verbose_name="تاریخ تولد", null=True, blank=True, help_text="تاریخ تولد خود را وارد نمایید")
    age = models.PositiveIntegerField(verbose_name="سن", max_digits=3, null=True, blank=True, help_text="سن خود را وارد نمایید")
    bio = models.TextField(verbose_name="درباره", null=True, blank=True, help_text="درباره خود میتوانید چند خط بنویسید")
#   courses_bought =
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, verbose_name="نوع حساب")
    favorite_tags = models.CharField(max_length=100, verbose_name="تگ های مورد علاقه", null=True, blank=True)
    wallet_stock = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="موجودی کیف پول")
    profile_image = models.ImageField(upload_to="profile_image/%Y/%m/%d", verbose_name="عکس پروفایل", blank=True, default="profile_image/default.png", help_text="عکس پروفایل خود را وارد نمایید")
    is_premium = models.BooleanField(default=False, verbose_name="آیا کاربر ویژه هستید؟")
    premium_until = models.DateTimeField(default=timezone.now, verbose_name="تا چه زمانی کاربر ویژه هستید")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{username} account"

    def is_premium_user(self) -> bool:
        if self.premium_until > timezone.now():
            self.is_premium = True
            return True
        else:
            self.is_premium = False
            return False

    def has_perm(self, perm, obj=None) -> True:
        return True


    def has_module_perms(self, app_label) -> True:
        return True

    @property
    def is_staff(self) -> bool :
        return self.is_admin

    class Meta:
        verbose_name = "حساب"
        verbose_name_plural = "حساب های کاربری"
        indexes = [
            models.Index(name="users_username_index", fields=['username'])
        ]
        constraints = [
            models.UniqueConstraint(name="check_username_and_email", fields=['username','email'])
        ]