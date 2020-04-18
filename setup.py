import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='hwmon',
    packages=['hwmon'],
    version='0.7',
    license='gpl-3.0',
    description='Hwmon is a collection of Python 3 scripts which are a native Python solution for obtaining '
                'information from Linux system sensors.',
    author='Guillermo-C-A',
    author_email='guillcal@ucm.es',
    url='https://github.com/Guillermo-C-A/Hwmon-python',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['info', 'system_info', 'hardware_monitor'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
