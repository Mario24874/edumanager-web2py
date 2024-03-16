// src/attendance/attendanceController.ts
import { Attendance } from './attendanceModel';
import { AttendanceRepository } from './attendanceRepository';
import { AttendanceRenderer } from './attendanceRenderer';

export class AttendanceController {
    constructor(private repository: AttendanceRepository, private renderer: AttendanceRenderer) {}

    registerAttendance(attendance: Attendance) {
        this.renderer.render(attendance);
        this.repository.registerAttendance(attendance);
    }
}
