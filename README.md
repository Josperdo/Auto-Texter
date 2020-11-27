# text-messages
Send your automated text messages. I plan on expanding this in some form to provide automated daily digests every morning pertaining to various interests based on the user (stocks, economics, news, sports stats, etc.) Also wouldn't be limited to apple devices using Imsg

Note: this script will only work if you have a Mac

In `send.scpt` you'll find an applescript that tells your laptop to send a message through iMsg:
```
on run {targetPhoneNumber, targetMessageToSend}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetPhoneNumber of targetService
        set targetMessage to targetMessageToSend
        send targetMessage to targetBuddy
    end tell
end run
```
Call this through `main.py`:
```
os.system('osascript send.scpt {} "{}"'.format(phone_number, message))
```

This tells your computer to run the defined applescript (given phone number and message). Allows us to send one word at a time with a for loop.
