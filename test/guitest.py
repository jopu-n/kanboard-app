# Name:         guitest.py
# Modified by:  Johannes Natunen, Nico Kranni
# Description:  A "GUI test" program, though it has turned into the main program file at this point.

import tkinter as tk
import save
import kanboard1 as kb

# Main app function for the Kanboard application
def app():
    items = save.load_all("pickle.dat") # Loads tickets from pickle.dat file, if no file, creates it
    counter = kb.TaskCounter()
    window = tk.Tk()
    window.geometry("1280x720")
    window.resizable(False, False)
    window.title("Kanboard")
    tk.Label(window, text="MAIN TASKS",borderwidth=1).grid(row=1,column=0)
    tk.Label(window, text="PROGRAM TASKS",borderwidth=1).grid(row=1,column=1)
    
    
    for item in items: # Seems like pickle objects have the real objects inside them
        for ticket in item: # Thus, we have to loop two times
            add_ticket(window, counter, ticket)
            print("ID: ",ticket.ticket_id)
            print("Row: ",ticket.kbpos,"\n")

        # Replaces list of classes with new list
        kb.data=item
        

    # Button that creates a pop up window for creating a new ticket
    def new_ticket():
        top = tk.Toplevel()
        top.title("New Ticket")
        deadline_var = tk.StringVar()
        end_date_var = tk.StringVar()
        worker_var = tk.StringVar()

        # Submit button inside the pop up window
        def submit():
            deadline = deadline_var.get()
            end_date = end_date_var.get()
            worker = worker_var.get()

            ticket = kb.MainTask(deadline, end_date, worker)
            add_ticket(window,counter,ticket)
            print(ticket.kbpos,"\n")

            deadline_var.set("")
            end_date_var.set("")
            worker_var.set("")
            save.save_all()


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

    # The actual button that appears in the main window
    new_entry_btn = tk.Button(window, text="New Ticket", bg="orange", command=new_ticket)
    new_entry_btn.grid(row=0, column=0,columnspan=1)
    new_entry_btn.config(width=20)

    # Button that saves changes to pickle.dat file
    save_btn = tk.Button(window, text="Plz Save", bg="lightgreen", command=save.save_all)
    save_btn.grid(row=0, column=1, columnspan=2)
    save_btn.config(width=20)

    window.mainloop()

# Function to add a new ticket. 
def add_ticket(window, counter, ticket):
    info = (
        f"""\
        Ticket id: {str(ticket.ticket_id)}\
        \n  Deadline: {ticket.deadline}\
        \n  Start date: {str(ticket.start_date.strftime("%x"))}\
        \n  End date: {ticket.end_date}\
        \n  Worker: {ticket.worker}\
        """
    )

    button = tk.Button(
        window,
        text=info,
        command=lambda x=ticket: show_info(x), # Calls the show_info command when clicked
        bg="lightgray",
        height=6,
        width=20,
    )
    button.grid(
        column=check_ticket_type(ticket, counter),
        row=ticket.get_kbpos(),
        padx=10,
        pady=10
    )

# Function that shows a ticket's info in a new window. 
# WIP: The object's status will be changeable in this window.
def show_info(ticket):
    top = tk.Toplevel()
    top.title("Information")
    top.geometry("300x200")
    text = (
        f""" \
        \n  Ticket id: {str(ticket.ticket_id)}\
        \n  Deadline: {ticket.deadline}\
        \n  Start date: {str(ticket.start_date.strftime("%x"))}\
        \n  End date: {ticket.end_date}\
        \n  Worker: {ticket.worker}\
        """
    )
    text_box = tk.Text(top)
    text_box.pack(expand=True)
    text_box.insert("end", text)
    text_box.config(state="disabled")


# Function that checks what the ticket type is, and also assigns the tickets their place in the main window
# WIP: This will be reworked soon as tickets will not be grouped by object types but rather their status
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
