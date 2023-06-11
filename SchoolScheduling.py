from gurobipy import *

class SchoolScheduling:
    def __init__(self, days, periods, courses, teachers, classrooms):
        self.days = days
        self.periods = periods
        self.courses = courses
        self.teachers = teachers
        self.classrooms = classrooms
        self.m = Model("school_scheduling")

    def optimization(self):
        # Add variables
        x = self.m.addVars(self.days, self.periods, range(len(self.courses)), range(len(self.teachers)), range(len(self.classrooms)), vtype=GRB.BINARY, name="x")

        # Set objective function
        self.m.setObjective(quicksum(x[day, period, course, teacher, classroom] for day in self.days for period in self.periods for course in range(len(self.courses)) for teacher in range(len(self.teachers)) for classroom in range(len(self.classrooms))), GRB.MAXIMIZE)

        # Add constraints
        for course in range(len(self.courses)):
            for classroom in range(len(self.classrooms)):
                if self.courses[course]['grade'] == self.classrooms[classroom]['grade']:
                    self.m.addConstr(quicksum(x[day, period, course, teacher, classroom] for day in self.days for period in self.periods for teacher in range(len(self.teachers))) == self.courses[course]['frequency'])

        for day in self.days:
            for period in self.periods:
                for classroom in range(len(self.classrooms)):
                    self.m.addConstr(quicksum(x[day, period, course, teacher, classroom] for course in range(len(self.courses)) for teacher in range(len(self.teachers))) <= 1)

        for day in self.days:
            for period in self.periods:
                for teacher in range(len(self.teachers)):
                    self.m.addConstr(quicksum(x[day, period, course, teacher, classroom] for course in range(len(self.courses)) for classroom in range(len(self.classrooms))) <= 1)

        for course in range(len(self.courses)):
            for teacher in range(len(self.teachers)):
                if self.courses[course]['major'] != self.teachers[teacher]['major']:
                    for day in self.days:
                        for period in self.periods:
                            for classroom in range(len(self.classrooms)):
                                self.m.addConstr(x[day, period, course, teacher, classroom] == 0)

        for course in range(len(self.courses)):
            for day in self.days:
                for classroom in range(len(self.classrooms)):
                    self.m.addConstr(quicksum(x[day, period, course, teacher, classroom] for period in self.periods for teacher in range(len(self.teachers))) <= 2)

        self.m.optimize()

    def print_results(self):
        if self.m.status == GRB.OPTIMAL:
            for classroom in range(len(self.classrooms)):
                print(f"\nClassroom {self.classrooms[classroom]['classroom_id']}, Grade {self.classrooms[classroom]['grade']}:")
                for day in self.days:
                    for period in self.periods:
                        for course in range(len(self.courses)):
                            for teacher in range(len(self.teachers)):
                                if self.m.getVarByName(f"x[{day},{period},{course},{teacher},{classroom}]").x > 0.5:  # if this class is scheduled
                                    print(f"Day {day}, Period {period}: Course {self.courses[course]['course_id']} by Teacher {self.teachers[teacher]['teacher_id']}")

