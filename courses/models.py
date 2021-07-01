from django.db import models
from django.core.validators import MinValueValidator as minv, MaxValueValidator as maxv
from django.utils import timezone



class Course(models.Model):

    COURSE_PERMISSIONS = (
        ("fr", "رایگان"),
        ("vp", "کاربر ویژه"),
        ("mn", "نقدی")
    )
    
    title = models.CharField(max_length=130, verbose_name="عنوان دوره", help_text="در اینجا میتوانید نام دوره خود را وارد کنید")
    slug = models.SlugField(max_length=230, verbose_name="لینک دوره")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت محصول", help_text="قیمت محصول رو وارد نمایید")
    body = models.TextField(verbose_name="توضیحات محصول", help_text="در اینجا میتوانید توضیحات مفید در رابطه با پروژه خود اضافه کنید")
    cover = models.ImageField(upload_to="course_cover/%Y/%m/%d", verbose_name="کاور پروژه", help_text="در اینجا کاور دوره رو آپلود کنید")
    cover_video = models.FileField(upload_to=f"course_video/{title}", verbose_name="ویدیو معرفی", help_text="در اینجا ویدیو معرفی دوره خود را ببینید")
#   parts =
    score = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="امتیاز دوره", blank=True, default=0.0, validators=[minv(0.0), maxv(10.0)])   
    total_score_voted = models.DecimalField(max_digits=300, blank=True, default=0.0, decimal_places=1)
    users_voted = models.ForeignKey("users.User", blank=True, null=True, on_delete=models.CASCADE, related_name="ucourse") 
    permission = models.CharField(max_length=8 ,choices=COURSE_PERMISSIONS, verbose_name="سطح دسترسی دوره", help_text="در اینجا سطح دسترسی دوره را تعریف کنید")
    publish_date = models.DateField(default=timezone.now, blank=True, verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'name: {self.title} | price: {self.price}'

    def vote_course(self, user, vote):
        self.total_score_voted += vote
        if user not in self.users_voted:
            self.users_voted += user
        else:
            return "شما از قبل امتیاز داده اید!"    
        self.score = self.total_score_voted / len(self.users_voted)

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها" 
        ordering = ["publish_date", "score"]    