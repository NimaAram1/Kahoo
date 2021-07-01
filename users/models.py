from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from courses.models import Course
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import UserManager
from .user_level_mechanism import is_increase_user_level

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
    age = models.IntegerField(verbose_name="سن", null=True, blank=True, help_text="سن خود را وارد نمایید")
    bio = models.TextField(verbose_name="درباره", null=True, blank=True, help_text="درباره خود میتوانید چند خط بنویسید")
    courses_bought = models.ManyToManyField(Course, related_name="cuser", verbose_name="دوره های خریداری شده", blank=True)
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, verbose_name="نوع حساب", default="df")
    favorite_tags = models.CharField(max_length=100, verbose_name="تگ های مورد علاقه", null=True, blank=True)
    wallet_stock = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="موجودی کیف پول", default=0)
    profile_image = models.ImageField(upload_to="profile_image/%Y/%m/%d", verbose_name="عکس پروفایل", blank=True, default="profile_image/default.png", help_text="عکس پروفایل خود را وارد نمایید")
    is_premium = models.BooleanField(default=False, verbose_name="آیا کاربر ویژه هستید؟")
    premium_until = models.DateTimeField(default=timezone.now, verbose_name="تا چه زمانی کاربر ویژه هستید")
    user_level = models.IntegerField(verbose_name="سطح حساب شما", blank=True, default=0)
    experiments = models.BigIntegerField(verbose_name="میزان تجربه کاربری", blank=True, default=15) 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return f"{self.username} account"

    def is_premium_user(self):
        if self.premium_until > timezone.now():
            self.is_premium = True
            return True
        else:
            self.is_premium = False
            return False

    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "حساب"
        verbose_name_plural = "حساب های کاربری"
        indexes = [
            models.Index(name="users_username_index", fields=['username'])
        ]
        constraints = [
            models.UniqueConstraint(fields=['username', 'email'], name="check_username_and_email" )
        ]

@receiver(post_save, sender=User)
def save_level(sender, **kwargs):
    pass                    