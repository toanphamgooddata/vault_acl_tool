#!/usr/bin/env python

from setuptools import setup
import subprocess
import os

with open('./PKG-INFO') as fh:
    readme = fh.read()

if os.path.isfile('VERSION'):
    with open('VERSION') as fh:
        ver = fh.read()
else:
    p = subprocess.Popen("git describe --tags --match '*.*.*' | tr -- '-' '_'", shell=True, stdout=subprocess.PIPE)
    ver, err = p.communicate()
ver = ver.strip()

setup(
    name='vault_acl_tool',
    version=ver,
    packages=['vault_acl_tool',
              'vault_acl_tool.actions',
              'vault_acl_tool.actions.load',
              'vault_acl_tool.actions.connect',
              'vault_acl_tool.actions.validate',
              'vault_acl_tool.actions.apply'],
    entry_points={
        'console_scripts': [
            'vault-acl-tool = vault_acl_tool:main',
        ]
    },
    license='proprietary',
    author='Toan Pham',
    author_email='toan.pham@gooddata.com',
    maintainer='GoodData Corporation',
    maintainer_email='python@gooddata.com',
    description='A tool for importing vault policies to vault server',
    long_description=readme,
    url='https://github.com/gooddata/vault_acl_tool',
    download_url='https://github.com/gooddata/vault_acl_tool',
    platform='POSIX',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    install_requires=['argparse',
                      'hvac',
                      'json_schema',
                      'logging',
                      'yaml'
                     ]
)

