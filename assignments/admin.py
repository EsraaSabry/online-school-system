from django.contrib import admin

# Register your models here.
from .models import Choice, Questions, Assignment, GradedAssignment

admin.site.register(Choice)
admin.site.register(Questions)
admin.site.register(Assignment)
admin.site.register(GradedAssignment)
