from setuptools import setup


try:
    long_description = open('README.md', encoding='utf-8').read()
except Exception:
    long_description = open('README.md').read()


setup(name='microbiopy',
      version='0.1.0',
      description='Filters features based on prevalance and abundance.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
      ],
      url='https://github.com/BigDataBiology/microbiopy',
      author='Karma Dolkar',
      author_email='karmadolkar29@gmail.com',
      license='MIT',
      install_requires=[
          # Technically, numpy is not directly needed, but some downstream
          # dependencies use it and fail to declare they need it:
          'pytest',
          'numpy',
          'flake8',
          'matplotlib',
          'sklearn',
          'pandas'
      ],
      package_data={
             'microbiopy': ['*.md']},
      zip_safe=False,
      )
