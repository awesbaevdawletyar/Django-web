# Generated by Django 4.1.7 on 2023-03-04 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_statuscrm_alter_order_options_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Текст Комментария')),
                ('comment_dt', models.DateTimeField(auto_now=True, verbose_name='Дата создание')),
                ('comment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
