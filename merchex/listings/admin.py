from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Ticket, Review, UserFollows
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('login', 'is_staff', 'is_active',)
    list_filter = ('login', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('login',)
    ordering = ('login',)


class CustomTicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ('title', 'user', 'image','time_created')
    list_filter = ('title', 'user', 'image','time_created')
    ordering = ('time_created',)


class CustomReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('headline','ticket', 'rating', 'user','time_created')
    list_filter = ('headline','ticket', 'rating', 'user','time_created')
    ordering = ('time_created',)


class CustomUserFollowAdmin(admin.ModelAdmin):
    model = UserFollows
    list_display = ('user', 'followed_user')
    list_filter = ('user', 'followed_user')
    ordering = ('user',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Ticket, CustomTicketAdmin)
admin.site.register(Review, CustomReviewAdmin)
admin.site.register(UserFollows, CustomUserFollowAdmin)