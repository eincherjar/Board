from django.contrib import admin
from .models import Notice


class NoticeAdmin(admin.ModelAdmin):
    search_fields = ('title','author')
    list_display = ('title','create_date','author','notice_poster')
    list_filter = ['create_date','author']
    exclude = ('author',)
    
    def save_model(self, request, task, form, change):
        task.author = request.user
        task.save()
        
    def get_queryset(self, request):
        qs = super(NoticeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

admin.site.register(Notice, NoticeAdmin),