from django.urls import include, path
from django.contrib import admin
from classroom.views import classroom, students, teachers
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register("login", classroom.LoginViewSet, basename="login")
router.register("profile", classroom.UserProfileViewSet)
#router.register("accounts/signup/student/", students.UserProfileViewSet)
#router.register("student", students.StudentSignUpView, basename='student_signup')



urlpatterns = [
	path('admin/', admin.site.urls),
    path('', include('classroom.urls')),
	#path('login/', classroom.LoginViewSet.as_view(), name='login'),
#path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),  # <-- And here	path('accounts/login/',auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', csrf_exempt(classroom.SignUpView.as_view()), name='signup'),
    path('accounts/signup/student/', csrf_exempt(students.StudentSignUpView.as_view({"post": "create"})), name='student_signup'),
#    path('accounts/signup/student/', students.UserProfileViewSet.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', csrf_exempt(teachers.TeacherSignUpView.as_view()), name='teacher_signup'),
	url(r'', include(router.urls)),
	#url(r'^auth/', include('rest_framework_social_oauth2.urls')),

]
#, auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'
#{"get": "retrieve", "post": "create", "put": "update"}
