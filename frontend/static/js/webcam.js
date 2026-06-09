/**
 * StressIntel PRO - Webcam Module
 */

const Webcam = {
    video: null,
    stream: null,
    canvas: document.createElement('canvas'),

    async init(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        try {
            this.stream = await navigator.mediaDevices.getUserMedia({ video: true });
            this.video = document.createElement('video');
            this.video.srcObject = this.stream;
            this.video.autoplay = true;
            this.video.style.width = '100%';
            this.video.style.height = '100%';
            this.video.style.objectFit = 'cover';

            container.innerHTML = '';
            container.appendChild(this.video);
            return true;
        } catch (error) {
            console.error('Webcam Error:', error);
            container.innerHTML = `
                <div class="webcam-placeholder">
                    <i class="fa-solid fa-triangle-exclamation"></i>
                    <p>Camera access denied</p>
                </div>`;
            return false;
        }
    },

    captureFrame() {
        if (!this.video) return null;
        
        this.canvas.width = this.video.videoWidth;
        this.canvas.height = this.video.videoHeight;
        const ctx = this.canvas.getContext('2d');
        ctx.drawImage(this.video, 0, 0);
        
        return this.canvas.toDataURL('image/jpeg', 0.8);
    },

    stop() {
        if (this.stream) {
            this.stream.getTracks().forEach(track => track.stop());
        }
    }
};

document.getElementById('start-webcam')?.addEventListener('click', async () => {
    const success = await Webcam.init('webcam-preview');
    if (success) {
        document.getElementById('start-webcam').innerHTML = '<i class="fa-solid fa-camera"></i> Scan Frame';
        document.getElementById('start-webcam').onclick = () => {
            const frame = Webcam.captureFrame();
            if (frame) {
                document.getElementById('face_data').value = frame;
                alert('Micro-expression captured successfully.');
            }
        };
    }
});
