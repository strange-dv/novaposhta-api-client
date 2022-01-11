from distutils.core import setup


setup(
  name = 'novaposhta',
  packages = ['novaposhta'],
  version = '0.0.9',
  license='MIT',
  description = 'Python client for Nova Poshta company\'s API.',
  author = 'andrii dovzhenko',
  author_email = 'andrii.dovzhenko.dv@gmail.com',
  url = 'https://github.com/strange-dv/novaposhta-api-client',
  download_url = 'https://github.com/strange-dv/novaposhta-api-client/archive/refs/tags/v0.0.9.tar.gz',
  keywords = ['nova', 'poshta'],
  install_requires=[
        'requests',
    ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.10',
  ],
)
