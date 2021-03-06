import setuptools

with open('README.md', 'rb') as fh:
    long_description = fh.read().decode('utf-8')

setuptools.setup(
    name='reds',
    version='0.1.9',
    url='https://github.com/treenoder/reds',
    license='MIT',
    author='treenoder',
    author_email='ondaemon@gmail.com',
    description='Request/Response library on top of Redis.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    install_requires=['redis', 'typing; python_version < "3.5.0"'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
