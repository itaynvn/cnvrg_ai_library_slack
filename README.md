
#  Slack channel integration

send a custom message to a slack channel using incoming webhook slack app.

## How It Works

Using Slack's built-in incoming webhook capabilities to send a message:
https://slack.dev/python-slack-sdk/webhook/index.html

## Running

1. Create a dedicated slack app: [](https://api.slack.com/apps)[https://api.slack.com/apps](https://api.slack.com/apps)

2. Install to workspace & choose the target slack channel.

3. Activate incoming webhooks & copy webhook URL

4. Define the slack incoming webhook URL as a secret in your cnvrg project:
```
SLACK_WEBHOOK_URL
```

5. Choose the Slack AI Library component, and pass the text you'd wish to send, to "message" argument.
                                     

Options:
  -h, --help            Show this help message and exit.
  -m, --message         The content of the message you'd like to send
 
```

> **NOTE**: Before running the demo with 

## Demo Inputs

The application .....
## Demo Outputs
The application outputs 

## Example Demo Cmd-Line
You can use the following command to try the demo
[LINKS](../../../tools/README.md) ):
```
    python3 main.py
          
```
The demo will use a....
## Demo Performance


## See Also
* [LINKS](../../README.md)

