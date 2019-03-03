from bs4 import BeautifulSoup


def test_functional_home(testapp):
    assert True
    soup: BeautifulSoup = testapp.get('/', status=200).html
    assert 'Home Page - Echo Sample' == soup.select_one('title').get_text().strip()
    assert 'Home Page' == soup.select_one('h1.title').get_text().strip()
    assert 'Changesets' == soup.select_one('h4').get_text().strip()
