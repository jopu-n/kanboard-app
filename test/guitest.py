import itertools,datetime, tkinter
from re import M


class MainTask:

    newid = itertools.count()

    def __init__(self, deadline, end_date, worker):
        self.ticket_id = next(MainTask.newid)
        self.deadline = deadline
        self.start_date = datetime.datetime.now()
        self.end_date = end_date
        self.worker = worker

    def __str__(self):
        return "\nTicket ID: {0}\nStart date is: {1}\nDeadline is: {2}\nEnd Date is: {3}\nWho is doing the ticket: {4}\n".format(self.ticket_id, self.start_date.strftime("%x"), self.deadline, self.end_date, self.worker)

    def set_deadline(self, date):
        self.deadline = date

    def set_ticketid(self, id):
        self.ticket_id = id

def app():
    test = MainTask("Tomorrow", "Yesterday", "nico")
    test2 = MainTask("Never","Never","Jope")
    test3 = MainTask("1.4.2022", "I dont know","A Slave")
    window = tkinter.Tk()
    window.geometry("500x350")
    tkinter.Label(window, text="test123",borderwidth=1).grid(row=0,column=0)
    x = 1
    for ticket in [test, test2, test3]:
        info = (
            "Ticket ID: " + str(ticket.ticket_id),
            "Deadline: " + ticket.deadline, 
            "Start Date: " + str(ticket.start_date.strftime("%x")), 
            "End Date: " + ticket.end_date, 
            "Worker: " + ticket.worker
            )
        info_var = tkinter.StringVar(value=info)

        listbox = tkinter.Listbox(
            window,
            listvariable=info_var,
            height=6,
            width=30,
            selectmode="extended"
        )
        listbox.grid(
            column=0,
            row=x,
            padx=10,
            pady=10
        )
        x += 1 
    window.mainloop()

app()
