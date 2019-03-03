from pathlib import Path

from pyramid_watcher.samples.tree.resources.processors import PROCESSORS, md


def test_md_processor_mapping():
    md = PROCESSORS['md']
    assert 'md' == md.__name__


def test_md_processor(dummy_request, dummy_tmpdir):
    root = dummy_request.registry.root
    target = dummy_tmpdir / Path('hello.md')
    document = md(target, root)
    assert 'hello' == document.__name__
    assert 'Dummy Siteroot' == document.__parent__.title
    assert 'Some Dummy Doc' == document.title
    assert '<p>You are not <em>here</em>.</p>\n' == document.body


def test_md_processor_no_frontmatter(dummy_request, dummy_tmpdir):
    root = dummy_request.registry.root
    target = dummy_tmpdir / Path('broken.md')
    document = md(target, root)
    assert None is document
