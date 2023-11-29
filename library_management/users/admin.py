from django.contrib import admin
from users import models


# Register your models here.
@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "user_name", "email", "date_joined", "updated"]
    search_fields = ["user_name", "email"]
    list_filter = ["deleted"]
    ordering = ["-date_joined"]

    class Meta:
        verbose_name = ("Пользователи библиотеки")
