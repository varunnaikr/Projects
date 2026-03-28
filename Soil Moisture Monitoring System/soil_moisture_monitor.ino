const int soilPin = A0;
const int pumpRelayPin = 8;
const int dryThreshold = 620;   // Higher ADC value = drier soil for most resistive sensors
const int wetThreshold = 350;

void setup() {
  pinMode(pumpRelayPin, OUTPUT);
  digitalWrite(pumpRelayPin, LOW);
  Serial.begin(9600);
}

void loop() {
  int rawValue = analogRead(soilPin);
  int moisturePercent = map(rawValue, 1023, 0, 0, 100);
  moisturePercent = constrain(moisturePercent, 0, 100);

  Serial.print("Raw: ");
  Serial.print(rawValue);
  Serial.print(" | Moisture: ");
  Serial.print(moisturePercent);
  Serial.print("% | Status: ");

  if (rawValue > dryThreshold) {
    digitalWrite(pumpRelayPin, HIGH); // Turn pump ON
    Serial.println("Dry - Pump ON");
  } else if (rawValue < wetThreshold) {
    digitalWrite(pumpRelayPin, LOW); // Turn pump OFF
    Serial.println("Wet - Pump OFF");
  } else {
    digitalWrite(pumpRelayPin, LOW);
    Serial.println("Moderate - Monitoring");
  }

  delay(2000);
}
