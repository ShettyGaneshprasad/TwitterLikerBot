from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('http://twitter.com/')
        time.sleep(5)
        email= bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys  (self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_tweet(self,hashtag):
        bot =self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(5)
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            tweets=bot.find_elements_by_class_name('tweet')
            links=[elem.get_attribute('data-permalink-path') for elem in tweets]
            print(links)
            for link in links:
                bot.get('https://twitter.com'+link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(5)
                except  Exception as ex:
                    time.sleep(60)

mail=input("Enter the mail / phone no of your Twitter Account")
password=input("Enter Password of your twitter Account")
hashtag=input("Enter the Hashtag you want to like")
gs= TwitterBot(mail,password)
gs.login() 
gs.like_tweet(hashtag)  