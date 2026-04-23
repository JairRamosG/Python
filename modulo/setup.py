from setuptools import setup

setup(
    name = "paquete_calculos",
    version = "1.0",
    description = "Este es un paquete que hace algunos calculos",
    author = "Jair",
    author_email = "ramosgonzalezjair@gmail.com",
    packages = ['paquete_calculos',
                'paquete_calculos.subpaquete_basicos',
                'paquete_calculos.subpaquete_extras']  

)