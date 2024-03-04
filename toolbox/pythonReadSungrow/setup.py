import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.1',
    author='Markus Martius',
    author_email='markusmartius@gmail.com',
    description='Off-Grid Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kisa72/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/kisa72/toolbox/issues"
    },
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)
