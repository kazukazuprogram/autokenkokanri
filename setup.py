from setuptools import setup

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="autokenkokanri",
    version="0.0.0",
    license="MIT",
    author="kazukazuprogram",
    packages=["autokenkokanri"],
    package_dir={"autokenkokanri": "src"},
    description="Auto Kenko Kanro.",
    long_description=long_description,
    install_requires=open("requirements.txt").read().strip().splitlines(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: Japanese",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "autokenkokanri = autokenkokanri.__main__:main",
        ]
    }
)
