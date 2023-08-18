from django import forms
from django.contrib import admin
from .models import *
# Register your models here.


class SongAdminForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'


class SongAdmin(admin.ModelAdmin):
    form = SongAdminForm
    list_display = ['title', 'scheduled_publish_time', 'is_published']

    def save_model(self, request, obj, form, change):
        if obj.can_publish() and not obj.is_published:
            obj.is_published = True
        super().save_model(request, obj, form, change)


admin.site.register(Song, SongAdmin)
admin.site.register(Tag)
admin.site.register(Album)
admin.site.register(Like)
admin.site.register(Favorite)
admin.site.register(Comment)
