from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views
from my_web.views import CaseViewSet
from my_web.login_views import login
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import serve
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'case', CaseViewSet)


# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/login$', login),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
    url(r'^', TemplateView.as_view(template_name="index.html")),
    url(r'^static/(?P<path>.*)$',serve,{'document_root': settings.STATIC_ROOT}),
   
]