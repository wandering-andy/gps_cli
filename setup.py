from setuptools import setup

setup(
    name='gps_cli',
    version='0.1.0',
    py_modules=['gps_cli'],
    install_requires=[
        'click',
        'gps',
        'time',
        'os',
    ],
    entry_points={
        'console_scripts': [
            'gps_cli = gps_cli:cli',
        ],
    },
)
