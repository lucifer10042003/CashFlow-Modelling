from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="cashflows",
    version="0.1.0",
    description="Investment modeling and advanced engineering economics using Python",
    long_description="Investment modeling and advanced engineering economics using Python",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Topic :: Office/Business :: Financial",
    ],
    keywords="cashflow investments bonds depreciation loan irr",
    author_email="Techbeast1004@gmail.com",
    license="MIT",
    packages=["cashflows"],
    test_suite="nose.collector",
    tests_require=["nose"],
    include_package_data=True,
    zip_safe=False,
)
