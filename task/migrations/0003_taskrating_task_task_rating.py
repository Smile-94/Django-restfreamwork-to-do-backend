# Generated by Django 4.1.5 on 2023-01-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_modified_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('poor', 'Poor')], default='good', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_rating',
            field=models.ManyToManyField(to='task.taskrating'),
        ),
    ]