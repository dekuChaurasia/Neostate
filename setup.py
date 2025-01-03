from setuptools import setup, find_packages

setup(
    name="Neostate",  # Replace with your library's unique name
    version="0.1.0",  # Start with an initial version
    author="Deku Chaurasia",
    author_email="angryg575@gmail.com",
    description="Welcome to Neostate! 🌈 A lightweight and intuitive library for managing shared states in Flet applications. With StateCraft, you can bind widgets to a shared state effortlessly, enabling seamless updates across your UI components with minimal boilerplate.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dekuChaurasia/Neostate",  # Add your GitHub repo URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
