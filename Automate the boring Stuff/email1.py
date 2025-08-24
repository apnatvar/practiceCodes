import smtplib
import imapclient
import pyzmail

myEmailID = "arawat@tcd.ie"
myAppSpecificPassword = "donc ngcl fkwg idxm"

def sendMail(sendTo, sendFrom, emailPass):
    conn = smtplib.SMTP('smtp.gmail.com',587) #smtp server and por number, 587 is usually the default
    print(conn.ehlo()) # hello world type shit
    print(conn.starttls()) # start the connection
    conn.login(sendFrom, emailPass) # google requires app specific passwords which is different from the main pasword ot access it
    conn.sendmail(sendFrom, sendTo, "Subject: Test from Python\n\n Sending a test message from arawat@tcd.ie to apnatvarawat90@gmail.com\n\n Sincerely, Apnatva Singh Rawat") # from, to, body
    conn.quit() # close the connection

# sendMail("apnatvarawat90@gmail.com", myEmailID, myAppSpecificPassword)

def readMail(readFrom, emailPass):
    conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
    conn.login(readFrom, emailPass)
    conn.select_folder('INBOX', readonly=True) # if you are not deleting anything
    print(conn.list_folders())
    UIDs = conn.search(['SINCE 20-Aug-2015']) # ALL, BEFORE/ON/SINCE date, SUBJECT/BODY/TEXT string 'TEXT "stringToSearch"'
    # https://afterlogic.com/mailbee/docs/IMAP4_methods_Search.htm
    rawMessage = conn.fetch(UIDs[0], ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(rawMessage[UIDs[0]][b'BODY[]'])
    print(message.get_subject())
    print(message.get_addresses('from'))
    print(message.get_addresses('to'))
    print(message.get_addresses('bcc'))
    print(message.text_part)
    print(message.html_part)
    print(message.text_part.get_payload().decode('UTF-8'))
    print(message.text_part.charset)
    # conn.delete(UIDs) # will delete the emails with the particular email IDs
