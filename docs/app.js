document.addEventListener('DOMContentLoaded', () => {
    // Sync slider values to text
    const syncSlider = (id) => {
        const slider = document.getElementById(id);
        const val = document.getElementById(`${id}-val`);
        slider.addEventListener('input', (e) => {
            val.textContent = e.target.value;
        });
    };
    syncSlider('age');
    syncSlider('crcl');
    syncSlider('ast');

    // Analyze Button Logic
    document.getElementById('analyze-btn').addEventListener('click', analyzeRisk);
});

function normalize(drug) {
    return drug.trim().toLowerCase();
}

function calculateMLProbability(d1, d2, age, crcl, ast) {
    let z = MODEL_INTERCEPT;
    let contributions = [];

    // Continuous features
    const contextFeats = {
        'age': age,
        'renal_function_crcl': crcl,
        'liver_function_ast': ast
    };

    for (const [feat, val] of Object.entries(contextFeats)) {
        let weight = MODEL_WEIGHTS[feat] || 0;
        let impact = weight * val;
        z += impact;
        contributions.push({ feature: feat, impact: impact });
    }

    // Drug categorical features
    for (const drug of ALL_DRUGS) {
        let val = (drug === d1 || drug === d2) ? 1.0 : 0.0;
        let weight = MODEL_WEIGHTS[`drug_${drug}`] || 0;
        let impact = weight * val;
        z += impact;
        // Only show drug impact if it's present (or if we want to show all, but present is better)
        if (val > 0) {
            contributions.push({ feature: `Drug: ${drug}`, impact: impact });
        }
    }

    // Sigmoid
    let probability = 1 / (1 + Math.exp(-z));
    
    // Sort contributions by absolute impact for XAI
    contributions.sort((a, b) => Math.abs(b.impact) - Math.abs(a.impact));

    return { probability, contributions };
}

function analyzeRisk() {
    // 1. Get Inputs
    const d1Raw = document.getElementById('drug1').value;
    const d2Raw = document.getElementById('drug2').value;
    const age = parseFloat(document.getElementById('age').value);
    const crcl = parseFloat(document.getElementById('crcl').value);
    const ast = parseFloat(document.getElementById('ast').value);

    if (!d1Raw || !d2Raw) {
        alert("Please enter both medications.");
        return;
    }

    // UI Transitions
    document.getElementById('blank-state').classList.add('hidden');
    document.getElementById('results-state').classList.add('hidden');
    document.getElementById('loading-state').classList.remove('hidden');

    // Simulate slight delay for "analysis" feeling
    setTimeout(() => {
        
        let d1 = normalize(d1Raw);
        let d2 = normalize(d2Raw);
        let drugs = [d1, d2].sort();
        let pairKey = `${drugs[0]}::${drugs[1]}`;

        // 2. Rule-based Check
        let ruleMatch = KNOWN_INTERACTIONS[pairKey];
        
        // 3. ML Prediction
        let mlResult = calculateMLProbability(drugs[0], drugs[1], age, crcl, ast);
        let mlProb = mlResult.probability;

        // 4. Hybrid Risk Engine Logic
        let riskCategory = "";
        let riskRationale = "";
        let theme = ""; // red, yellow, green
        let icon = "";

        if (ruleMatch) {
            riskCategory = "High Risk (Known Evidence)";
            riskRationale = "Found in known interaction database.";
            theme = "red";
            icon = "fa-solid fa-triangle-exclamation";
        } else if (mlProb >= 0.7) {
            riskCategory = "High Risk (Model Predicted)";
            riskRationale = "Based on similarity and patient context, ML predicts high risk.";
            theme = "red";
            icon = "fa-solid fa-triangle-exclamation";
        } else if (mlProb >= 0.4) {
            riskCategory = "Moderate Risk (Model Predicted)";
            riskRationale = "ML model predicts potential moderate risk based on context.";
            theme = "amber";
            icon = "fa-solid fa-circle-exclamation";
        } else {
            riskCategory = "Low Risk (Insufficient Evidence)";
            riskRationale = "No known interaction and ML predicts low probability.";
            theme = "emerald";
            icon = "fa-solid fa-circle-check";
        }

        // 5. Update UI
        renderResults(riskCategory, riskRationale, theme, icon, ruleMatch, mlResult);

    }, 800);
}

