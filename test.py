import speedtest

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes / MB)

try:
    st = speedtest.Speedtest()
    st.get_servers()  # Get a list of available servers
    st.get_best_server()  # Select the best server based on ping
    input("Press Enter to start the speed test")  # Removed unused variable 'start'
    download_speed = str(bytes_to_mb(st.download()))
    upload_speed = str(bytes_to_mb(st.upload()))
    ping = st.results.ping

    print(f"Download Speed: {download_speed} MB/s")
    print(f"Upload Speed: {upload_speed} MB/s")
    print(f"Ping: {ping} ms")
except speedtest.ConfigRetrievalError as e:
    print(f"Failed to retrieve speedtest configuration: {e}")
except Exception as e:
    print(f"An error occurred: {e}")