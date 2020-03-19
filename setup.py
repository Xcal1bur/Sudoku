from setuptools import setup, find_packages

with open('README.md', "r") as file:
    long_description = file.read()

setup(
    name='sudoku',
    version='0.0.1',
    packages=find_packages(),
    author='David Voigt',
    author_email='David.Voigt1998@gmail.com',
    description='Sudoku solving and generation.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Xcal1bur/Sudoku',
    license='GNU General Public License v3.0',
    install_requires=[],
    entry_points={'console_scripts': ['sudoku=src.main:main']}
)
