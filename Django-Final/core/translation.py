from modeltranslation.translator import translator, TranslationOptions
from .models import Department, Position, Employee

class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)  

class PositionTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Department, DepartmentTranslationOptions)
translator.register(Position, PositionTranslationOptions)