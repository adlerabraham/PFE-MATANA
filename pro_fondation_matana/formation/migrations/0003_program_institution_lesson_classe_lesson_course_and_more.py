# Generated by Django 4.1.3 on 2022-12-21 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_institution_delete_ecole'),
        ('formation', '0002_classroom_course_lesson_level_period_program_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='Institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institution', to='school.institution'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.classroom'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.course'),
        ),
        migrations.AddField(
            model_name='course',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.classroom'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.subject'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='program_period_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.program_period_level'),
        ),
    ]