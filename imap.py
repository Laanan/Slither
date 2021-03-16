### imap.py -- A module for Slither handling all interaction with IMAP servers

import ssl
from imapclient import IMAPClient
import email




class ImapFunctions:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.client = IMAPClient(host)


    def login(self, username, password):
        "Handling various auth protocols"
        #client.starttls() --- gmail does not support starttls
        self.client.login(username, password)
        return;

    def get_folders(self):
        "Grabbing the list of folders for the account"
        get_folders = self.client.list_folders()
        folder_list = []
        for folders in get_folders:
            folder_list.append(folders[2])
        return folder_list;


    def get_messages(self, folder):
        
        self.client.select_folder(folder)
        messages = self.client.search([ u'OLD'])
        message_list = []
        for uid, message_data in self.client.fetch(messages, "RFC822").items():
            email_message = email.message_from_bytes(message_data[b"RFC822"])
            message_list.append(email_message.get("Subject"))

        return message_list;


