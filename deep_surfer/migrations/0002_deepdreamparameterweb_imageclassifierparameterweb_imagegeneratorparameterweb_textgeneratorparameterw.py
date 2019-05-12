# Generated by Django 2.2.1 on 2019-05-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deep_surfer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeepDreamParameterWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dream_layer', models.CharField(default='mixed3a', max_length=9)),
                ('naive_render_iter', models.IntegerField(default=20)),
                ('naive_step', models.FloatField(default=1.0)),
                ('deep_render_iter', models.IntegerField(default=10)),
                ('deep_step', models.FloatField(default=1.5)),
                ('octave_number', models.IntegerField(default=4)),
                ('octave_scaled', models.FloatField(default=1.4)),
                ('downsize', models.FloatField(default=255.0)),
                ('img_noise_size', models.IntegerField(default=224)),
                ('imagenet_mean_init', models.FloatField(default=117.0)),
                ('grad_tile_size', models.IntegerField(default=256)),
                ('strip_const_size', models.IntegerField(default=32)),
            ],
        ),
        migrations.CreateModel(
            name='ImageClassifierParameterWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_steps', models.IntegerField(default=4000)),
                ('learn_rate', models.FloatField(default=0.01)),
                ('print_misclass', models.BooleanField(default=False)),
                ('flip_l_r', models.BooleanField(default=False)),
                ('rnd_crop', models.BooleanField(default=False)),
                ('rnd_scale', models.BooleanField(default=False)),
                ('rnd_brightness', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ImageGeneratorParameterWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resize_side_length', models.IntegerField(default=256)),
                ('height', models.IntegerField(default=128)),
                ('width', models.IntegerField(default=128)),
                ('channels', models.IntegerField(default=3)),
                ('batch_size', models.IntegerField(default=64)),
                ('epochs', models.IntegerField(default=1000)),
                ('random_dim', models.IntegerField(default=100)),
                ('learn_rate', models.FloatField(default=0.0002)),
                ('clip_weights', models.FloatField(default=0.01)),
                ('d_iters', models.IntegerField(default=5)),
                ('g_iters', models.IntegerField(default=1)),
                ('save_ckpt_rate', models.IntegerField(default=500)),
                ('save_img_rate', models.IntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='TextGeneratorParameterWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_epochs', models.IntegerField(default=15)),
                ('num_generate', models.IntegerField(default=800)),
                ('temperature', models.IntegerField(default=1.0)),
                ('trim_text', models.IntegerField(default=1)),
                ('embedding_dim', models.IntegerField(default=128)),
                ('step_size', models.IntegerField(default=3)),
                ('seq_length', models.IntegerField(default=40)),
                ('BATCH_SIZE', models.IntegerField(default=128)),
            ],
        ),
    ]
