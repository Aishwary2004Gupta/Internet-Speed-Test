import speedtest

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes / MB)

st = speedtest.Speedtest()

input("Press Enter to start the speed test")  # Removed unused variable 'start'
download_speed = str(bytes_to_mb(st.download()))
upload_speed = str(bytes_to_mb(st.upload()))
ping = st.results.ping

print(f"Download Speed: {download_speed} MB/s")
print(f"Upload Speed: {upload_speed} MB/s")
print(f"Ping: {ping} ms")