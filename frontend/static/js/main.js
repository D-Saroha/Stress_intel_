/**
 * StressIntel PRO - Main Controller
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Handle Navigation Highlighting
    const currentPath = window.location.pathname;
    const navLinks = {
        '/': 'nav-home',
        '/dashboard': 'nav-dashboard',
        '/simulation-lab': 'nav-simulation',
        '/peer-analytics': 'nav-peer',
        '/mitigation-planner': 'nav-mitigation',
        '/research-lab': 'nav-research',
        '/about': 'nav-about'
    };
    const activeId = navLinks[currentPath];
    if (activeId) {
        document.getElementById(activeId)?.classList.add('active');
    }

    // 2. Handle Assessment Form Submission
    const assessmentForm = document.getElementById('assessment-form');
    if (assessmentForm) {
        assessmentForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = document.getElementById('submit-assessment');
            
            // Visual feedback
            submitBtn.innerHTML = '<i class="fa-solid fa-microscope fa-spin"></i> Analyzing Biomarkers...';
            submitBtn.disabled = true;

            const formData = new FormData(assessmentForm);
            const data = Object.fromEntries(formData.entries());
            
            // Convert numbers
            const numericFields = ['sleep_hours', 'study_hours', 'physical_activity', 'social_interaction', 'screen_time', 'heart_rate', 'anxiety_score', 'diet_quality'];
            numericFields.forEach(field => {
                if (data[field]) data[field] = parseFloat(data[field]);
            });

            try {
                const result = await API.predict(data);
                if (result.success) {
                    // Store result in session storage for the dashboard
                    sessionStorage.setItem('last_prediction', JSON.stringify(result.data));
                    sessionStorage.setItem('last_user_data', JSON.stringify(data));
                    
                    // Redirect to dashboard
                    window.location.href = '/dashboard';
                } else {
                    alert('Analysis failed: ' + (result.error || 'Unknown error'));
                    submitBtn.innerHTML = '<i class="fa-solid fa-microscope"></i> Run Neural Diagnostic';
                    submitBtn.disabled = false;
                }
            } catch (err) {
                console.error(err);
                alert('Fatal system error during inference.');
                submitBtn.disabled = false;
            }
        });
    }

    // 3. Handle Dashboard Initialization
    if (window.location.pathname === '/dashboard') {
        const result = JSON.parse(sessionStorage.getItem('last_prediction'));
        const userData = JSON.parse(sessionStorage.getItem('last_user_data'));

        if (result && userData) {
            updateDashboard(result, userData);
        } else {
            document.getElementById('results-view').innerHTML = `
                <div class="glass-card text-center p-8">
                    <i class="fa-solid fa-circle-info text-accent mb-4" style="font-size: 3rem;"></i>
                    <h2>No Active Session</h2>
                    <p class="text-muted">Please complete the behavioral assessment to view results.</p>
                    <a href="/" class="btn btn-primary mt-4">Start Assessment</a>
                </div>`;
        }
    }

    // 4. Handle Peer Analytics Initialization
    if (window.location.pathname === '/peer-analytics') {
        const userData = JSON.parse(sessionStorage.getItem('last_user_data')) || {
            sleep_hours: 7, study_hours: 6, physical_activity: 30,
            social_interaction: 60, screen_time: 4, diet_quality: 8,
            heart_rate: 72, anxiety_score: 45
        };
        initPeerAnalytics(userData);
    }
});

async function initPeerAnalytics(userData) {
    try {
        const response = await API.getPeerAnalytics(userData);
        if (response.success) {
            const data = response.data;
            
            // Update Marker
            const marker = document.getElementById('user-marker');
            const percentileText = document.getElementById('percentile-val');
            if (marker) marker.style.left = `${data.percentile}%`;
            if (percentileText) percentileText.textContent = `${data.percentile}th`;

            // Distribution Chart
            const distCtx = document.getElementById('distribution-chart')?.getContext('2d');
            if (distCtx) {
                new Chart(distCtx, {
                    type: 'bar',
                    data: {
                        labels: ['Low', 'Med', 'High'],
                        datasets: [{
                            label: 'Cohort Distribution',
                            data: [30, 45, 25],
                            backgroundColor: ['#06B6D4', '#F59E0B', '#F43F5E']
                        }]
                    },
                    options: { responsive: true, maintainAspectRatio: false }
                });
            }

            // Comparison Chart
            const compCtx = document.getElementById('comparison-chart')?.getContext('2d');
            if (compCtx) {
                new Chart(compCtx, {
                    type: 'radar',
                    data: {
                        labels: ['Sleep', 'Study', 'Activity', 'Social', 'Screen', 'Diet'],
                        datasets: [
                            { label: 'You', data: [70, 60, 50, 65, 40, 80], borderColor: '#06B6D4', backgroundColor: 'rgba(6, 182, 212, 0.2)' },
                            { label: 'Peers', data: [65, 55, 45, 60, 50, 70], borderColor: '#F59E0B', backgroundColor: 'rgba(245, 158, 11, 0.2)' }
                        ]
                    },
                    options: { responsive: true, maintainAspectRatio: false }
                });
            }
        }
    } catch (err) {
        console.error('Peer Analytics Error:', err);
    }
}


/**
 * Updates dashboard UI with prediction results
 */
