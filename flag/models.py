from django.db import models
from django.contrib import messages

FLAGS = {
        'xss1': 'GOTROOT{flag_is_xss1}',
        'xss2': 'GOTROOT{flag_is_xss2}',
        'SQL1': 'GOTROOT{flag_is_SQL1}',
        'traversal': 'GOTROOT{flag_is_4}',
}
class Flag(models.Model):

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True) #flag 제출한 시간 기록
    data = models.CharField(blank=True, max_length=255, verbose_name="data")

    def __str__(self):
        return self.user.email

    @property
    def check_flag(self):
        for item in FLAGS:
            if self.data == FLAGS[item]:
                return 1
        return 0

    @property
    def get_user(self):
        return self.user

class User_total(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email

    @property
    def add_total(self):
        self.total += 1000

    @property
    def get_total(self):
        return self.total

    @property
    def get_user(self):
        return self.user
