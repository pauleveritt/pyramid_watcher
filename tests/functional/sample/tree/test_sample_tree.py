from bs4 import BeautifulSoup


def test_functional_root(testapp):
    soup: BeautifulSoup = testapp.get('/', status=200).html
    assert 'Home Page - Tree Sample' == soup.select_one('title').get_text().strip()
    assert 'Root: Home Page' == soup.select_one('h1.title').get_text().strip()

    nav = soup.select_one('nav > a')
    assert 'Home' == nav.get_text().strip()
    assert '/' == nav.attrs['href']

    child = soup.select_one('li > a')
    assert 'Some Dummy Doc' == child.get_text().strip()
    assert 'http://localhost/about/' == child.attrs['href']


def test_functional_document(testapp):
    soup: BeautifulSoup = testapp.get('/about', status=200).html
    assert 'Some Dummy Doc - Tree Sample' == soup.select_one('title').get_text().strip()
    assert 'Document: Some Dummy Doc' == soup.select_one('h1.title').get_text().strip()
