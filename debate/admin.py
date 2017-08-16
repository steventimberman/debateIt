# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import DebateTopic, DebateSide, Point, UserProfile, Friend

admin.site.register(DebateTopic)
admin.site.register(DebateSide)
admin.site.register(Point)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp')

    def user_info(self, obj):
        pass

    user_info.short_description = 'Info'

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Friend)
admin.site.site_header = 'DebateIt Administration'