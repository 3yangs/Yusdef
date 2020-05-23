from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    print('readed')
    
setup(name='Yusdef',
      version='0.0.3',
      description='A example package for all people',
      author='Yangs',
      author_email='mandi.yang@elev.kungsbacka.se',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/3yangs/Yusdef',
      python_requires='>=3.4',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX :: Linux",
          "Operating System :: Microsoft :: Windows :: Windows 10",
          "Natural Language :: Swedish",
      ],
      packages=find_packages()
)

