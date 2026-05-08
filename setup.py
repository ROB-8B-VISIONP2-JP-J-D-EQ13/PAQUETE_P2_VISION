from setuptools import setup, find_packages

setup(
    name="vision_p2",
    version="1.0",

    packages=find_packages(),

    install_requires=[
        "opencv-python",
        "matplotlib",
        "numpy"
    ],

    author="Pablo",

    description="Paquete para segmentacion y conteo de objetos",

    python_requires=">=3.10"
)