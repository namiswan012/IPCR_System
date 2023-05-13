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
    previous_response_classroomobservation = IPCR_ClassroomObservation_model.objects.filter(author=request.user).last()
    previous_response_midtermtosrubrics = IPCR_MidtermTOSRubrics_model.objects.filter(author=request.user).last()
    previous_response_finaltermtosrubrics = IPCR_FinaltermTOSRubrics_model.objects.filter(author=request.user).last()
    previous_response_midtermtestquestions = IPCR_MidtermTestQuestions_model.objects.filter(author=request.user).last()
    previous_response_finaltermtestquestions = IPCR_FinaltermTestQuestions_model.objects.filter(author=request.user).last()
    previous_response_midtermanswerkey = IPCR_MidtermAnswerKey_model.objects.filter(author=request.user).last()
    previous_response_finaltermanswerkey = IPCR_FinaltermAnswerKey_model.objects.filter(author=request.user).last()
    previous_response_gradingsheet = IPCR_GradingSheet_model.objects.filter(author=request.user).last()
    previous_response_studentadviced = IPCR_StudentAdviced_model.objects.filter(author=request.user).last()
    previous_response_accomplishmentreport = IPCR_AccomplishmentReport_model.objects.filter(author=request.user).last()
    previous_response_researchproposalsubmitted = IPCR_ResearchProposalSubmitted_model.objects.filter(author=request.user).last()
    previous_response_researchimplemented = IPCR_ResearchImplemented_model.objects.filter(author=request.user).last()
    previous_response_researchpresented = IPCR_ResearchPresented_model.objects.filter(author=request.user).last()
    previous_response_researchpublished = IPCR_ResearchPublished_model.objects.filter(author=request.user).last()
    previous_response_approvediprights = IPCR_ApprovedIPRights_model.objects.filter(author=request.user).last()
    previous_response_researchutilized = IPCR_ResearchUtilized_model.objects.filter(author=request.user).last()
    previous_response_numberofcitations = IPCR_NumberOfCitations_model.objects.filter(author=request.user).last()
   
    
    if (request.method == 'POST'):
        form_syllabus = IPCR_Syllabus_form(request.POST)
        form_courseguide = IPCR_CourseGuide_form(request.POST)
        form_SLM = IPCR_SLM_form(request.POST)
        form_subjectareas = IPCR_SubjectAreas_form(request.POST)
        form_attendancesheet = IPCR_AttendanceSheet_form(request.POST)              
        form_classrecord = IPCR_ClassRecord_form(request.POST)              
        form_teachingeffectiveness = IPCR_TeachingEffectiveness_form(request.POST)   
        form_classroomobservation = IPCR_ClassroomObservation_form(request.POST)   
        form_midtermtosrubrics = IPCR_MidtermTOSRubrics_form(request.POST)   
        form_finaltermtosrubrics = IPCR_FinaltermTOSRubrics_form(request.POST)   
        form_midtermtestquestions = IPCR_MidtermTestQuestions_form(request.POST)   
        form_finaltermtestquestions = IPCR_FinaltermTestQuestions_form(request.POST)   
        form_midtermanswerkey = IPCR_MidtermAnswerKey_form(request.POST)   
        form_finaltermanswerkey = IPCR_FinaltermAnswerKey_form(request.POST)   
        form_gradingsheet = IPCR_GradingSheet_form(request.POST)   
        form_studentadviced = IPCR_StudentAdviced_form(request.POST)   
        form_accomplishmentreport = IPCR_AccomplishmentReport_form(request.POST)   
        form_researchproposalsubmitted = IPCR_ResearchProposalSubmitted_form(request.POST)   
        form_researchimplemented = IPCR_ResearchImplemented_form(request.POST)   
        form_researchpresented = IPCR_ResearchPresented_form(request.POST)   
        form_researchpublished = IPCR_ResearchPublished_form(request.POST)   
        form_approvediprights = IPCR_ApprovedIPRights_form(request.POST)   
        form_researchutilized = IPCR_ResearchUtilized_form(request.POST)   
        form_numberofcitations = IPCR_NumberOfCitations_form(request.POST)   

        
              
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
            
        if (form_classroomobservation.is_valid()):
            cd = form_classroomobservation.cleaned_data
            IPCR_classroomobservation =IPCR_ClassroomObservation_model(
               ClassroomObservation_Target = cd['ClassroomObservation_Target'],
               ClassroomObservation_Accomplished = cd ['ClassroomObservation_Accomplished'],
            )

            IPCR_classroomobservation.author = request.user
            IPCR_classroomobservation.ClassroomObservation_Submitted = date.today()
            IPCR_classroomobservation.save()

            messages.success(request, "The IPCR Form has been saved.")

        if (form_midtermtosrubrics.is_valid()):
            cd = form_midtermtosrubrics.cleaned_data
            IPCR_midtermtosrubrics =IPCR_MidtermTOSRubrics_model(
               MidtermTOSRubrics_Target = cd['MidtermTOSRubrics_Target'],
               MidtermTOSRubrics_Accomplished = cd ['MidtermTOSRubrics_Accomplished'],
            )

            IPCR_midtermtosrubrics.author = request.user
            IPCR_midtermtosrubrics.MidtermTOSRubrics_Submitted = date.today()
            IPCR_midtermtosrubrics.save()

            messages.success(request, "The IPCR Form has been saved.")
            
        if (form_finaltermtosrubrics.is_valid()):
            cd = form_finaltermtosrubrics.cleaned_data
            IPCR_finaltermtosrubrics =IPCR_FinaltermTOSRubrics_model(
               FinaltermTOSRubrics_Target = cd['FinaltermTOSRubrics_Target'],
               FinaltermTOSRubrics_Accomplished = cd ['FinaltermTOSRubrics_Accomplished'],
            )

            IPCR_finaltermtosrubrics.author = request.user
            IPCR_finaltermtosrubrics.FinaltermTOSRubrics_Submitted = date.today()
            IPCR_finaltermtosrubrics.save()

            messages.success(request, "The IPCR Form has been saved.")            

        if (form_midtermtestquestions.is_valid()):
            cd = form_midtermtestquestions.cleaned_data
            IPCR_midtermtestquestions =IPCR_MidtermTestQuestions_model(
               MidtermTestQuestions_Target = cd['MidtermTestQuestions_Target'],
               MidtermTestQuestions_Accomplished = cd ['MidtermTestQuestions_Accomplished'],
            )

            IPCR_midtermtestquestions.author = request.user
            IPCR_midtermtestquestions.MidtermTestQuestions_Submitted = date.today()
            IPCR_midtermtestquestions.save()

            messages.success(request, "The IPCR Form has been saved.")            

        if (form_finaltermtestquestions.is_valid()):
            cd = form_finaltermtestquestions.cleaned_data
            IPCR_finaltermtestquestions =IPCR_FinaltermTestQuestions_model(
               FinaltermTestQuestions_Target = cd['FinaltermTestQuestions_Target'],
               FinaltermTestQuestions_Accomplished = cd ['FinaltermTestQuestions_Accomplished'],
            )

            IPCR_finaltermtestquestions.author = request.user
            IPCR_finaltermtestquestions.FinaltermTestQuestions_Submitted = date.today()
            IPCR_finaltermtestquestions.save()

            messages.success(request, "The IPCR Form has been saved.")             

        if (form_midtermanswerkey.is_valid()):
            cd = form_midtermanswerkey.cleaned_data
            IPCR_midtermanswerkey =IPCR_MidtermAnswerKey_model(
               MidtermAnswerKey_Target = cd['MidtermAnswerKey_Target'],
               MidtermAnswerKey_Accomplished = cd ['MidtermAnswerKey_Accomplished'],
            )

            IPCR_midtermanswerkey.author = request.user
            IPCR_midtermanswerkey.MidtermAnswerKey_Submitted = date.today()
            IPCR_midtermanswerkey.save()

            messages.success(request, "The IPCR Form has been saved.")    

        if (form_finaltermanswerkey.is_valid()):
            cd = form_finaltermanswerkey.cleaned_data
            IPCR_finaltermanswerkey =IPCR_FinaltermAnswerKey_model(
               FinaltermAnswerKey_Target = cd['FinaltermAnswerKey_Target'],
               FinaltermAnswerKey_Accomplished = cd ['FinaltermAnswerKey_Accomplished'],
            )

            IPCR_finaltermanswerkey.author = request.user
            IPCR_finaltermanswerkey.FinaltermAnswerKey_Submitted = date.today()
            IPCR_finaltermanswerkey.save()

            messages.success(request, "The IPCR Form has been saved.")   
            
        if (form_gradingsheet.is_valid()):
            cd = form_gradingsheet.cleaned_data
            IPCR_gradingsheet =IPCR_GradingSheet_model(
               GradingSheet_Target = cd['GradingSheet_Target'],
               GradingSheet_Accomplished = cd ['GradingSheet_Accomplished'],
            )

            IPCR_gradingsheet.author = request.user
            IPCR_gradingsheet.GradingSheet_Submitted = date.today()
            IPCR_gradingsheet.save()

            messages.success(request, "The IPCR Form has been saved.") 
            
        if (form_studentadviced.is_valid()):
            cd = form_studentadviced.cleaned_data
            IPCR_studentadviced =IPCR_StudentAdviced_model(
               StudentAdviced_Target = cd['StudentAdviced_Target'],
               StudentAdviced_Accomplished = cd ['StudentAdviced_Accomplished'],
            )

            IPCR_studentadviced.author = request.user
            IPCR_studentadviced.StudentAdviced_Submitted = date.today()
            IPCR_studentadviced.save()

            messages.success(request, "The IPCR Form has been saved.")
            
        if (form_accomplishmentreport.is_valid()):
            cd = form_accomplishmentreport.cleaned_data
            IPCR_accomplishmentreport =IPCR_AccomplishmentReport_model(
               AccomplishmentReport_Target = cd['AccomplishmentReport_Target'],
               AccomplishmentReport_Accomplished = cd ['AccomplishmentReport_Accomplished'],
            )

            IPCR_accomplishmentreport.author = request.user
            IPCR_accomplishmentreport.AccomplishmentReport_Submitted = date.today()
            IPCR_accomplishmentreport.save()

            messages.success(request, "The IPCR Form has been saved.")
        
        if (form_researchproposalsubmitted.is_valid()):
            cd = form_researchproposalsubmitted.cleaned_data
            IPCR_researchproposalsubmitted =IPCR_ResearchProposalSubmitted_model(
               ResearchProposalSubmitted_Target = cd['ResearchProposalSubmitted_Target'],
               ResearchProposalSubmitted_Accomplished = cd ['ResearchProposalSubmitted_Accomplished'],
            )

            IPCR_researchproposalsubmitted.author = request.user
            IPCR_researchproposalsubmitted.ResearchProposalSubmitted_Submitted = date.today()
            IPCR_researchproposalsubmitted.save()

            messages.success(request, "The IPCR Form has been saved.")                                
 
        if (form_researchimplemented.is_valid()):
            cd = form_researchimplemented.cleaned_data
            IPCR_researchimplemented =IPCR_ResearchImplemented_model(
               ResearchImplemented_Target = cd['ResearchImplemented_Target'],
               ResearchImplemented_Accomplished = cd ['ResearchImplemented_Accomplished'],
            )

            IPCR_researchimplemented.author = request.user
            IPCR_researchimplemented.ResearchImplemented_Submitted = date.today()
            IPCR_researchimplemented.save()

            messages.success(request, "The IPCR Form has been saved.")  

        if (form_researchpresented.is_valid()):
            cd = form_researchpresented.cleaned_data
            IPCR_researchpresented =IPCR_ResearchPresented_model(
               ResearchPresented_Target = cd['ResearchPresented_Target'],
               ResearchPresented_Accomplished = cd ['ResearchPresented_Accomplished'],
            )

            IPCR_researchpresented.author = request.user
            IPCR_researchpresented.ResearchPresented_Submitted = date.today()
            IPCR_researchpresented.save()

            messages.success(request, "The IPCR Form has been saved.") 

        if (form_researchpublished.is_valid()):
            cd = form_researchpublished.cleaned_data
            IPCR_researchpublished =IPCR_ResearchPublished_model(
               ResearchPublished_Target = cd['ResearchPublished_Target'],
               ResearchPublished_Accomplished = cd ['ResearchPublished_Accomplished'],
            )

            IPCR_researchpublished.author = request.user
            IPCR_researchpublished.ResearchPublished_Submitted = date.today()
            IPCR_researchpublished.save()

            messages.success(request, "The IPCR Form has been saved.")
            
        if (form_approvediprights.is_valid()):
            cd = form_approvediprights.cleaned_data
            IPCR_approvediprights =IPCR_ApprovedIPRights_model(
               ApprovedIPRights_Target = cd['ApprovedIPRights_Target'],
               ApprovedIPRights_Accomplished = cd ['ApprovedIPRights_Accomplished'],
            )

            IPCR_approvediprights.author = request.user
            IPCR_approvediprights.ApprovedIPRights_Submitted = date.today()
            IPCR_approvediprights.save()

            messages.success(request, "The IPCR Form has been saved.")  
            
        if (form_researchutilized.is_valid()):
            cd = form_researchutilized.cleaned_data
            IPCR_researchutilized =IPCR_ResearchUtilized_model(
               ResearchUtilized_Target = cd['ResearchUtilized_Target'],
               ResearchUtilized_Accomplished = cd ['ResearchUtilized_Accomplished'],
            )

            IPCR_researchutilized.author = request.user
            IPCR_researchutilized.ResearchUtilized_Submitted = date.today()
            IPCR_researchutilized.save()

            messages.success(request, "The IPCR Form has been saved.")

        if (form_numberofcitations.is_valid()):
            cd = form_numberofcitations.cleaned_data
            IPCR_numberofcitations =IPCR_NumberOfCitations_model(
               NumberOfCitations_Target = cd['NumberOfCitations_Target'],
               NumberOfCitations_Accomplished = cd ['NumberOfCitations_Accomplished'],
            )

            IPCR_numberofcitations.author = request.user
            IPCR_numberofcitations.NumberOfCitations_Submitted = date.today()
            IPCR_numberofcitations.save()

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

            if previous_response_classroomobservation:
                initial_data['ClassroomObservation_Target'] = previous_response_classroomobservation.ClassroomObservation_Target
                initial_data['ClassroomObservation_Accomplished'] = previous_response_classroomobservation.ClassroomObservation_Accomplished                                 

            if previous_response_midtermtosrubrics:
                initial_data['MidtermTOSRubrics_Target'] = previous_response_midtermtosrubrics.MidtermTOSRubrics_Target
                initial_data['MidtermTOSRubrics_Accomplished'] = previous_response_midtermtosrubrics.MidtermTOSRubrics_Accomplished                                 

            if previous_response_finaltermtosrubrics:
                initial_data['FinaltermTOSRubrics_Target'] = previous_response_finaltermtosrubrics.FinaltermTOSRubrics_Target
                initial_data['FinaltermTOSRubrics_Accomplished'] = previous_response_finaltermtosrubrics.FinaltermTOSRubrics_Accomplished                                 

            if previous_response_midtermtestquestions:
                initial_data['MidtermTestQuestions_Target'] = previous_response_midtermtestquestions.MidtermTestQuestions_Target
                initial_data['MidtermTestQuestions_Accomplished'] = previous_response_midtermtestquestions.MidtermTestQuestions_Accomplished                                 

            if previous_response_finaltermtestquestions:
                initial_data['FinaltermTestQuestions_Target'] = previous_response_finaltermtestquestions.FinaltermTestQuestions_Target
                initial_data['FinaltermTestQuestions_Accomplished'] = previous_response_finaltermtestquestions.FinaltermTestQuestions_Accomplished                                 

            if previous_response_midtermanswerkey:
                initial_data['MidtermAnswerKey_Target'] = previous_response_midtermanswerkey.MidtermAnswerKey_Target
                initial_data['MidtermAnswerKey_Accomplished'] = previous_response_midtermanswerkey.MidtermAnswerKey_Accomplished                                 

            if previous_response_finaltermanswerkey:
                initial_data['FinaltermAnswerKey_Target'] = previous_response_finaltermanswerkey.FinaltermAnswerKey_Target
                initial_data['FinaltermAnswerKey_Accomplished'] = previous_response_finaltermanswerkey.FinaltermAnswerKey_Accomplished                                 

            if previous_response_gradingsheet:
                initial_data['GradingSheet_Target'] = previous_response_gradingsheet.GradingSheet_Target
                initial_data['GradingSheet_Accomplished'] = previous_response_gradingsheet.GradingSheet_Accomplished                                 

            if previous_response_studentadviced:
                initial_data['StudentAdviced_Target'] = previous_response_studentadviced.StudentAdviced_Target
                initial_data['StudentAdviced_Accomplished'] = previous_response_studentadviced.StudentAdviced_Accomplished                                 

            if previous_response_accomplishmentreport:
                initial_data['AccomplishmentReport_Target'] = previous_response_accomplishmentreport.AccomplishmentReport_Target
                initial_data['AccomplishmentReport_Accomplished'] = previous_response_accomplishmentreport.AccomplishmentReport_Accomplished

            if previous_response_researchproposalsubmitted:
                initial_data['ResearchProposalSubmitted_Target'] = previous_response_researchproposalsubmitted.ResearchProposalSubmitted_Target
                initial_data['ResearchProposalSubmitted_Accomplished'] = previous_response_researchproposalsubmitted.ResearchProposalSubmitted_Accomplished

            if previous_response_researchimplemented:
                initial_data['ResearchImplemented_Target'] = previous_response_researchimplemented.ResearchImplemented_Target
                initial_data['ResearchImplemented_Accomplished'] = previous_response_researchimplemented.ResearchImplemented_Accomplished

            if previous_response_researchpresented:
                initial_data['ResearchPresented_Target'] = previous_response_researchpresented.ResearchPresented_Target
                initial_data['ResearchPresented_Accomplished'] = previous_response_researchpresented.ResearchPresented_Accomplished

            if previous_response_researchpublished:
                initial_data['ResearchPublished_Target'] = previous_response_researchpublished.ResearchPublished_Target
                initial_data['ResearchPublished_Accomplished'] = previous_response_researchpublished.ResearchPublished_Accomplished

            if previous_response_approvediprights:
                initial_data['ApprovedIPRights_Target'] = previous_response_approvediprights.ApprovedIPRights_Target
                initial_data['ApprovedIPRights_Accomplished'] = previous_response_approvediprights.ApprovedIPRights_Accomplished

            if previous_response_researchutilized:
                initial_data['ResearchUtilized_Target'] = previous_response_researchutilized.ResearchUtilized_Target
                initial_data['ResearchUtilized_Accomplished'] = previous_response_researchutilized.ResearchUtilized_Accomplished

            if previous_response_numberofcitations:
                initial_data['NumberOfCitations_Target'] = previous_response_numberofcitations.NumberOfCitations_Target
                initial_data['NumberOfCitations_Accomplished'] = previous_response_numberofcitations.NumberOfCitations_Accomplished



            form_syllabus = IPCR_Syllabus_form(initial=initial_data)
            form_courseguide = IPCR_CourseGuide_form(initial=initial_data)
            form_SLM = IPCR_SLM_form(initial=initial_data)
            form_subjectareas = IPCR_SubjectAreas_form(initial=initial_data)
            form_attendancesheet = IPCR_AttendanceSheet_form(initial=initial_data)
            form_classrecord = IPCR_ClassRecord_form(initial=initial_data)
            form_teachingeffectiveness = IPCR_TeachingEffectiveness_form(initial=initial_data)
            form_classroomobservation = IPCR_ClassroomObservation_form(initial=initial_data)
            form_midtermtosrubrics = IPCR_MidtermTOSRubrics_form(initial=initial_data)
            form_finaltermtosrubrics = IPCR_FinaltermTOSRubrics_form(initial=initial_data)
            form_midtermtestquestions = IPCR_MidtermTestQuestions_form(initial=initial_data)
            form_finaltermtestquestions = IPCR_FinaltermTestQuestions_form(initial=initial_data)
            form_midtermanswerkey = IPCR_MidtermAnswerKey_form(initial=initial_data)
            form_finaltermanswerkey = IPCR_FinaltermAnswerKey_form(initial=initial_data)
            form_gradingsheet = IPCR_GradingSheet_form(initial=initial_data)
            form_studentadviced = IPCR_StudentAdviced_form(initial=initial_data)
            form_accomplishmentreport = IPCR_AccomplishmentReport_form(initial=initial_data)
            form_researchproposalsubmitted = IPCR_ResearchProposalSubmitted_form(initial=initial_data)
            form_researchimplemented = IPCR_ResearchImplemented_form(initial=initial_data)
            form_researchpresented = IPCR_ResearchPresented_form(initial=initial_data)
            form_researchpublished = IPCR_ResearchPublished_form(initial=initial_data)
            form_approvediprights = IPCR_ApprovedIPRights_form(initial=initial_data)
            form_researchutilized = IPCR_ResearchUtilized_form(initial=initial_data)
            form_numberofcitations = IPCR_NumberOfCitations_form(initial=initial_data)
         


    
    return render (request, 'forms/IPCRForm.html', {'form_syllabus' : form_syllabus , 'form_courseguide' : form_courseguide,
                                                    'form_SLM' : form_SLM, 'form_subjectareas' : form_subjectareas, 'form_attendancesheet' : form_attendancesheet,
                                                    'form_classrecord' : form_classrecord, 'form_teachingeffectiveness' : form_teachingeffectiveness,
                                                    'form_classroomobservation' : form_classroomobservation, 'form_midtermtosrubrics' :form_midtermtosrubrics, 
                                                    'form_finaltermtosrubrics' :form_finaltermtosrubrics, 'form_midtermtestquestions' :form_midtermtestquestions,
                                                    'form_finaltermtestquestions' :form_finaltermtestquestions, 'form_midtermanswerkey' :form_midtermanswerkey,
                                                    'form_finaltermanswerkey' :form_finaltermanswerkey, 'form_gradingsheet' :form_gradingsheet,
                                                    'form_studentadviced' :form_studentadviced, 'form_accomplishmentreport' :form_accomplishmentreport,
                                                    'form_researchproposalsubmitted' :form_researchproposalsubmitted, 'form_researchimplemented' :form_researchimplemented,
                                                    'form_researchpresented' :form_researchpresented, 'form_researchpublished' :form_researchpublished,
                                                    'form_approvediprights' :form_approvediprights, 'form_researchutilized' :form_researchutilized,
                                                    'form_numberofcitations' :form_numberofcitations, })



def Show_IPCR(request):
    Current_user = request.user
    IPCR_Data = IPCR_Syllabus_model.objects.filter(author = Current_user)
    
    return render (request, 'forms/IPCRForm_View.html', {'IPCR_Data' : IPCR_Data})
    
    