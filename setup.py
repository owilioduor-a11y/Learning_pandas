from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="learning_pandas",
    version="0.1.0",
    author="Peter Owili",
    author_email="owilioduor@gmail.com",
    description="A hands-on learning repository for data analysis and manipulation using pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/owilioduor-a11y/Learning_pandas",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Data Analysis",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.22.0",
        "jupyter>=1.0.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0.0", "black>=22.0", "flake8>=4.0"],
    },
)