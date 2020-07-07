

from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    # file = models.FileField(blank=False, null=False)
    # image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    photo = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
        return self.name



class Actors(models.Model):

    Hispanic_Latino = 'Hispanic/Latino'
    Asian_PacificIslander = ' Asian/Pacific Islander'
    Caucasian = 'Caucasian'
    AfricanAmerican = 'African American'
    NativeAmerican = 'Native American'
    not_provided = 'none'

    Talent = 'Talent'
    Director = 'Director'
    Crew = 'Crew'
    NOT_PROVIDED = "none"
    
    TYPE_CHOICES = (
        (Talent, 'Talent'),
        (Director, 'Director'),
        (Crew, 'Crew'),
    )

    Ethnicity_choices = (
        (Hispanic_Latino, 'Hispanic/Latino'),
        (Asian_PacificIslander, 'Asian/Pacific Islander'),
        (Caucasian, 'Caucasian'),
        (AfricanAmerican, 'African American'),
        (NativeAmerican, 'Native American'),
    )
    role = models.CharField(max_length = 8,
    choices =TYPE_CHOICES,
    default=NOT_PROVIDED)

    ethnicity = models.CharField(max_length = 30,
    choices = Ethnicity_choices,
    default = not_provided)

    bio = models.TextField(default="")
    age = models.IntegerField(blank=True, null=True)
    height_feet = models.IntegerField(blank=True, null=True)
    height_inches = models.IntegerField(blank=True, null=True)
    location = models.IntegerField(blank=True, null=True) 
    middle = models.CharField(max_length = 30,default="")




    firstname = models.CharField(max_length=25,default="")
    lastname = models.CharField(max_length=25,default="")
    experience = models.IntegerField(blank=True, null=True)
    
    headshot = models.ImageField(upload_to='images/',null=True)
    
    
    def __str__(self):
        return self.firstname



    
  

# class Users(models.Model): 


class Listings(models.Model): 
    date = models.DateField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.IntegerField()
    overview = models.TextField()
    studio = models.CharField(max_length = 40)
   

    Horror = "Horror"
    Action = "Action"
    Short_Film = "Short Film"
    Romamce = "Romance"
    Thriller = "Thriller"
    Drama = "Drama"
    Musical = "Musical"
    null = "null"

    GENRE_CHOICES = (
       (Horror, 'Horror'),
       (Action,'Action'),
       (Short_Film,'Short Film'),
       (Romamce, 'Romamce'),
       (Thriller,' Thriller'),
       (Drama,'Drama'),
       (Musical,' Musical'),
   )
    genre = models.CharField(max_length = 40,
    choices =GENRE_CHOICES,
    default= null)

    Paid = "Paid"
    Volunteer = "Volunteer"
    Status_Choices = (
        (Paid,'Paid'),
        (Volunteer,'Volunteer'),
    )
    status = models.CharField(max_length = 12,
    choices = Status_Choices,
    default= null)

    Fulltime = "Fulltime"
    Part_Time = "Part Time"
    JOB_CHOICES = (
        (Fulltime,"Fulltime"),
        (Part_Time,'Part Time'),
    )
    job_type = models.CharField(max_length=15,
    choices = JOB_CHOICES,
    default= null)


# class Applied(models.Model):

class User_applications(models.Model): 
    role = models.CharField(max_length = 60)
    company = models.CharField(max_length = 60)
   
    Pending = "Pending"
    Accepted = "Accepted"
    Rejected = "Rejected"

    STATUS_CHOICES = (
        (Pending,"Pending"),
        (Accepted,"Accepted"),
        (Rejected,"Rejected"),
    )
    status = models.CharField(max_length=15,
    choices = STATUS_CHOICES,
    default = "null")
# class Hashtrags(models.Model): 
# class User_hashtags(models.Model): 
# class User_notifications(models.Model): 




