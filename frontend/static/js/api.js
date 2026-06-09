/**
 * StressIntel PRO - API Integration Layer
 */

const API = {
    baseUrl: '/api',

    async post(endpoint, data) {
        try {
            const response = await fetch(`${this.baseUrl}${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            return await response.json();
        } catch (error) {
            console.error(`API Error (${endpoint}):`, error);
            return { success: false, error: 'Network communication failure' };
        }
    },

    async get(endpoint) {
        try {
            const response = await fetch(`${this.baseUrl}${endpoint}`);
            return await response.json();
        } catch (error) {
            console.error(`API Error (${endpoint}):`, error);
            return { success: false, error: 'Network communication failure' };
        }
    },

    // Specific endpoints
    async predict(formData) {
        return await this.post('/predict', formData);
    },

    async getPeerAnalytics(userData) {
        return await this.post('/analytics/peer', userData);
    },

    async runSimulation(baseData, modifications) {
        return await this.post('/simulation/run', { baseData, modifications });
    },

    async analyzeMicroExpression(imageData) {
        return await this.post('/webcam/analyze', { image: imageData });
    }
};
