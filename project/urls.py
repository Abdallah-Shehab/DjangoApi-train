
from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)


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

    # 5.1 mixins get post
    path('rest/ml/', views.mixins_list.as_view()),

    # 5.2 mixins retrive delete put
    path('rest/ml/<int:pk>', views.mixins_pk.as_view()),


    # 6.1 generics get post
    path('rest/gen/', views.generics_list.as_view()),

    # 6.2 generics get put delete
    path('rest/gen/<int:pk>', views.generics_pk.as_view()),


    # 7 viewsets
    path('rest/viewsets/', include(router.urls)),

    # 8 find movies
    path('fbv/findmovie/', views.find_movie),

    # 9 new reservation
    path('function/newres', views.new_reservation),
]
