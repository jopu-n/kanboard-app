# Name:         guitest.py
# Modified by:  Johannes Natunen, Nico Kranni
# Description:  A GUI program, that turns class objects into more visual


import tkinter as tk
import tkinter.ttk as ttk
import save
import kanboard1 as kb

def app():
    root = tk.Tk()
    root.grid_rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.geometry('532x600')
    root.resizable(False, False)
    root.title('Kanboard')
    items = save.load_all('pickle.dat') # Loads tickets from pickle.dat file, if no file, creates it

    frame_main = tk.Frame(root, bg='#f5f5f5')
    frame_main.grid(sticky='news')
    
    def ticket_choice():
        choice_window = tk.Toplevel()
        choice_window.geometry("200x50")
        choice_window.title("Choose ticket type")
        ticket_types = ["Main Task","Program Task"]
        for ticket_type in ticket_types:
            choice_button = ttk.Button(
                choice_window,
                text=ticket_type,
                command=lambda x=ticket_types.index(ticket_type): after_choice(x), # Calls the new_ticket command when clicked
                #bg='#ededed',
                # height=50,
                width=100,
                style='Fun.TButton',
            )
            choice_button.pack()
        
        def after_choice(num):
            new_ticket(num)
            choice_window.destroy()


    # New ticket function.
    # with ticket_type_num we will define if the user wants to make a main or program task.
    def new_ticket(ticket_type_num):

        top = tk.Toplevel()
        top.geometry('250x170')
        top.title('New Ticket')
        deadline_var = tk.StringVar()
        end_date_var = tk.StringVar()
        worker_var = tk.StringVar()
        description_var = tk.StringVar()
        program_var = tk.StringVar()
        
        # Dropdown settings for status
        status_var = tk.StringVar()
        list_status = ['Yet to start','In progress','Done']
        status_var.set(list_status[0])

        # Submit button inside the pop up window
        def submit():
            deadline = deadline_var.get()
            end_date = end_date_var.get()
            worker = worker_var.get()
            description = description_var.get()
            status = list_status.index(status_var.get())
            program = program_var.get()
            

            if ticket_type_num == 0:
                ticket = kb.MainTask(deadline, end_date, worker, description, status)
                add_ticket(frame_buttons1,ticket)

            elif ticket_type_num == 1:
                ticket = kb.ProgramTask(deadline, end_date, worker, description, status, program)
                add_ticket(frame_buttons1,ticket)

            deadline_var.set('')
            end_date_var.set('')
            worker_var.set('')
            description_var.set('')
            program_var.set('')
            status_var.set(list_status[0])
            save.save_all()
            


        deadline_label = tk.Label(top, text='Deadline: ')
        deadline_entry = tk.Entry(top, textvariable=deadline_var)

        end_date_label = tk.Label(top, text='End date: ')
        end_date_entry = tk.Entry(top, textvariable=end_date_var)

        worker_label = tk.Label(top, text='Worker: ')
        worker_entry = tk.Entry(top, textvariable=worker_var)

        description_label = tk.Label(top, text='Description: ')
        description_entry = tk.Entry(top, textvariable=description_var)

        if ticket_type_num == 1:
            program_label = tk.Label(top, text="Program: ")
            program_entry = tk.Entry(top, textvariable=program_var)

        # Dropdown box with status settings
        status_label = tk.Label(top, text='Status: ')
        status_menu = tk.OptionMenu(top, status_var, *list_status)
        

        submit_btn = tk.Button(top, text = 'Submit', command=submit)

        deadline_label.grid(row=0,column=0)
        deadline_entry.grid(row=0,column=1)
        end_date_label.grid(row=1,column=0)
        end_date_entry.grid(row=1,column=1)
        worker_label.grid(row=2,column=0)
        worker_entry.grid(row=2,column=1)
        description_label.grid(row=3,column=0)
        description_entry.grid(row=3,column=1)
        if ticket_type_num == 0:
            status_label.grid(row=4,column=0)
            status_menu.grid(row=4,column=1)
            submit_btn.grid(row=5,column=0)
        elif ticket_type_num == 1:
            program_label.grid(row=4,column=0)
            program_entry.grid(row=4,column=1)
            status_label.grid(row=5,column=0)
            status_menu.grid(row=5,column=1)
            submit_btn.grid(row=6,column=0)
        
    def remove_ticket():
        top = tk.Toplevel()
        top.title('Remove Ticket')
        remove_var = tk.StringVar()

        # Remove button inside the pop up window
        def delete():
            remove = remove_var.get()
            for i in kb.data:
                if i.ticket_id == int(remove):
                    # Checks from which column to remove correct button
                    if i.get_status()==1:
                        frame_buttons2.grid_slaves(row=i.ticket_id)[0].destroy()
                    elif i.get_status()==0:
                        frame_buttons1.grid_slaves(row=i.ticket_id)[0].destroy()
                    elif i.get_status()==2:
                        frame_buttons3.grid_slaves(row=i.ticket_id)[0].destroy()
                    kb.data.remove(i)
            remove_var.set('')

        remove_label = tk.Label(top, text='Remove: ')
        remove_entry = tk.Entry(top, textvariable=remove_var)

        remove_btn = tk.Button(top, text = 'Delete', command=delete)
        check_status()
        remove_label.grid(row=0,column=0)
        remove_entry.grid(row=0,column=1)

        remove_btn.grid(row=3,column=0)


    # The actual button that appears in the main window
    new_entry_btn = tk.Button(frame_main, text='New Ticket', bg='#dbdbdb', command=ticket_choice)
    new_entry_btn.grid(row=0, column=0,padx=10,pady=10)
    new_entry_btn.config(width=20)

    # Button that saves changes to pickle.dat file
    save_btn = tk.Button(frame_main, text='Plz Save', bg='#dbdbdb', command=save.save_all)
    save_btn.grid(row=0, column=1,padx=10,pady=10)
    save_btn.config(width=20)

    # Button that removes ticket from pickle.dat file
    remove_ticket_btn = tk.Button(frame_main, text='Remove', bg='#dbdbdb', command=remove_ticket)
    remove_ticket_btn.grid(row=0, column=2,padx=10,pady=10)
    remove_ticket_btn.config(width=20)

    # Labels for the columns
    label1 = tk.Label(frame_main, text='Uncompleted', fg='black')
    label1.grid(row=1, column=0, padx=10,pady=10, sticky='we')
    label1.config(width=20)

    label2 = tk.Label(frame_main, text='In Progress', fg='black')
    label2.grid(row=1, column=1, padx=10,pady=10, sticky='we')
    label2.config(width=20)

    label3 = tk.Label(frame_main, text='Completed', fg='black')
    label3.grid(row=1, column=2, padx=10,pady=10, sticky='we')
    label3.config(width=20)

    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas1 = tk.Frame(frame_main)
    frame_canvas1.grid(row=2, column=0, padx=(5, 0), sticky='nw')
    frame_canvas1.grid_rowconfigure(0, weight=1)
    frame_canvas1.grid_columnconfigure(0, weight=1)

    # Set grid_propagate to False to allow buttons resizing later
    frame_canvas1.grid_propagate(False)


    # Add a canvas in that frame
    canvas1 = tk.Canvas(frame_canvas1, bg='white')
    canvas1.grid(row=0, column=0, sticky='news')


    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas2 = tk.Frame(frame_main)
    frame_canvas2.grid(row=2, column=1, padx=(5, 0), sticky='nw')
    frame_canvas2.grid_rowconfigure(0, weight=1)
    frame_canvas2.grid_columnconfigure(0, weight=1)
    frame_canvas2.grid_propagate(False)

    # Add a canvas in that frame
    canvas2 = tk.Canvas(frame_canvas2, bg='white')
    canvas2.grid(row=0, column=0, sticky='news')

    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas3 = tk.Frame(frame_main)
    frame_canvas3.grid(row=2, column=2, padx=(5, 0), sticky='nw')
    frame_canvas3.grid_rowconfigure(0, weight=1)
    frame_canvas3.grid_columnconfigure(0, weight=1)
    frame_canvas3.grid_propagate(False)

    # Add a canvas in that frame
    canvas3 = tk.Canvas(frame_canvas3, bg='white')
    canvas3.grid(row=0, column=0, sticky='news')


    # Link a scrollbar to the canvas
    
    vertical_scroll_bar1 = tk.Scrollbar(frame_canvas1, orient='vertical', command=canvas1.yview)
    vertical_scroll_bar1.grid(row=0, column=1, sticky='news')
    canvas1.configure(yscrollcommand=vertical_scroll_bar1.set)

    # Link a scrollbar to the canvas
    vertical_scroll_bar2 = tk.Scrollbar(frame_canvas2, orient='vertical', command=canvas2.yview)
    vertical_scroll_bar2.grid(row=0, column=1, sticky='ns')
    canvas2.configure(yscrollcommand=vertical_scroll_bar2.set)

    # Link a scrollbar to the canvas
    vertical_scroll_bar3 = tk.Scrollbar(frame_canvas3, orient='vertical', command=canvas3.yview)
    vertical_scroll_bar3.grid(row=0, column=2, sticky='ns')
    canvas3.configure(yscrollcommand=vertical_scroll_bar3.set)

    # Create a frame to contain the buttons
    frame_buttons1 = tk.Frame(canvas1, bg='#7d7d7d')
    canvas1.create_window((0, 0), window=frame_buttons1, anchor='nw')

    frame_buttons2 = tk.Frame(canvas2, bg='#8dd8eb')
    canvas2.create_window((0, 0), window=frame_buttons2, anchor='nw')

    frame_buttons3 = tk.Frame(canvas3, bg='#6fde74')
    canvas3.create_window((0, 0), window=frame_buttons3, anchor='nw')



    def add_ticket(frame_buttons1,ticket):
        try:
            info = (
                f'''\
                Ticket id: {str(ticket.ticket_id)}\
                \n  Deadline: {ticket.deadline}\
                \n  Start date: {str(ticket.start_date.strftime('%x'))}\
                \n  End date: {ticket.end_date}\
                \n  Worker: {ticket.worker}\
                \n  Program: {ticket.program}\
                '''
            )
        except AttributeError:
            info = (
            f'''\
            Ticket id: {str(ticket.get_ticket_id())}\
            \n  Deadline: {ticket.get_deadline()}\
            \n  Start date: {str(ticket.get_start_date().strftime('%x'))}\
            \n  End date: {ticket.get_end_date()}\
            \n  Worker: {ticket.get_worker()}\
            '''
        )
        check_status()
        if ticket.get_status()==0:
            button = ttk.Button(
            frame_buttons1,
            text=info,
            command=lambda x=ticket: show_info(x), # Calls the show_info command when clicked
            #bg='#ededed',
            #height=6,
            width=20,
            style='Fun.TButton',
        )
        elif ticket.get_status()==1:
            button = ttk.Button(
            frame_buttons2,
            text=info,
            command=lambda x=ticket: show_info(x), # Calls the show_info command when clicked
            #bg='#ededed',
            #height=6,
            width=20,
            style='Fun.TButton',
        )
        else:
            button = ttk.Button(
            frame_buttons3,
            text=info,
            command=lambda x=ticket: show_info(x), # Calls the show_info command when clicked
            #bg='#ededed',
            #height=6,
            width=20,
            style='Fun.TButton',
        )
        
        button.grid(
            column=0,
            row=ticket.ticket_id,
            padx=10,
            pady=10
        )

        frame_buttons1.update_idletasks()
        frame_canvas1.config(width=170 ,height=500)

        frame_buttons2.update_idletasks()
        frame_canvas2.config(width=170 ,height=500)

        frame_buttons3.update_idletasks()
        frame_canvas3.config(width=170 ,height=500)

        canvas1.config(scrollregion=canvas1.bbox('all'))
        canvas2.config(scrollregion=canvas2.bbox('all'))
        canvas3.config(scrollregion=canvas3.bbox('all'))


    for item in items: # Seems like pickle objects have the real objects inside them
        for ticket in item: # Thus, we have to loop two times
            add_ticket(frame_buttons1, ticket)

        # Replaces list of classes with new list
        kb.data=item


    frame_buttons1.update_idletasks()
    frame_canvas1.config(width=170 ,height=500)

    frame_buttons2.update_idletasks()
    frame_canvas2.config(width=170 ,height=500)

    frame_buttons3.update_idletasks()
    frame_canvas3.config(width=170 ,height=500)


    canvas1.config(scrollregion=canvas1.bbox('all'))
    canvas2.config(scrollregion=canvas2.bbox('all'))
    canvas3.config(scrollregion=canvas3.bbox('all'))
    
    # Launch the GUI
    root.mainloop()


