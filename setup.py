import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="ankit_test_pa",
    version="0.0.1",
    author="Ankit",
    author_email="author@example.com",
    description="A small example package",
    long_description='long_description',
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",

    packages=['src'],
    python_requires=">=3.6",
)
