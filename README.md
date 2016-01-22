# slack-sharedlinks-manager

`slack-sharedlinks-manager` is a tool to manage links shared on [Slack](https://slack.com).

This program allows you to extrapolate shared links from selected Slack channels and manage them.
A simple manager is provided, storing retrieved links to file.
Other managers may be implemented, i.e., to export shared links on social networks or social bookmarking services.

This project is a fork of [auino/slack-downloader](https://github.com/auino/slack-downloader), used for a different purpose.

### Requirements ###

* `Slack API Token`: Get it from (https://api.slack.com/web)
* `Python`: The app is written in Python
* `python-requests`: web request library for Python

### Installation Instructions ###

1. Clone the project:

   ```
   git clone https://github.com/auino/slack-sharedlinks-manager.git
   ```

2. Make `slack-sharedlinks-manager.py` executable:

   ```
   cd slack-sharedlinks-manager
   chmod +x slack-sharedlinks-manager.py
   ```

3. Open the `config.py` script with a text editor and configure it accordingly to your needs
4. Optionally, you can add the program to your `crontab` to automatically check for new shared links on Slack:

   ```
   crontab -e
   ```

5. Now you have to append the following line (press `i` button to insert data):

   ```
   0 * * * * python /directory_path/slack-sharedlinks-manager.py
   ```

   where `/directory_path/` identifies the path of the directory containing the script, while `0 *` specifies the program has to be called every hour.
6. Hit `:q` to close, saving the file
7. Enjoy!

### Extensions ###

You can extend the program by implementing your own link manager.
In order to do that, you have to implement a `savelink(channel, user, data)` function.
Then you have to include the function on the main `slack-sharedlinks-manager.py` file.
For more information, check the `linkmanager.py` file.

### Contacts ###

You can find me on Twitter as [@auino](https://twitter.com/auino).
