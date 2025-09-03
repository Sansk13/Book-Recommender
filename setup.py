from setuptools import setup
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "Parth282003"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Parth282003",
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{"Parth282003"}/{"Books-Recommender-System-Using-Machine-Learning"}",
    author_email="parthsk2003@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.13.1",
    install_requires=LIST_OF_REQUIREMENTS
)