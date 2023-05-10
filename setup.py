#!/usr/bin/python3
import setuptools

setuptools.setup(
    name='Surfshark VPN GUI',
    version='1.1',
    description='Surfshark VPN GUI',
    keywords='vpn',
    author='Jake Day',
    contributor='Quentin Lienhardt',
    url='https://github.com/Quentium-Forks/Surfshark-VPN-GUI/',
    python_requires='>=3.7',
    include_package_data=True,
    data_files=[
        ('/usr/share/icons/hicolor/scalable/apps', ['surfsharkgui/assets/surfsharkgui.png']),
        ('/usr/share/applications', ['surfsharkgui/assets/surfsharkgui.desktop'])
    ],
    package_data={
        '': ['assets/*']
    },
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'surfsharkvpngui=surfsharkgui:main',
        ],
    },
)
