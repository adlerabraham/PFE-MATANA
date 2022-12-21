# Generated by Django 4.1.3 on 2022-12-21 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('abbreviation', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'classroom',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('coefficient', models.PositiveSmallIntegerField()),
                ('logo', models.ImageField(blank=True, upload_to='course')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('chapter', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'lesson',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('level', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'level',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('start_date', models.DateField(max_length=25, null=True)),
                ('end_date', models.DateField(max_length=25, null=True)),
                ('coefficient', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'period',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, upload_to='program')),
                ('description', models.TextField(max_length=100)),
                ('responsible', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'program',
            },
        ),
        migrations.CreateModel(
            name='Program_period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('duration', models.PositiveSmallIntegerField()),
                ('unit_duration', models.CharField(choices=[('month', 'Mois'), ('year', 'Annee')], max_length=25, null=True)),
                ('number_student', models.IntegerField()),
                ('number_teacher', models.IntegerField()),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.period')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.program')),
            ],
            options={
                'db_table': 'program_period',
            },
        ),
        migrations.CreateModel(
            name='Program_period_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.level')),
                ('program_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.program_period')),
            ],
            options={
                'db_table': 'program_period_level',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Subject_program_period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_deleted_at', models.DateTimeField(null=True)),
                ('is_deleted_by', models.CharField(max_length=255, null=True)),
                ('Programme_periode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.program_period')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.subject')),
            ],
            options={
                'db_table': 'subject_program_period',
            },
        ),
        migrations.RemoveField(
            model_name='cours',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='cours',
            name='matiere',
        ),
        migrations.RemoveField(
            model_name='lecon',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='lecon',
            name='cours',
        ),
        migrations.RemoveField(
            model_name='matiere_programme_periode',
            name='Programme_periode',
        ),
        migrations.RemoveField(
            model_name='matiere_programme_periode',
            name='matiere',
        ),
        migrations.RemoveField(
            model_name='programme',
            name='ecole',
        ),
        migrations.RemoveField(
            model_name='programme_periode',
            name='periode',
        ),
        migrations.RemoveField(
            model_name='programme_periode',
            name='programme',
        ),
        migrations.RemoveField(
            model_name='programme_periode_niveau',
            name='niveau',
        ),
        migrations.RemoveField(
            model_name='programme_periode_niveau',
            name='programme_periode',
        ),
        migrations.DeleteModel(
            name='Classe',
        ),
        migrations.DeleteModel(
            name='Cours',
        ),
        migrations.DeleteModel(
            name='Lecon',
        ),
        migrations.DeleteModel(
            name='Matiere',
        ),
        migrations.DeleteModel(
            name='Matiere_programme_periode',
        ),
        migrations.DeleteModel(
            name='Niveau',
        ),
        migrations.DeleteModel(
            name='Periode',
        ),
        migrations.DeleteModel(
            name='Programme',
        ),
        migrations.DeleteModel(
            name='Programme_periode',
        ),
        migrations.DeleteModel(
            name='Programme_periode_niveau',
        ),
    ]