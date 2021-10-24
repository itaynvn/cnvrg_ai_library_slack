
#  Slack channel integration

send a custom message to a slack channel using incoming webhook slack app.

## How It Works

Using Slack's built-in incoming webhook capabilities to send a message:
https://slack.dev/python-slack-sdk/webhook/index.html

## Running

1. Go here to create a [new slack app](https://api.slack.com/apps). 
Select **Create New App** -> **From Scratch**.
Choose a **Name** & **Workspace**.

2. Install app to workspace & choose the target slack channel.
From app page, select **Settings** -> **Install App**

3. Copy the **webhook URL** from the bottom of the page.

4. Define a new secret:
In your project, go to **Settings** -> **Secrets** -> **Add**. Set the secret's name to be ```SLACK_WEBHOOK_URL```, and the value to be the URL.

5. Choose the Slack AI Library component, and pass the text you'd wish to send, to "message" argument.
                                     
## Demo Inputs

Send a custom text message:
```
--message "this is my message"
```

Send the value of an environemnt variable:
```
--message $SOME_ENV_VAR
```

Send the value of a local variable within your code runtime:
```
--message local_variable
```

Send the value of a previous task's tag (read more about flow tags [here](https://app.cnvrg.io/docs/core_concepts/flows.html#tags-parameters-flow)):
```
--message {{training.length}}
```

## Example Demo Cmd-Line
You can use the following command to try the demo
[LINKS](../../../tools/README.md) ):
```
    python3 main.py
          
```
The demo will use a....
## Customizing the Slack app appearance
You can customize the "bot user" that will send the messages in your webhook app, by visiting the app page and going to **Settings** -> **Basic Information** -> then scroll to bottom for **Display Information**


## See Also
* [LINKS](../../README.md)

