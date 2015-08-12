from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dblog.views.home', name='home'),
    # url(r'^dblog/', include('dblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include( 'django_markdown.urls')),

    url(r'^$', 'blog.views.index', name='index'),
    url(r'^blog/beauty$','blog.views.beauty'),
    url(r'^blog/Ios$','blog.views.Ios'),
    url(r'^blog/Linux$','blog.views.Linux'),
    url(r'^blog/Music$','blog.views.Music'),
    url(r'^blog/Fo$','blog.views.Fo'),
    url(r'^blog/Python$','blog.views.Python'),
    url(r'^blog/Game$','blog.views.Game'),
    url(r'^blog/Django$','blog.views.Django'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/detail/$', 'blog.views.blog_detail'),

)

#urlpatterns += staticfiles_urlpatterns()

