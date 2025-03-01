# Steam Download Scheduler 

This script automatically starts Steam at a **specific time** (4 AM). It continuously checks the system time and launches Steam once the specified hour is reached.

## How It Works
1. **Time Check**: The script checks the current system time.
2. **Loop Until 4 AM**: It runs a loop until the system time reaches 4 AM.
3. **Launches Steam**: Once 4 AM is reached, it runs `steam.exe` using the `subprocess` module.

## Dependencies
This script only uses built-in Python modules:
- `subprocess`
- `time`
- `datetime`

## Running the Script
Ensure that Steam is installed and the executable (`steam.exe`) is in the system's PATH.
Run the script using:
```sh
python main.py
```

## Customization
- Change the target time by modifying this line:
  ```python
  while int(x.strftime("%H")) != 4:
  ```
  Replace `4` with your desired hour.
- If Steam is installed in a different location, modify the `command` variable accordingly.

## Notes
- The script must remain running for it to function.
- Ensure Python is installed and added to your system PATH.

## Author
This script was developed for automating Steam startup at a specific time.

