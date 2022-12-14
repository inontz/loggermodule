import pathlib
from setuptools import setup
#The directory containing this file
HERE = pathlib.Path(__file__).parent
#The text of the README file
README = (HERE / "README.md").read_text()
#This call to setup() does all the work
setup(
     name="loggermodule_X",
     version="1.0.4",
     description="Logging in console and collect to file !",
     long_description=README,
     long_description_content_type="text/markdown",
     url="https://github.com/iNonTz/loggermodule",
     author="KHUNANON",
     author_email="ch.khunanon@gmail.com",
     license="InfoQuest Limited",
     classifiers=[
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.8",
     ],
     packages=["loggermodule_X"],
     include_package_data=True,
     install_requires=[],
     entry_points={
         "console_scripts": [
             "mcs=samplepackage.__main__:main",
         ]
     },
 )