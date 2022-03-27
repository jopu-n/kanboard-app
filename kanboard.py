import itertools
import datetime



class MainTask:
    newid = itertools.count()
    def __init__(self, deadline, endDate, worker):
        self.ticketID = next(MainTask.newid)     
        self.deadline=deadline
        self.startDate=datetime.datetime.now()
        self.endDate=endDate
        self.worker=worker
        
    def __str__(self):
        return "\nTicket ID: {0}\nStart date is: {1}\nDeadline is: {2}\nEnd Date is: {3}\nWho is doing the ticket: {4}\n".format(self.ticketID, self.startDate.strftime("%x"), self.deadline, self.endDate, self.worker)

    def set_deadline (self, date):        
        self.deadline=date
    
    def set_ticketID(self, ID):
        self.ticketID=ID


test=MainTask("Tomorrow","Yesterday", "nico")

print(test)