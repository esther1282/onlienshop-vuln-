from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
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
        super().save(*args, **kwargs)

def xss_filter(title):
    title = title.lower()
    _filter = ["window", "self", "this", "img", "script"]
    for f in _filter:
        if f in title:
            title = title.replace(f, "")
    return title

