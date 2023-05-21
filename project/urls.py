
from django.contrib import admin
from django.urls import path, include
from tickets import views
urlpatterns = [
    path('admin/', admin.site.urls),

    # 1
    path('django/jsonres/',views.no_rest_no_model),

    #2
    path('django/jsonresfrommodel/',views.no_rest_from_model),

]
