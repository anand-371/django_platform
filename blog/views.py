from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,RedirectView


def home(request):
	context={
			'posts':Post.objects.all()
	}
	return render(request,'blog/home.html',context)
# Create your views here. 
def like_post(request):
	post=get_object_or_404(Post,id=request.POST.get('id')) 
	post.likes.add(request.user)
	return HttpResponseRedirect(post.get_absolute_url())




class PostListView(ListView):
	model=Post
	template_name='blog/home.html'
	context_object_name='posts'
	ordering=['-date_posted']

class PostDetailView(DetailView):
	model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields=['domain','Subject','Description','file']

	def form_valid(self, form):
		form.instance.author = self.request.user
		post = form.save(commit=False)
		post.save()
		return redirect('blog-about')

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['title','content','file']

	def form_valid(self, form):
		form.instance.author = self.request.user
		post = form.save(commit=False)
		post.save()
		return redirect('blog-about')
	def test_func(self):
		post=self.get_object()
		if self.request.user== post.author:
			return True
		return False	
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post	
	success_url='/'
	def test_func(self):
		post=self.get_object()
		if self.request.user== post.author:
			return True
		return False				
def about(request):
	return render(request,'blog/about.html',{'title':'about'})