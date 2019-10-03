from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import js2py


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        username = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23webdeveloper&src=typeahead_click')
        time.sleep(3)
        for i in range(1, 10):
            bot.execute_script(
                'window.scroll.To(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_element_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)

                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)


WileE = TwitterBot('MyUsername', 'MyPassword')
WileE.login()
WileE.like_tweet('webdeveloper')
