from setuptools import setup

install_requires = [
    # 必要な依存ライブラリがあれば記述
]

packages = [
    'sample_lib',
    'sample_lib.submodule',
    'sample_lib_cli',
]

console_scripts = [
    'sample_lib_cli=sample_lib_cli.call:main',
]


setup(
    name='sample_lib',
    version='0.0.0',
    packages=packages,
    install_requires=install_requires,
    entry_points={'console_scripts': console_scripts},
)
