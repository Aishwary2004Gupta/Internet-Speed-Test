# Internet-Speed-Test

This Python script measures your internet speed by calculating the download speed, upload speed, and ping time using the `speedtest` library. It's a simple and effective way to test your network performance directly from the terminal.


## Features

- Measures **Download Speed** (in MB/s).
- Measures **Upload Speed** (in MB/s).
- Displays the **Ping** (in milliseconds).
- User-friendly interface to start the test.

## Prerequisites

- **Python**: Ensure you have Python 3.x installed on your system.
- **speedtest-cli**: This script uses the `speedtest` library. Install it via pip if not already installed.

```bash
pip install speedtest-cli
```

## How to Use

1. Clone or download the script.
2. Open a terminal in the script's directory.
3. Run the script using Python:

   ```bash
   python speedtest_script.py
   ```

4. Follow the on-screen instructions to start the speed test.

## Output

The script will display the following details:

- **Download Speed**: The download speed in MB/s.
- **Upload Speed**: The upload speed in MB/s.
- **Ping**: The ping time in milliseconds.

## Error Handling

The script includes basic error handling for:
- Failed configurations due to network issues.
- Unexpected errors during execution.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

