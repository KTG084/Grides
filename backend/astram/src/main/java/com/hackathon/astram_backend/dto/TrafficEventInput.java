package com.hackathon.astram_backend.dto;

import com.fasterxml.jackson.annotation.JsonProperty;

public class TrafficEventInput {

    @JsonProperty("event_type")
    private String eventType;

    @JsonProperty("event_cause")
    private String eventCause;

    private double latitude;
    private double longitude;

    @JsonProperty("veh_type")
    private String vehType;

    private String description;

    public TrafficEventInput() {
    }

    public String getEventType() {
        return eventType;
    }

    public void setEventType(String eventType) {
        this.eventType = eventType;
    }

    public String getEventCause() {
        return eventCause;
    }

    public void setEventCause(String eventCause) {
        this.eventCause = eventCause;
    }

    public double getLatitude() {
        return latitude;
    }

    public void setLatitude(double latitude) {
        this.latitude = latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    public void setLongitude(double longitude) {
        this.longitude = longitude;
    }

    public String getVehType() {
        return vehType;
    }

    public void setVehType(String vehType) {
        this.vehType = vehType;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}