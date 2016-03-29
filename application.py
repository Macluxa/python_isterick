from selenium.webdriver.firefox.webdriver import WebDriver

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get('http://localhost/addressbook/')

    def login(self, username, password):
        wd = self.wd
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_name("submit").click()

    def opens_group(self):
        wd = self.wd
        wd.find_elements_by_link_text('groups').click()

    def create_group(self, group):
        wd = self.wd
        self.open_home_page(wd)
        wd.find_element_by_class_name('new').click()
        wd.find_element_by_name('group_name').click()
        wd.find_element_by_name('group_name').clear()
        wd.find_element_by_name('group_name').send_keys(group.name)
        wd.find_element_by_name('group_header').click()
        wd.find_element_by_name('group_header').clear()
        wd.find_element_by_name('group_header').send_keys(group.header)
        wd.find_element_by_name('group_footer').click()
        wd.find_element_by_name('group_footer').clear()
        wd.find_element_by_name('group_footer').send_keys(group.footer)
        self.return_page_list_group()

    def return_page_list_group(self):
        wd = self.wd
        wd.find_elements_by_link_text('group page').click()


    def loguot(self):
        wd = self.wd
        wd.find_elements_by_link_text("Logout").click()


    def destroy(self):
        self.wd.quit()