function updateDashboard(result, userData) {
    const predLabel = document.getElementById('prediction-label');
    const probLabel = document.getElementById('probability-label');
    const topStressor = document.getElementById('top-stressor');
    const riskBar = document.getElementById('risk-bar');

    predLabel.textContent = `${result.prediction} Stress`;
    
    // Fix: Multiply by 100 once for display
    const probPercent = (result.probability * 100).toFixed(1);
    probLabel.textContent = `${probPercent}%`;
    
    riskBar.style.width = `${probPercent}%`;
    if (result.prediction.toLowerCase() === 'high') riskBar.style.backgroundColor = '#F43F5E';
    else if (result.prediction.toLowerCase() === 'medium') riskBar.style.backgroundColor = '#F59E0B';
    else riskBar.style.backgroundColor = '#06B6D4';

    if (result.feature_importance && result.feature_importance.length > 0) {
        topStressor.textContent = result.feature_importance[0].feature.replace('_', ' ');
    }

    const shapCtx = document.getElementById('shap-chart')?.getContext('2d');
    if (shapCtx) Charts.initShapChart(shapCtx, result.feature_importance);

    const radarCtx = document.getElementById('radar-chart')?.getContext('2d');
    if (radarCtx) Charts.initRadarChart(radarCtx, userData, {});

    const reportContainer = document.getElementById('report-content');
    if (reportContainer && result.clinical_report) {
        reportContainer.innerHTML = marked.parse(result.clinical_report.report_md || result.clinical_report);
    }
}

// Research Lab Logic
if (window.location.pathname === '/research-lab') {
    const video = document.getElementById('research-video');
    const canvas = document.getElementById('research-canvas');
    const researchForm = document.getElementById('research-form');

    // 1. Initialize Camera
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                video.srcObject = stream;
            })
            .catch(err => console.error("Camera access denied:", err));
    }

    // 2. Handle Form Submission
    if (researchForm) {
        researchForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('run-research');
            const output = document.getElementById('ollama-output');
            const resultCard = document.getElementById('research-results');
            const visualCard = document.getElementById('visual-output-card');
            const impactImg = document.getElementById('impact-image');
            const visualMeta = document.getElementById('visual-meta');
            const downloadBtn = document.getElementById('download-research-report');

            let currentResearchResult = null;

            btn.innerHTML = '<i class="fa-solid fa-dna fa-spin"></i> Running Deep Diagnostic...';
            btn.disabled = true;

            // Capture Frame
            let imageB64 = null;
            if (video.srcObject) {
                const context = canvas.getContext('2d');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                context.drawImage(video, 0, 0, canvas.width, canvas.height);
                imageB64 = canvas.toDataURL('image/jpeg');
            }

            const formData = new FormData(researchForm);
            const data = Object.fromEntries(formData.entries());
            
            // Convert to numbers
            Object.keys(data).forEach(key => data[key] = parseFloat(data[key]));
            
            // Add image
            data.image = imageB64;

            try {
                const response = await fetch('/api/research/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    resultCard.classList.remove('hidden');
                    output.innerHTML = marked.parse(result.insight);
                    
                    // Save for report
                    sessionStorage.setItem('last_research_data', JSON.stringify(data));
                    sessionStorage.setItem('last_visual_analysis', JSON.stringify(result.visual_analysis || null));
                    
                    // Handle Visual Analysis
                    if (result.visual_analysis) {
                        visualCard.classList.remove('hidden');
                        impactImg.src = result.visual_analysis.annotated_image;
                        const meta = result.visual_analysis.metadata;
                        visualMeta.innerHTML = `
                            <div class="mb-2"><strong>Impact Score:</strong> ${(meta.impact_score * 100).toFixed(1)}%</div>
                            <div class="mb-2"><strong>Markers:</strong> ${meta.stress_markers_detected.join(', ')}</div>
                            <div class="text-xs italic text-accent">${meta.clinical_interpretation}</div>
                        `;
                    } else {
                        visualCard.classList.add('hidden');
                    }

                    // Store for report generation
                    currentResearchResult = result;
                    currentResearchResult.user_data = data;

                    window.scrollTo({ top: resultCard.offsetTop - 50, behavior: 'smooth' });
                } else {
                    alert('Analysis Error: ' + result.error);
                }
            } catch (err) {
                console.error('Research API Error:', err);
                alert('System Connection Error: ' + err.message);
            } finally {
                btn.innerHTML = '<i class="fa-solid fa-dna"></i> Run Deep Research Diagnostic (Ollama Llama3)';
                btn.disabled = false;
            }
        });
    }

    // 3. Handle Report Download
    const downloadBtn = document.getElementById('download-research-report');
    if (downloadBtn) {
        downloadBtn.addEventListener('click', async () => {
            const resultCard = document.getElementById('research-results');
            const ollamaOutput = document.getElementById('ollama-output');
            
            // Re-capture data if needed or use stored
            // Since we need to send this to a new tab, we'll use a form submission or a temporary storage
            
            // Get the data we stored during analysis
            // Note: In a real app, we might use sessionStorage, but here we can just post to the endpoint
            
            // We'll use a hidden form to POST data and open in a new tab
            const researchData = {
                user_data: JSON.parse(sessionStorage.getItem('last_research_data')),
                insight: ollamaOutput.innerHTML,
                visual_analysis: JSON.parse(sessionStorage.getItem('last_visual_analysis'))
            };

            const response = await fetch('/api/report/research', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(researchData)
            });

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.target = '_blank';
            // Actually, we want to open the HTML in a new tab
            const newWindow = window.open();
            newWindow.document.write(await response.text());
            newWindow.document.close();
        });
    }
}

