#!/usr/bin/env python

import unittest
from selenium import webdriver
from pyvirtualdisplay import Display
import os,random,string,time
import imaplib,re, webbrowser

class doHack0Engine(unittest.TestCase):

    def setUp(self):
        display = Display(visible=0, size=(1366, 768))
        display.start()
	self.driver.maximize_window()

        self.driver = webdriver.Firefox()
	self.url2 = ''
	
	self.bill_card_num = '<YOUR-VIRTUAL-CARD-NUM-HERE>'
	self.bill_card_mm_yy = '<MM-YY>'
	self.bill_card_cvv = '<CVV>'
	self.bill_first_name = '<NAME>'
	self.bill_last_name = '<SURNAME>'
	self.bill_street_addr = '<STREET-ADDR>'
	self.bill_city = '<CITY>'
	self.bill_state = '<COUNTRY>'
	self.bill_post_code = 'POST-CODE'
	self.bill_country = '<COUNTRY>'
	self.phone_num = '<PHONE-NUM>'

    def mail_verify(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('<GMAIL-ADDR>','GMAIL-PASS')
        mbox = mail.list()
        rv, data = mail.select("INBOX")
        if rv== "OK":
                print 'Processing mailbox...\n'

        for num in data[0].split():
                rv, data = mail.fetch(num, '(RFC822)')
                match = re.search(r'(https://cloud.digitalocean.com/account_verification/email/.*)\\r\\n\\r\\n',str(data))
                act_url =  match.group()
                act_url = act_url[:-8]
                #activation curl py
                webbrowser.open(act_url,new=0, autoraise=True)
		self.url2 = act_url

                #set promo code
                #DROPLET10
                mail.close()
        mail.logout()


    def createNewMail(self):
        global RAND_TEXT
	RAND_TEXT = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(7))
        os.system('echo \'%s@<YOUR-DOMAIN-ADDR>  <YOUR-GMAIL-ADDR>\' >> /etc/postfix/vmail_aliases'%RAND_TEXT)
        os.system('postmap /etc/postfix/vmail_aliases')
        os.system('echo %s | mail -s "do new account" "<YOUR-REAL-MAIL-ADDR>"'%RAND_TEXT)
 
    def test_001doSign(self):
        self.createNewMail()
        self.driver.get('https://cloud.digitalocean.com/registrations/new')                                                                                                                       
        driver = self.driver                                                                                                                                                                      
        driver.implicitly_wait(10)                                                                                                                                                                
        email = driver.find_element_by_id('user_email')
        mail_addr = '%s@<YOUR-DOMAIN-NAME>'%RAND_TEXT
        email.send_keys(mail_addr)                                                                                                                                                                
        password = driver.find_element_by_id('user_password')                                                                                                                                     
        password.send_keys(RAND_TEXT)                                                                                                                                                             
        driver.find_element_by_xpath('.//*[@id=\'new_user\']/input[5]').click()


    def test_002doLogIn(self):
	self.mail_verify()
        self.driver.get('https://cloud.digitalocean.com/login')
	driver = self.driver
	driver.implicitly_wait(10)
	driver.find_element_by_id('user_email').send_keys('%s@<YOUR-DOMAIN-NAME>'%RAND_TEXT)
	driver.find_element_by_id('user_password').send_keys(RAND_TEXT)
	driver.find_element_by_xpath('.//*[@id=\'new_user\']/input[5]').click()
        time.sleep(3)
	self.driver.get(self.url2)	
	print 'Activation OK'
        

    def test_003doBilling(self):
	self.driver.get('https://cloud.digitalocean.com/login')
	driver = self.driver
	driver.implicitly_wait(10)
	driver.find_element_by_id('user_email').send_keys('%s@<YOUR-DOMAIN-NAME>'%RAND_TEXT)
	driver.find_element_by_id('user_password').send_keys(RAND_TEXT)
	driver.find_element_by_xpath('.//*[@id=\'new_user\']/input[5]').click()
        time.sleep(3)
		
		


	
                                                                          
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == '__main__':
    unittest.main()
