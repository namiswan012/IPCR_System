# Generated by Django 4.1.7 on 2023-05-07 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0020_ipcr_syllabus_model_syllabus_deadline_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IPCR_AttendanceSA_model',
            new_name='IPCR_SpiritualActivityAttendance_model',
        ),
        migrations.RemoveField(
            model_name='ipcr_spiritualactivityattendance_model',
            name='AttendanceSA_Accomplished',
        ),
        migrations.RemoveField(
            model_name='ipcr_spiritualactivityattendance_model',
            name='AttendanceSA_Deadline',
        ),
        migrations.RemoveField(
            model_name='ipcr_spiritualactivityattendance_model',
            name='AttendanceSA_Submitted',
        ),
        migrations.RemoveField(
            model_name='ipcr_spiritualactivityattendance_model',
            name='AttendanceSA_Target',
        ),
        migrations.AddField(
            model_name='ipcr_spiritualactivityattendance_model',
            name='SpiritualActivityAttendance_Accomplished',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ipcr_spiritualactivityattendance_model',
            name='SpiritualActivityAttendance_Deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ipcr_spiritualactivityattendance_model',
            name='SpiritualActivityAttendance_Submitted',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ipcr_spiritualactivityattendance_model',
            name='SpiritualActivityAttendance_Target',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='IPCR_WellnessProgramAttendance_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WellnessProgramAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('WellnessProgramAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('WellnessProgramAttendance_Deadline', models.DateField(blank=True, null=True)),
                ('WellnessProgramAttendance_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_TrainingAttendance_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TrainingAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('TrainingAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TrainingAttendance_Deadline', models.DateField(blank=True, null=True)),
                ('TrainingAttendance_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_TechnicalAdvice_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TechnicalAdvice_Target', models.IntegerField(blank=True, null=True)),
                ('TechnicalAdvice_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TechnicalAdvice_Deadline', models.DateField(blank=True, null=True)),
                ('TechnicalAdvice_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_TeachingEffectiveness_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeachingEffectiveness_Target', models.IntegerField(blank=True, null=True)),
                ('TeachingEffectiveness_Accomplished', models.IntegerField(blank=True, null=True)),
                ('TeachingEffectiveness_Deadline', models.DateField(blank=True, null=True)),
                ('TeachingEffectiveness_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_SubjectAreas_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectAreas_Target', models.IntegerField(blank=True, null=True)),
                ('SubjectAreas_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SubjectAreas_Deadline', models.DateField(blank=True, null=True)),
                ('SubjectAreas_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_StudentAdviced_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentAdviced_Target', models.IntegerField(blank=True, null=True)),
                ('StudentAdviced_Accomplished', models.IntegerField(blank=True, null=True)),
                ('StudentAdviced_Deadline', models.DateField(blank=True, null=True)),
                ('StudentAdviced_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_SLM_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SLM_Target', models.IntegerField(blank=True, null=True)),
                ('SLM_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SLM_Deadline', models.DateField(blank=True, null=True)),
                ('SLM_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_SchoolCelebrationAttendance_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SchoolCelebrationAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('SchoolCelebrationAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('SchoolCelebrationAttendance_Deadline', models.DateField(blank=True, null=True)),
                ('SchoolCelebrationAttendance_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_ResearchUtilized_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResearchUtilized_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchUtilized_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchUtilized_Deadline', models.DateField(blank=True, null=True)),
                ('ResearchUtilized_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_ResearchPublished_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResearchPublished_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchPublished_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchPublished_Deadline', models.DateField(blank=True, null=True)),
                ('ResearchPublished_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_ResearchProposalSubmitted_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResearchProposalSubmitted_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchProposalSubmitted_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchProposalSubmitted_Deadline', models.DateField(blank=True, null=True)),
                ('ResearchProposalSubmitted_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_ResearchPresented_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResearchPresented_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchPresented_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchPresented_Deadline', models.DateField(blank=True, null=True)),
                ('ResearchPresented_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_ResearchImplemented_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResearchImplemented_Target', models.IntegerField(blank=True, null=True)),
                ('ResearchImplemented_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ResearchImplemented_Deadline', models.DateField(blank=True, null=True)),
                ('ResearchImplemented_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_PersonTrainedRatedGood_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonTrainedRatedGood_Target', models.IntegerField(blank=True, null=True)),
                ('PersonTrainedRatedGood_Accomplished', models.IntegerField(blank=True, null=True)),
                ('PersonTrainedRatedGood_Deadline', models.DateField(blank=True, null=True)),
                ('PersonTrainedRatedGood_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_PersonTrained_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonTrained_Target', models.IntegerField(blank=True, null=True)),
                ('PersonTrained_Accomplished', models.IntegerField(blank=True, null=True)),
                ('PersonTrained_Deadline', models.DateField(blank=True, null=True)),
                ('PersonTrained_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_PersonAvailedRatedGood_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonAvailedRatedGood_Target', models.IntegerField(blank=True, null=True)),
                ('PersonAvailedRatedGood_Accomplished', models.IntegerField(blank=True, null=True)),
                ('PersonAvailedRatedGood_Deadline', models.DateField(blank=True, null=True)),
                ('PersonAvailedRatedGood_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_NumberOfCitations_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumberOfCitations_Target', models.IntegerField(blank=True, null=True)),
                ('NumberOfCitations_Accomplished', models.IntegerField(blank=True, null=True)),
                ('NumberOfCitations_Deadline', models.DateField(blank=True, null=True)),
                ('NumberOfCitations_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_MidtermTOSRubrics_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MidtermTOSRubrics_Target', models.IntegerField(blank=True, null=True)),
                ('MidtermTOSRubrics_Accomplished', models.IntegerField(blank=True, null=True)),
                ('MidtermTOSRubrics_Deadline', models.DateField(blank=True, null=True)),
                ('MidtermTOSRubrics_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_MidtermTestQuestions_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MidtermTestQuestions_Target', models.IntegerField(blank=True, null=True)),
                ('MidtermTestQuestions_Accomplished', models.IntegerField(blank=True, null=True)),
                ('MidtermTestQuestions_Deadline', models.DateField(blank=True, null=True)),
                ('MidtermTestQuestions_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_MidtermAnswerKey_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MidtermAnswerKey_Target', models.IntegerField(blank=True, null=True)),
                ('MidtermAnswerKey_Accomplished', models.IntegerField(blank=True, null=True)),
                ('MidtermAnswerKey_Deadline', models.DateField(blank=True, null=True)),
                ('MidtermAnswerKey_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_GradingSheet_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GradingSheet_Target', models.IntegerField(blank=True, null=True)),
                ('GradingSheet_Accomplished', models.IntegerField(blank=True, null=True)),
                ('GradingSheet_Deadline', models.DateField(blank=True, null=True)),
                ('GradingSheet_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_FlagRaisingAttendance_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FlagRaisingAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('FlagRaisingAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FlagRaisingAttendance_Deadline', models.DateField(blank=True, null=True)),
                ('FlagRaisingAttendance_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_FlagLoweringAttendance_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FlagLoweringAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('FlagLoweringAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FlagLoweringAttendance_Deadline', models.DateField(blank=True, null=True)),
                ('FlagLoweringAttendance_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_FinaltermTOSRubrics_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FinaltermTOSRubrics_Target', models.IntegerField(blank=True, null=True)),
                ('FinaltermTOSRubrics_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FinaltermTOSRubrics_Deadline', models.DateField(blank=True, null=True)),
                ('FinaltermTOSRubrics_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_FinaltermTestQuestions_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FinaltermTestQuestions_Target', models.IntegerField(blank=True, null=True)),
                ('FinaltermTestQuestions_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FinaltermTestQuestions_Deadline', models.DateField(blank=True, null=True)),
                ('FinaltermTestQuestions_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_FinaltermAnswerKey_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FinaltermAnswerKey_Target', models.IntegerField(blank=True, null=True)),
                ('FinaltermAnswerKey_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FinaltermAnswerKey_Deadline', models.DateField(blank=True, null=True)),
                ('FinaltermAnswerKey_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_FacultyMeetingAttendance_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FacultyMeetingAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('FacultyMeetingAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('FacultyMeetingAttendance_Deadline', models.DateField(blank=True, null=True)),
                ('FacultyMeetingAttendance_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_ExtensionProposalSubmitted_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExtensionProposalSubmitted_Target', models.IntegerField(blank=True, null=True)),
                ('ExtensionProposalSubmitted_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ExtensionProposalSubmitted_Deadline', models.DateField(blank=True, null=True)),
                ('ExtensionProposalSubmitted_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_ClassroomObservation_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassroomObservation_Target', models.IntegerField(blank=True, null=True)),
                ('ClassroomObservation_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ClassroomObservation_Deadline', models.DateField(blank=True, null=True)),
                ('ClassroomObservation_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_ClassRecord_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassRecord_Target', models.IntegerField(blank=True, null=True)),
                ('ClassRecord_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ClassRecord_Deadline', models.DateField(blank=True, null=True)),
                ('ClassRecord_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_AttendanceSheet_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AttendanceSheet_Target', models.IntegerField(blank=True, null=True)),
                ('AttendanceSheet_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AttendanceSheet_Deadline', models.DateField(blank=True, null=True)),
                ('AttendanceSheet_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_ApprovedIPRights_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApprovedIPRights_Target', models.IntegerField(blank=True, null=True)),
                ('ApprovedIPRights_Accomplished', models.IntegerField(blank=True, null=True)),
                ('ApprovedIPRights_Deadline', models.DateField(blank=True, null=True)),
                ('ApprovedIPRights_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_AccreditationAttendance_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccreditationAttendance_Target', models.IntegerField(blank=True, null=True)),
                ('AccreditationAttendance_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AccreditationAttendance_Deadline', models.DateField(blank=True, null=True)),
                ('AccreditationAttendance_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_AccomplishmentReportDeligatedAssignment_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccomplishmentReportDeligatedAssignment_Target', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReportDeligatedAssignment_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReportDeligatedAssignment_Deadline', models.DateField(blank=True, null=True)),
                ('AccomplishmentReportDeligatedAssignment_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPCR_AccomplishmentReport_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccomplishmentReport_Target', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReport_Accomplished', models.IntegerField(blank=True, null=True)),
                ('AccomplishmentReport_Deadline', models.DateField(blank=True, null=True)),
                ('AccomplishmentReport_Submitted', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
