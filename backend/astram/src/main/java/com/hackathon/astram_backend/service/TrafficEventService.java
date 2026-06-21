package com.hackathon.astram_backend.service;

import com.hackathon.astram_backend.dto.PredictionResponse;
import com.hackathon.astram_backend.dto.TrafficEventInput;
import com.opencsv.CSVReader;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;
import org.springframework.beans.factory.annotation.Value;

import java.io.FileReader;
import java.util.List;
import java.util.Random;

@Service
public class TrafficEventService {

    private final WebClient webClient;

    public TrafficEventService(
            WebClient.Builder webClientBuilder,
            @Value("${python.ai.url}") String pythonAiUrl) {

        this.webClient = webClientBuilder.baseUrl(pythonAiUrl).build();
    }

    /**
     * CORE PIPELINE: Sends the Java Object to Python via HTTP POST and maps the JSON response.
     */
    public Mono<PredictionResponse> predictTrafficImpact(TrafficEventInput inputData) {
        return this.webClient.post()
                .bodyValue(inputData)
                .retrieve()
                .bodyToMono(PredictionResponse.class);
    }

    /**
     * HACKATHON SIMULATOR: Reads a random row from the CSV to simulate a live traffic alert.
     */
    public TrafficEventInput fetchRandomEventFromCsv() {
        String csvFilePath = "Astram_event_data_anonymized.csv";

        try (CSVReader reader = new CSVReader(new FileReader(csvFilePath))) {
            List<String[]> allRows = reader.readAll();

            Random rand = new Random();
            String[] randomRow = allRows.get(rand.nextInt(allRows.size() - 1) + 1);

            TrafficEventInput input = new TrafficEventInput();

            input.setEventType(randomRow[1].isEmpty() ? "unplanned" : randomRow[1]);
            input.setLatitude(Double.parseDouble(randomRow[2]));
            input.setLongitude(Double.parseDouble(randomRow[3]));
            input.setEventCause(randomRow[8].isEmpty() ? "others" : randomRow[8]);
            input.setDescription(randomRow[17].isEmpty() ? "Standard event" : randomRow[17]);
            input.setVehType(randomRow[18].isEmpty() ? "unknown" : randomRow[18]);

            return input;

        } catch (Exception e) {
            throw new RuntimeException("Failed to parse CSV file: " + e.getMessage());
        }
    }
}