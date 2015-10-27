from codecs import open as codecs_open
from setuptools import setup


# Parse the version from the affine module.
with open('boolean/__init__.py') as f:
    for line in f:
        if "__version__" in line:
            version = line.split("=")[1].strip()
            version = version.strip('"').strip("'")
            break

with codecs_open('README.rst', encoding='utf-8') as f:
    readme = f.read()


setup(name='boolean',
      version=version,
      description="Converts string to their equivalent boolean value",
      long_description=readme,
      classifiers=[],
      keywords='boolean true false yes no',
      author='Alireza J (Scisco)',
      author_email='scisco7@gmail.com',
      url='https://github.com/scisco/boolean',
      license='CC0',
      packages=['boolean'],
      include_package_data=True,
      zip_safe=False,
      test_suite="test",
      classifiers=[
          # Indicate who your project is intended for
          'Intended Audience :: Developers',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
      )
