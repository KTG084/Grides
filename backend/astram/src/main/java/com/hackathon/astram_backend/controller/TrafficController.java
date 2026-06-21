package com.hackathon.astram_backend.controller;

import com.hackathon.astram_backend.dto.PredictionResponse;
import com.hackathon.astram_backend.dto.TrafficEventInput;
import com.hackathon.astram_backend.service.TrafficEventService;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/api/dashboard")
@CrossOrigin(origins = "*") // Allows your future frontend dashboard to connect without CORS errors
public class TrafficController {

    private final TrafficEventService trafficEventService;

    public TrafficController(TrafficEventService trafficEventService) {
        this.trafficEventService = trafficEventService;
    }

    /**
     * Endpoint 1: Manual Prediction Input
     * Receives a specific traffic scenario from the frontend and pushes it straight to the AI model.
     */
    @PostMapping("/predict")
    public Mono<PredictionResponse> predictIncident(@RequestBody TrafficEventInput input) {
        return trafficEventService.predictTrafficImpact(input);
    }

    /**
     * Endpoint 2: Live Feed Simulation
     * Automatically pulls a random record out of the dataset CSV and runs it through the engine.
     */
    @GetMapping("/live-feed")
    public Mono<PredictionResponse> triggerLiveFeedAlert() {
        TrafficEventInput randomInput = trafficEventService.fetchRandomEventFromCsv();
        return trafficEventService.predictTrafficImpact(randomInput);
    }
}