from setuptools import setup

setup(name='anchor_custom',
      version='0.0.0.5',
      description='Anchor explanations for machine learning models',
      url='http://github.com/phineasng/anchor',
      author='An-phi Nguyen',
      author_email='nguyen.phineas@gmail.com',
      license='BSD',
      packages=['anchor'],
      install_requires=[
          'numpy',
          'scipy',
          'spacy',
          'lime',
          'scikit-learn'
      ],
      include_package_data=True,
      zip_safe=False)

