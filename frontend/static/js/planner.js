/**
 * StressIntel PRO - Mitigation Planner Logic
 */

const Planner = {
    init() {
        const checkboxes = document.querySelectorAll('.custom-check');
        checkboxes.forEach(check => {
            check.addEventListener('change', () => this.updateProgress());
        });
    },

    updateProgress() {
        const checkboxes = document.querySelectorAll('.custom-check');
        const checked = Array.from(checkboxes).filter(c => c.checked).length;
        const total = checkboxes.length;
        const percent = Math.round((checked / total) * 100);

        const fill = document.getElementById('progress-fill');
        const text = document.getElementById('progress-text');

        if (fill) fill.style.width = `${percent}%`;
        if (text) text.textContent = `${percent}%`;
    }
};

document.addEventListener('DOMContentLoaded', () => Planner.init());
