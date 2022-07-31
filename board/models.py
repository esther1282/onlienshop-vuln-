from django.db import models
import requests
import uuid

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    #hits = models.PositiveIntegerField(default=0)
    is_secret = models.BooleanField(default=False)
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)

    def __str__self(self):
        return self.post_title

    @property
    def get_writer(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.title = xss_filter(self.title)
        """uuid = self.uuid
        url = "http://127.0.0.1:8000/board/" + str(uuid) + "/"
        cookie = {'flag': 'GOTROOT{c00ki3_i3_Fla9}'}
        res = requests.get(url, cookies=cookie)"""
        super().save(*args, **kwargs)

def xss_filter(title):
    title = title.lower()
    _filter = ["window", "self", "this", "img", "script"]
    for f in _filter:
        if f in title:
            title = title.replace(f, "")
    return title

