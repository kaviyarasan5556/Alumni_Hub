# from django.shortcuts import render,redirect
# from django.http import response
# from django.contrib import messages
# from .models import Studentsignup,Alumnisignup
# from django.contrib.auth import authenticate, login, logout
# Create your views here.
# def home(request):
#   return render(request,'home.html')

# def login(request):
#   if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         if not email or not password:
#             messages.error(request, "Both fields are required.")
#             return redirect('login')

#         try:
#             user = Studentsignup.objects.get(Email=email, Password=password)
#             request.session['student_id'] = user.id  # set session manually
#             request.session['student_name'] = user.Name
#             messages.success(request, f"Welcome, {user.Name}!")
#             return redirect('studentdashboard')  # replace with your actual URL name
#         except Studentsignup.DoesNotExist:
#             messages.error(request, "Invalid email or password.")
#             return redirect('login')

#   return render(request, 'login.html')

# def studentsignup(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         roll_no = request.POST.get('rollNumber')
#         course = request.POST.get('course')
#         branch = request.POST.get('branch')
#         year = request.POST.get('year')

#         #Check if user already exists
#         if Studentsignup.objects.filter(Email=email).exists():
#             messages.error(request, 'User is already registered')
#         else:
#             # Save the student details
#           student = Studentsignup(
#               Name=name,
#               Email=email,
#               Password=password,
#               Roll_Number=roll_no,
#               Course=course,
#               Branch=branch,
#               Year=year
#           )
#           student.save()
#           return redirect('studentdashboard') 

#     return render(request, 'studentsignup.html')

# def aluminsignup(request):
#    if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         designation = request.POST.get('designation')
#         passoutYear = request.POST.get('passoutYear')
#         location = request.POST.get('location')
#         company = request.POST.get('company')

#         if Alumnisignup.objects.filter(email=email).exists():
#             messages.error(request, 'User is already registered')
#         else:
#             # Save the student details
#           Alumin = Alumnisignup(
#               name=name,
#               email=email,
#               password=password,
#               designation=designation,
#               passedout=passoutYear,
#               location=location,
#               company=company)
#           Alumin.save()
#           messages.success(request, 'Student registered successfully!')
#           return redirect('home')

#    return render(request,"alumnisignup.html")

# def studentdashboard(request):
#    return render(request,"studentdashboard/studentdashboard.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Alumni_Profile,Job_Posting,Internship,Student_Profile,Career_Resource,Upcoming_Events,Conference,Studentsignup,Alumnisignup

from .models import Alumni_Profile,Job_Posting,Internship,Student_Profile,Career_Resource,Upcoming_Events,Conference,Studentsignup,Alumnisignup,Student_Feedback,Financial_Campaign


# Home page view
def home(request):
    return render(request, 'home.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Please enter both email and password')
            return render(request, 'login.html')

        # Admin check
        if email == 'kavi@gmail.com' and password == 'kavi123':
            return redirect('admin_dashboard')

        # Student check
        student = Studentsignup.objects.filter(Email=email, Password=password).first()
        if student:
            return redirect('student_dashboard')

        # Alumni check
        alumni = Alumnisignup.objects.filter(email=email, password=password).first()
        if alumni:
            return redirect('alumni_dashboard')

        # No match found
        messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')
# Student signup view
def student_signup(request):
    if request.method == 'POST':
        # Process form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        roll_number = request.POST.get('rollNumber')
        course = request.POST.get('course')
        year = request.POST.get('year')
        branch = request.POST.get('branch')

        student= Studentsignup(
            Name=name,
            Email=email,
            Password=password,
            Roll_Number=roll_number,
            Course=course,
            Year=year,
            Branch=branch
        )
        student.save() 
        # Check if user already exists
        
        # Validate data
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'studentsignup.html')
        
        # In a real app, you would save the user to the database here
        
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
    
    return render(request, 'studentsignup.html')

# Alumni signup view
def alumni_signup(request):
    if request.method == 'POST':
        # Process form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        designation = request.POST.get('designation')
        passout_year = request.POST.get('passoutYear')
        location = request.POST.get('location')
        company = request.POST.get('company')
        
        # Validate data
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'alumnisignup.html')
        
        # In a real app, you would save the user to the database here
        
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
    
    return render(request, 'alumnisignup.html')

# Dashboard views
@login_required
def student_dashboard(request):
    return render(request, 'studentdashboard/studentdashboard.html')

@login_required
def apply_internship(request):
    internships = Internship.objects.all()

    return render(request, 'studentdashboard/internshipoutput.html', {
        'internships': internships,
    })
