import os
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from plyer import notification
import tkinter as tk

class FileBlockerHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        print(f"Detected new file: {file_path}")
        if "OperaSetup" in os.path.basename(file_path) or "OperaGXSetup" in os.path.basename(file_path):
            self.delete_file(file_path)
        else:
            self.block_file(file_path)

    def block_file(self, file_path):
        try:
            os.chmod(file_path, 0o444)
            print(f"Blocked file: {file_path}")
            self.send_notification(file_path, action='blocked')
        except Exception as e:
            print(f"Error blocking file: {e}")

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
            self.send_notification(file_path, action='deleted')
        except Exception as e:
            print(f"Error deleting file: {e}")

    def send_notification(self, file_path, action='blocked'):
        notification.notify(
            title='File Action',
            message=f'The file {file_path} has been {action} successfully.',
            timeout=10,
        )

class FileBlockerApp:
    def __init__(self, master):
        self.master = master
        master.title("File Blocker")
        self.label = tk.Label(master, text="File Blocker is running.")
        self.label.pack()
        self.toggle_button = tk.Button(master, text="Stop Monitoring", command=self.toggle_monitoring)
        self.toggle_button.pack()
        self.is_monitoring = False
        self.observer = None
        self.start_monitoring()

    def toggle_monitoring(self):
        if self.is_monitoring:
            self.stop_monitoring()
        else:
            self.start_monitoring()

    def start_monitoring(self):
        if not self.is_monitoring:
            self.is_monitoring = True
            self.label.config(text="Monitoring for downloaded files...")
            self.toggle_button.config(text="Stop Monitoring")
            threading.Thread(target=self.run_monitoring, daemon=True).start()

    def stop_monitoring(self):
        if self.is_monitoring:
            self.is_monitoring = False
            self.label.config(text="File Blocker is not running.")
            self.toggle_button.config(text="Start Monitoring")
            if self.observer:
                self.observer.stop()
                self.observer.join()

    def run_monitoring(self):
        path = os.path.join(os.path.expanduser('~'), 'Downloads')
        event_handler = FileBlockerHandler()
        self.observer = Observer()
        self.observer.schedule(event_handler, path, recursive=False)
        self.observer.start()
        print(f"Monitoring {path} for new files...")
        try:
            while self.is_monitoring:
                time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = FileBlockerApp(root)
    root.mainloop()
