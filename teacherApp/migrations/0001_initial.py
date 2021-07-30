# Generated by Django 3.1.6 on 2021-05-18 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('assignment', models.FileField(upload_to='media')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('due_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classname', to='adminapp.tblclassmodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursename', to='adminapp.coursemodel')),
                ('teacher', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='teachername', to='adminapp.teachermodel')),
            ],
        ),
        migrations.CreateModel(
            name='createQuizModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblclassmodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
            ],
        ),
        migrations.CreateModel(
            name='quizQuestionsAndAnswersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=0, max_length=20)),
                ('question', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=20)),
                ('option2', models.CharField(max_length=20)),
                ('option3', models.CharField(max_length=20)),
                ('option4', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherApp.createquizmodel')),
            ],
        ),
        migrations.CreateModel(
            name='RoleNameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('test', models.FileField(default='no test yet', upload_to='media')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('due_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblclassmodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
            ],
        ),
        migrations.CreateModel(
            name='SubmittestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_file', models.FileField(default='no file', upload_to='media')),
                ('is_submit', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.schoolmodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentmodel')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitTest', to='teacherApp.testmodel')),
            ],
        ),
        migrations.CreateModel(
            name='SubmitquestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_file', models.FileField(default='no file', upload_to='media')),
                ('is_submit', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizQuestionsAndAnswers', to='teacherApp.quizquestionsandanswersmodel')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.schoolmodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='SubmitAssignmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_file', models.FileField(default='no file', upload_to='media')),
                ('is_submit', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitAssignment', to='teacherApp.assignmentmodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFeedBackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('rating', models.CharField(choices=[('Good', 'Good'), ('Average', 'Average'), ('Bad', 'Bad')], default='none', max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblclassmodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ResultModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.CharField(max_length=10)),
                ('obtained_marks', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblclassmodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='NotesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('due_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='adminapp.teachermodel')),
            ],
        ),
        migrations.CreateModel(
            name='LectureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('tutorial_link', models.CharField(max_length=100)),
                ('notes', models.FileField(upload_to='media')),
                ('recorded_lecture', models.FileField(upload_to='media')),
                ('description', models.TextField(max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblclassmodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.teachermodel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DiscussionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblclassmodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='teacherApp.discussionmodel')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentmodel')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.teachermodel')),
            ],
        ),
        migrations.CreateModel(
            name='CalenderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.CharField(default='NULL', max_length=200)),
                ('due_date', models.DateField()),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblclassmodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncementModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
                ('short_description', models.CharField(max_length=700)),
                ('long_description', models.CharField(max_length=1400)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='adminapp.teachermodel')),
            ],
        ),
    ]