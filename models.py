from django.db import models

# Create your models here.

class Skills(models.Model):
    skill_ID = models.AutoField(primary_key=True)  # Primary Key, INT
    skill_name = models.CharField(max_length=255, unique=True)  # TEXT, UNIQUE
    skill_description = models.TextField()  # TEXT
    skill_type = models.IntegerField()  # INT

    def __str__(self):
        return self.skill_name  # A readable string representation of the object


class User(models.Model):
    user_ID = models.AutoField(primary_key=True)  # Primary Key, INT
    username = models.CharField(max_length=150, unique=True)  # TEXT, UNIQUE
    user_password = models.CharField(max_length=255)  # TEXT (hashed password recommended)
    user_email = models.EmailField(unique=True)  # TEXT, ensures valid email format

    def __str__(self):
        return self.username  # Readable string representation
    
from django.db import models

class CareerFields(models.Model):
    careerfield_ID = models.AutoField(primary_key=True)  # Primary Key, INT
    careerfield_name = models.CharField(max_length=255, unique=True)  # TEXT, UNIQUE

    def __str__(self):
        return self.careerfield_name  # Readable string representation
    

class Career(models.Model):
    career_ID = models.AutoField(primary_key=True)  # Primary Key, INT
    career_name = models.CharField(max_length=255, unique=True)  # TEXT, UNIQUE
    careerfield_ID = models.ForeignKey(
        'CareerFields',  # Refers to the CareerFields model
        on_delete=models.CASCADE,  # Deletes related careers if a careerfield is deleted
        related_name='careers'  # Enables reverse lookup from CareerFields to Career
    )

    def __str__(self):
        return self.career_name  # Readable string representation
    
class CareerSkills(models.Model):
    careerskill_ID = models.AutoField(primary_key=True)  # Primary Key, INT
    career_ID = models.ForeignKey(
        'Career',  # Refers to the Career model
        on_delete=models.CASCADE,  # Deletes related CareerSkills if a Career is deleted
        related_name='career_skills'  # Enables reverse lookup from Career to CareerSkills
    )
    skill_ID = models.ForeignKey(
        'Skills',  # Refers to the Skills model
        on_delete=models.CASCADE,  # Deletes related CareerSkills if a Skill is deleted
        related_name='skill_careers'  # Enables reverse lookup from Skills to CareerSkills
    )
    yearsExperience_recommended = models.IntegerField()

    def __str__(self):
        return f"{self.career_ID.career_name} - {self.skill_ID.skill_name}"  # Readable string representation
    


class FieldSkills(models.Model):
    fieldskill_ID = models.AutoField(primary_key=True)  # Primary Key, INT
    careerfield_ID = models.ForeignKey(
        'CareerFields',  # Refers to the CareerFields model
        on_delete=models.CASCADE,  # Deletes related FieldSkills if a CareerField is deleted
        related_name='field_skills'  # Enables reverse lookup from CareerFields to FieldSkills
    )
    skill_ID = models.ForeignKey(
        'Skills',  # Refers to the Skills model
        on_delete=models.CASCADE,  # Deletes related FieldSkills if a Skill is deleted
        related_name='skill_fields'  # Enables reverse lookup from Skills to FieldSkills
    )

    def __str__(self):
        return f"{self.careerfield_ID.careerfield_name} - {self.skill_ID.skill_name}"  # Readable string representation


class UserSkills(models.Model):
    userskill_ID = models.AutoField(primary_key=True)  # Primary Key, INT
    user_ID = models.ForeignKey(
        'User',  # Refers to the User model
        on_delete=models.CASCADE,  # Deletes related UserSkills if a User is deleted
        related_name='user_skills'  # Enables reverse lookup from User to UserSkills
    )
    skill_ID = models.ForeignKey(
        'Skills',  # Refers to the Skills model
        on_delete=models.CASCADE,  # Deletes related UserSkills if a Skill is deleted
        related_name='skill_users'  # Enables reverse lookup from Skills to UserSkills
    )
    years_experience = models.IntegerField()  # INT, for storing years of experience

    def __str__(self):
        return f"{self.user_ID.username} - {self.skill_ID.skill_name} ({self.years_experience} years)"
    


class UserInterests(models.Model):
    userinterest_ID = models.AutoField(primary_key=True)  # Primary Key, INT
    user_ID = models.ForeignKey(
        'User',  # Refers to the User model
        on_delete=models.CASCADE,  # Deletes related UserInterests if a User is deleted
        related_name='user_interests'  # Enables reverse lookup from User to UserInterests
    )
    career_ID = models.ForeignKey(
        'Career',  # Refers to the Career model
        on_delete=models.CASCADE,  # Deletes related UserInterests if a Career is deleted
        related_name='career_interests'  # Enables reverse lookup from Career to UserInterests
    )

    def __str__(self):
        return f"{self.user_ID.username} - {self.career_ID.career_name}"  # Readable string representation