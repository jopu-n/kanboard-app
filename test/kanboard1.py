import itertools, datetime, json, pickle

# Empty list for classes
data=[]
class MainTask:

    newid = itertools.count()

    def __init__(self, deadline, end_date, worker):
        self.ticket_id = next(MainTask.newid)
        self.deadline = deadline
        self.start_date = datetime.datetime.now()
        self.end_date = end_date
        self.worker = worker
        self.kbpos = 1 # The position where the object is on the kanboard.
        data.append(self)
    def __str__(self):
        return "\nTicket ID: {0}\nStart date is: {1}\nDeadline is: {2}\nEnd Date is: {3}\nWho is doing the ticket: {4}\n".format(self.ticket_id, self.start_date.strftime("%x"), self.deadline, self.end_date, self.worker)

    def get_ticket_id(self): return self.ticket_id
    def set_ticket_id(self, id): self.ticket_id = id

    def get_deadline(self): return self.deadline    
    def set_deadline(self, date): self.deadline = date

    def get_start_date(self): return self.start_date
    
    def get_end_date(self): return self.end_date
    def set_end_date(self, date): self.end_date = date

    def get_worker(self): return self.worker
    def set_worker(self, worker): self.worker = worker

    def get_kbpos(self): return self.kbpos
    def set_kbpos(self, pos): self.kbpos = pos

    

class ProgramTask(MainTask):
    def __init__(self, deadline, end_date, worker, program):
        super().__init__(deadline, end_date, worker)
        self.program=program
        self.kbpos = 1

    def get_kbpos(self): return self.kbpos
    def set_kbpos(self, pos): self.kbpos = pos    
    
    def get_program(self): return self.program
    def set_program(self, program): self.program = program
    
    def __str__(self):
        st=super().__str__()
        st += 'Program: ' + str(self.program) + "\n"
        return st

class TaskCounter:
    def __init__(self):
        self.pr_task_count = 0
        self.main_task_count = 0

    def get_pr_task_count(self): return self.pr_task_count
    def set_pr_task_count(self, num): self.pr_task_count = num

    def get_main_task_count(self): return self.main_task_count
    def set_main_task_count(self, num): self.main_task_count = num