// src/classroom/classroomController.ts
import { Classrooms } from './classroomsModel';
import { ClassroomsRepository } from './classroomsRepository';
import { ClassroomsRenderer } from './classroomsRenderer';

export class ClassroomsController {
    constructor(private repository: ClassroomsRepository, private renderer: ClassroomsRenderer) {}

    createClassrooms(classrooms: Classrooms) {
        this.renderer.render(classrooms);
        this.repository.createClassrooms(classrooms);
    }
}