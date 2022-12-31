# FlibCartScraping 🐧🌐

FlibCart website scrap laptops details with python beautifulSoup 4

<img width="1440" alt="Screenshot 2022-12-31 at 8 59 29 AM" src="https://user-images.githubusercontent.com/60796459/210128300-66f489b8-552d-4f54-add4-bd0583ca9be9.png">

## Using BeautifulSaop Library To Scrap HTML 🐉 🚀

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

installtion using python package manager PIP

```bash
(venv) $ pip install beautifulsoup4 
```

## Code Snipptes 👨🏿‍💻

```python
# Looping for Laptops detials {title, price, ratings}
# append iterator ouput in Lists 
for iterator in document.findAll('a', href=True, attrs={'class': "_1fQZEK"}):
    name = iterator.find('div', attrs={'class': '_4rR01T'})
    price = iterator.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    rating = iterator.find('div', attrs={'class': '_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

# Make use of pandas lib to generate output in Files.
outputDocument = pd.DataFrame(
    {'Product Name': products, 'Product Price': prices, 'Product Rating': ratings})
outputDocument.head()
outputDocument.to_csv('products.csv')  # generating csv file
```

### Clone The Repository 🐛

```bash
git clone https://github.com/iNightjar/FlibCartScraping.git
cd FlibCartScraping
git checkout master
rm -rf .git
git init .
git branch [branch-name] # make it descriptive
git add [file]  # individual commits for each file are prefered
git commit -m "Your Commit Message"
```

### Create virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate
```

Use `.\venv\Scripts\activate` if on windows

### Install requirements

```bash
(venv) python -m pip install pip --upgrade
(venv) python -m pip install -r requirements.txt
```

### Open VSCode & Start Coding

```bash
cd /path/Sclamp
code .
```
