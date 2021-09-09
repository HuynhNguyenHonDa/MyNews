from django import forms
from django.contrib import admin
from firstapp.models import StoriesCategory, StoriesStory
from ckeditor.widgets import CKEditorWidget

admin.site.site_header = 'Chào mừng đến với trang quản trị '                    # default: "Django Administration"
admin.site.index_title = 'Quản lý dữ liệu cho cẩn thận kẻo hư nha!'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration' # default: "Django site admin"

class StoriesStoryAmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'url', 'public_day', 'category', 'image', )
    list_filter = ['category']
admin.site.register(StoriesStory, StoriesStoryAmin)

# class PostAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = StoriesStory
#         fields = '__all__'
# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm

# admin.site.register(StoriesStory, PostAdmin)
