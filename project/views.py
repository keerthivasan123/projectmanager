from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from .models import Project,ProjectAllocationPlan,ProjectPhase,ProjectAssignmentPlan
from django.shortcuts import render

def projectListPage(request):
    all_project=Project.objects.all()
    context = {'all_project'all_project}
    return render(request,'project/index.html',context)

def projectDetailPage(request,project_id):
    project=get_list_or_404(Project,pk=project_id)
    return render(request,'project/details.html',{'project':project})

def phaseDefinitionPage(request):
    all_project_phase=Album.objects.all()
    context = {'all_albums':all_albums}
    return render(request,'music/index.html',context)

def resourseAssignmentPage(request,album_id):
    album=get_list_or_404(Album,pk=album_id)
    return render(request,'music/details.html',{'album':album})

def resourseAllocationPage(request):
    all_albums=Album.objects.all()
    context = {'all_albums':all_albums}
    return render(request,'music/index.html',context)

def resourseLoadReport(request,album_id):
    album=get_list_or_404(Album,pk=album_id)
    return render(request,'music/details.html',{'album':album})
def resoursePlanReport(request):
    all_albums=Album.objects.all()
    context = {'all_albums':all_albums}
    return render(request,'music/index.html',context)
