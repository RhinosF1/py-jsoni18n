"""Builds the package."""
from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

# with open('CHANGELOG.md') as history_file:
# history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = list(requirements_file.readlines())


with open("dev-requirements.txt") as dev_requirements_file:
    dev_requirements = list(dev_requirements_file.readlines())

username = "Pycryptor10"
email = "Pycryptor10@gmail.com"

setup(
    name="jsoni18n",
    version="1.0.0",
    url="https://github.com/Pycryptor10/py-jsoni18n",
    description="A simple i18n system using json + pycountry alpha_3 ISO codes.",
    keywords="pycountry localization json i18n l10n internationalization",
    long_description=readme,  # + '\n\n' + history,
    long_description_content_type="text/markdown",  # This is important!
    author=username,
    author_email=email,
    maintainer=username,
    maintainer_email=email,
    platforms="any",
    packages=find_packages("."),
    include_package_data=True,
    install_requires=requirements,
    tests_require=dev_requirements,
    test_suite="tests",
    license="GPL3",
)
