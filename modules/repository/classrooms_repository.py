# This file defines the StudentRepository class, which contains the methods to perform CRUD (Create, Read, Update, Delete) operations on the classrooms table in the database.

class ClassroomRepository:
    def __init__(self, db):
        self.db = db

    def create_classrooms(self, classrooms):
        return self.db.insert('classrooms', **classrooms.__dict__)

    def get_classroom(self, id):
        return self.db.select('classrooms', where='id=$id', vars={'id': id})

    def update_classrooms(self, id, classrooms):
        return self.db.update('classrooms', where='id=$id', vars={'id': id}, **classrooms.__dict__)

    def delete_classrooms(self, id):
        return self.db.delete('classrooms', where='id=$id', vars={'id': id})
