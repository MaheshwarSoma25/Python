from abc import ABC,abstractmethod 

class person(ABC):
    def _init_(self,name,age):
        self.name=name 
        self.age=age 
    
    @abstractmethod 
    def role(self):
        pass 

class student(person):
    def _init_(self,student_id,name,age):
        super()._init_(name,age)
        self.student_id=student_id
        self.__list_of_student_enrolled_courses=[]
    def role(self):
        print('student')
    def enroll_in_course(self,course_name):
        if(course_name in (self.__list_of_student_enrolled_courses)):
            print("student already registered in this course")
        else:
            (self.__list_of_student_enrolled_courses).append(course_name)
    def display_list_of_student_enrolled_courses(self):
        print(self.name,"enrolled courses: ",self.__list_of_student_enrolled_courses)

class teacher(person):
    def _init_(self,teacher_id,name,age):
        super()._init_(name,age)
        self.teacher_id=teacher_id
        self.__list_of_teacher_enrolled_courses=[]
    def role(self):
        print('teacher')
    def enroll_in_course(self,course_name):
        if(course_name in (self.__list_of_teacher_enrolled_courses)):
            print("teacher already assigned to this course")
        else:
            (self.__list_of_teacher_enrolled_courses).append(course_name)
    def display_list_of_teacher_enrolled_courses(self):
        print(self.name,"enrolled courses: ",self.__list_of_teacher_enrolled_courses) 

class course:
    def _init_(self,course_name,course_code):
        self.course_name=course_name 
        self.course_code=course_code 
        self.teacher=""
        self.__list_students_in_course=[]
    def set_teacher(self,teacher_name):
        self.teacher=teacher_name  
    def enroll_student(self,student_name):
        (self.__list_students_in_course).append(student_name)
    def display_course_info(self):
        print(self.course_name)
        print(self.course_code)
        if(self.teacher != ""):
            print(self.teacher)
        print(self.__list_students_in_course)

class department:
    def _init_(self,dept_name):
        self.department_name=dept_name 
        self.__list_of_courses_in_department=[]
        self.__list_of_teachers_in_department=[]
        self.__list_of_students_in_department=[]
    def add_course(self,course_name):
        (self.__list_of_courses_in_department).append(course_name)
    def add_teacher(self,teacher_name):
        (self.__list_of_teachers_in_department).append(teacher_name)
    def add_student(self,student_name):
        (self.__list_of_students_in_department).append(student_name)
    def display_department_info(self):
        print("department name: ",self.department_name)
        print("list of courses in department: ",self.__list_of_courses_in_department)
        print("list of teachers in department: ",self.__list_of_teachers_in_department)
        print("list of students in department: ",self.__list_of_students_in_department)

class administration:
    def _init_(self):
        self.__list_of_departments_in_administration=[]
    def add_department(self,dept_name):
        (self.__list_of_departments_in_administration).append(dept_name)
    def display_administration_info(self):
        print(self.__list_of_departments_in_administration) 


dp1=department("computer science")
dp1.add_course("data structures")
dp1.add_course("algorithms")
dp1.add_teacher("alice")
dp1.add_teacher("bob")
dp1.add_student("john")
dp1.add_student("jane")
dp1.display_department_info()
t1=teacher("too1","alice",25,)
t1.enroll_in_course("data structures")
t2=teacher("t002","bob",30)
t2.enroll_in_course("algorithms")
s1=student("s001","john",18)
s1.enroll_in_course("data structures")
s1.enroll_in_course("algorithms")
s2=student("s002","jane",20)
s2.enroll_in_course("data structures")
s2.enroll_in_course("algorithms")
t1.display_list_of_teacher_enrolled_courses()
t2.display_list_of_teacher_enrolled_courses()
s1.display_list_of_student_enrolled_courses()
s2.display_list_of_student_enrolled_courses()