from django.contrib import admin
from .models import Place, Feedback


admin.site.register(Place)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['place', 'text', 'user', 'checked']
    list_editable = ['checked']
    list_filter = ['checked']
    search_fields = ['text', 'place__name', 'place__location', 'place__decription']

    fields = ['user', 'place', 'text']
    readonly_fields = ['place', 'text']



admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
