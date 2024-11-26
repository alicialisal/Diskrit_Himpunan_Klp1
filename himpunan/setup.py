from setuptools import setup, find_packages

setup(
    name="himpunan",
    version="0.1.0",
    description="Library untuk operasi himpunan di Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="alicia_michael_feli_calvin",
    author_email="ajuanita@student.ciputra.ac.id",
    url="https://github.com/alicialisal/Diskrit_Himpunan_Klp1.git",  # Ganti dengan repo Anda
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
