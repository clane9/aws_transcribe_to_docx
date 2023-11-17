import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="tscribe",
    version="1.3.1",
    author="Robert Williams",
    author_email="robertedwardwilliams@me.com",
    description="Produce Word Document, CSV, SQLite and VTT transcriptions using the automatic speech recognition from AWS Transcribe.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kibaffo33/aws_transcribe_to_docx",
    packages=setuptools.find_packages(),
    install_requires=["python-docx", "matplotlib", "pandas", "webvtt-py"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "tscribe = tscribe.__main__:main",
        ]
    }   ,
)
