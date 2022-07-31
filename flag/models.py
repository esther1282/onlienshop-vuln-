from django.db import models
from django.contrib import messages

FLAGS = {
        'xss1': 'GOTROOT{flag_is_xss1}',
        'xss2': 'GOTROOT{y0oure_Xss_m@st3r}',
        'SQL1': 'GOTROOT{flag_is_SQL1}',
        'directory_traversal1': 'GOTROOT{ddfdg_ssd23_eccts3l}',
        'source1':'GOTROOT{s0UrC3_c0de1_g00d}',
        'source2':'GOTROOT{m3dia_fl@g_h3re}',
        'param1':'GOTROOT{p@r@m3T3r}',
        'javascript1':'GOTROOT{jAv@3cript_w311}',
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

