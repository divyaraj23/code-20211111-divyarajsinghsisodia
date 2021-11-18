#BMI Calculator

###Description:
This app takes in a json formatted file with BMI data of people in the Gender,Height and Weight format.
And shows the number of overweight people as per the BMI matrix.


###Libraries used:
1. Pandas
2. Pytest

###Features:
- As it is using the vanilla pandas library, it can handle pretty much a large amount of BMI metric data (limit is your system memory). If in case the size is too much(>100 GB).
We can apply chunking which pandas inherently support, in case we have a line-delimited json.
- The script has some filters to remove erroneous rows (weght height being zero or exponentially large) causing a skew in data analysis.
- pytest test cases cover most of the scenarios ans more test cases can be added as required.

###CI/CD pipeline: 
The Github actions (python-package.yml) file lists jobs that checkout, lint, test and deploy the project as a tarball on the Python Package Index (PyPi) (PyPi Link : https://test.pypi.org/project/bmicalculator/1.0.0/).

(c) Divyaraj Singh Sisodia
