
from django.db import models
from django_markdown.models import MarkdownField


class Tag(models.Model):#biaoqian
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.tag_name)


class Classification(models.Model):#leibie
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.name)


class Author(models.Model):#zuozhe
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Article(models.Model):#wenzhang
    caption = models.CharField(max_length=30)#biaoti
    subcaption = models.CharField(max_length=50, blank=True)#fubiaoti
    publish_time = models.DateTimeField(auto_now_add=True)#fabushijian
    update_time = models.DateTimeField(auto_now=True)#gengxinriqi
    author = models.ForeignKey(Author)#zuozhe
    classification = models.ForeignKey(Classification)#feilei
    tags = models.ManyToManyField(Tag, blank=True)#biaoqian
    content = MarkdownField()#neirong


