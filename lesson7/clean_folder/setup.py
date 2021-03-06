import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clean_package_misha_sid", # Replace with your own username
    version="1.0.0",
    author="misha_sid",
    author_email="mishasydorchuk@gmail.com",
    description="Sort the folder identified by its Window path",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    entry_points={'console_scripts': ['sort_folder = clean_folder.clean:sort_folder']}
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "clean_folder"},
    packages=setuptools.find_packages(where="clean_folder"),
    python_requires=">=3.6",
)
