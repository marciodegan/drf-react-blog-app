from django.urls import path
from .views import PostList, PostDetail, PostListDetailFilter, CreatePost, EditPost, AdminPostDetail, DeletePost
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls


# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#     path('', PostList.as_view(), name='listcreate'),
   
# ]

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
    
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost')
]