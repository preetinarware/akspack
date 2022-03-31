# Generated by Django 3.2.6 on 2022-03-29 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20220329_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetail',
            old_name='discount',
            new_name='min_pack_ordr',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='base',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='gst',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='material',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='price',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='size',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='thickness',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='transports',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='uses',
        ),
        migrations.RemoveField(
            model_name='productmaterial',
            name='mate_id',
        ),
        migrations.RemoveField(
            model_name='productstyle',
            name='col_id',
        ),
        migrations.RemoveField(
            model_name='productthickness',
            name='thick_id',
        ),
        migrations.RemoveField(
            model_name='productuses',
            name='use_id',
        ),
        migrations.AddField(
            model_name='productsize',
            name='size_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=1000, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('price_base', models.IntegerField()),
                ('transports', models.IntegerField()),
                ('gst', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productcategory')),
                ('color', models.ManyToManyField(to='shop.productStyle')),
                ('material', models.ManyToManyField(to='shop.productMaterial')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.productdetail')),
                ('size', models.ManyToManyField(to='shop.productSize')),
                ('thickness', models.ManyToManyField(to='shop.productThickness')),
                ('uses', models.ManyToManyField(to='shop.productUses')),
            ],
        ),
    ]
