# from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'Django' in browser.title

# browser.quit()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import StaticLiveServerTestCase

class NewVisitorTest(StaticLiveServerTestCase):  #1

    def setUp(self):  #2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) # Wait three seconds before trying anything.

    def tearDown(self):  #3
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  #5
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
        'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')







        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)


        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.fail('Finish the test!')
# if __name__ == '__main__':  #7
#     unittest.main(warnings='ignore')  #8