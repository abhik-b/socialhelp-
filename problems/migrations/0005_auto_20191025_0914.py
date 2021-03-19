# Generated by Django 2.2.6 on 2019-10-25 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_replytosolution'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='problems.Solution'),
        ),
        migrations.DeleteModel(
            name='ReplyToSolution',
        ),
    ]