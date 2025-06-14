import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"
REPO_NAME="Text-Summarizer-Project"
AUTHOR_USER_NAME="Sukhmanpeet123"
SRC_REPO="textsummarizer"
AUTHOR_EMAIL="shine.khurana01@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
   project_urls={
       "Bug Tracker":"https://github.com/Sukhamnpreet123/Text-Summarizer-Project/issues",
   },
   package_dir={"":"src"},
   packages=setuptools.find_packages(where="src")
    
)