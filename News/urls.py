from django.urls import path
from News.views import bloghome, blogdetail, addblog, editblog, deleteblog

app_name = "news"

urlpatterns = [
    path("bloghome", bloghome, name="bloghome"),
    path("blogdetail/<int:blogid>/", blogdetail, name="blogdetail"),
    path("addblog/", addblog, name="addblog"),
    path("editnewsblog/<int:blogid>/", editblog, name="editnewsblog"),
    path("deleteblog/<int:blogid>/", deleteblog, name="deleteblog"),
    # path("usersblog/<int:user_id>/", blogkolist, name="userblog"),


]
