from django.contrib import admin
from .models import Project, Skill, Tags, Messages, Endorsements, Comments
# Register your models here.


admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tags)
admin.site.register(Messages)
admin.site.register(Endorsements)
admin.site.register(Comments)