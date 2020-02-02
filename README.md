# MySQL Replication Monitor

Monitor MySQL replication and send alerts to slack

## Usage

Clone the repository:

    $ git clone https://github.com/mohtork/mysql-replication-monitor.git && cd mysql-replication-monitor

Install requirments:

    $ pip install -r requirments 

Edit setup.ini:

    $ add mysql & slack info in conf/setup.ini file

Add cronjob:

    $ add a crontab to excute the script

## Inputs


 Inputs                    | Description
---------------------------|----------------------------------------------------------------------------------------
 `mysql_host`              | It could be hostname or IP
 `mysql_username`          | MySQL username
 `mysql_password`          | MySQL password
 `slack_webhook_token`     | Slack webhook token
 `slack_channel`           | Slack channel that the script will send alert to 
 `slack_username`          | Slack username who will post the alert message
