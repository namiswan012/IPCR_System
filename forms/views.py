from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date

# Create your views here.

def IPCRForm(request):
    previous_response_syllabus = IPCR_Syllabus_model.objects.filter(author=request.user).last()
    previous_response_courseguide = IPCR_CourseGuide_model.objects.filter(author=request.user).last()
    previous_response_SLM = IPCR_SLM_model.objects.filter(author=request.user).last()
    previous_response_subjectareas = IPCR_SubjectAreas_model.objects.filter(author=request.user).last()
    previous_response_attendancesheet = IPCR_AttendanceSheet_model.objects.filter(author=request.user).last()
    previous_response_classrecord = IPCR_ClassRecord_model.objects.filter(author=request.user).last()
    previous_response_teachingeffectiveness = IPCR_TeachingEffectiveness_model.objects.filter(author=request.user).last()

    
    
    if (request.method == 'POST'):
        form_syllabus = IPCR_Syllabus_form(request.POST)
        form_courseguide = IPCR_CourseGuide_form(request.POST)
        form_SLM = IPCR_SLM_form(request.POST)
        form_subjectareas = IPCR_SubjectAreas_form(request.POST)
        form_attendancesheet = IPCR_AttendanceSheet_form(request.POST)              
        form_classrecord = IPCR_ClassRecord_form(request.POST)              
        form_teachingeffectiveness = IPCR_TeachingEffectiveness_form(request.POST)   
        
        
              
        if (form_syllabus.is_valid()):
            cd = form_syllabus.cleaned_data
            IPCR_syllabus = IPCR_Syllabus_model(
                syllabus_Target = cd['syllabus_Target'],
                syllabus_Accomplished = cd ['syllabus_Accomplished'],
            )

            IPCR_syllabus.author = request.user
            IPCR_syllabus.syllabus_Submitted = date.today()
            IPCR_syllabus.save()

        if (form_courseguide.is_valid()):
            cd = form_courseguide.cleaned_data
            IPCR_courseguide =IPCR_CourseGuide_model(
               CourseGuide_Target = cd['CourseGuide_Target'],
               CourseGuide_Accomplished = cd ['CourseGuide_Accomplished'],
            )

            IPCR_courseguide.author = request.user
            IPCR_courseguide.CourseGuide_Submitted = date.today()
            IPCR_courseguide.save()

            messages.success(request, "The IPCR Form has been saved.")

        if (form_SLM.is_valid()):
            cd = form_SLM.cleaned_data
            IPCR_SLM =IPCR_SLM_model(
               SLM_Target = cd['SLM_Target'],
               SLM_Accomplished = cd ['SLM_Accomplished'],
            )

            IPCR_SLM.author = request.user
            IPCR_SLM.SLM_Submitted = date.today()
            IPCR_SLM.save()

            messages.success(request, "The IPCR Form has been saved.")

        if (form_subjectareas.is_valid()):
            cd = form_subjectareas.cleaned_data
            IPCR_subjectareas =IPCR_SubjectAreas_model(
               SubjectAreas_Target = cd['SubjectAreas_Target'],
               SubjectAreas_Accomplished = cd ['SubjectAreas_Accomplished'],
            )

            IPCR_subjectareas.author = request.user
            IPCR_subjectareas.SubjectAreas_Submitted = date.today()
            IPCR_subjectareas.save()

            messages.success(request, "The IPCR Form has been saved.")

        if (form_attendancesheet.is_valid()):
            cd = form_attendancesheet.cleaned_data
            IPCR_attendancesheet =IPCR_AttendanceSheet_model(
               AttendanceSheet_Target = cd['AttendanceSheet_Target'],
               AttendanceSheet_Accomplished = cd ['AttendanceSheet_Accomplished'],
            )

            IPCR_attendancesheet.author = request.user
            IPCR_attendancesheet.AttendanceSheet_Submitted = date.today()
            IPCR_attendancesheet.save()

            messages.success(request, "The IPCR Form has been saved.")

        if (form_classrecord.is_valid()):
            cd = form_classrecord.cleaned_data
            IPCR_classrecord =IPCR_ClassRecord_model(
               ClassRecord_Target = cd['ClassRecord_Target'],
               ClassRecord_Accomplished = cd ['ClassRecord_Accomplished'],
            )

            IPCR_classrecord.author = request.user
            IPCR_classrecord.ClassRecord_Submitted = date.today()
            IPCR_classrecord.save()

            messages.success(request, "The IPCR Form has been saved.")

        if (form_teachingeffectiveness.is_valid()):
            cd = form_teachingeffectiveness.cleaned_data
            IPCR_teachingeffectiveness =IPCR_TeachingEffectiveness_model(
               TeachingEffectiveness_Target = cd['TeachingEffectiveness_Target'],
               TeachingEffectiveness_Accomplished = cd ['TeachingEffectiveness_Accomplished'],
            )

            IPCR_teachingeffectiveness.author = request.user
            IPCR_teachingeffectiveness.TeachingEffectiveness_Submitted = date.today()
            IPCR_teachingeffectiveness.save()

            messages.success(request, "The IPCR Form has been saved.")


    else:
            initial_data = {}
            if previous_response_syllabus:
                initial_data['syllabus_Target'] = previous_response_syllabus.syllabus_Target
                initial_data['syllabus_Accomplished'] = previous_response_syllabus.syllabus_Accomplished

            if previous_response_courseguide:
                initial_data['CourseGuide_Target'] = previous_response_courseguide.CourseGuide_Target
                initial_data['CourseGuide_Accomplished'] = previous_response_courseguide.CourseGuide_Accomplished
                
            if previous_response_SLM:
                initial_data['SLM_Target'] = previous_response_SLM.SLM_Target
                initial_data['SLM_Accomplished'] = previous_response_SLM.SLM_Accomplished

            if previous_response_subjectareas:
                initial_data['SubjectAreas_Target'] = previous_response_subjectareas.SubjectAreas_Target
                initial_data['SubjectAreas_Accomplished'] = previous_response_subjectareas.SubjectAreas_Accomplished
                
            if previous_response_attendancesheet:
                initial_data['AttendanceSheet_Target'] = previous_response_attendancesheet.AttendanceSheet_Target
                initial_data['AttendanceSheet_Accomplished'] = previous_response_attendancesheet.AttendanceSheet_Accomplished
                
            if previous_response_classrecord:
                initial_data['ClassRecord_Target'] = previous_response_classrecord.ClassRecord_Target
                initial_data['ClassRecord_Accomplished'] = previous_response_classrecord.ClassRecord_Accomplished  
                
            if previous_response_teachingeffectiveness:
                initial_data['TeachingEffectiveness_Target'] = previous_response_teachingeffectiveness.TeachingEffectiveness_Target
                initial_data['TeachingEffectiveness_Accomplished'] = previous_response_teachingeffectiveness.TeachingEffectiveness_Accomplished                 
                

            form_syllabus = IPCR_Syllabus_form(initial=initial_data)
            form_courseguide = IPCR_CourseGuide_form(initial=initial_data)
            form_SLM = IPCR_SLM_form(initial=initial_data)
            form_subjectareas = IPCR_SubjectAreas_form(initial=initial_data)
            form_attendancesheet = IPCR_AttendanceSheet_form(initial=initial_data)
            form_classrecord = IPCR_ClassRecord_form(initial=initial_data)
            form_teachingeffectiveness = IPCR_TeachingEffectiveness_form(initial=initial_data)
    
    return render (request, 'forms/IPCRForm.html', {'form_syllabus' : form_syllabus , 'form_courseguide' : form_courseguide,
                                                    'form_SLM' : form_SLM, 'form_subjectareas' : form_subjectareas, 'form_attendancesheet' : form_attendancesheet,
                                                    'form_classrecord' : form_classrecord, 'form_teachingeffectiveness' : form_teachingeffectiveness,
                                                    })



def Show_IPCR(request):
    Current_user = request.user
    IPCR_Data = IPCR_Syllabus_model.objects.filter(author = Current_user)
    
    return render (request, 'forms/IPCRForm_View.html', {'IPCR_Data' : IPCR_Data})
    
    