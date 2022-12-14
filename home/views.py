from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from blogapp.models import Post

# Create your views here.
def bloghome(request):
    return render(request,'home/index.html')

def contact(request):
    if request.method == "POST":
        print()
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        if len(name) < 2 or len(email) < 11 or len(phone) < 10 or len(desc) < 5:
            messages.error(request, 'Please fill the information correctly')
        else:
            print(name, email, phone, desc)
            contact = Contact(name=name, email=email, phone=phone, content=desc)
            contact.save()
            messages.success(request, 'We have recieved your query,we will get back to you soon')
    return render(request, 'home/contact.html')



def about(request):
    return render(request, 'home/about.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPostsCategory =Post.objects.filter(category__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor,allPostsCategory)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts,'query': query}
    return render(request, 'home/search.html', params)