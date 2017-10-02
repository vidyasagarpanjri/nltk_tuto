import email

#from email import Message
def message_body(msg_file_addr):
    msg = email.message_from_file(open(msg_file_addr,'r'))
    if (len(msg.get_payload())<1):
        return str(msg.get_payload()[0])
    else:
        return str(msg.get_payload())
               
#print message_body(r'/home/vidyasagar/automation/messages/dat2/2683277295')
