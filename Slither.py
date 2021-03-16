### Slither -- a console based IMAP client utilizing Py_CUI and IMAPclient

import py_cui
from imap import ImapFunctions
#from itertools import chain



# My plan is to put the login info into a config file
host = "imap.gmail.com"
username = "username@gmail.com"
password = "password"

ImapFunctions = ImapFunctions(host, username, password)
ImapFunctions.login(username, password)
class Slither:

    def __init__(self, master):
        self.master = master
        
        # Creating widgets for mailbox list on left and message list onright


        ### MAILBOX WIDGET ###
        self.Mailboxes = self.master.add_scroll_menu('Mailboxes', 0, 0, row_span=6, column_span=1)
        self.Mailboxes.add_item_list(ImapFunctions.get_folders())
        
        ### MESSAGES WIDGET ###
        self.Messages = self.master.add_scroll_menu('Messages', 0, 1, row_span=6, column_span=5)
       

        ### KEY COMMANDS ###
        self.Mailboxes.add_key_command(py_cui.keys.KEY_ENTER, self.add_msg)

    def add_msg(self):

        Mailbox_at_cursor = self.Mailboxes.get()
        message_list = ImapFunctions.get_messages(Mailbox_at_cursor)
        self.Messages.add_item_list(message_list)


        
        #### Progress notes ####
        # Current issue is I'm getting is an error about th
       
        
        



# Create the CUI with 7 rows 6 columns (may change later), pass it to the wrapper object, and start it
root = py_cui.PyCUI(7, 6)
root.set_title('Slither')
s = Slither(root)
root.start()

