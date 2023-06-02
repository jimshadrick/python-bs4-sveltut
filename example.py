from bs4 import BeautifulSoup

html = """
<optgroup label="1. Introduction">
  <option value="basics">a. Basics</option>
  <option value="adding-data">b. Adding data</option>
  <option value="dynamic-attributes">c. Dynamic attributes</option>
  <option value="styling">d. Styling</option>
  <option value="nested-components">e. Nested components</option>
  <option value="making-an-app">f. Making an app</option>
</optgroup>
<optgroup label="2. Reactivity">
  <option value="reactive-assignments">a. Assignments</option>
  <option value="reactive-declarations">b. Declarations</option>
  <option value="reactive-statements">c. Statements</option>
  <option value="updating-arrays-and-objects">
    d. Updating arrays and objects
  </option>
</optgroup>
"""

soup = BeautifulSoup(html, 'html.parser')

optgroup_dict = {}

optgroups = soup.find_all('optgroup')

for optgroup in optgroups:
    label = optgroup['label']
    options = optgroup.find_all('option')
    option_texts = [option.text.strip() for option in options]
    optgroup_dict[label] = option_texts

print(optgroup_dict)
