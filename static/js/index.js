function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// Set canvas size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Line properties
const circuitLines = [];
const maxLines = 10; // Number of animated lines
let animationFrame;

// Function to create a new line
function createLine() {
    return {
        startX: Math.random() * canvas.width,
        startY: Math.random() * canvas.height,
        endX: Math.random() * canvas.width,
        endY: Math.random() * canvas.height,
        progress: 0 // Animation progress (0 to 1)
    };
}

// Populate initial lines
for (let i = 0; i < maxLines; i++) {
    circuitLines.push(createLine());
}

// Function to draw lines
function drawCircuit() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas

    ctx.lineWidth = 2;
    ctx.strokeStyle = "rgba(0, 100, 255, 0.7)"; // Blue color

    circuitLines.forEach(line => {
        ctx.beginPath();
        ctx.moveTo(line.startX, line.startY);

        // Calculate animated endpoint
        const currentX = line.startX + (line.endX - line.startX) * line.progress;
        const currentY = line.startY + (line.endY - line.startY) * line.progress;

        ctx.lineTo(currentX, currentY);
        ctx.stroke();

        // Update progress
        line.progress += 0.02;

        // Reset line when animation completes
        if (line.progress >= 1) {
            Object.assign(line, createLine());
        }
    });

    animationFrame = requestAnimationFrame(drawCircuit);
}

// Start animation
drawCircuit();

// Resize canvas on window resize
window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
