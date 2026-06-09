/**
 * StressIntel PRO - Temporal Heatmap Engine
 */

const Heatmap = {
    render(containerId, data) {
        const container = document.getElementById(containerId);
        if (!container) return;

        container.innerHTML = '';
        
        // data: 7 days x 24 hours
        data.forEach((day, dayIdx) => {
            day.forEach((risk, hourIdx) => {
                const cell = document.createElement('div');
                cell.className = `heatmap-cell l${risk}`;
                cell.title = `Day ${dayIdx + 1}, Hour ${hourIdx}:00 - Risk Level ${risk}`;
                container.appendChild(cell);
            });
        });
    }
};

// Auto-init for Mitigation Planner page
if (document.getElementById('heatmap-grid')) {
    // Mock data for initial render
    const mockHeatmap = Array(7).fill(0).map(() => 
        Array(24).fill(0).map(() => Math.floor(Math.random() * 4))
    );
    Heatmap.render('heatmap-grid', mockHeatmap);
}
