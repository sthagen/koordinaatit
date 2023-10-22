# [[[fill git_describe()]]]
__version__ = '2023.10.22+parent.1ccad3f7'
# [[[end]]] (checksum: 3c4b47bcb7a39a589a2d51e1a775f7f3)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
