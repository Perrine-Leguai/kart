# Generated by Django 2.2.6 on 2020-01-08 11:01

import common.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_studentapp-modelsv3-corrections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='artist',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='student', to='people.Artist'),
        ),
        migrations.AlterField(
            model_name='student',
            name='promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.Promotion'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='application_complete',
            field=models.BooleanField(default=False, help_text='Administration - Candidature is complete'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='application_completed',
            field=models.BooleanField(default=False, help_text="Candidature's validation"),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_application', to='people.Artist'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='artistic_referencies_project_1',
            field=models.FileField(blank=True, help_text="Artistic references for first first year's project", null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='artistic_referencies_project_2',
            field=models.FileField(blank=True, help_text="Artistic references for second first year's project", null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='binomial_application',
            field=models.BooleanField(default=False, help_text='Candidature with another artist'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='binomial_application_with',
            field=models.CharField(blank=True, help_text="Name of the binominal artist's candidate with", max_length=50),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='school.StudentApplicationSetup'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='considered_project_1',
            field=models.FileField(blank=True, help_text='Considered project first year', null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='considered_project_2',
            field=models.FileField(blank=True, help_text='Considered project second year', null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='curriculum_vitae',
            field=models.FileField(blank=True, help_text='BIO CV', null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='cursus_justifications',
            field=models.ForeignKey(blank=True, help_text='Gallery of justificaitons', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='student_application_cursus_justification', to='assets.Gallery'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='doctorate_interest',
            field=models.BooleanField(default=False, help_text='Interest in the doctorate'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='experience_justification',
            field=models.FileField(blank=True, help_text='If no master Degree, experience letter', null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='first_time',
            field=models.BooleanField(default=False, help_text="If the first time the Artist's applying"),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='free_document',
            field=models.FileField(blank=True, help_text='Free document', null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='identity_card',
            field=models.FileField(blank=True, help_text='Identity justificative', null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='interview_date',
            field=models.DateTimeField(blank=True, help_text='Administration - Date for interview', null=True),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='justification_letter',
            field=models.FileField(blank=True, help_text='Justification / Motivation', null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='master_degree',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No'), ('P', 'Pending')], help_text='Obtained a Master Degree', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='observation',
            field=models.TextField(blank=True, help_text='Administration - Comments on the application', null=True),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='presentation_video',
            field=models.URLField(blank=True, help_text='Url presentation video Link', null=True),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='presentation_video_details',
            field=models.TextField(blank=True, help_text='Details for the video', null=True),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='reference_letter',
            field=models.FileField(blank=True, help_text='Reference / Recommendation letter', null=True, upload_to=common.utils.make_filepath),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='remark',
            field=models.TextField(blank=True, help_text="Free expression'", null=True),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='remote_interview_info',
            field=models.CharField(blank=True, help_text='ID / Number / ... ', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='selected',
            field=models.BooleanField(default=False, help_text='Administration - Is the candidat selected'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='selected_for_interview',
            field=models.BooleanField(default=False, help_text='Administration - Is the candidat selected for the Interview'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='unselected',
            field=models.BooleanField(default=False, help_text='Administration - Is the candidat not choosen by the Jury'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='wait_listed',
            field=models.BooleanField(default=False, help_text='Administration - Is the candidat wait listed'),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='wait_listed_for_interview',
            field=models.BooleanField(default=False, help_text='Administration - Is the candidat wait listed for the Interview'),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='authentification_url',
            field=models.URLField(help_text='Front : Url authentification'),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='candidatures_url',
            field=models.URLField(help_text='Front : Url list of candidatures'),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='date_of_birth_max',
            field=models.DateField(blank=True, help_text='Maximum date of birth to apply', null=True),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='interviews_end_date',
            field=models.DateField(help_text='Front : interviews end date', null=True),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='interviews_publish_date',
            field=models.DateTimeField(help_text='Interviews web publish', null=True),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='interviews_start_date',
            field=models.DateField(help_text='Front : interviews start date', null=True),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='is_current_setup',
            field=models.BooleanField(default=True, help_text='This configuration is actived'),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.Promotion'),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='recover_password_url',
            field=models.URLField(help_text='Front : Url recover password'),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='reset_password_url',
            field=models.URLField(help_text='Front : Url reset password'),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='selected_publish_date',
            field=models.DateTimeField(help_text='Final selection web publish', null=True),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='video_service_name',
            field=models.CharField(blank=True, help_text='video service name', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='video_service_token',
            field=models.CharField(blank=True, help_text='Video service token', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='studentapplicationsetup',
            name='video_service_url',
            field=models.URLField(help_text='service URL'),
        ),
    ]