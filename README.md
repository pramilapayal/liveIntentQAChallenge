Steps to Execute Test Cases:

Install the requirements from the requirements.txt documents
pip3 install -r requirements.txt

To run the test case through pycharm
a. Load project in pycharm.
b. Select Edit Configuration from Run menu.
c. Select + option at the top of the config window.
d. Select Python test ->> py.test from the dropdown.
e. Select project directory in right side of the window.
f. Add additional parameters in pycharm : -sv --html=Reports/report.html  --self-contained-html
g. Select the Run option from the top.

To run the command from command prompt.
a. Navigate to the Checkout directory.
b. Run below command.
pytest -k validateStreamData --html=report.html
