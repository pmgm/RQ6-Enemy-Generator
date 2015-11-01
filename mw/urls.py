from django.conf.urls import patterns, url

from mw import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^enemies/$', views.index, name='index'),
    url(r'^parties/$', views.party_index, name='party_index'),
    url(r'^generate_enemies/$', views.generate_enemies, name='generate_enemies'),
    url(r'^generate_party/$', views.generate_party, name='generate_party'),
    url(r'^edit_index/$', views.edit_index, name='edit_index'),
    url(r'^enemy_template/(?P<enemy_template_id>\d+)/$', views.enemy_template, name='enemy_template'),
    url(r'^party/(?P<party_id>\d+)/$', views.party, name='party'),
    url(r'^instructions/$', views.instructions, name='instructions'),
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^about/$', views.about, name='about'),
    url(r'^whats_new/$', views.whats_new, name='whats_new'),
    url(r'^set_filter/$', views.set_filter, name='set_filter'),
    url(r'^set_party_filter/$', views.set_party_filter, name='set_party_filter'),

    url(r'^pdf_export/$', views.pdf_export, name='pdf_export'),
    url(r'^png_export/$', views.png_export, name='png_export'),
    url(r'^delete_template/(?P<template_id>\d+)/$', views.delete_template, name='delete_template'),
    url(r'^clone_template/(?P<template_id>\d+)/$', views.clone_template, name='clone_template'),
    url(r'^clone_party/(?P<party_id>\d+)/$', views.clone_party, name='clone_party'),
    url(r'^create_enemy_template/$', views.create_enemy_template, name='create_enemy_template'),
    url(r'^apply_skill_bonus/(?P<template_id>\d+)/$', views.apply_skill_bonus, name='apply_skill_bonus'),
    url(r'^delete_party/(?P<party_id>\d+)/$', views.delete_party, name='delete_party'),
    url(r'^create_party/$', views.create_party, name='create_party'),
)
