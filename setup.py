import distutils.core

distutils.core.setup(
    name='ezprogress',
    version='1.0.3',
    description='Simple, easy to use progress bar.',
    long_description=open('README.rst', 'r').read(),
    author='Jonas Kloster Jacobsen',
    author_email='joklost@gmail.com',
    license='MIT',
    py_modules=['ezprogress'],
    url='https://github.com/Joklost/ezprogress',
    python_requires='>=3.6',
    zip_safe=False
)
