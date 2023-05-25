from django.contrib import admin
from .models import Guest, Movie, Reservation
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'email',
#                     'is_active', 'is_staff')
#     list_display_links = ('id', 'email')

#     list_editable = ('is_active', 'is_staff')
#     search_fields = ('username', 'email')
#     list_per_page = 25


# admin.site.register(UserAccount, UserAdmin)
admin.site.register(Guest)
admin.site.register(Movie)
admin.site.register(Reservation)
