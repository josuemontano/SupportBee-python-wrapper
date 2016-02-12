from setuptools import setup, find_packages

requires = [
    'marshmallow',
    'requests',
    'pytest',
]

setup(
    name='supportbee-wrapper',
    version='1.0',
    description='A Python wrapper around the SupportBee API ',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    author='Josue Montano',
    author_email='josuemontanoa@gmail.com',
    url='https://github.com/josuemontano/SupportBee-python-wrapper',
    keywords='supportbee wrapper',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    tests_require=requires,)
