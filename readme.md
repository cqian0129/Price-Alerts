# Pricing Service

This is an application built to allow the periodic scanning of online webstores, to notify users of changes in prices of items they select.

It allows administrators (defined via `src/config.py`) to add, remove, and edit online stores.

E-mails are sent via executing the `src/alert_updater.py` file. In order to check e.g. every 10 minutes, the file must be executed every 10 minutes. This can be done with a cron job or a Windows service.

It parses the store websites using `requests` and `BeautifulSoup`.

It allows users to register, log in, and create and modify their alerts.

Technology stack: MongoDB, Python (Flask & Jinja2), HTML/CSS/Bootstrap, Mailgun.


