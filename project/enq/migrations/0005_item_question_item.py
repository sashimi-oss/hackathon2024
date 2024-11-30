# Generated by Django 4.2 on 2024-11-30 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enq', '0004_alter_format_format_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.CharField(default='非常に満足', max_length=100, null=True, verbose_name='項目1')),
                ('item2', models.CharField(default='やや満足', max_length=100, null=True, verbose_name='項目2')),
                ('item3', models.CharField(default='少し満足', max_length=100, null=True, verbose_name='項目3')),
                ('item4', models.CharField(default='どちらともいえない', max_length=100, null=True, verbose_name='項目4')),
                ('item5', models.CharField(default='少し不満', max_length=100, null=True, verbose_name='項目5')),
                ('item6', models.CharField(default='やや不満', max_length=100, null=True, verbose_name='項目6')),
                ('item7', models.CharField(default='非常に不満', max_length=100, null=True, verbose_name='項目7')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='enq.item'),
        ),
    ]
