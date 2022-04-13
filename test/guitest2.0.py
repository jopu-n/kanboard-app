import tkinter as tk
import save
import kanboard1 as kb
def app():
    root = tk.Tk()
    root.grid_rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.geometry("900x600")
    root.resizable(False, False)
    root.title("Kanboard")
    items = save.load_all("pickle.dat") # Loads tickets from pickle.dat file, if no file, creates it

    frame_main = tk.Frame(root, bg="lightgray")
    frame_main.grid(sticky='news')

    def new_ticket():
        top = tk.Toplevel()
        top.geometry("250x150")
        top.title("New Ticket")
        deadline_var = tk.StringVar()
        end_date_var = tk.StringVar()
        worker_var = tk.StringVar()
        description_var = tk.StringVar()
        
        # Dropdown settings for status
        status_var = tk.StringVar()
        list_status = ["Yet to start","In progress","Done"]
        status_var.set(list_status[0])

        # Submit button inside the pop up window
        def submit():
            deadline = deadline_var.get()
            end_date = end_date_var.get()
            worker = worker_var.get()
            description = description_var.get()
            status = list_status.index(status_var.get())

            ticket = kb.MainTask(deadline, end_date, worker, description, status)
            add_ticket(frame_buttons1,ticket)
            print("Row",ticket.kbpos)
            print("Column",ticket.status)


            deadline_var.set("")
            end_date_var.set("")
            worker_var.set("")
            description_var.set("")
            status_var.set(list_status[0])
            save.save_all()
            


        deadline_label = tk.Label(top, text="Deadline: ")
        deadline_entry = tk.Entry(top, textvariable=deadline_var)

        end_date_label = tk.Label(top, text="End date: ")
        end_date_entry = tk.Entry(top, textvariable=end_date_var)

        worker_label = tk.Label(top, text="Worker: ")
        worker_entry = tk.Entry(top, textvariable=worker_var)

        description_label = tk.Label(top, text="Description: ")
        description_entry = tk.Entry(top, textvariable=description_var)

        # Dropdown box with status settings
        status_label = tk.Label(top, text="Status: ")
        status_menu = tk.OptionMenu(top, status_var, *list_status)
        

        submit_btn = tk.Button(top, text = "Submit", command=submit)

        deadline_label.grid(row=0,column=0)
        deadline_entry.grid(row=0,column=1)
        end_date_label.grid(row=1,column=0)
        end_date_entry.grid(row=1,column=1)
        worker_label.grid(row=2,column=0)
        worker_entry.grid(row=2,column=1)
        description_label.grid(row=3,column=0)
        description_entry.grid(row=3,column=1)
        status_label.grid(row=4,column=0)
        status_menu.grid(row=4,column=1)
        submit_btn.grid(row=5,column=0)
        
    def remove_ticket():
        top = tk.Toplevel()
        top.title("Remove Ticket")
        remove_var = tk.StringVar()

        # Remove button inside the pop up window
        def delete():
            remove = remove_var.get()
            for i in kb.data:
                if i.ticket_id == int(remove):
                    print("Die!")
                    print(i.ticket_id)
                    print(remove)
                    # There's some kind of bug in this, sometimes does not recognize items by id.
                    frame_buttons1.grid_slaves(row=i.get_kbpos(), column=i.get_status())[0].destroy()
                    kb.data.remove(i)
                    

            remove_var.set("")

        remove_label = tk.Label(top, text="Remove: ")
        remove_entry = tk.Entry(top, textvariable=remove_var)

        remove_btn = tk.Button(top, text = "Delete", command=delete)
        check_status()
        remove_label.grid(row=0,column=0)
        remove_entry.grid(row=0,column=1)

        remove_btn.grid(row=3,column=0)


      # The actual button that appears in the main window
    new_entry_btn = tk.Button(frame_main, text="New Ticket", bg="orange", command=new_ticket)
    new_entry_btn.grid(row=0, column=0,padx=10,pady=10)
    new_entry_btn.config(width=20)

    # Button that saves changes to pickle.dat file
    save_btn = tk.Button(frame_main, text="Plz Save", bg="lightgreen", command=save.save_all)
    save_btn.grid(row=0, column=1,padx=10,pady=10)
    save_btn.config(width=20)

    # Button that removes ticket from pickle.dat file
    remove_ticket_btn = tk.Button(frame_main, text="Remove", bg="red", command=remove_ticket)
    remove_ticket_btn.grid(row=0, column=2,padx=10,pady=10)
    remove_ticket_btn.config(width=20)


    label1 = tk.Label(frame_main, text="UNCOMPLETED", fg="green")
    label1.grid(row=1, column=0, padx=10,pady=10, sticky='nw')
    label1.config(width=20)

    label2 = tk.Label(frame_main, text="In Progress", fg="blue")
    label2.grid(row=1, column=1, padx=10,pady=10, sticky='nw')
    label2.config(width=20)

    label3 = tk.Label(frame_main, text="Completed", fg="red")
    label3.grid(row=1, column=2, padx=10,pady=10, sticky='nw')
    label3.config(width=20)

    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas1 = tk.Frame(frame_main)
    frame_canvas1.grid(row=2, column=0, padx=(5, 0), sticky='nw')
    frame_canvas1.grid_rowconfigure(0, weight=1)
    frame_canvas1.grid_columnconfigure(0, weight=1)
    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
    frame_canvas1.grid_propagate(False)


    # Add a canvas in that frame
    canvas1 = tk.Canvas(frame_canvas1, bg="yellow")
    canvas1.grid(row=0, column=0, sticky="news")


    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas2 = tk.Frame(frame_main)
    frame_canvas2.grid(row=2, column=1, padx=(5, 0), sticky='nw')
    frame_canvas2.grid_rowconfigure(0, weight=1)
    frame_canvas2.grid_columnconfigure(0, weight=1)
    frame_canvas2.grid_propagate(False)

    # Add a canvas in that frame
    canvas2 = tk.Canvas(frame_canvas2, bg="red")
    canvas2.grid(row=0, column=1, sticky="news")

    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas3 = tk.Frame(frame_main)
    frame_canvas3.grid(row=2, column=2, padx=(5, 0), sticky='nw')
    frame_canvas3.grid_rowconfigure(0, weight=1)
    frame_canvas3.grid_columnconfigure(0, weight=1)
    frame_canvas3.grid_propagate(False)

    # Add a canvas in that frame
    canvas3 = tk.Canvas(frame_canvas3, bg="lightgreen")
    canvas3.grid(row=0, column=2, sticky="news")


    # Link a scrollbar to the canvas
    vsb1 = tk.Scrollbar(frame_canvas1, orient="vertical", command=canvas1.yview)
    vsb1.grid(row=0, column=1, sticky='ns')
    canvas1.configure(yscrollcommand=vsb1.set)

    # Link a scrollbar to the canvas
    vsb2 = tk.Scrollbar(frame_canvas2, orient="vertical", command=canvas2.yview)
    vsb2.grid(row=0, column=1, sticky='ns')
    canvas2.configure(yscrollcommand=vsb2.set)

    # Link a scrollbar to the canvas
    vsb3 = tk.Scrollbar(frame_canvas3, orient="vertical", command=canvas3.yview)
    vsb3.grid(row=0, column=2, sticky='ns')
    canvas3.configure(yscrollcommand=vsb3.set)

    # Create a frame to contain the buttons
    frame_buttons1 = tk.Frame(canvas1, bg="red")
    canvas1.create_window((0, 0), window=frame_buttons1, anchor='nw')

    frame_buttons2 = tk.Frame(canvas2, bg="yellow")
    canvas2.create_window((0, 0), window=frame_buttons2, anchor='nw')

    frame_buttons3 = tk.Frame(canvas3, bg="green")
    canvas3.create_window((0, 0), window=frame_buttons3, anchor='nw')



    def add_ticket(frame_buttons1,ticket):
        try:
            info = (
                f"""\
                Ticket id: {str(ticket.ticket_id)}\
                \n  Deadline: {ticket.deadline}\
                \n  Start date: {str(ticket.start_date.strftime("%x"))}\
                \n  End date: {ticket.end_date}\
                \n  Worker: {ticket.worker}\
                \n  Program: {ticket.program}\
                """
            )
        except AttributeError:
            info = (
            f"""\
            Ticket id: {str(ticket.get_ticket_id())}\
            \n  Deadline: {ticket.get_deadline()}\
            \n  Start date: {str(ticket.get_start_date().strftime("%x"))}\
            \n  End date: {ticket.get_end_date()}\
            \n  Worker: {ticket.get_worker()}\
            """
        )
        button = tk.Button(
            frame_buttons1,
            text=info,
            command=lambda x=ticket: show_info(x), # Calls the show_info command when clicked
            bg="lightgray",
            height=6,
            width=20,
        )
        check_status()
        button.grid(
            column=0,
            row=ticket.get_kbpos(),
            padx=10,
            pady=10
        )

    teksti=("Hölöm")
    nappula=tk.Button(frame_buttons3, text=teksti, bg="pink",height=6,width=20)
    nappula.grid(
        column=1,
        row=1,
        padx=10,
        pady=10
    )

    nappula1=tk.Button(frame_buttons2, text=teksti, bg="pink",height=6,width=20)
    nappula1.grid(
        column=1,
        row=1,
        padx=10,
        pady=10
    )


    # Add 9-by-5 buttons to the frame
    for item in items: # Seems like pickle objects have the real objects inside them
        for ticket in item: # Thus, we have to loop two times
            add_ticket(frame_buttons1, ticket)

        # Replaces list of classes with new list
        kb.data=item


    frame_buttons1.update_idletasks()
    frame_canvas1.config(width=190 ,height=500)

    frame_buttons2.update_idletasks()
    frame_canvas2.config(width=190 ,height=500)

    frame_buttons3.update_idletasks()
    frame_canvas3.config(width=190 ,height=500)
    # Set the canvas scrolling region
    canvas1.config(scrollregion=canvas1.bbox("all"))
    canvas2.config(scrollregion=canvas2.bbox("all"))
    canvas3.config(scrollregion=canvas3.bbox("all"))


    


    # Launch the GUI
    root.mainloop()



