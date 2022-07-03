from . import views
from django.urls import URLPattern, path


urlpatterns = [
    path('', views.index, name='index'),
    path('log', views.log, name='log'),
    path('reg', views.reg, name='reg'),
    path('main', views.main, name='main'),
    path('sp_dis', views.sp_dis, name='sp_dis'),
    path('sp_komp', views.sp_komp, name='sp_komp'),
]