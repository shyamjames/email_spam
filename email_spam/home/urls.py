"""email_spam URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from .import views


urlpatterns = [
  path('',views.public_home),
  path('login',views.login),
  path('registration',views.registration),
  path('raise_complaint',views.raise_complaint),
  path('feedback',views.feedback),
  path('submit_message',views.submit_message),
  path('view_history',views.view_history),
  path('admin_home',views.admin_home),
  path('user_home',views.user_home),
  path('user_header',views.user_header),
  path('update_message/<id>',views.update_message),
  path('delete_message/<id>',views.delete_message),
  path('logout',views.logout),
  path('admin_complaints',views.admin_complaints),
  path('admin_resolve_complaint/<id>',views.admin_resolve_complaint),
  path('admin_complaint_delete/<id>',views.admin_complaint_delete),
#   path("view_user/",views.view_user),
  path('admin_user_delete',views.admin_user_delete),
  path('admin_feedback',views.admin_feedback),
  path('admin_header',views.admin_header),
  path('admin_footer',views.admin_footer),
  path('user_footer',views.user_footer),

    path("signup_and",views.signup_and),
    path("login_and",views.login_and),
    path("complaint_and",views.complaint_and),
    path("feedback_and",views.feeedback_and),
    path("reply_and",views.reply_and),
    path("predict_and",views.predict_and),
    path("msgs_and",views.msgs_and)
]
