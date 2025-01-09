from django.contrib import admin
from port.models import About,Education,Skills,Certificate,Project,ProjectImage

# Register your models here.
admin.site.register(About)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Certificate)
# admin.site.register(Project)
# admin.site.register(ProjectImage)
class ProjectImageInline(admin.TabularInline):  # You can also use StackedInline if you prefer
    model = ProjectImage
    extra = 1  # Number of empty image slots shown by default

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'category', 'client')
    search_fields = ('title', 'category', 'client')

admin.site.register(Project, ProjectAdmin)

