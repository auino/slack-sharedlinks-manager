# slack-sharedmessages-manager

`slack-sharedmessages-manager` is a tool to manage messages shared on [Slack](https://slack.com).

This program allows you to extrapolate shared messages from selected Slack channels and manage them.
A simple manager is provided, storing retrieved links to file.
Other managers may be implemented, i.e., to export shared links or pictures on social networks or social bookmarking services.

This project is a fork of [auino/slack-downloader](https://github.com/auino/slack-downloader), used for a different purpose.

### Requirements ###

* `Slack API Token`: Get it from (https://api.slack.com/web)
* `Python`: The app is written in Python
* `python-requests`: web request library for Python

### Installation Instructions ###

1. Clone the project:

   ```
   git clone https://github.com/auino/slack-sharedmessages-manager.git
   ```

2. Make `slack-sharedmessages-manager.py` executable:

   ```
   cd slack-sharedmessages-manager
   chmod +x slack-sharedmessages-manager.py
   ```

3. Open the `config.py` script with a text editor and configure it accordingly to your needs
4. Optionally, you can add the program to your `crontab` to automatically check for new shared messages on Slack:

   ```
   crontab -e
   ```

5. Now you have to append the following line (press `i` button to insert data):

   ```
   0 * * * * python /directory_path/slack-sharedmessages-manager.py
   ```

   where `/directory_path/` identifies the path of the directory containing the script, while `0 *` specifies the program has to be called every hour.
6. Hit `:q` to close, saving the file
7. Enjoy!

### Extensions ###

You can extend the program by implementing your own messages manager.
In order to do that, you have to implement a `managemessage(channel, user, data)` function.
Then you have to include the function on the main `slack-sharedmessages-manager.py` file.
For more information, check the `linkmanager.py` sample file.

### Contacts ###

You can find me on Twitter as [@auino](https://twitter.com/auino).
