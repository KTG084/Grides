package com.hackathon.astram_backend.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import java.util.Map;

@Data
public class PredictionResponse {

    @JsonProperty("bayesian_forecast")
    private BayesianForecast bayesianForecast;

    @JsonProperty("llm_reasoning_engine")
    private Map<String, Object> llmReasoningEngine;

    @JsonProperty("rl_agentic_deployment")
    private Map<String, Object> rlAgenticDeployment;

    @Data
    public static class BayesianForecast {
        @JsonProperty("mean_impact_score")
        private double meanImpactScore;

        @JsonProperty("mean_duration_mins")
        private double meanDurationMins;

        @JsonProperty("confidence_interval")
        private String confidenceInterval;

        @JsonProperty("epistemic_uncertainty")
        private double epistemicUncertainty;

        @JsonProperty("ai_predicted_road_closure")
        private boolean aiPredictedRoadClosure;
    }
}