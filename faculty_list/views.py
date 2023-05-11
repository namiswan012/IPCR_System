from django.shortcuts import render

# Create your views here.
def member_faculty_list(request):
    return render(request, ('faculty_list/member_faculty_list.html'))