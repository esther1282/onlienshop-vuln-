from django.db import models
import uuid
from selenium import webdriver

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
        uuid = self.uuid
        super().save(*args, **kwargs)
        url = "http://127.0.0.1:7878/board/" + str(uuid) + "/"
        cookie = {"name": "flag", "value": 'GOTROOT{c00ki3_i3_Fla9}'}
        read_url(url, cookie)

def read_url(url, cookie={"name": "name", "value": "value"}):
    cookie.update({"domain": "127.0.0.1"})
    try:
        options = webdriver.ChromeOptions()
        for _ in [
            "headless",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ]:
            options.add_argument(_)
        driver = webdriver.Chrome('C:\\Users\\seoji\\Desktop\\chromedriver.exe', options=options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get("http://127.0.0.1:7878/")
        driver.add_cookie(cookie)
        driver.get(url)
    except Exception as e:
        driver.quit()
        # return str(e)
        return False
    driver.quit()
    return True

def xss_filter(title):
    title = title.lower()
    _filter = ["window", "self", "this", "img", "script"]
    for f in _filter:
        if f in title:
            title = title.replace(f, "")
    return title

