/**
 * StressIntel PRO - Charting Engine
 */

const Charts = {
    colors: {
        navy: '#1E0E1C',
        blue: '#9D174D',   /* Berry */
        orange: '#F59E0B', /* Amber */
        peach: '#4C0519',  /* Dark Berry */
        text: '#F8FAFC',
        muted: 'rgba(248, 250, 252, 0.6)'
    },


    initShapChart(ctx, data) {
        // data: [{feature: 'sleep', importance: 1.2}, ...]
        const labels = data.map(d => d.feature.replace('_', ' '));
        const values = data.map(d => d.importance);

        return new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Feature Influence',
                    data: values,
                    backgroundColor: values.map(v => v > 0 ? this.colors.orange : this.colors.blue),
                    borderRadius: 8,
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        grid: { color: 'rgba(255,255,255,0.05)' },
                        ticks: { color: this.colors.muted }
                    },
                    y: {
                        grid: { display: false },
                        ticks: { color: this.colors.text }
                    }
                }
            }
        });
    },

    initRadarChart(ctx, userData, peerData) {
        const labels = ['Sleep', 'Study', 'Activity', 'Social', 'Screen', 'Diet'];
        const userVals = [
            userData.sleep_hours * 8, 
            userData.study_hours * 6,
            userData.physical_activity * 0.8,
            userData.social_interaction * 0.8,
            (12 - userData.screen_time) * 8,
            userData.diet_quality * 10
        ];
        
        const peerVals = [50, 45, 40, 55, 50, 60]; // Mock peer data

        return new Chart(ctx, {
            type: 'radar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'You',
                        data: userVals,
                        borderColor: this.colors.orange,
                        backgroundColor: 'rgba(245, 126, 62, 0.2)',
                        pointBackgroundColor: this.colors.orange
                    },
                    {
                        label: 'Peer Average',
                        data: peerVals,
                        borderColor: this.colors.blue,
                        backgroundColor: 'rgba(193, 230, 241, 0.2)',
                        pointBackgroundColor: this.colors.blue
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { color: this.colors.text } }
                },
                scales: {
                    r: {
                        angleLines: { color: 'rgba(255,255,255,0.1)' },
                        grid: { color: 'rgba(255,255,255,0.1)' },
                        pointLabels: { color: this.colors.muted },
                        ticks: { display: false }
                    }
                }
            }
        });
    }
};
