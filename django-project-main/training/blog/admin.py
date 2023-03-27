from django.contrib import admin
from blog.models import Blog
from datetime import timedelta
from django.utils import timezone

# Register your models here.

class RegisteredBlog(admin.ModelAdmin):
      
      list_display=['title','author','description','is_published','is_recently_published']

      def is_recently_published(self,pub_date):

        if pub_date.is_published==True:
           date=pub_date.published_on
           now = timezone.now()
           end = now - timezone.timedelta(days=1)
           begin = now + timezone.timedelta(days=1)

           if date > end and date < begin:
                return True
           else:
                return False
      is_recently_published.short_description = 'Latest Published'  
              

admin.site.register(Blog,RegisteredBlog)
    