def show_info(ticket):
    top = tk.Toplevel()
    top.title("Information")
    top.geometry("500x450")
    try:
        text = (
            f"""\
            Ticket id: {str(ticket.ticket_id)}\
            \n  Deadline: {ticket.deadline}\
            \n  Start date: {str(ticket.start_date.strftime("%x"))}\
            \n  End date: {ticket.end_date}\
            \n  Worker: {ticket.worker}\
            \n  Program: {ticket.program}\
            """
        )
    except AttributeError:
        text = (
        f"""\
        Ticket id: {str(ticket.ticket_id)}\
        \n  Deadline: {ticket.deadline}\
        \n  Start date: {str(ticket.start_date.strftime("%x"))}\
        \n  End date: {ticket.end_date}\
        \n  Worker: {ticket.worker}\
        \n  Description: {ticket.get_description()}
        \n  Status: {ticket.get_status()}
        """
    )

    
    text_box = tk.Text(top)
    text_box.pack()
    text_box.insert("end", text)
    text_box.config(state="disabled")


    # Dropdown settings for status
    status_var = tk.StringVar()
    list_status = ["Yet to start","In progress","Done"]
    status_var.set(list_status[ticket.get_status()])
    
    
    # Dropdown box with status settings
    status_label = tk.Label(top, text="Status: ")
    status_menu = tk.OptionMenu(top, status_var, *list_status)
    status_label.pack()
    status_menu.pack()

    def on_closing():
        ticket.set_status(list_status.index(status_var.get()))
        check_status()
        save.save_all()
        top.destroy()

    top.protocol("WM_DELETE_WINDOW", on_closing)


def check_status():
    uncompleted = []
    in_progress = []
    done = []

    for item in kb.data:
        if item.get_status() == 0: uncompleted.append(item)
        elif item.get_status() == 1: in_progress.append(item)
        elif item.get_status() == 2: done.append(item)

    for list in [uncompleted,in_progress,done]:
        x=0
        for item in list:
            item.set_kbpos(2+x)
            x+=1

app()