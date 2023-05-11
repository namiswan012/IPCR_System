from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#1
class IPCR_Syllabus_model (models.Model):
    syllabus_Target = models.IntegerField(null = True, blank = True)
    syllabus_Accomplished = models.IntegerField(null = True, blank = True)
    syllabus_Deadline = models.DateField(null = True, blank = True)
    syllabus_Submitted = models.DateField(null = True, blank = True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_CourseGuide_model(models.Model):
    CourseGuide_Target = models.IntegerField(null = True, blank = True)
    CourseGuide_Accomplished = models.IntegerField(null = True, blank = True)
    CourseGuide_Deadline = models.DateField(null = True, blank = True)
    CourseGuide_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_SLM_model(models.Model):
    SLM_Target = models.IntegerField(null = True, blank = True)
    SLM_Accomplished = models.IntegerField(null = True, blank = True)
    SLM_Deadline = models.DateField(null = True, blank = True)
    SLM_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_SubjectAreas_model(models.Model):
    SubjectAreas_Target = models.IntegerField(null = True, blank = True)
    SubjectAreas_Accomplished = models.IntegerField(null = True, blank = True)
    SubjectAreas_Deadline = models.DateField(null = True, blank = True)
    SubjectAreas_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#2
class IPCR_AttendanceSheet_model(models.Model):
    AttendanceSheet_Target = models.IntegerField(null = True, blank = True)
    AttendanceSheet_Accomplished = models.IntegerField(null = True, blank = True)
    AttendanceSheet_Deadline = models.DateField(null = True, blank = True)
    AttendanceSheet_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class IPCR_ClassRecord_model(models.Model):
    ClassRecord_Target = models.IntegerField(null = True, blank = True)
    ClassRecord_Accomplished = models.IntegerField(null = True, blank = True)
    ClassRecord_Deadline = models.DateField(null = True, blank = True)
    ClassRecord_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#3
class IPCR_TeachingEffectiveness_model(models.Model):
    TeachingEffectiveness_Target = models.IntegerField(null = True, blank = True)
    TeachingEffectiveness_Accomplished = models.IntegerField(null = True, blank = True)
    TeachingEffectiveness_Deadline = models.DateField(null = True, blank = True)
    TeachingEffectiveness_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_ClassroomObservation_model(models.Model):
    ClassroomObservation_Target = models.IntegerField(null = True, blank = True)
    ClassroomObservation_Accomplished = models.IntegerField(null = True, blank = True)
    ClassroomObservation_Deadline = models.DateField(null = True, blank = True)
    ClassroomObservation_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#4
class IPCR_MidtermTOSRubrics_model(models.Model):
    MidtermTOSRubrics_Target = models.IntegerField(null = True, blank = True)
    MidtermTOSRubrics_Accomplished = models.IntegerField(null = True, blank = True)
    MidtermTOSRubrics_Deadline = models.DateField(null = True, blank = True)
    MidtermTOSRubrics_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_FinaltermTOSRubrics_model(models.Model):
    FinaltermTOSRubrics_Target = models.IntegerField(null = True, blank = True)
    FinaltermTOSRubrics_Accomplished = models.IntegerField(null = True, blank = True)
    FinaltermTOSRubrics_Deadline = models.DateField(null = True, blank = True)
    FinaltermTOSRubrics_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_MidtermTestQuestions_model(models.Model):
    MidtermTestQuestions_Target = models.IntegerField(null = True, blank = True)
    MidtermTestQuestions_Accomplished = models.IntegerField(null = True, blank = True)
    MidtermTestQuestions_Deadline = models.DateField(null = True, blank = True)
    MidtermTestQuestions_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)   

class IPCR_FinaltermTestQuestions_model(models.Model):
    FinaltermTestQuestions_Target = models.IntegerField(null = True, blank = True)
    FinaltermTestQuestions_Accomplished = models.IntegerField(null = True, blank = True)
    FinaltermTestQuestions_Deadline = models.DateField(null = True, blank = True)
    FinaltermTestQuestions_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_MidtermAnswerKey_model(models.Model):
    MidtermAnswerKey_Target = models.IntegerField(null = True, blank = True)
    MidtermAnswerKey_Accomplished = models.IntegerField(null = True, blank = True)
    MidtermAnswerKey_Deadline = models.DateField(null = True, blank = True)
    MidtermAnswerKey_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)  

