from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    '''
    Read(R)
    포스트들을 불러와서 리스트형태로 보여준다.
    '''

    posts = Post.objects.all() #READ
    ctx = {'posts': posts}

    return render(request, template_name="posts/list.html", context=ctx)


def post_detail(request, post_id):
    '''
    Read(R)
    특정 포스트를 불러와서 상세정보를 보여준다.
    '''

    post = Post.objects.get(id=post_id)
    ctx = {'post': post}

    return render(request, template_name="posts/detail.html", context=ctx)

def create_post(request):
    '''
    Create(C)
    포스트를 새로 생성한다
    request method ==> GET, POST
    '''

    if request.method == 'POST':
        #글쓰기 칸을 저장할 때 '저장하기' 버튼을 눌렀을 때
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:list')
    else:
        #글쓰기 칸을 보여줄 때
        form = PostForm()
        ctx = {'form': form}

        return render(request, template_name='posts/post_form.html', context=ctx)