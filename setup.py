"""setup.py file."""
import uuid
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

from setuptools import find_packages, setup


__author__ = 'Shem Valentine <shem.valentine@vivint.com>'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
try:
    reqs = [str(ir.req) for ir in install_reqs]
except AttributeError:
    reqs = [str(ir.requirement) for ir in install_reqs]


setup(
    name="napalm-cumulus",
    version="4.0.1",
    packages=find_packages(exclude=["test", "test.*"]),
    author="Shem Valentine",
    author_email="shem.valentine@vivint.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://source.vivint.com/projects/POPS/repos/napalm-cumulus/browse",
    include_package_data=True,
    install_requires=reqs,
)
