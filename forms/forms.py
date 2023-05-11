from django import forms
from .models import IPCR_Syllabus_model

#1
class IPCR_Syllabus_form(forms.Form):
    syllabus_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    syllabus_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_CourseGuide_form(forms.Form):
    CourseGuide_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    CourseGuide_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_SLM_form(forms.Form):
    SLM_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    SLM_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_SubjectAreas_form(forms.Form):
    SubjectAreas_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    SubjectAreas_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

#2
class IPCR_AttendanceSheet_form(forms.Form):
    AttendanceSheet_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    AttendanceSheet_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_ClassRecord_form(forms.Form):
    ClassRecord_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    ClassRecord_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)    

#3
class IPCR_TeachingEffectiveness_form(forms.Form):
    TeachingEffectiveness_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    TeachingEffectiveness_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)    

class IPCR_ClassroomObservation_form(forms.Form):
    ClassroomObservation_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    ClassroomObservation_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)    

#4
class IPCR_MidtermTOSRubrics_form(forms.Form):
    MidtermTOSRubrics_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    MidtermTOSRubrics_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)    

class IPCR_FinaltermTOSRubrics_form(forms.Form):
    FinaltermTOSRubrics_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    FinaltermTOSRubrics_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)    

class IPCR_MidtermTestQuestions_form(forms.Form):
    MidtermTestQuestions_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    MidtermTestQuestions_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)    

class IPCR_FinaltermTestQuestions_form(forms.Form):
    FinaltermTestQuestions_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    FinaltermTestQuestions_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False) 

class IPCR_MidtermAnswerKey_form(forms.Form):
    MidtermAnswerKey_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    MidtermAnswerKey_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False) 

class IPCR_FinaltermAnswerKey_form(forms.Form):
    FinaltermAnswerKey_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    FinaltermAnswerKey_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)      
    
#5
class IPCR_GradingSheet_form(forms.Form):
    GradingSheet_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    GradingSheet_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)      

#6   
class IPCR_StudentAdvised_form(forms.Form):
    StudentAdvised_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    StudentAdvised_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)      

#7
class IPCR_AccomplishmentReport_form(forms.Form):
    AccomplishmentReport_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    AccomplishmentReport_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)      

#8
class IPCR_ResearchProposalSubmitted_form(forms.Form):
    ResearchProposalSubmitted_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    ResearchProposalSubmitted_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)      

class IPCR_ResearchImplemented_form(forms.Form):
    ResearchImplemented_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    ResearchImplemented_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)      

class IPCR_ResearchPresented_form(forms.Form):
    ResearchPresented_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    ResearchPresented_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_ResearchPublished_form(forms.Form):
    ResearchPublished_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    ResearchPublished_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_ApprovedIPRights_form(forms.Form):
    ApprovedIPRights_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    ApprovedIPRights_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_ResearchUtilized_form(forms.Form):
    ResearchUtilized_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    ResearchUtilized_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_NumberOfCitations_form(forms.Form):
    NumberOfCitations_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    NumberOfCitations_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

#9
class IPCR_ExtensionProposalSubmitted_form(forms.Form):
    ExtensionProposalSubmitted_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    ExtensionProposalSubmitted_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_PersonTrained_form(forms.Form):
    PersonTrained_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    PersonTrained_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_PersonAvailedRatedGood_form(forms.Form):
    PersonAvailedRatedGood_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    PersonAvailedRatedGood_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_PersonTrainedRatedGood_form(forms.Form):
    PersonTrainedRatedGood_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    PersonTrainedRatedGood_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

class IPCR_TechnicalAdvice_form(forms.Form):
    TechnicalAdvice_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    TechnicalAdvice_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

#10
class IPCR_AccomplishmentReportDeligatedAssignment_form(forms.Form):
    AccomplishmentReportDeligatedAssignment_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    AccomplishmentReportDeligatedAssignment_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

#11
class IPCR_FlagRaisingAttendance_form(forms.Form):
    FlagRaisingAttendance_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    FlagRaisingAttendance_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

#12
class IPCR_FlagLoweringAttendance_form(forms.Form):
    FlagLoweringAttendance_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    FlagLoweringAttendance_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)

#13
class IPCR_WellnessProgramAttendance_form(forms.Form):
    WellnessProgramAttendance_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    WellnessProgramAttendance_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)  
    
#14
class IPCR_SchoolCelebrationAttendance_form(forms.Form):
    SchoolCelebrationAttendance_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    SchoolCelebrationAttendance_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)     

#15
class IPCR_TrainingAttendance_form(forms.Form):
    TrainingAttendance_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    TrainingAttendance_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)  

#16
class IPCR_FacultyMeetingAttendance_form(forms.Form):
    FacultyMeetingAttendance_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    FacultyMeetingAttendance_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)  

#17
class IPCR_AccreditationAttendance_form(forms.Form):
    AccreditationAttendance_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    AccreditationAttendance_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)  

#18
class IPCR_SpiritualActivityAttendance_form(forms.Form):
    SpiritualActivityAttendance_Target = forms.IntegerField(label = 'Target', min_value = 0, max_value = 100, widget=forms.NumberInput, required= False)
    SpiritualActivityAttendance_Accomplished = forms.IntegerField(label = 'Accomplished', min_value = 0, max_value = 100, widget=forms.NumberInput, required = False)  


   
    
    