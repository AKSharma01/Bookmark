from django.conf.urls import url
from django.views.generic import ListView
from models import book_db
urlpatterns=[
	url(r'^$',ListView.as_view(queryset=book_db.objects.all().order_by("id"),template_name='bookmark/index.html')),
]