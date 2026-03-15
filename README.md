# 🤖 Game Automation Bot (PyAutoGUI)

A Python automation bot that uses **image recognition and screen automation** to perform repetitive in-game actions automatically.

The bot detects UI elements on the screen (buttons, icons, ads, confirmations, etc.) and clicks them in sequence to automate gameplay actions such as **attacking, confirming actions, handling ads, and skipping timers**.

---

# 🚀 Features

* 🖱️ **Automated Clicking** using PyAutoGUI
* 🖼️ **Image Recognition** for detecting UI elements
* ⚡ **Dynamic Wait System** that adjusts based on detection speed
* 📢 **Automatic Ad Closing**
* ⏩ **Timeskip Handling**
* 🔁 **Iterative Automation Loop**
* 📄 **Logging System** to track bot activity
* 🧠 **Human-like Click Offsets** to avoid robotic behavior
* 🛑 **Failsafe Exit (Press `Q`)**

---

# 🛠️ Tech Stack

* **Python**
* **PyAutoGUI**
* **Keyboard**
* **OpenCV (for image recognition confidence)**
* **Datetime**
* **Random**

---

# 📂 Project Structure

```
project/
│
├── bot.py                # Main automation script
├── images/               # UI element images used for detection
│   ├── messages.png
│   ├── archive.png
│   ├── notifications.png
│   ├── locate.png
│   ├── attack.png
│   ├── confirm.png
│   ├── preset.png
│   ├── applypreset.png
│   ├── cross.png
│   ├── confirm2.png
│   ├── confirmattack.png
│   ├── timeskip.png
│   ├── rubyskip.png
│   └── adtemplate*.png
│
├── success_marker.png
├── nomad_bot_log.txt
└── README.md
```

---


# ⚠️ Disclaimer

This project is created **for educational purposes only** to demonstrate:

* Python automation
* Computer vision based UI detection
* Workflow automation

Use responsibly and ensure it complies with the game's terms of service.

---

# 👨‍💻 Author

**Masif Ahmed**