class IPCR_FinaltermAnswerKey_model(models.Model):
    FinaltermAnswerKey_Target = models.IntegerField(null = True, blank = True)
    FinaltermAnswerKey_Accomplished = models.IntegerField(null = True, blank = True)
    FinaltermAnswerKey_Deadline = models.DateField(null = True, blank = True)
    FinaltermAnswerKey_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#5
class IPCR_GradingSheet_model(models.Model):
    GradingSheet_Target = models.IntegerField(null = True, blank = True)
    GradingSheet_Accomplished = models.IntegerField(null = True, blank = True)
    GradingSheet_Deadline = models.DateField(null = True, blank = True)
    GradingSheet_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#6
class IPCR_StudentAdviced_model(models.Model):
    StudentAdviced_Target = models.IntegerField(null = True, blank = True)
    StudentAdviced_Accomplished = models.IntegerField(null = True, blank = True)
    StudentAdviced_Deadline = models.DateField(null = True, blank = True)
    StudentAdviced_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#7
class IPCR_AccomplishmentReport_model(models.Model):
    AccomplishmentReport_Target = models.IntegerField(null = True, blank = True)
    AccomplishmentReport_Accomplished = models.IntegerField(null = True, blank = True)
    AccomplishmentReport_Deadline = models.DateField(null = True, blank = True)
    AccomplishmentReport_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#8
class IPCR_ResearchProposalSubmitted_model(models.Model):
    ResearchProposalSubmitted_Target = models.IntegerField(null = True, blank = True)
    ResearchProposalSubmitted_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchProposalSubmitted_Deadline = models.DateField(null = True, blank = True)
    ResearchProposalSubmitted_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_ResearchImplemented_model(models.Model):
    ResearchImplemented_Target = models.IntegerField(null = True, blank = True)
    ResearchImplemented_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchImplemented_Deadline = models.DateField(null = True, blank = True)
    ResearchImplemented_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class IPCR_ResearchPresented_model(models.Model):
    ResearchPresented_Target = models.IntegerField(null = True, blank = True)
    ResearchPresented_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchPresented_Deadline = models.DateField(null = True, blank = True)
    ResearchPresented_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class IPCR_ResearchPublished_model(models.Model):
    ResearchPublished_Target = models.IntegerField(null = True, blank = True)
    ResearchPublished_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchPublished_Deadline = models.DateField(null = True, blank = True)
    ResearchPublished_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class IPCR_ApprovedIPRights_model(models.Model):
    ApprovedIPRights_Target = models.IntegerField(null = True, blank = True)
    ApprovedIPRights_Accomplished = models.IntegerField(null = True, blank = True)
    ApprovedIPRights_Deadline = models.DateField(null = True, blank = True)
    ApprovedIPRights_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_ResearchUtilized_model(models.Model):
    ResearchUtilized_Target = models.IntegerField(null = True, blank = True)
    ResearchUtilized_Accomplished = models.IntegerField(null = True, blank = True)
    ResearchUtilized_Deadline = models.DateField(null = True, blank = True)
    ResearchUtilized_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE) 
 
class IPCR_NumberOfCitations_model(models.Model):
    NumberOfCitations_Target = models.IntegerField(null = True, blank = True)
    NumberOfCitations_Accomplished = models.IntegerField(null = True, blank = True)
    NumberOfCitations_Deadline = models.DateField(null = True, blank = True)
    NumberOfCitations_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE) 

#9
class IPCR_ExtensionProposalSubmitted_model(models.Model):
    ExtensionProposalSubmitted_Target = models.IntegerField(null = True, blank = True)
    ExtensionProposalSubmitted_Accomplished = models.IntegerField(null = True, blank = True)
    ExtensionProposalSubmitted_Deadline = models.DateField(null = True, blank = True)
    ExtensionProposalSubmitted_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE) 

