from setuptools import find_packages, setup

setup(
    name='tesis_chatbot',
    author='Hans Matos Rios',
    author_email='hans.matos@pucp.edu.pe',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'aiohttp',
        'aiofile',
        'beautifulsoup4',
        'PyPDF2',
        'spacy',
    ]
)