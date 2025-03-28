from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="index"),
    path('register/',Registration,name="register"),
    path('services/',services,name="services"),
    path('regsave/',regsave,name="regsave"),
    path('contact/',contact,name="contact"),
    path('login/',Login,name="login"),
    path('logcode/',logcode,name="logcode"),
    path('studentzone/',studentzone,name="studentzone"),
    path('logout/',logout,name="logout"),
    path('studenthome/',studenthome,name="studenthome"),
    path('updateprofile/',updateprofile,name="updateprofile"),
    path('upprofile/',upprofile,name="upprofile"),
    path('upsave/',upsave,name="upsave"),
    path('adminzone/',adminzone,name="adminzone"),
    path('adminhome/',adminhome,name="adminhome"),
    path('adminlogout/',adminlogout,name="adminlogout"),
    path('managestudent/',managestudent,name="managestudent"),
    path('showenq/',showenq,name="showenq"),
    path('usm/',Usm,name="usm"),
    path('usmsave/',usmsave,name="usmsave"),
    path('upload_lecture/',Upload_lecture,name="upload_lecture"),
    path('lecturesave/',lecturesave,name="lecturesave"),
    path('viewstudy/',viewstudy,name="viewstudy"),
    path('viewlecture/',showlecture,name="viewlecture"),
    path('upass/',upass,name="upass"),
    path('upasssave/',upasssave,name="upasssave"),
    path('viewassignment/',viewassignment,name="viewassignment"),
    path('feedback/',feedback,name="feedback"),
    path('feedsave/',feedsave,name="feedsave"),
    path('comp/',comp,name="comp"),
    path('compsave/',compsave,name="compsave"),
    path('deletefeed/<int:id>',deletefeed,name="deletefeed"),
    path('deletecomp/<int:id>',deletecomp,name="deletecomp"),
    path('viewcomp',ViewComp,name="viewcomp"),
    path('viewfeed',ViewFeed,name="viewfeed"),
    path('deletestu/<int:id>',deletestu,name="deletestu"),
    path('editstu/<int:id>',editstu,name="editstu"),
    path('stusave',stusave,name="stusave"),
    path('deleteenq/<int:id>',deleteenq,name="deleteenq"),
    path('deleteusm/<int:id>',deleteusm,name="deleteusm"),
    path('deletelec/<int:id>',deletelec,name="deletelec"),
    path('deleteass/<int:id>',deleteass,name="deleteass"),
    path('deletecomp/<int:id>',deletecomp,name="deletecomp"),
    path('deletefeed/<int:id>',deletefeed,name="deletefeed"),
    path('addnoti',addnoti,name="addnoti"),
    path('editenq/<int:id>',editenq,name="editenq"),
    path('enqsave/<int:id>',enqsave,name="enqsave"),
    path('asssave',asssave,name="asssave"),
    path('editass/<int:id>',editass,name="editass"),
    path('editfeed/<int:id>',editfeed,name="editfeed"),
    path('efeedsave/<int:id>',efeedsave,name="efeedsave"),
    path('editcomp/<int:id>',editcomp,name="editcomp"),
    path('ecompsave/<int:id>',ecompsave,name="ecompsave"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

