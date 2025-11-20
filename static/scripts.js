console.log("Moodify loaded successfully.");

document.addEventListener("DOMContentLoaded", () => {
    const audio = document.getElementById("bg-music");
    const toggleBtn = document.getElementById("toggle-music");

    // ------------------------------
    // 1️⃣ Restore last playback time
    // ------------------------------
    const savedTime = localStorage.getItem("bgMusicTime");
    if (savedTime) {
        audio.currentTime = parseFloat(savedTime);
    }

    // ------------------------------
    // 2️⃣ Try playing automatically
    // ------------------------------
    const tryPlay = () => {
        audio.play().catch(() => {
            console.log("Autoplay blocked — waiting for click...");
        });
    };

    tryPlay();

    // Start music on first body click if autoplay was blocked
    let hasStarted = false;
    document.body.addEventListener("click", () => {
        if (!hasStarted && audio.paused) {
            audio.play();
            hasStarted = true;
        }
    });

    // ------------------------------
    // 3️⃣ Save playback time every second
    // ------------------------------
    setInterval(() => {
        localStorage.setItem("bgMusicTime", audio.currentTime);
    }, 1000);

    // ------------------------------
    // 4️⃣ Toggle button logic
    // ------------------------------
    toggleBtn.addEventListener("click", () => {
        if (audio.paused) {
            audio.play();
            toggleBtn.textContent = "🔊";
        } else {
            audio.pause();
            toggleBtn.textContent = "🔇";
        }
    });
});
