import tkinter as tk
import pickle
import kanboard1 as kb

def app():
    items = get_items()
    counter = kb.TaskCounter()
    window = tk.Tk()
    window.geometry("1280x720")
    window.title("Kanboard")
    tk.Label(window, text="MAIN TASKS",borderwidth=1).grid(row=0,column=0)
    tk.Label(window, text="PROGRAM TASKS",borderwidth=1).grid(row=0,column=1)
    

    for item in items: # Seems like pickle objects have the real objects inside them
        for ticket in item: # Thus, we have to loop two times
            add_ticket(window, counter, ticket)

    def new_ticket():
        top = tk.Toplevel()
        top.title("New Ticket")
        deadline_var = tk.StringVar()
        end_date_var = tk.StringVar()
        worker_var = tk.StringVar()

        def submit():
            deadline = deadline_var.get()
            end_date = end_date_var.get()
            worker = worker_var.get()

            ticket = kb.MainTask(deadline, end_date, worker)
            add_ticket(window,counter,ticket)

            deadline_var.set("")
            end_date_var.set("")
            worker_var.set("")

        deadline_label = tk.Label(top, text="Deadline: ")
        deadline_entry = tk.Entry(top, textvariable=deadline_var)

        end_date_label = tk.Label(top, text="End date: ")
        end_date_entry = tk.Entry(top, textvariable=end_date_var)

        worker_label = tk.Label(top, text="Worker: ")
        worker_entry = tk.Entry(top, textvariable=worker_var)

        submit_btn = tk.Button(top, text = "Submit", command=submit)

        deadline_label.grid(row=0,column=0)
        deadline_entry.grid(row=0,column=1)
        end_date_label.grid(row=1,column=0)
        end_date_entry.grid(row=1,column=1)
        worker_label.grid(row=2,column=0)
        worker_entry.grid(row=2,column=1)
        submit_btn.grid(row=3,column=0)




    new_entry_btn = tk.Button(window, text="New Ticket", command=new_ticket)
    row, column = window.grid_size()
    new_entry_btn.grid(row=row, column=column)

    

    window.mainloop()

def add_ticket(window, counter, ticket):
    info = (
            "Ticket ID: " + str(ticket.ticket_id),
            "Deadline: " + ticket.deadline, 
            "Start Date: " + str(ticket.start_date.strftime("%x")), 
            "End Date: " + ticket.end_date, 
            "Worker: " + ticket.worker
        )
    info_var = tk.StringVar(value=info)

    listbox = tk.Listbox(
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
