## THE EXE CURRENTLY DOES NOT SEND NOTIFICATIONS AND HAS ISSUES BLOCKING OPERAGX I AM WORKING ON IT WAIT FOR V2

# Opera Blocker

Opera Blocker is a Python application that monitors your Downloads folder for opera and prevents it from being downloaded.

## Features

- Monitors the Downloads folder for new files.
- Auto-deletes that annoying spyware opera
- User-friendly GUI with a toggle button to start and stop monitoring.
- Notifications for actions taken on files.

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `watchdog`
  - `plyer`
  - `tkinter` (included with Python)

## Installation

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Install the required packages using pip:

   ```bash
   pip install watchdog plyer
   ```

## Usage

1. Run the application:

   ```bash
   python file_blocker.py
   ```

2. The application will start monitoring the Downloads folder automatically.
3. Use the toggle button to start or stop monitoring.

## Auto Start on Windows

To make the application start automatically when your PC boots up:

1. Create a shortcut for `operaisass.py` or `operaisass.exe`.
2. Place the shortcut in the Windows Startup folder. You can access the Startup folder by pressing `Win + R`, typing `shell:startup`, and pressing Enter.
3. The application will now run at startup, monitoring your Downloads folder.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to not have opera on your system
