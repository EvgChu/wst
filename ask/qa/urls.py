"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from qa import views

urlpatterns = [
    path( '',  views.test ),
    re_path(r'^login\/.*$', views.test),
    path( 'signup',  views.test ),
    path( "questin/<int:id>/",  views.test ),
    path( 'ask',  views.test ),
    path( 'popular',  views.test ),
    path( 'new',  views.test ),
]

# /
# /login/
# /signup/
# /question/<123>/    # вместо <123> - произвольный ID
# /ask/
# /popular/
# /new/