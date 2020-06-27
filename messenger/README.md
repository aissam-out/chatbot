# Messenger Chatbot

<p>
<img src="./images/messenger.png" alt="messenger" width="100" height="100" align="right">
  
[Messenger](https://www.messenger.com) is an American messaging app and platform developed by Facebook, it enables users to send messages and exchange photos, videos, stickers, audio, and files. 

In this project we will build a Messenger Chatbot using Twilio Autopilot.
</p>


## Twilio

<p align="center">
<img src="./images/twilio.png" alt="twilio" width="350" height="100">
</p>

[Twilio](https://www.twilio.com) is a cloud communications platform as a service (CPaaS) company which allows software developers to programmatically make and receive phone calls, send and receive text messages, and perform other communication functions using its web service APIs.

Before starting this project, make sure you have a Facebook Page for your brand or business, and the Messenger App installed in your phone. If so, the following steps will walk you through the process of creating and configuring your Facebook Messenger channel on Twilio, and then to link it with your FB page :

Make sure you have created an Autopilot assistant to power the Facebook Messenger Bot.

## Create and configure the Autopilot assistant

**1.** Create a [Twilio account](https://www.twilio.com/try-twilio)

**2.** Create a [new project](https://www.twilio.com/console/projects/create)
      
**3.** On project console, open **Autopilot**, then create a new bot _from scratch_ if you don't have one.

<img src="./images/createbot.PNG" alt="create bot">

**4.** In the dashboard of your bot, select _Tasks_ on the left menu. 

A bot usually has many tasks that power it. These could be simple tasks like confirm or cancel or more complex tasks like make-a-reservation

**5.** CLick on _Add a task_ and give it a (meaningful) name. Create as many tasks as your bot have to handle.

Every task has two main features _Program_ and _Train_

<img src="./images/tasks.PNG" alt="tasks">

**Program** helps you program the actions your bot will perform in a given task. You need to replace the JSON text with your proper needs. for instance if you want to answer by a static text, change the text after **"say" :** by whatever you want your bot to say when this task is called :

```
{
    "actions": [
        {
            "say": "Hello, how can I help you?"
        }
    ]
}
```

If you want to execute a distant code or call an API :

```
{
	"actions": [
		{
			"redirect": "PUT THE URL HERE"
		}
	]
}
```

**Train** Click on this button to add the expressions that will trigger this task. Add as many samples as possible so that your bot can map human input to the task.

<img src="./images/train.PNG" alt="tasks">

:warning: DO NOT FORGET to click **BUILD MODEL** whenever you make changes to your bot

## Link the assistant to your Facebook Messenger 

you can build Facebook Messenger bots. On this page, we'll walk you through how to link your Facebook account to Autopilot so you can get started building your Facebook Messenger bot.
