import pyautogui
import time
import keyboard
import sys
import random
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

# === Configurable Parameters ===
MAX_ITERATIONS = 200
CLICK_DELAY = 0.6
BASE_WAIT_TIMEOUT = 1.2
CONFIDENCE_LEVEL = 0.85
LOG_FILE = "nomad_bot_log.txt"

# Icons list
step_icons = [
    "messages.png",
    "archive.png",
    "notifications.png",
    "locate.png",
    "attack.png",
    "confirm.png",
    "preset.png",
    "applypreset.png",  # After this, look for cross.png
    "cross.png",
    "confirm2.png",
    "7.png",
    "confirmattack.png"
]

# === Ads and Other Icons ===
ad_templates = [
    "adtemplate1.png",
    "adtemplate2.png", 
    "adtemplate4.png",
    "adtemplate5.png",
    "adtemplate6.png",
    "adtemplate7.png",
    "adtemplate8.png"
]
timeskip_icon = "timeskip.png"
rubyskip_icon = "rubyskip.png"
cross_icon = "cross.png"

# === Regions ===
timeskip_region = (893, 543, 133, 195)
cross_region = (1077, 179, 170, 155)

# === Logging ===
def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_msg = f"{timestamp} {message}"
    print(log_msg)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_msg + "\n")

# === Click with Human Offset ===
def human_click(x, y):
    offset_x = random.randint(-5, 5)
    offset_y = random.randint(-5, 5)
    pyautogui.click(x + offset_x, y + offset_y)

# === Wait and Click with Timeout ===
def wait_and_click(image, timeout, region=None, grayscale=True):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if keyboard.is_pressed('q'):
            log("Failsafe (Q) triggered. Exiting.")
            sys.exit()
        try:
            found = pyautogui.locateCenterOnScreen(image, confidence=CONFIDENCE_LEVEL, region=region, grayscale=grayscale)
            if found:
                log(f"Found {image} at {found}")
                human_click(found.x, found.y)
                time.sleep(CLICK_DELAY)
                return time.time() - start_time
        except Exception as e:
            log(f"Error searching for {image}: {str(e)}")
        time.sleep(0.1)
    log(f"Timeout waiting for {image}")
    return -1

# === Ad Closing Functions === 
def close_ads():
    for ad in ad_templates:
        try:
            found = pyautogui.locateCenterOnScreen(ad, confidence=0.7, grayscale=True)
            if found:
                human_click(found.x, found.y)
                log(f"Closed ad: {ad}")
                time.sleep(0.5)
        except:
            continue

# === Timeskip Handling ===
def handle_timeskip():
    # First try to find and click timeskip icon
    elapsed = wait_and_click(timeskip_icon, 1.5, timeskip_region)
    if elapsed == -1:
        # If timeskip not found, try rubyskip
        elapsed = wait_and_click(rubyskip_icon, 1.0, timeskip_region)
    return elapsed != -1

# === Main Loop ===
print("Starting in 5 seconds...")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

log("Bot started.")
dynamic_wait = BASE_WAIT_TIMEOUT
consecutive_failures = 0

for iteration in range(MAX_ITERATIONS):
    log(f"\n--- Iteration {iteration + 1} ---")
    failed = False

    # === STAGE 1: Initial sequence ===
    for icon in step_icons[:4]:  # 1.png, 2.png, attack.png, confirm.png
        elapsed = wait_and_click(icon, dynamic_wait)
        if elapsed == -1:
            log(f"[FAIL] {icon} not found")
            failed = True
            break
        dynamic_wait = min(2.0, elapsed * 1.5)  # Dynamic adjustment

    if failed:
        close_ads()
        consecutive_failures += 1
        if consecutive_failures >= 3:
            log("Too many consecutive failures, trying timeskip")
            if handle_timeskip():
                consecutive_failures = 0
                continue
            else:
                log("Failed to find timeskip option")
                break
        continue

    # === STAGE 2: Completion sequence ===
    for icon in step_icons[4:]:  # cross.png through confirmattack.png
        elapsed = wait_and_click(icon, dynamic_wait)
        if elapsed == -1:
            log(f"[WARNING] {icon} not found (continuing)")
            continue
        
        # Special handling for cross.png
        if icon == "cross.png":
            cross_delay = random.uniform(0.5, 1.0)
            log(f"Waiting {cross_delay:.2f}s after cross...")
            time.sleep(cross_delay)
    
    # === Timeskip check ===
    handle_timeskip()
    
    # === Final verification ===
    log("Checking for completion...")
    try:
        if pyautogui.locateOnScreen("success_marker.png", confidence=0.7):
            log("[SUCCESS] Attack completed")
            consecutive_failures = 0
        else:
            log("[UNKNOWN] Completion uncertain")
    except:
        log("Completion check failed")

    # === Cooldown ===
    cooldown = random.uniform(16, 21)
    log(f"Cooldown: {cooldown:.2f} seconds")
    time.sleep(cooldown)

log("Script finished")
