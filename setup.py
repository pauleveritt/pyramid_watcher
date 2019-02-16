from setuptools import setup, find_packages


def readfile(name):
    with open(name) as f:
        return f.read()


readme = readfile('README.rst')
changes = readfile('CHANGES.rst')

requires = [
    'pyramid'
]

docs_require = [
    'Sphinx',
    'pylons-sphinx-themes',
]

tests_require = [
    'pytest',
    'pytest-cov',
    'mock',
]

sample_requires = [
    'pyramid_jinja2',
    'waitress',
    'plaster_pastedeploy',
    'pydantic',
    'mistletoe'
]

setup(
    name='pyramid_watcher',
    version='0.1',
    description=(
        'Watch for file changes, call handlers, and reload browser'
    ),
    long_description=readme + '\n\n' + changes,
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    url='https://github.com/pauleveritt/pyramid_watcher',
    license='MIT',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=requires,
    extras_require={
        'docs': docs_require,
        'testing': tests_require,
        'sample': sample_requires
    },
    entry_points={
        "console_scripts": [
            "watcher = pyramid_watcher.cli:main",
        ],
    },
    zip_safe=False,
    keywords='watch reload',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
