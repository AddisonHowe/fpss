from setuptools import setup, find_packages

setup(
    name="fpss",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fpss = fpss.__main__:main",
        ]
    },
)
