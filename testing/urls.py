from django.contrib import admin
from django.urls import path
from core.views import home,article,addblog,editblog,deleteblog,login_user,sign_up,log_out,addCategory,ListCategories,Specific_categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",home.as_view(),name="home"),
    path("article/<int:pk>",article.as_view(),name="article_detail"),
    path("add_post/",addblog.as_view(),name="addpost"),
    path("atricle/edit/<int:pk>",editblog.as_view(),name="editBlog"),
    path("article/delete/<int:pk>",deleteblog.as_view(),name="deleteBlog"),
    path("",login_user,name="login"),
    path("signup/",sign_up,name="signup"),
    path("logout/",log_out,name="logout"),
    path("add_category",addCategory,name="add_Category"),
    path("Categories_list/",ListCategories,name="category_list"),
    path("specific_categoy/<int:pk>",Specific_categories,name="specific_categoy")
]
