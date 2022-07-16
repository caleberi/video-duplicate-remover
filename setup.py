from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="video-cleaner",
    version="0.1.0",
    description="A video cleaning cli application",
    license="MIT",
    long_description=long_description,
    author="caleb eri",
    author_email="caleberioluwa@gmail.com",
    url="https://github.com/caleberi/video-cleaner",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "black",
    ],
    entry_points={"console_scripts": ["video-cleaner-cli = command.main:cli"]},
)
