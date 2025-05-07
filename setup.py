from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="meu_pacote_python",
    version="1.0.8",
    author="Igor Pompeo",
    author_email="pompbass@gmail.com",
    description="Exercicios de Python - Curso em Video",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/igorpompeo/Python",
    packages=find_packages(include=["Mundo01", "Mundo01.*"]),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Mantenha por compatibilidade
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "colorama>=0.4.0",
        "emoji>=2.0.0",
    ],
    extras_require={
        "games": ["pygame>=2.0.0"],
        "dev": [
            "flake8",
            "black",
            "pytest",
            "coverage",
        ],
    },
    entry_points={
        "console_scripts": [
            "meupacote=meu_modulo:main",  # Se quiser criar um CLI
        ],
    },
)
