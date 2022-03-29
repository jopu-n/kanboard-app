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
        data.append(self)
    def __str__(self):
        return "\nTicket ID: {0}\nStart date is: {1}\nDeadline is: {2}\nEnd Date is: {3}\nWho is doing the ticket: {4}\n".format(self.ticket_id, self.start_date.strftime("%x"), self.deadline, self.end_date, self.worker)

    def set_deadline(self, date):
        "Manually set deadline"
        self.deadline = date

    def set_ticketid(self, id):
        """Manually set ticket_id"""
        self.ticket_id = id

class ProgramTask(MainTask):
    def __init__(self, deadline, end_date, worker, program):
        super().__init__(deadline, end_date, worker)
        self.program=program
        
    def __str__(self):
        st=super().__str__()
        st += 'Program: ' + str(self.program) + "\n"
        return st

