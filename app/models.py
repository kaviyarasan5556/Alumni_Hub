from django.db import models

# Create your models here.
class Studentsignup(models.Model):
  Name=models.CharField(max_length=100)
  Email=models.EmailField()
  Password=models.CharField(max_length=10)
  Roll_Number=models.CharField(max_length=15)
  Course=models.CharField(max_length=8)
  Branch=models.CharField(max_length=15)
  Year=models.CharField(max_length=10)
  
  def __str__(self):
    return f"{self.Name} ({self.Roll_Number})"
  
class Alumnisignup(models.Model):
  name=models.CharField(max_length=30)
  email=models.CharField(max_length=30)
  password=models.CharField(max_length=30)
  designation=models.CharField(max_length=30)
  passedout=models.IntegerField()
  location=models.CharField(max_length=30)
  company=models.CharField(max_length=30)

  def __str__(self):
    return f"{self.name} ({self.email})"


class Alumni_Profile(models.Model):
  profile_picture=models.ImageField(upload_to='profile_pictures/')
  name=models.CharField(max_length=30)
  passout_year=models.IntegerField()
  degree=models.CharField(max_length=30)
  department=models.CharField(max_length=30)  
  designation=models.CharField(max_length=30)
  company=models.CharField(max_length=30)
  description=models.TextField()
  linkedin_profile=models.URLField(max_length=30)
  location=models.CharField(max_length=30)
  
  
  def __str__(self):
    return f"{self.name} ({self.designation})"

class Student_Profile(models.Model):
  profile_picture=models.ImageField(upload_to='profile_pictures/')
  name=models.CharField(max_length=30)
  roll_number=models.CharField(max_length=30)
  cgpa=models.FloatField()
  standing_arrear=models.BooleanField(default=False)
  arrear_history=models.IntegerField()
  attendance=models.FloatField()
  year=models.CharField(max_length=30)
  degree=models.CharField(max_length=30)
  department=models.CharField(max_length=30)
  location=models.CharField(max_length=30)

  def __str__(self):
    return f"{self.name} ({self.roll_number})"

class Job_Posting(models.Model):
  job_title=models.CharField(max_length=30)
  job_company=models.CharField(max_length=30)
  job_location=models.CharField(max_length=30)
  job_salary=models.IntegerField()
  job_type=models.CharField(max_length=30)
  job_experience=models.CharField(max_length=30)
  job_skills=models.TextField()
  job_description=models.TextField()

  def __str__(self):
    return f"{self.job_title} ({self.job_company})"

class Internship(models.Model):
  internship_title=models.CharField(max_length=30)
  internship_company=models.CharField(max_length=30)
  internship_location=models.CharField(max_length=30)
  internship_duration=models.CharField(max_length=30)
  internship_type=models.CharField(max_length=30)
  internship_start_date=models.DateField()
  internship_eligibility=models.TextField()
  internship_description=models.TextField()

  def __str__(self):
    return f"{self.internship_title} ({self.internship_company})"

class Career_Resource(models.Model):
  resource_title=models.CharField(max_length=30)
  resource_description=models.TextField()
  resource_type=models.CharField(max_length=30)
  resource_file=models.FileField(upload_to='resource_files/')
  youtube_link=models.URLField(max_length=30)

  def __str__(self):
    return f"{self.resource_title}"


class Upcoming_Events(models.Model):
  event_document=models.FileField(upload_to='event_documents/')
  event_primary_image=models.ImageField(upload_to='event_documents/')
  event_secondary_image=models.ImageField(upload_to='event_documents/')
  event_venue=models.CharField(max_length=30)
  event_date=models.DateField()
  event_title=models.CharField(max_length=30)

  def __str__(self):
    return f"{self.event_title}"

class Conference(models.Model):
  conference_document=models.FileField(upload_to='conference_documents/')
  conference_primary_image=models.ImageField(upload_to='conference_documents/')
  conference_secondary_image=models.ImageField(upload_to='conference_documents/')
  conference_venue=models.CharField(max_length=30)
  conference_date=models.DateField()
  conference_alumni_name=models.CharField(max_length=30)

  def __str__(self):
    return f"{self.conference_title}"
  
class Student_Feedback(models.Model):
  student_name=models.CharField(max_length=30)
  student_email=models.EmailField()
  student_phone=models.IntegerField()
  student_department=models.CharField(max_length=30)
  student_year=models.CharField(max_length=30)
  feedback=models.TextField()

  def __str__(self):
    return f"{self.student_name}"
  
class Financial_Campaign(models.Model):
  campaign_name=models.CharField(max_length=30)
  campaign_description=models.TextField()
  campaign_target_amount=models.IntegerField()

  def __str__(self):
    return f"{self.campaign_name}"  

