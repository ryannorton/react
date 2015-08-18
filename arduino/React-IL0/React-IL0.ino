void setup() {
  Serial.begin(9600);
}

int prev = 0;

void loop() {
  if ((analogRead(0) > 270) != prev)
  {
    prev = (prev + 1) % 2;
    Serial.print("{IL0");
    Serial.print(prev);
    Serial.print("}");
  }
}
