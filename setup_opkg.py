from setuptools import setup, find_packages

setup(
    name="opkg-utils",
    version="0.1",
    py_modules=['opkg', 'arfile'],
    scripts=[
        'opkg-build',
        'opkg-buildpackage',
        'opkg-compare-indexes',
        'opkg-diff',
        'opkg-extract-file',
        'opkg-feed',
        'opkg-graph-deps',
        'opkg-list-fields',
        'opkg-make-index',
        'opkg-show-deps',
        'opkg-unbuild',
        'opkg-update-index',
        'update-alternatives'
    ],
)
