from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """自定义用户模型类"""

    # 在用户模型类中增加 mobile 字段
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    # 对当前表进行相关设置:
    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    # 在 str 魔法方法中, 返回用户名称
    def __str__(self):
        return self.username



class userlist(models.Model):
    """自定义用户模型类"""

    # 在用户模型类中增加 mobile 字段
    date=models.DateTimeField(auto_now=True,null=True)
    name=models.CharField(max_length=10)
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    address=models.CharField(max_length=64)
    state=models.BooleanField(default=False)

    # 对当前表进行相关设置:
    class Meta:
        db_table = 'tb_userlist'
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name

    # 在 str 魔法方法中, 返回用户名称
    def __str__(self):
        return self.name