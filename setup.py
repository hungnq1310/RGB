from distutils.core import setup

NAME = 'rgb'
VERSION = '0.1.1'
with open('readme.md', encoding="utf-8") as file: 
    description = file.read()
setup(
    name=NAME, 
    version=VERSION, 
    packages=['models'],  
    classifiers=[
        'Development Status :: 1 - Planning', 
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9'
    ],
)