def show_info(ticket):
    top = tk.Toplevel()
    top.title('Information')
    top.geometry('500x450')
    try:
        text = (
            f'''\
            Ticket id: {str(ticket.ticket_id)}\
            \n  Deadline: {ticket.deadline}\
            \n  Start date: {str(ticket.start_date.strftime('%x'))}\
            \n  End date: {ticket.end_date}\
            \n  Worker: {ticket.worker}\
            \n  Program: {ticket.program}\
            '''
        )
    except AttributeError:
        text = (
        f'''\
        Ticket id: {str(ticket.ticket_id)}\
        \n  Deadline: {ticket.deadline}\
        \n  Start date: {str(ticket.start_date.strftime('%x'))}\
        \n  End date: {ticket.end_date}\
        \n  Worker: {ticket.worker}\
        \n  Description: {ticket.get_description()}
        \n  Status: {ticket.get_status()}
        '''
    )

    
    text_box = tk.Text(top)
    text_box.pack()
    text_box.insert('end', text)
    text_box.config(state='disabled')


    # Dropdown settings for status
    status_var = tk.StringVar()
    list_status = ['Yet to start','In progress','Done']
    status_var.set(list_status[ticket.get_status()])
    
    
    # Dropdown box with status settings
    status_label = tk.Label(top, text='Status: ')
    status_menu = tk.OptionMenu(top, status_var, *list_status)
    status_label.pack()
    status_menu.pack()

    def on_closing():
        ticket.set_status(list_status.index(status_var.get()))
        check_status()
        save.save_all()
        
        
        
        top.destroy()


    top.protocol('WM_DELETE_WINDOW', on_closing)


def check_status():
    uncompleted = []
    in_progress = []
    done = []

    for item in kb.data:
        if item.get_status() == 0: uncompleted.append(item)
        elif item.get_status() == 1: in_progress.append(item)
        elif item.get_status() == 2: done.append(item)


app()