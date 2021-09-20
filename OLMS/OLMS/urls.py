from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('students.urls')),
    path('adminPanel/', include('adminDashboard.urls')),
    path('', include('shared.urls')), 

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)