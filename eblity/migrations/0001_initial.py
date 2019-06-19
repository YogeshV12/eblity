# Generated by Django 2.2.1 on 2019-06-19 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic_Table',
            fields=[
                ('topic_id', models.IntegerField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(blank=True, max_length=100)),
                ('weightage', models.CharField(blank=True, max_length=15)),
                ('grade', models.IntegerField(null=True)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('sequence', models.IntegerField(null=True)),
                ('month', models.CharField(blank=True, max_length=15)),
                ('hours', models.IntegerField(null=True)),
                ('min_hours', models.IntegerField(null=True)),
                ('mean_hours', models.FloatField(null=True)),
                ('max_hours', models.IntegerField(null=True)),
                ('pre_mid_term', models.CharField(blank=True, max_length=15)),
                ('mid_term', models.CharField(blank=True, max_length=15)),
                ('pre_final_term', models.CharField(blank=True, max_length=15)),
                ('final_term', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Subtopic_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic_id', models.IntegerField()),
                ('subtopic_name', models.CharField(blank=True, max_length=25)),
                ('sequence', models.IntegerField(null=True)),
                ('min_hours', models.IntegerField(null=True)),
                ('mean_hours', models.FloatField(null=True)),
                ('max_hours', models.IntegerField(null=True)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eblity.Topic_Table')),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('resource_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subtopic_id', models.IntegerField()),
                ('resource_type', models.CharField(blank=True, max_length=30)),
                ('resource_link', models.URLField(blank=True)),
                ('tags', models.CharField(blank=True, max_length=30)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eblity.Topic_Table')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(blank=True, max_length=100)),
                ('weightage', models.CharField(blank=True, max_length=15)),
                ('sequence', models.IntegerField(null=True)),
                ('month', models.CharField(max_length=15)),
                ('hours', models.IntegerField(null=True)),
                ('subject', models.CharField(blank=True, max_length=20)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eblity.Topic_Table')),
            ],
        ),
        migrations.CreateModel(
            name='Journey_template',
            fields=[
                ('student_id', models.IntegerField(default=1)),
                ('subtopic_id', models.IntegerField()),
                ('journey_template_key', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(default='pending', max_length=30)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('time_spent', models.TimeField(blank=True, null=True)),
                ('feedback', models.CharField(blank=True, max_length=1000, null=True)),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eblity.Resources')),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eblity.Topic_Table')),
            ],
        ),
    ]
