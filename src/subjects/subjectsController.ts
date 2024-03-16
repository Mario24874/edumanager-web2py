// src/subject/subjectController.ts
import { Subjects } from './subjectsModel';
import { SubjectsRepository } from './subjectsRepository';
import { SubjectsRenderer } from './subjectsRenderer';

export class SubjectsController {
    constructor(private repository: SubjectsRepository, private renderer: SubjectsRenderer) {}

    createSubjects(subjects: Subjects) {
        this.renderer.render(subjects);
        this.repository.createSubjects(subjects);
    }
}
