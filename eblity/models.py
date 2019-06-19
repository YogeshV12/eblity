from django.db import models
from django.contrib.auth.models import User

import pandas as pd


import pandas as pd

from datetime import date

from django.utils import timezone


# import os
# Create your models here.
class Resources(models.Model):
    resource_id = models.IntegerField(primary_key=True)
    topic_id = models.ForeignKey('Topic_Table', on_delete=models.CASCADE)
    # topic_id = models.IntegerField()
    subtopic_id = models.IntegerField()
    resource_type = models.CharField(max_length=30, blank=True)
    resource_link = models.URLField(blank=True)
    tags = models.CharField(max_length=30, blank=True)


class Topic_Table(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    topic_name = models.CharField(max_length=100, blank=True)
    weightage = models.CharField(max_length=15, blank=True)
    grade = models.IntegerField(null=True)
    subject = models.CharField(max_length=100, blank=True)
    sequence = models.IntegerField(null=True)
    month = models.CharField(max_length=15, blank=True)
    hours = models.IntegerField(null=True)
    min_hours = models.IntegerField(null=True)
    mean_hours = models.FloatField(null=True)
    max_hours = models.IntegerField(null=True)
    pre_mid_term = models.CharField(max_length=15, blank=True)
    mid_term = models.CharField(max_length=15, blank=True)
    pre_final_term = models.CharField(max_length=15, blank=True)
    final_term = models.CharField(max_length=15, blank=True)


class Subtopic_Table(models.Model):
    # topic_id = models.ForeignKey('Topic_Table',on_delete=models.CASCADE)
    topic_id = models.ForeignKey('Topic_Table', on_delete=models.CASCADE)
    subtopic_id = models.IntegerField()
    subtopic_name = models.CharField(max_length=25, blank=True)
    sequence = models.IntegerField(null=True)
    min_hours = models.IntegerField(null=True)
    mean_hours = models.FloatField(null=True)
    max_hours = models.IntegerField(null=True)


class Journey_template(models.Model):
    student_id = models.IntegerField(default=1)
    # subtopic_id = models.ForeignKey('Subtopic',to_field='subtopic_id',on_delete=models.CASCADE)
    topic_id = models.ForeignKey('Topic_Table', on_delete=models.CASCADE)
    subtopic_id = models.IntegerField()
    journey_template_key = models.IntegerField(primary_key=True)
    resource_id = models.ForeignKey('Resources', on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default='pending')
    rating = models.IntegerField(blank=True, null=True)
    time_spent = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    feedback = models.CharField(max_length=1000, blank=True, null=True)


class Plan_Table(models.Model):
    topic_id = models.ForeignKey('Topic_Table', on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100, blank=True)
    weightage = models.CharField(max_length=15, blank=True)
    sequence = models.IntegerField(null=True)
    month = models.CharField(max_length=15)
    hours = models.IntegerField(null=True)
    subject = models.CharField(max_length=20, blank=True)

# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     portfolio_site = models.URLField(blank=True)
#     profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
#     def __str__(self):
#         return self.user.username

# class Student_Table(models.Model):
#     student_id = models.IntegerField(default=1)
#     student_name = models.CharField(max_length=30, blank=False)
#     grade = models.IntegerField(blank=False)
#     parent_id = models.IntegerField(blank=True)
#     parent_email = models.CharField(max_length=20, blank=True)
#     status = models.CharField()


# df =  pd.read_csv('Student_table')
# for student_id, student_name, grade, parent_id, parent_email, status in zip(df['student_id'], df['student_name'], df['grade'], df['parent_id'], df['parent_email'], df['status'],):
#     Student_Table(student_id=int(student_id), student_name=str(student_name), grade=int(grade), parent_id=int(parent_id), parent_email=str(parent_email), status=str(status)).save()


class Attendance_Table(models.Model):
    student_id = models.IntegerField(default=1)
    date = models.DateField(default=date.today)    
    check_in = models.DateTimeField(default=timezone.now)
    check_out = models.DateTimeField(default=timezone.now)
    tutor_time = models.DateTimeField(default=timezone.now)
    intention = models.CharField(max_length=100);
    absent_present = models.CharField(max_length=15)
    reasonOfAbsence = models.CharField(max_length=100)

# df = pd.read_csv('Plan_Table.csv')
# for topic_id, topic_name, weightage, sequence, month, hours, subject in zip(df['topic_id'], df['topic_name'], df['weightage'], df['sequence'], df['month'], df['hours'], df['subject']):
#     Id = Topic_Table.objects.get(topic_id=topic_id)
#     Plan_Table(topic_id=Id, topic_name=str(topic_name), weightage=str(weightage), sequence=int(sequence), month=str(month), hours=int(hours), subject=str(subject)).save()

# from django.db.models import Topic_Table
# Data insertion
# df = pd.read_csv('Table.csv')
# for resource_id, topic_id, subtopic_id, resource_type, resource_link, tags in zip(df['resource_id'], df['topic_id'], df['subtopic_id'],
# 	df['resource_type'], df['resource_link'], df['tags']) :
# 	# print("Printing")
# 	Id = Topic_Table.objects.get(topic_id=topic_id)
# 	Resources(resource_id=int(resource_id), topic_id=Id, subtopic_id=int(subtopic_id), resource_type=str(resource_type),
# 		resource_link=str(resource_link), tags=str(tags)).save()
#     df['resource_type'], df['resource_link'], df['tags']) :
#     # print("Printing")
#     Id = Topic_Table.objects.get(topic_id=topic_id)
#     if str(resource_link) != 'nan':
#         Resources(resource_id=int(resource_id), topic_id=Id, subtopic_id=int(subtopic_id), resource_type=str(resource_type),
#         resource_link=str(resource_link), tags=str(tags)).save()

# df = pd.read_csv('Topic_Table.csv')
# df['mean_hours'].fillna(float(0), inplace=True)
# df['min_hours'].fillna(float(0), inplace=True)
# df['max_hours'].fillna(float(0), inplace=True)
# for topic_id, topic_name, weightage, grade, subject, sequence, month, hours, min_hours, mean_hours, max_hours, pre_mid_term, mid_term, pre_final_term, final_term in zip(df['topic_id'], df['topic_name'], df['weightage'], df['grade'],
# 	df['subject'], df['sequence'], df['month'], df['hours'], df['min_hours'], df['mean_hours'], df['max_hours'],
# 	df['pre_mid_term'], df['mid_term'], df['pre_final_term'], df['final_term']) :

# 	Topic_Table(topic_id=int(topic_id), topic_name=str(topic_name), weightage=str(weightage), grade=int(grade), subject=str(subject),
# 		sequence=int(sequence), month=str(month), hours=int(hours), min_hours=int(min_hours), mean_hours=float(mean_hours),
# 		max_hours=int(max_hours), pre_mid_term=str(pre_mid_term), mid_term=str(mid_term), pre_final_term=str(pre_final_term),
# 		final_term=str(final_term)).save()
#
# df = pd.read_csv('Subtopic_Table.csv')
# df['mean_hours'].fillna(float(0), inplace=True)
# df['min_hours'].fillna(float(0), inplace=True)
# df['max_hours'].fillna(float(0), inplace=True)
# for topic_id, subtopic_id, subtopic_name, sequence, min_hours, mean_hours, max_hours in zip(df['topic_id'], df['subtopic_id'], df['subtopic_name'], df['sequence'], df['min_hours'], df['mean_hours'], df['max_hours']):
# 	Id = Topic_Table.objects.get(topic_id=topic_id)
# 	Subtopic_Table(topic_id=Id, subtopic_id=int(subtopic_id), subtopic_name=str(subtopic_name), sequence=int(sequence), min_hours=int(min_hours), mean_hours=float(mean_hours), max_hours=int(max_hours)).save()
