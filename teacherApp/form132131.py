from django import forms
from django.forms import CheckboxSelectMultiple, DateInput

from teacherApp.models import *


class lectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ('lectureid','lecturename','courseid','tutoriallink','schoolid','uploaddate','lecturenotes','recordedlecture','lecturedescription')

class assigmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('assignmentid', 'assignmentname', 'classid', 'courseid','assignment','duedate','schoolid','createddate','teacherid')

class calenderForm(forms.ModelForm):
    class Meta:
        model = Calender
        fields = ('event_id', 'event_name', 'event_details', 'due_date','course_id','class_id')
        
class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
)
class AttendanceForm(forms.ModelForm):
    # mark_attendance = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=class_attendance)
    class Meta:
        model = Attendance
        fields = ('mark_attendance',)
        widgets = {
            'mark_attendance': CheckboxSelectMultiple(attrs={'choices'  : class_attendance}),
        }

class createquizForm(forms.ModelForm):
    class Meta:
        model = createQuiz
        fields = ('quizid', 'quizname', 'quizdate', 'courseid','classid')
        widgets = {
            'quizdate': forms.DateInput(),
        }

class questionForm(forms.ModelForm):
    class Meta:
        model = quizQuestionsAndAnswers
        fields = ( '__all__' )
        
        