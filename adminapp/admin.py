from django.contrib import admin
from adminapp.models import *
# Register your models here.

admin.site.register(SchoolModel)
admin.site.register(TblClassModel)
admin.site.register(CourseModel)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(Assign_TeacherModel)
admin.site.register(Enroll_StudentModel)
admin.site.register(ContactFormModel)
admin.site.register(ParentModel)
admin.site.register(Enroll_ParentModel)
