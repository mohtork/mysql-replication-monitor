# MySQL Replication Monitor
Monitor MySQL replication and send alerts to slack
## Usage
Clone the repository:
    $ git clone https://github.com/mohtork/mysql-replication-monitor.git && cd mysql-replication-monitor
    $ pip -r requirments.txt
    $ add mysql & slack info in conf/setup.ini file
    $ add a crontab to excute the script

## Inputs
 Inputs | Description ---------------------------|----------------------------------------------------------------------------------------
 `mysql_host` | mysql hostname or ip
 `mysql_user` | mysql username
 `mysql_password` | mysql password
 `slack_webhook_url` | slack webhook url
 `slack_channel` | slack channel which you will send alerts to
 `slack_username` | slack user who will post the alert message
