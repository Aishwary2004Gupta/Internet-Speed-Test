async function startSpeedTest() {
    const results = document.getElementById("results");
    results.style.display = "none";

    try {
        const response = await fetch("http://127.0.0.1:5000/api/speedtest");
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        document.getElementById("download-speed").textContent = `Download Speed: ${data.download_speed} MB/s`;
        document.getElementById("upload-speed").textContent = `Upload Speed: ${data.upload_speed} MB/s`;
        document.getElementById("ping").textContent = `Ping: ${data.ping} ms`;

        results.style.display = "block";
    } catch (error) {
        alert(`Error running speed test: ${error.message}`);
        console.error(error);
    }
}
