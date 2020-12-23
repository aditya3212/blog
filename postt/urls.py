from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('postt.urls'))
    path('',views.index,name="index"),
     path('allpost',views.PostList.as_view(),name='home'),
    path('<slug:slug>/',views.PostDetail.as_view(),name='post_detail'),
]