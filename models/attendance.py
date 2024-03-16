# This file corresponds to the attendance data model.

class Attendance:
    def __init__(self, id, student_id, classrooms_id, subjects_id, date, status):
        self.id = id
        self.student_id = student_id
        self.classrooms_id = classrooms_id
        self.subjects_id = subjects_id
        self.date = date
        self.status = status
