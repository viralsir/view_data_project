from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns=[
    #path("",views.home,name="blog-home"),
    path("",PostListView.as_view(),name="blog-home"),
    path("post/<int:pk>",PostDetailView.as_view(),name="post-detail"),
    path("post/<int:pk>/update",PostUpdateView.as_view(),name="post-update"),
    path("post/<int:pk>/delete",PostDeleteView.as_view(),name="post-delete"),
    path("post/new",PostCreateView.as_view(),name="post-create"),
    path("post/<str:username>", UserPostListView.as_view(), name="user-post"),
    path("about",views.about,name="blog-about")
]

#app_dir/model_viewtype.html
#blog/post_detail.html
#blog/post_form.html
#app_dir/model_confirm_delete.html
