
from django.contrib import admin
from django.urls import path, include
from tickets import views
urlpatterns = [
    path('admin/', admin.site.urls),

    # 1
    path('django/jsonres/', views.no_rest_no_model),

    # 2
    path('django/jsonresfrommodel/', views.no_rest_from_model),

    # 3.1 GET POST from rest framework function based view @api_view
    path('rest/fbv/', views.FBV_List),

    # 3.2 GET PUT DELETE from rest framework function based view @api_view
    path('rest/fbv/<int:pk>', views.FBV_PK),

    # 4.1 GET POST from rest framework Class  based view APIVIEW
    path('rest/cbv/', views.CBV_List.as_view()),

    # 4.2 GET PUt DELETE from rest framework Class  based view APIVIEW
    path('rest/cbv/<int:pk>', views.CBV_PK.as_view()),

]
