from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md', "r") as f:
    long_description = f.read()

setup(
    name='pyavl3',
    version='1.0.0',
    author='Ian Laird',
    author_email='irlaird@gmail.com',
    url='https://github.com/en0/pyavl3',
    keywords=['avl','avltree','balancedtree','bst'],
    description='Pure python implementation of avl trees.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['pyavl3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
)
