# This file defines the StudentRepository class, which contains the methods to perform CRUD (Create, Read, Update, Delete) operations on the subjects table in the database.

class SubjectsRepository:
    def __init__(self, db):
        self.db = db

    def create_subjects(self, subjects):
        return self.db.insert('subjects', **subjects.__dict__)

    def get_subjects(self, id):
        return self.db.select('subjects', where='id=$id', vars={'id': id})

    def update_subjects(self, id, subjects):
        return self.db.update('subjects', where='id=$id', vars={'id': id}, **subjects.__dict__)

    def delete_subjects(self, id):
        return self.db.delete('subjects', where='id=$id', vars={'id': id})
