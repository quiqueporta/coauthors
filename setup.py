from setuptools import setup
from coauthors import __version__

setup(name='coauthors',
      version=__version__,
      description="Add coauthors to your last git commit message.",
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Utilities'
      ],
      keywords='',
      author=u'Quique Porta',
      author_email='quiqueporta@gmail.com',
      url='https://github.com/quiqueporta/coauthors',
      download_url='https://github.com/quiqueporta/coauthors/releases',
      license='GPLv3',
      packages=['coauthors'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['gitpython'],
      entry_points={
          'console_scripts': [
              'coauthors = coauthors.coauthors:main'
          ]
      })
