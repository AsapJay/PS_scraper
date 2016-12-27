'''
Created on Dec 2, 2016

@author: JR
'''
import smtplib

class DealEmailer(object):
    '''
    classdocs
    '''


    def __init__(self, to_email):
        self.to_email = to_email
        self.user = ""
        self.pass_ = ""
        pass
    
    
    def send_matches(self , matches):
        mail = smtplib.SMTP('smtp.gmail.com' , 587)
        mail.ehlo()
        mail.starttls()
        mail.login(self.user , self.pass_)
        email_text = ''.join(matches)
        mail.sendmail(self.user , self.to_email , "\n" + email_text)
        mail.close()
        
        
    
    
        
        