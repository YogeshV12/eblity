from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Resources, Topic_Table, Subtopic_Table, Journey_template, Plan_Table, Attendance_Table, Student_Table, UserProfileInfo, User

admin.site.register(Resources)
admin.site.register(Topic_Table)
admin.site.register(Subtopic_Table)
admin.site.register(Journey_template)
admin.site.register(Plan_Table)
admin.site.register(Attendance_Table)
admin.site.register(Student_Table)
admin.site.register(UserProfileInfo)
