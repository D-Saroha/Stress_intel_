/**
 * StressIntel PRO - Simulation Lab Controller
 */

const Simulation = {
    chart: null,

    init() {
        const sliders = document.querySelectorAll('.styled-slider');
        sliders.forEach(slider => {
            slider.addEventListener('input', (e) => {
                const id = e.target.id.replace('sim-', 'val-');
                const badge = document.getElementById(id);
                if (badge) {
                    let suffix = '';
                    if (id.includes('sleep')) suffix = 'h';
                    if (id.includes('study')) suffix = 'h';
                    if (id.includes('physical')) suffix = 'm';
                    badge.textContent = e.target.value + suffix;
                }
            });
        });

        document.getElementById('run-simulation')?.addEventListener('click', () => this.run());
        
        // Initial chart render
        this.renderChart([4, 5, 4.5, 6, 5.5, 4, 3]);
    },

    async run() {
        const btn = document.getElementById('run-simulation');
        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Processing...';
        btn.disabled = true;

        // Mocking API call for demo speed
        setTimeout(() => {
            const newVal = Array(7).fill(0).map(() => (Math.random() * 5 + 2).toFixed(1));
            this.renderChart(newVal);
            
            const insight = document.getElementById('simulation-insight');
            insight.textContent = "Forecast updated: Current lifestyle adjustments show a 12% decrease in cumulative cortisol exposure over the next 7 days.";
            
            btn.innerHTML = '<i class="fa-solid fa-play"></i> Recalculate Trajectory';
            btn.disabled = false;
        }, 1000);
    },

    renderChart(data) {
        const ctx = document.getElementById('simulation-chart')?.getContext('2d');
        if (!ctx) return;

        if (this.chart) this.chart.destroy();

        this.chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],
                datasets: [{
                    label: 'Simulated Stress Level',
                    data: data,
                    borderColor: '#F57E3E',
                    backgroundColor: 'rgba(245, 126, 62, 0.1)',
                    fill: true,
                    tension: 0.4,
                    borderWidth: 3,
                    pointRadius: 5,
                    pointBackgroundColor: '#F57E3E'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { color: '#FFFFFF' } }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 10,
                        grid: { color: 'rgba(255,255,255,0.05)' },
                        ticks: { color: 'rgba(255,255,255,0.6)' }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: 'rgba(255,255,255,0.6)' }
                    }
                }
            }
        });
    }
};

document.addEventListener('DOMContentLoaded', () => Simulation.init());
