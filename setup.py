from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name = "plotutils",
    version = "0.1",
    description = "Simple matplotlib-related utility functions.",
    long_descriptoin = readme(),
    author = "Timothy D. Morton",
    author_email = "tim.morton@gmail.com",
    url = "https://github.com/timothydmorton/plotutils",
    packages = ['plotutils'],
    install_requires=['matplotlib'],
    zip_safe = False
) 
