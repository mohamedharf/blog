from django.contrib import admin
#import blog
from .models import Blog , Coment


# Register your models here.
admin.site.register ( [
    Blog  , Coment])

