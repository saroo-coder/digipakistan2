from django.contrib import admin
from django.template.defaultfilters import register
from .models import *


admin.site.register(BlogModel)
admin.site.register(AnnouncementModel)
admin.site.register(EventModel)
admin.site.register(ArticleModel)
admin.site.register(KidStoryModel)
admin.site.register(KidTalentModel)
admin.site.register(Enroll_CourseModel)
admin.site.register(ClientCourseModel)
admin.site.register(QuestionModel)
admin.site.register(Client_testModel)
admin.site.register(Client_SubmittestModel)
admin.site.register(Client_SubmitquestionModel)
