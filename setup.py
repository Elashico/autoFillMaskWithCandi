from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Fill-mask with custom candidate'

# Setting up
setup(
    name="ohayo-fill-mask-wCandi",
    version=VERSION,
    author="Elatot",
    author_email="<elashiishii@gmail.com>",
    license="MIT",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['torch','transformers'],
    keywords=['python', 'hugging-face', 'fill-mask', 'natural language processing','pretrained langugae model'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)