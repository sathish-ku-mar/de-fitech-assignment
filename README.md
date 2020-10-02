# de-fitech-assignment
### System Requirements
- Python 3+
------------
### 1. Clone project to the local machine
In the terminal, navigate to the location where the project folder has to be created. Then enter the git command to clone the project:<br />`$ git clone https://github.com/sathish-ku-mar/de-fitech-assignment.git`<br />
Once cloned, change the directory to **de-fitech-assignment**<br />`$ cd de-fitech-assignment`

------------
### 2. Install the project requirements
Install the python packages listed in the **requirements.txt** file.
Enter the following command in the terminal:<br />`$ pip install -r requirements.txt`

------------

### 3. Add crontab to the projects
To add crontab to the project, run the following command:<br />`$ crontab -e`<br />
Enter the following line in the crontab editor for run jobs every 15mins:<br />`$ 15 * * * * cd Desktop/de-fitech-assignment && /usr/bin/python3.6 task.py`<br />
Enter the following line in the crontab editor for run jobs every 1 hour:<br />`$ * 1 * * * cd Desktop/de-fitech-assignment && /usr/bin/python3.6 orderbook.py`

------------
### 4. To see the results stored in the influxdb
Enter the following command in the terminal:<br />`$ python3 db_result.py`

------------
