import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='hwmon',
    packages=['hwmon'],
    version='0.9',
    license='gpl-3.0',
    description='Hwmon is a collection of Python 3 scripts which are a native Python solution for obtaining '
                'information from Linux system sensors.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Guillermo-C-A & Bla6',
    author_email='guillcal@ucm.es',
    url='https://github.com/Guillermo-C-A/Hwmon-python',
    download_url='https://github.com/bla6-apm/Hwmon-python/archive/0.9.tar.gz',
    keywords=['system_info', 'hardware_monitor', 'monitoring', 'hardware', 'sensors'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Topic :: System',
        'Topic :: System :: Hardware',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires=">=3.6",
)
