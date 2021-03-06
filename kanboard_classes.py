# Name:         kanboard_classes.py
# Modified by:  Johannes Natunen, Nico Kranni
# Description:  Class file for the main program

import datetime


# Empty list for classes
data=[]

# Main task class, without any special information
class MainTask:

    def __init__(self, ticket_id, deadline, start_date, end_date, worker, description, status):
        self.ticket_id=ticket_id
        self.deadline = deadline
        self.start_date = start_date
        self.end_date = end_date
        self.worker = worker
        self.description = description
        self.status = status
        self.kbpos = 2  # The position where the object is on the kanboard.
        #                 18.04.2022: This no longer seems to be in use.
        data.append(self)

    # Str method 
    def __str__(self):
        return "\nTicket ID: {0}\nStart date is: {1}\nDeadline is: {2}\nEnd Date is: {3}\nWho is doing the ticket: {4}\n".format(self.ticket_id, self.start_date.strftime("%x"), self.deadline, self.end_date, self.worker)

    # Getters and setters for attributes
    
    def get_ticket_id(self): return self.ticket_id
    def set_ticket_id(self, id): self.ticket_id = id

    def get_deadline(self): return self.deadline    
    def set_deadline(self, date): self.deadline = date

    def get_start_date(self): return self.start_date
    
    def get_end_date(self): return self.end_date
    def set_end_date(self, date): self.end_date = date

    def get_worker(self): return self.worker
    def set_worker(self, worker): self.worker = worker

    def get_description(self): return self.description
    def set_description(self, description): self.description = description

    def get_status(self): return self.status
    def set_status(self, status): self.status = status

    def get_kbpos(self): return self.kbpos
    def set_kbpos(self, pos): self.kbpos = pos

    
# Program task class, inherits most of its attributes from the main task class
# but has its own program attribute as well.
class ProgramTask(MainTask):
    def __init__(self, ticket_id, deadline, start_date, end_date, worker, description, status, program):
        super().__init__(ticket_id, deadline, start_date, end_date, worker, description, status)
        self.program=program
        self.kbpos = 2

    # Getters and setters 
    def get_kbpos(self): return self.kbpos
    def set_kbpos(self, pos): self.kbpos = pos    
    
    def get_program(self): return self.program
    def set_program(self, program): self.program = program
    
    # Str method
    def __str__(self):
        st=super().__str__()
        st += 'Program: ' + str(self.program) + "\n"
        return st
