# Stage 1: Build the application
FROM maven:3.8.5-openjdk-17 AS build
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

# Stage 2: Run the application
FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /app/target/astram-backend-0.0.1-SNAPSHOT.jar astram.jar
COPY --from=build /app/Astram_event_data_anonymized.csv ./Astram_event_data_anonymized.csv
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "astram.jar"]