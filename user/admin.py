from django.contrib import admin
from user.models import Profile, SMScode



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age')
    fields = ('user', 'age', 'avatar', 'bio')

@admin.register(SMScode)
class SMScodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'code')

