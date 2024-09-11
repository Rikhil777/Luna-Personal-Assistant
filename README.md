Here’s a well-structured and detailed README file for your Luna Voice Assistant project:

```md
# Luna Voice Assistant

Luna is a Python-based personal voice assistant designed to make your life easier by assisting with various tasks like sending emails, playing music, fetching weather reports, browsing the web, and sending WhatsApp messages.

## Features
- **Wikipedia Search**: Get quick information from Wikipedia.
- **Open Applications**: Easily open Google Chrome, YouTube, and VS Code with voice commands.
- **Music Player**: Play your favorite songs from a pre-defined music directory.
- **Time Telling**: Ask Luna for the current time.
- **Send Emails**: Send emails to your contacts with simple voice commands.
- **Weather Updates**: Get the current weather for any city.
- **WhatsApp Messaging**: Send WhatsApp messages by specifying the contact and message.

## Prerequisites
- Python 3.x
- Libraries: You can install all required libraries using the following command:
  ```bash
  pip install pyttsx3 speechrecognition wikipedia webbrowser smtplib pywhatkit pyautogui
  ```

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/Rikhil777/Luna-Voice-Assistant.git
   ```
   
2. Navigate to the directory:
   ```bash
   cd Luna-Voice-Assistant
   ```

3. Run the script:
   ```bash
   python luna.py
   ```

4. Upon starting, Luna will greet you and ask for commands. Simply speak to interact with Luna!

## Voice Commands
- **Wikipedia Search**: "Search [query] on Wikipedia."
- **Open Applications**: "Open Google Chrome", "Open YouTube", or "Open VS Code."
- **Play Music**: "Play music" and choose the song from the directory.
- **Time**: "What's the time?"
- **Send Email**: "Send an email to [contact name]."
- **Weather**: "What's the weather like in [city]?"
- **WhatsApp**: "Send a WhatsApp message to [contact name]."

## Configuration

- **Contacts**: Edit the `email` and `contacts` dictionaries in the script to add your own email addresses and WhatsApp contacts.
- **Music Directory**: Update the `music_dir` variable with the path to your music folder.

## Future Improvements
- Integration with Google Contacts API for dynamic contact retrieval.
- GUI for more user-friendly interactions.
- Smarter error handling and response systems.

## Contributing
Feel free to fork this project, open issues, or create pull requests. Any contributions are welcome!

## Contact
For any questions or suggestions, feel free to contact me at:
- **Email**: kakanirikhil7@gmail.com
- **GitHub**: [Rikhil777](https://github.com/Rikhil777)
- **LinkedIn**: [Rikhil Kakani](https://www.linkedin.com/in/rikhil-kakani-1a139a212/)

---

*Thank you for using Luna!*
```

