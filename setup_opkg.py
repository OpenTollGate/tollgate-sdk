from setuptools import setup

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
        'opkg-list-fields',
        'opkg-make-index',
        'opkg-show-deps',
        'opkg-unbuild',
        'opkg-update-index'
    ],
)
