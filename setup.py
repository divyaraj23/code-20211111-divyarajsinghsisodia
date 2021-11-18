from setuptools import setup, find_packages

setup(
    name="bmicalculator",
    version="1.0.1",
    author="Divyaraj Singh Sisodia",
    author_email="sisodia.divyarajsingh@gmail.com",
    url="https://www.divyaraj.tech",
    long_description="Calculates the Body Mass Index from a list of people and assigns the requisite category and risk",
    packages=find_packages(),
    install_requires=["pandas","numpy"],
    setup_requires=['flake8','pytest-runner'],
    tests_require=['pytest'],
    package_data={'BMICalculator': ['weightheight.json']}
)
