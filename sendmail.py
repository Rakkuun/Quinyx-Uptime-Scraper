import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_status_email():
    message = Mail(
        from_email='sjtenkate@live.nl',
        to_emails='sander.tenkate@coolblue.nl',
        subject='One or more HR Systems report issues',
        html_content='<strong>Check if current HR Systems are operational.</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.body)