class IPCR_PersonTrained_model(models.Model):
    PersonTrained_Target = models.IntegerField(null = True, blank = True)
    PersonTrained_Accomplished = models.IntegerField(null = True, blank = True)
    PersonTrained_Deadline = models.DateField(null = True, blank = True)
    PersonTrained_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_PersonAvailedRatedGood_model(models.Model):
    PersonAvailedRatedGood_Target = models.IntegerField(null = True, blank = True)
    PersonAvailedRatedGood_Accomplished = models.IntegerField(null = True, blank = True)
    PersonAvailedRatedGood_Deadline = models.DateField(null = True, blank = True)
    PersonAvailedRatedGood_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class IPCR_PersonTrainedRatedGood_model(models.Model):
    PersonTrainedRatedGood_Target = models.IntegerField(null = True, blank = True)
    PersonTrainedRatedGood_Accomplished = models.IntegerField(null = True, blank = True)
    PersonTrainedRatedGood_Deadline = models.DateField(null = True, blank = True)
    PersonTrainedRatedGood_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

class IPCR_TechnicalAdvice_model(models.Model):
    TechnicalAdvice_Target = models.IntegerField(null = True, blank = True)
    TechnicalAdvice_Accomplished = models.IntegerField(null = True, blank = True)
    TechnicalAdvice_Deadline = models.DateField(null = True, blank = True)
    TechnicalAdvice_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#10
class IPCR_AccomplishmentReportDeligatedAssignment_model(models.Model):
    AccomplishmentReportDeligatedAssignment_Target = models.IntegerField(null = True, blank = True)
    AccomplishmentReportDeligatedAssignment_Accomplished = models.IntegerField(null = True, blank = True)
    AccomplishmentReportDeligatedAssignment_Deadline = models.DateField(null = True, blank = True)
    AccomplishmentReportDeligatedAssignment_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#11
class IPCR_FlagRaisingAttendance_model(models.Model):
    FlagRaisingAttendance_Target = models.IntegerField(null = True, blank = True)
    FlagRaisingAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    FlagRaisingAttendance_Deadline = models.DateField(null = True, blank = True)
    FlagRaisingAttendance_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#12
class IPCR_FlagLoweringAttendance_model(models.Model):
    FlagLoweringAttendance_Target = models.IntegerField(null = True, blank = True)
    FlagLoweringAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    FlagLoweringAttendance_Deadline = models.DateField(null = True, blank = True)
    FlagLoweringAttendance_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#13
class IPCR_WellnessProgramAttendance_model(models.Model):
    WellnessProgramAttendance_Target = models.IntegerField(null = True, blank = True)
    WellnessProgramAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    WellnessProgramAttendance_Deadline = models.DateField(null = True, blank = True)
    WellnessProgramAttendance_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#14
class IPCR_SchoolCelebrationAttendance_model(models.Model):
    SchoolCelebrationAttendance_Target = models.IntegerField(null = True, blank = True)
    SchoolCelebrationAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    SchoolCelebrationAttendance_Deadline = models.DateField(null = True, blank = True)
    SchoolCelebrationAttendance_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#15
class IPCR_TrainingAttendance_model(models.Model):
    TrainingAttendance_Target = models.IntegerField(null = True, blank = True)
    TrainingAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    TrainingAttendance_Deadline = models.DateField(null = True, blank = True)
    TrainingAttendance_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#16
class IPCR_FacultyMeetingAttendance_model(models.Model):
    FacultyMeetingAttendance_Target = models.IntegerField(null = True, blank = True)
    FacultyMeetingAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    FacultyMeetingAttendance_Deadline = models.DateField(null = True, blank = True)
    FacultyMeetingAttendance_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#17
class IPCR_AccreditationAttendance_model(models.Model):
    AccreditationAttendance_Target = models.IntegerField(null = True, blank = True)
    AccreditationAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    AccreditationAttendance_Deadline = models.DateField(null = True, blank = True)
    AccreditationAttendance_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

#18
class IPCR_SpiritualActivityAttendance_model(models.Model):
    SpiritualActivityAttendance_Target = models.IntegerField(null = True, blank = True)
    SpiritualActivityAttendance_Accomplished = models.IntegerField(null = True, blank = True)
    SpiritualActivityAttendance_Deadline = models.DateField(null = True, blank = True)
    SpiritualActivityAttendance_Submitted = models.DateField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)



