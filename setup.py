from setuptools import find_packages, setup

setup(
    name="meu_pacote_python",  # 🔁 troque pelo nome único no PyPI
    version="1.0.7",
    author="Igor Pompeo",
    author_email="pompbass@gmail.com",
    description="Exercícios de Python - Curso em Vídeo",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/igorpompeo/Python",
    packages=find_packages(include=["Mundo01", "Mundo01.*"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
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
