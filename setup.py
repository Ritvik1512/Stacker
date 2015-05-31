from setuptools import setup


setup(
    name="stacker",
    version="1.0.0",
    packages=['stacker'],
    install_requires=
    [
        'Click',
        'Py-StackExchange',
        'html2text',
    ],
    
    author="Ritvik Choudhary",
    author_email="ritvik@outlook.com",
    description="An awesome feature stacked CLI interface for StackOverflow.",
    license="MIT",
    keywords="stack overflow stackoverflow stack exchange stackexchange",
    download_url="https://github.com/Ritvik1512/stacker/tarball/1.0.0",

    entry_points=
    {
        'console_scripts': 
        [
            'stacker=stacker.stacker_arc:main'
        ]
    }

)
