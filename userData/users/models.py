from django.db import models
from django.core.validators import RegexValidator

class Userinfo(models.Model):
    f_name      = models.CharField(max_length=120)
    l_name      = models.CharField(max_length=120)
    s_name      = models.CharField(max_length=120)
    title_name  = models.CharField(max_length=120)
    email       = models.EmailField(null=False,blank=False)
    contact     = models.CharField(max_length=10, blank=True)
    contact_ext = models.CharField(max_length=4)
    join_date   = models.DateField()
    picture_lg  = models.URLField(blank=True,null=True)
    picture_md  = models.URLField(blank=True,null=True)
    picture_sm  = models.URLField(blank=True,null=True)
    team        = models.CharField(max_length=120)
    job_title   = models.CharField(max_length=120)
    logged_in   = models.BooleanField(default=False)
    last_logged = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    @property
    def is_loggedin(self):
        return self.logged_in
    
