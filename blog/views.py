from django.shortcuts import redirect, render ,get_object_or_404
from . models import *
from taggit.models import Tag

# Create your views here.
def home(request):
    #.order_by دي عشان التصنيف 
   all_blogs=Blog.objects.all().order_by("-id")
   return render(request , 'blog/index.html',{'all_blogs':all_blogs})

def detail(request , pk):
    blog=Blog.objects.get(id=pk)
    coment=Coment.objects.filter(blog=blog , active=True).order_by('-crated_at')
    return render(request , 'blog/detail.html',{'blog':blog ,'coment':coment})

def get_tags(request,tag_slug):
   all_blogs=Blog.objects.all().order_by("-id")
   if tag_slug:
      tag = get_object_or_404(Tag , slug=tag_slug)
      blogs=all_blogs.filter(tags__in=[tag])
      
   context = {
        
        'all_blogs':blogs,
        tag:tag,
        
    }
   return render(request , 'blog/tags.html',context)



def save_comment(request):
    
    if request.method == "POST":
        id= request.POST.get('id')
        blog = Blog.objects.get(id=id)
        crated_at= request.POST.get('crated_at')
        message = request.POST.get('message')
       
        user = request.user
        new_Coment = Coment.objects.create(content=message, active=True, user=user, blog=blog , crated_at=crated_at) 
        new_Coment.save()
        return redirect ('detail' , id)
    
    
def delet(requst):
    if requst.method == "POST":
        pk= requst.POST.get('id-delet')
        id= requst.POST.get('id')
        comment=Coment.objects.get(id=pk)
        comment.delete()
        #دي طريقة للحذف مباشر اني جبت id coment بشكل مباشر
        #return redirect ('detail' , comment.blog.id)
        
        #دي طريقه تانيه اني ذودت انبت يجبلي رقم البلوج id
        return redirect ('detail' , id)
