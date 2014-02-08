from setuptools import setup
from vcard4 import __package__, __doc__, __url__, __author__, __email__, __maintainer__, __license__
from version import __version__

setup(
    name=__package__,
    version=__version__,
    description='vcard4 validator, class and utility functions',
    long_description=__doc__,
    url=__url__,
    keywords='vCard vCards RFC 6350 RFC6350 validator',
    packages=[__package__],
    test_suite='vcard4.test_vcard4',
    entry_points={
        'console_scripts': [
            '%(package)s=%(package)s.%(package)s:main' % {
                'package': __package__}]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    author=__author__,
    author_email=__email__,
    maintainer=__maintainer__,
    maintainer_email=__email__,
    download_url='http://pypi.python.org/pypi/vcard4/',
    platforms=['POSIX', 'Windows'],
    license=__license__,
)
