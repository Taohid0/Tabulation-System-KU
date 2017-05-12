'''import unittest
import loginPage
from caltulateResult import *
from disciplineForm import *
from home import *
from  main import *
from marksEntry import *
from newstudentform import *
from registration import *
from registrationConfiguration import *

#def fun():
  #  return 3 + 1

class CalculateResultTest(unittest.TestCase):
    def test(self):
        calculateResultObject = caltulateResult.CalculateResult()
        self.assertEqual(calculateResultObject.calculate(33),(0.0,'F'))


class LoginTest(unittest.TestCase):
    def test(self):
        loginPageObject = loginPage.Login()
        self.assertEqual(loginPageObject.show(),None)

class AddCourseTest(unittest.TestCase):
    def test(self):
        addCourseObject =AddCourse()
        self.assertEqual(addCourseObject.show(),None)

class DisciplineFormTest(unittest.TestCase):
    def test(self):
        disciplineFormObject =DisciplineFormClass()
        self.assertEqual(disciplineFormObject.show(),None)

class home(unittest.TestCase):
    def test(self):
        homeObject = Home()
        self.assertEqual(homeObject.show(),None)

class MarksEntryTest(unittest.TestCase):
    def test(self):
        marksEntryObject =MarksEntry()
        self.assertEqual(marksEntryObject.show(),None)

class NewStudentFormTest(unittest.TestCase):
    def test(self):
        newStudentFormObjec = NewStudentForm()
        self.assertEqual(newStudentFormObjec.show(),None)

class resigtrationTest(unittest.TestCase):
    def test(self):
        registrationObject = Registration()
        self.assertEqual(registrationObject.show(),None)

class registrationConfigurationTest(unittest.TestCase):
    def test(self):
        registrationConfigurationObject = RegistrationConfiguratinClass()
        self.assertEqual(registrationConfigurationObject.show(),None)'''
