// src/student/studentController.ts
import { Student } from './studentModel';
import { StudentRepository } from './studentRepository';
import { StudentRenderer } from './studentRenderer';

export class StudentController {
    constructor(private repository: StudentRepository, private renderer: StudentRenderer) {}

    registerStudent(student: Student) {
        this.renderer.render(student);
        this.repository.registerStudent(student);
    }
}
