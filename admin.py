from django.contrib import admin
from .models import Skills, User, CareerFields, Career, CareerSkills, FieldSkills, UserSkills, UserInterests

# Register your models here.
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill_ID', 'skill_name', 'skill_type')  # Columns to display


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_ID', 'username', 'user_email')  # Columns to display

@admin.register(CareerFields)
class CareerFieldsAdmin(admin.ModelAdmin):
    list_display = ('careerfield_ID', 'careerfield_name')  # Columns to display

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('career_ID', 'career_name', 'careerfield_ID')  # Columns to display

@admin.register(CareerSkills)
class CareerSkillsAdmin(admin.ModelAdmin):
    list_display = ('careerskill_ID', 'career_ID', 'skill_ID', 'yearsExperience_recommended')  # Columns to display

@admin.register(FieldSkills)
class FieldSkillsAdmin(admin.ModelAdmin):
    list_display = ('fieldskill_ID', 'careerfield_ID', 'skill_ID')  # Columns to display

@admin.register(UserSkills)
class UserSkillsAdmin(admin.ModelAdmin):
    list_display = ('userskill_ID', 'user_ID', 'skill_ID', 'years_experience')  # Columns to display

@admin.register(UserInterests)
class UserInterestsAdmin(admin.ModelAdmin):
    list_display = ('userinterest_ID', 'user_ID', 'career_ID')  # Columns to display