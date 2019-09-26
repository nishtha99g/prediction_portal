from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', TemplateView.as_view(template_name='home/homepage.html'), name='home'),
                  path('admin/', admin.site.urls),
                  path('user/', include(('student.urls','student'), namespace='student')),
                  path('accounts/', include('django.contrib.auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