function renderResults(title, desc, theme, iconClass, ruleMatch, mlResult) {
    const alertBox = document.getElementById('risk-alert');
    const titleEl = document.getElementById('risk-title');
    const descEl = document.getElementById('risk-desc');
    const iconEl = document.getElementById('risk-icon');
    
    // Reset classes
    alertBox.className = "rounded-2xl p-6 border shadow-sm transition-all flex items-start gap-4 slide-in-right";
    
    if (theme === 'red') {
        alertBox.classList.add('bg-red-50', 'border-red-200', 'text-red-900');
        iconEl.className = `${iconClass} text-red-500 mt-1`;
    } else if (theme === 'amber') {
        alertBox.classList.add('bg-amber-50', 'border-amber-200', 'text-amber-900');
        iconEl.className = `${iconClass} text-amber-500 mt-1`;
    } else {
        alertBox.classList.add('bg-emerald-50', 'border-emerald-200', 'text-emerald-900');
        iconEl.className = `${iconClass} text-emerald-500 mt-1`;
    }

    titleEl.textContent = title;
    descEl.textContent = desc;

    // Known Details
    const knownBox = document.getElementById('known-details');
    if (ruleMatch) {
        knownBox.classList.remove('hidden');
        document.getElementById('k-type').textContent = ruleMatch.interaction_type.replace(/_/g, ' ').toUpperCase();
        document.getElementById('k-severity').textContent = ruleMatch.severity;
        document.getElementById('k-source').textContent = ruleMatch.evidence_source;
    } else {
        knownBox.classList.add('hidden');
    }

    // XAI Chart
    document.getElementById('ml-prob-text').textContent = (mlResult.probability * 100).toFixed(1) + "%";
    
    const chartContainer = document.getElementById('xai-chart');
    chartContainer.innerHTML = '<div class="chart-center-line"></div>'; // Reset and add center line
    
    // Find max absolute impact for scaling
    const maxImpact = Math.max(...mlResult.contributions.map(c => Math.abs(c.impact)));
    const scale = maxImpact > 0 ? 50 / maxImpact : 1; // 50% max width each side

    mlResult.contributions.slice(0, 5).forEach(c => {
        let width = Math.abs(c.impact) * scale;
        let isPositive = c.impact > 0;
        
        // Clean feature name
        let fName = c.feature.replace('renal_function_crcl', 'CrCl').replace('liver_function_ast', 'AST').toUpperCase();

        const barRow = document.createElement('div');
        barRow.className = 'chart-bar-container z-10 relative';
        
        // We use a trick: 
        // If positive, it grows to the right from 50%.
        // If negative, it grows to the left from 50%.
        let barStyle = isPositive 
            ? `left: 50%; width: 0%;` 
            : `right: 50%; width: 0%;`;
        let targetWidth = `${width}%`;
            
        barRow.innerHTML = `
            <div class="chart-label" title="${fName}">${fName}</div>
            <div class="chart-track">
                <div class="chart-bar ${isPositive ? 'positive' : 'negative'}" style="${barStyle}" data-target="${targetWidth}"></div>
            </div>
            <div class="w-16 text-right text-xs text-gray-500 font-mono">${c.impact.toFixed(2)}</div>
        `;
        chartContainer.appendChild(barRow);
    });

    // Toggle Visibility
    document.getElementById('loading-state').classList.add('hidden');
    document.getElementById('results-state').classList.remove('hidden');

    // Trigger animations for bars
    setTimeout(() => {
        const bars = document.querySelectorAll('.chart-bar');
        bars.forEach(bar => {
            bar.style.width = bar.getAttribute('data-target');
        });
    }, 50);
}
