

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
                ('date', models.DateField(verbose_name='дата поступления')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=8, verbose_name='цена')),
                ('unit', models.IntegerField(choices=[(1, 'шт.'), (2, 'кг.')], verbose_name='единица измерения')),
                ('provider', models.CharField(blank=True, max_length=256, verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
