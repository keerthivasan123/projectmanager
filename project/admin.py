from django.contrib import admin
from .models import Project,ProjectPhase,ProjectAllocationPlan,ProjectAssignmentPlan

admin.site.register(Project)
admin.site.register(ProjectPhase)
admin.site.register(ProjectAssignmentPlan)
admin.site.register(ProjectAllocationPlan)