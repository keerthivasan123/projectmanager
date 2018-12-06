from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Project(models.Model):
    name = models.CharField(default='inactive',max_length=250)
    comments = models.CharField(default='inactive,max_length=250')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    comments = models.CharField(default='inactive,max_length=250')
    plannedStateDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    projectType = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    engagementType = models.ForeignKey(ET, on_delete=models.CASCADE)
    partner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    paymentTerms = models.IntegerField(default='inactive',max_length=250)
    actualStartDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    actualEndDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE)
    type = models.CharField(default='inactive,max_length=250')

    def __str__(self):
        return self.name

class ProjectPhase(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    plannedStartDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    plannedEndDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    actualStartDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    actualEndDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    status = models.ForeignKey(ProjectPhaseStatus, on_delete=models.CASCADE)
    def __str__(self):
        return self.phase

class ProjectAssignmentPlan(models.Model):
    components = models.CharField(max_length=250)
    startDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    endDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    FTE = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.components

class ProjectAllocationPlan(models.Model):
    components = models.CharField(max_length=250)
    startDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    endDate = models.DateField(auto_now=False, auto_now_add=False, **options)
    FTE = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.components