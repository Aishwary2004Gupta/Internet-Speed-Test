import speedtest

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes / MB)

st = speedtest.Speedtest()

start = input("Press Enter to start the speed test")
download_speed = str(bytes_to_mb(st.download()))