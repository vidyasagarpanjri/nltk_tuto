import email

#from email import Message
def message_body(msg_file_addr):
    msg = email.message_from_file(open(msg_file_addr,'r'))
    print len(msg.get_payload())
    print msg.get_params()
    if msg.is_multipart():
        for p in msg.get_payload():
            return str(p.get_payload())
    else:
        return str(msg.get_payload())
               

print message_body(r'/home/vidyasagar/git_repo/nltk_tuto/spam/0001.bfc8d64d12b325ff385cca8d07b84288')
#print message_body(r'/home/vidyasagar/automation/messages/dat2/2683277295')


