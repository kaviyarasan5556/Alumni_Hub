# from . import views
# from django.urls import path

# urlpatterns = [
#     path('',views.home,name='home'),
#     path('login/',views.login,name='login'),
#     path('Studentsignup/',views.studentsignup,name='Studentsignup'),
#     path('aluminsignup/',views.aluminsignup,name='aluminsignup'),
#     path('studentdashboard/',views.studentdashboard,name='studentdashboard'),
# ]

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('student-signup/', views.student_signup, name='Studentsignup'),
    path('alumni-signup/', views.alumni_signup, name='aluminsignup'),
    
    # Dashboard URLs
    path('studentdashboard/', views.student_dashboard, name='student_dashboard'),
    path('alumnidashboard/', views.alumni_dashboard, name='alumni_dashboard'),
    path('admindashboard/', views.admin_dashboard, name='admin_dashboard'),
<<<<<<< HEAD
=======

    # Student Dashboard Sub-pages
    path('studentdashboard/apply-internship/', views.apply_internship, name='apply_internship'),
    path('studentdashboard/apply-job/', views.apply_job, name='apply_job'),
    path('studentdashboard/apply-conference/', views.apply_conference, name='apply_conference'),
    path('studentdashboard/student_feedback/', views.student_feedback, name='studentfeedback'),
    path('studentdashboard/Career_Resource/', views.career_resource_view, name='career_output_resource'),
>>>>>>> 0891298 (final push)
    
    # Admin Dashboard Sub-pages
    path('admindashboard/student-data/', views.student_data, name='student_data'),
    path('admindashboard/alumni-data/', views.alumni_data, name='alumni_data'),
    path('admindashboard/donation/', views.donation, name='donation'),
    path('admindashboard/crowdfunding/', views.crowdfunding, name='crowdfunding'),
    
    # Alumni Dashboard Sub-pages

    path('alumnidirectory/', views.alumindirectory_view , name='alumnidirectory'),
    path('alumnidashboard/profile/', views.alumni_profile, name='alumni_profile'),
    path('studentdashboard/profile/', views.student_profile, name='student_profile'),
    path('alumnidashboard/management/', views.alumni_management, name='alumni_management'),
    path('alumnidashboard/job-posting/', views.job_posting, name='job_posting'),
    path('alumnidashboard/internship/', views.internship, name='internship'),
    path('alumnidashboard/career-resource/', views.career_resource, name='career_resource'),
    path('alumnidashboard/upcoming-events/', views.upcoming_events, name='upcoming_events'),
    path('alumnidashboard/conference/', views.conference, name='conference'),
<<<<<<< HEAD

=======
    path('alumnidashboard/alumni_survey/', views.alumni_survey, name='alumni_survey'),
    path('aluminidashboard/croudfunding/', views.croudfunding_view, name='alumni_crowdfunding'),
    path('alumnidashboard/campaignoutput/', views.croudfunding_output, name='campaignoutput'),
>>>>>>> 0891298 (final push)

    #Nav common
    path('about/',views.about,name='about')
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
