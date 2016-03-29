class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.wd
        self.opens_group()
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

    def opens_group(self):
        wd = self.app.wd
        wd.find_elements_by_link_text('groups').click()


    def return_page_list_group(self):
        wd = self.app.wd
        wd.find_elements_by_link_text('group page').click()

    def delete_first_grou(self):
        wd = self.app.wd
        self.opens_group()

