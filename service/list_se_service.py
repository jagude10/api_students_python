from model.student import Student
from model.list_se import ListSE

class ListSEService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']

    def __init__(self):
        self.students = ListSE()
       # #carloaiza = Student("363763763", 1, 5000000,True, "Carlos Loaiza",self.cities[2])
        #carloaiza = Student({"idenfication":"75147236","name":"Carlos Loaiza",
                  #           "gender":1,"salary":2000000,"job":True,"city":self.cities[2]})
        #self.students.add(carloaiza)
        #self.students.add(Student({"idenfication": "1060456789",
           #                        "name": "Valentina Hurtado",
          #                         "gender":2, "salary":0,"job":False,
            #                       "city":self.cities[0]}))

    def get_all_students(self):
        return self.students.head

    def add_student(self,data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add(student)

        else:
            raise Exception("la ciudad ingresada no es valida")

    def add_student(self,data):
        student = Student(data)

    def get_all_linked(self):
        return self.list.head

    def invert(self):
        if self.list.head == None:
            return {"message":"La lista está vacía"}
        else:
            self.list.invert()
            return {"message": "Se ha invertido la lista"}

    def add(self,data,dict):
        self.list.add(data(dict))
        return {"message":"Adicionado con éxito"}

    def add_to_start(self,dict,data):
        self.list.add_to_start(data(dict))
        return {"message":"Adicionado con éxito"}

    def add_to_position(self,position,dict,data):
        try:
            self.list.add_to_position(position,data(dict))
            return {"message":"Adicionado con éxito"}
        except Exception as e:
            return {"message": str(e)}

    def delete_for_multiplo(self, p):
        self.students.delete_multiplo(p)
        return {"mesagge": "no existen datos " }
