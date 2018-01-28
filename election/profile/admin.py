from django.contrib import admin
from election.profile.models import UserProfile
from import_export import resources

class UserProfileResource (resources.ModelResource):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'created_at', 'active', )

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'is_active',)

admin.site.register(UserProfile, UserProfileAdmin)