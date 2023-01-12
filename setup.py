from setuptools import setup

dev = [
    "black>=22.12.0",
    "flake8>=6.0.0",
    "isort",
    "pytest==7.2.0",
    "pyyaml",
    "setuptools<=59.5.0",
    "typing>=3.7.4.3",
]

setup(
    author="Toribird.tech",
    author_email="toribird.tech@gmail.com",
    description="Python coding prep repo",
    include_package_data=True,
    install_requires=dev,
    license="GNU General Public License v3.0",
    name="coding-prep",
    package_dir={"": "src"},
    version=1.0,
)