from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Post
def hello_view(request):
    return HttpResponse("Hello world")

def example_view(request):
    return HttpResponse(f"""
    {request.method}
    {request.GET.get("name")}
    {request.POST.get("title")}
    {request.user}
    {request.session}
""")

def post_create(requst):
    if requst.method == "POST":
        title=requst.POST.get("title")
        return HttpResponse("Created")
    
def post_list(request):
    context = {
        "title": "My posting"
    }
    return render(request, "post_list.html",context=context)

def example(reqest):
    return redirect("post_list")

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context={"post":post}
    return render(request, "detail.html",context=context )

class MyView(View):
    def get(self,request):
        return HttpResponse("get response")
    def post(self,reqest):
        return HttpResponse("post response")

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name="posts"