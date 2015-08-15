 # coding=utf8
from blog.models import Article, Tag, Classification
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404



def index(request):
    return render_to_response('index.html')
#def blog_list(request):
   # blogs = Article.objects.all().order_by('-publish_time')

    #return render_to_response('index.html', {"blogs": blogs}, context_instance=RequestContext(request))
def contact_me(reqest):
    return render_to_response('contact_me.html', RequestContext(reqest))



def beauty(request):
    str = "美女"
    cls = Classification.objects.get(name=str)
    blogs = Article.objects.filter(classification=cls)

    return render_to_response('beauty.html',{"blogs":blogs},context_instance=RequestContext(request))


def Python(request):
    cls = Classification.objects.get(name="python")
    blogs = Article.objects.filter(classification=cls)
    return render_to_response('python.html',{"blogs":blogs},context_instance=RequestContext(request))


def Django(request):
    cls = Classification.objects.get(name="django")
    blogs = Article.objects.filter(classification=cls)
    return render_to_response('django.html',{"blogs":blogs},context_instance=RequestContext(request))


def Fo(request):
    str = "佛"
    cls = Classification.objects.get(name=str)
    blogs = Article.objects.filter(classification=cls)
    return render_to_response('fo.html',{"blogs":blogs},context_instance=RequestContext(request))


def Ios(request):
    cls = Classification.objects.get(name="Ios")
    blogs = Article.objects.filter(classification=cls)
    return render_to_response('Ios.html',{"blogs":blogs},context_instance=RequestContext(request))


def Linux(request):
    cls = Classification.objects.get(name="Linux")
    blogs = Article.objects.filter(classification=cls)
    return render_to_response('Linux.html',{"blogs":blogs},context_instance=RequestContext(request))

def Music(request):
    cls = Classification.objects.get(name="Music")
    blogs = Article.objects.filter(classification=cls)
    return render_to_response('Music.html',{"blogs":blogs},context_instance=RequestContext(request))


def Game(request):
    cls = Classification.objects.get(name="Game")
    blogs = Article.objects.filter(classification=cls)
    return render_to_response('Game.html',{"blogs":blogs},context_instance=RequestContext(request))


def blog_detail(request):
    if request.method == 'GET':
        id = request.GET.get('id', '');
        try:
            blog = Article.objects.get(id=id)
        except Article.DoesNotExist:
            raise Http404
        return render_to_response("detail.html", {"blog": blog}, context_instance=RequestContext(request))
    else:
        raise Http404