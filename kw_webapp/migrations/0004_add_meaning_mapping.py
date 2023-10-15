# Generated by Django 2.2.24 on 2023-10-14 19:19

from django.db import migrations, models
import django.db.models.deletion
import kw_webapp.constants


class Migration(migrations.Migration):

    dependencies = [
        ('kw_webapp', '0003_vocabulary_manual_reading_whitelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaning', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='vocabulary',
            name='auxiliary_meanings_whitelist',
        ),
        migrations.RemoveField(
            model_name='vocabulary',
            name='meaning',
        ),
        migrations.CreateModel(
            name='MeaningMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PRIMARY', 'Primary'), ('SECONDARY', 'Secondary'), ('AUXILIARY', 'Auxiliary')], max_length=20)),
                ('meaning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocabulary', to='kw_webapp.Meaning')),
                ('vocabulary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meanings', to='kw_webapp.Vocabulary')),
            ],
        ),
        migrations.AddConstraint(
            model_name='meaningmapping',
            constraint=models.UniqueConstraint(condition=models.Q(type=kw_webapp.constants.MeaningType('Primary')), fields=('vocabulary', 'type'), name='unique_primary_meaning'),
        ),
        migrations.AlterField(
            model_name='meaning',
            name='meaning',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddConstraint(
            model_name='meaningmapping',
            constraint=models.UniqueConstraint(condition=models.Q(type=kw_webapp.constants.MeaningType('Primary')), fields=('meaning', 'vocabulary'), name='only_one_type_for_mapping'),
        ),
    ]
