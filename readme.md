# BS4 Scrape of Svelte Tutorial topics

This Python and BeautifulSoup4 app scrapes the menu items and related topics from the official Svelte Tutorial and organizes them to create a learning plan for Svelte. The results are stored in a dictionary and then output to the screen. The results can then be copied/pasted into a document for tracking purposes.

### How it works

The application reads the content of the website https://svelte.dev/tutorial/basics. It finds all the "optgroup" (menu) elements using soup.find_all('optgroup'). Then, it iterates over each "optgroup" element, extracts the label using optgroup['label'], and finds all the "option" elements within that "optgroup" using optgroup.find_all('option'). It then extracts the text values of each "option" using option.text.strip() and stores them in a list. Finally, it adds the label as a key in the optgroup_dict dictionary and assigns the list of option texts as the corresponding value.

When you run the code, it will print the resulting dictionary containing the "optgroup" labels as keys and their related "option" text values as lists.

### Installation

To install the repository, please clone this repository and install the requirements:

Using pip:

```bash
pip install -r requirements.txt
```

Once the environment is created, you can activate it using the following command:

```bash
source myvenv/bin/activate
```

Using conda:

```bash
conda env create -f environment.yml
```

The new environment will be named according to the name field in the environment.yml file and can be changed before creating it.

Once the environment is created, you can activate it using the following command:

```bash
conda activate environment_name
```

### Using the app

To use the application, run the app.py file either from the command line or open the file and run it within the code editor of your choice.

```bash
python3 app.py
```