@login_required
def apply_job(request):
    jobs = Job_Posting.objects.all()
    for job in jobs:
        job.skills_list = job.job_skills.split(',')

    return render(request, 'studentdashboard/jobportaloutput.html', {
        'jobs': jobs,
    })
@login_required
def apply_conference(request):
    conferences = Conference.objects.all()
    events= Upcoming_Events.objects.all()
    return render(request, 'studentdashboard/conferenceoutput.html', {
        'conferences': conferences,'events':events
    })

@login_required
def alumni_dashboard(request):
    return render(request, 'alumnidashboard/alumnidashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admindashboard/admindashboard.html')

@login_required
def student_feedback(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        year = request.POST.get('year')
        feedback = request.POST.get('feedback')

        feedback_entry = Student_Feedback(
            student_name=name,
            student_email=email,
            student_phone=phone,
            student_department=department,
            student_year=year,
            feedback=feedback
        )
        feedback_entry.save()

        # Save feedback to the database or process it as needed
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('studentfeedback')
    return render(request, 'studentdashboard/studentfeedback.html')
@login_required
def alumni_survey(request):
    return render(request, 'alumnidashboard/alumnisurveyform.html') 

# @login_required
# def admin_dashboard(request):
#     jobs = Job_Posting.objects.all()
#     internships = Internship.objects.all()
#     resources = Career_Resource.objects.all()
#     events = Upcoming_Events.objects.all()
#     conferences = Conference.objects.all()
#     print("✅ This view is being used")
#     print("📄 Jobs in view:", jobs)

#     return render(request, 'alumnidashboard/alumnidashboard.html', {
#         'jobs': jobs,
#         'internships': internships,
#         'resources': resources,
#         'events': events,
#         'conferences': conferences,
#     })
    #return render(request, 'admindashboard/admindashboard.html')

# Admin dashboard sub-pages
@login_required
def student_data(request):
    return render(request, 'admindashboard/studentdata.html')

@login_required
def alumni_data(request):
    return render(request, 'admindashboard/alumnidata.html')

@login_required
def donation(request):
    return render(request, 'admindashboard/donation.html')

@login_required
def crowdfunding(request):
    return render(request, 'admindashboard/crowndfunding.html')

# Alumni dashboard sub-pages
@login_required
def alumni_profile(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get('photo')
        name = request.POST.get('fullName')
        passout_year = request.POST.get('graduationYear')
        degree = request.POST.get('degree')
        department = request.POST.get('department')
        designation = request.POST.get('jobTitle')
        company = request.POST.get('company')
        description = request.POST.get('skills')
        linkedin_profile = request.POST.get('linkedin')
        location = request.POST.get('location')

        alumni_profile = Alumni_Profile(
            profile_picture=profile_picture,
            name=name,
            passout_year=passout_year,
            degree=degree,
            department=department,
            designation=designation,
            company=company,
            description=description,
            linkedin_profile=linkedin_profile,
            location=location
        )
        alumni_profile.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('alumni_dashboard')
        
    return render(request, 'alumnidashboard/alumniprofile.html')

def student_profile(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get('photo')
        name = request.POST.get('fullName')
        roll_number = request.POST.get('rollNumber')
        cgpa = request.POST.get('cgpa')
        standing_arrear = request.POST.get('standingArrear') == 'true'
        arrear_history = request.POST.get('arrearHistory')
        attendance = request.POST.get('attendance')
        year = request.POST.get('graduationYear')
        degree = request.POST.get('degree')
        department = request.POST.get('department')
        location = request.POST.get('location')
        
        student_profile = Student_Profile(
            profile_picture=profile_picture,
            name=name,
            roll_number=roll_number,
            cgpa=cgpa,
            standing_arrear=standing_arrear,
            arrear_history=arrear_history,
            attendance=attendance,
            year=year,
            degree=degree,
            department=department,
            location=location
        )
        student_profile.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('student_dashboard')
    return render(request, 'studentdashboard/studentprofile.html')

@login_required
def alumni_management(request):
    return render(request, 'alumnidashboard/alumnimanagement.html')

@login_required
def job_posting(request):
    if request.method == 'POST':
        job_title = request.POST.get('jobTitle')
        job_company = request.POST.get('companyName')
        job_location = request.POST.get('location')
        job_salary=request.POST.get('salary')
        job_type = request.POST.get('employmentType')
        job_experience=request.POST.get('experience')
        job_skills=request.POST.get('skills')
        job_description = request.POST.get('description')

        job_posting = Job_Posting(
            job_title=job_title,
            job_company=job_company,
            job_location=job_location,
            job_salary=job_salary,
            job_type=job_type,
            job_experience=job_experience,
            job_skills=job_skills,
            job_description=job_description
        )
        job_posting.save()
        messages.success(request, 'Job posting created successfully')
        return redirect('alumni_dashboard')
    return render(request, 'alumnidashboard/jobposting.html')

@login_required
def internship(request):
    if request.method == 'POST':
        internship_title = request.POST.get('title')
        internship_company = request.POST.get('company')
        internship_location = request.POST.get('location')
        internship_duration = request.POST.get('duration')
        internship_type = request.POST.get('type')
        internship_start_date = request.POST.get('startDate')
        internship_eligibility = request.POST.get('eligibility')
        internship_description = request.POST.get('description')

        internship = Internship(
            internship_title=internship_title,
            internship_company=internship_company,
            internship_location=internship_location,
            internship_duration=internship_duration,
            internship_type=internship_type,
            internship_start_date=internship_start_date,
            internship_eligibility=internship_eligibility,
            internship_description=internship_description
        )
        internship.save()
        messages.success(request, 'Internship created successfully')
        return redirect('alumni_dashboard')
        
    return render(request, 'alumnidashboard/internship.html')

@login_required
def career_resource(request):
    if request.method == 'POST':
        resource_title = request.POST.get('resource_title')
        resource_description = request.POST.get('resource_description')
        resource_type = request.POST.get('resource_type')
        resource_file = request.FILES.get('resource_file')
        youtube_link = request.POST.get('youtubeLink')
        
        career_resource = Career_Resource(
            resource_title=resource_title,
            resource_description=resource_description,
            resource_type=resource_type,
            resource_file=resource_file,
            youtube_link=youtube_link
        )
        career_resource.save()
        messages.success(request, 'Career resource created successfully')
        return redirect('alumni_dashboard')


    return render(request, 'alumnidashboard/careerresource.html')

@login_required
def upcoming_events(request):
    if request.method == 'POST':
        event_document = request.FILES.get('eventDocument')
        event_primary_image = request.FILES.get('eventPrimaryImage')
        event_secondary_image = request.FILES.get('eventSecondaryImage')
        event_venue = request.POST.get('eventVenue')
        event_date = request.POST.get('eventDate')
        event_title = request.POST.get('eventTitle')

        upcoming_events = Upcoming_Events(
            event_document=event_document,
            event_primary_image=event_primary_image,
            event_secondary_image=event_secondary_image,
            event_venue=event_venue,
            event_date=event_date,
            event_title=event_title
        )
        upcoming_events.save()
        messages.success(request, 'Upcoming event created successfully')
        return redirect('alumni_dashboard')
    return render(request, 'alumnidashboard/upcomingevents.html')

@login_required
def conference(request):
    if request.method == 'POST':
        conference_document = request.FILES.get('conferenceDocument')
        conference_primary_image = request.FILES.get('conferencePrimaryImage')
        conference_secondary_image = request.FILES.get('conferenceSecondaryImage')
        conference_venue = request.POST.get('conferenceVenue')
        conference_date = request.POST.get('conferenceDate')    
        conference_alumni_name = request.POST.get('conferenceAlumniName')

        conference_alumni_name = request.POST.get('conferenceAlumni')


        conference = Conference(
            conference_document=conference_document,
            conference_primary_image=conference_primary_image,
            conference_secondary_image=conference_secondary_image,
            conference_venue=conference_venue,
            conference_date=conference_date,
            conference_alumni_name=conference_alumni_name
        )
        conference.save()
        messages.success(request, 'Conference created successfully')
        return redirect('alumni_dashboard') 
    
    return render(request, 'alumnidashboard/conference.html')

# Logout view
def logout_view(request):
    # In a real app, you would use Django's logout functionality
    return redirect('login')

def about(request):
    return render(request, "about.html")

def alumindirectory_view(request):
    return render(request,'alumnidirectory.html')


def croudfunding_view(request):
    if request.method == 'POST':
        campaign_name = request.POST.get('campaign-title')
        campaign_description = request.POST.get('campaign-purpose')
        campaign_target_amount = request.POST.get('goal-amount')

        crowdfunding_campaign = Financial_Campaign( 
            campaign_name=campaign_name,
            campaign_description=campaign_description,
            campaign_target_amount=campaign_target_amount,
        )
        crowdfunding_campaign.save()
        messages.success(request, 'Crowdfunding campaign created successfully')
    return render(request,'admindashboard\crowndfunding.html')

def croudfunding_output(request):
    campaigns = Financial_Campaign.objects.all()
    return render(request, 'alumnidashboard\campaignoutput.html', {
        'campaigns': campaigns,
    })

def career_resource_view(request):
    return render(request, 'studentdashboard/resourceoutput.html', {
        'resources': Career_Resource.objects.all(),
    })