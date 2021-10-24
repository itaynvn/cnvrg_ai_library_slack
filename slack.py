from argparse import ArgumentParser, SUPPRESS
from slack_sdk.webhook import WebhookClient
import os

def slack(webhook_url,message):
    webhook = WebhookClient(webhook_url)
    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"
    
#TODO --- ADD your imports Classes and methods

if __name__ == '__main__':
    parser = ArgumentParser(add_help=False)
    # TODO --- ADD your parameters
    parser.add_argument('-h', '--help', action='help', default=SUPPRESS, help='Show this help message and exit.')
    parser.add_argument('-m', '--message', action='store', help="the string that will be sent as message to the slack channel",
                      required=True, type=str)

    args = parser.parse_args()

    print(args)
    print("TEMPLATE AI COMPONENT WORKS!!")
    #TODO --- execut your AI Component code
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    slack(webhook_url,args.message)
