import tkinter, pickle
import kanboard1 as kb

def app():
    items = get_items()
    counter = kb.TaskCounter()
    window = tkinter.Tk()
    window.geometry("1280x720")
    tkinter.Label(window, text="MAIN TASKS",borderwidth=1).grid(row=0,column=0)
    tkinter.Label(window, text="PROGRAM TASKS",borderwidth=1).grid(row=0,column=1)
    for item in items: # Seems like pickle objects have the real objects inside them
        for ticket in item: # Thus, we have to loop two times
            add_ticket(window, counter, ticket)
    window.mainloop()

def add_ticket(window, counter, ticket):
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
        column=check_ticket_type(ticket, counter),
        row=ticket.get_kbpos(),
        padx=10,
        pady=10
    )

def get_items():

    test = kb.MainTask("Tomorrow", "Yesterday","Nico")
    test2 = kb.ProgramTask("Tomorrow","Yesterday","Nico","Facebook")

    test3 = kb.MainTask("Tomorrow", "Yesterday","Nico")
    test4 = kb.ProgramTask("Tomorrow","Yesterday","Nico","Facebook")
    tes = kb.MainTask("Tomorrow", "Yesterday","Nico")
    test5 = kb.ProgramTask("Tomorrow","Yesterday","Nico","Facebook")

    PIK="pickle.dat"

    # We dump data list which includes classes to pickle.dat
    with open(PIK,"wb") as f:
        pickle.dump(kb.data,f)

    # Loads everything from pickle.dat
    def loadall(filename):
        with open(filename, "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

    items = loadall("pickle.dat")
    return items


def check_ticket_type(obj, counter):
    if isinstance(obj, kb.ProgramTask):
        obj.set_kbpos(obj.get_kbpos() + counter.get_pr_task_count())
        counter.set_pr_task_count(counter.get_pr_task_count() + 1)
        return 1
    elif isinstance(obj, kb.MainTask): 
        obj.set_kbpos(obj.get_kbpos() + counter.get_main_task_count())
        counter.set_main_task_count(counter.get_main_task_count() + 1)
        return 0
    else: return 2

app()
