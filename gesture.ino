#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "Akatsuki";
const char* password = "wireless";

WebServer server(80);

int leds[] = {2, 3, 4, 5, 6};

void setLeds(int number) {
  for (int i = 0; i < 5; i++) {
    digitalWrite(leds[i], i < number ? HIGH : LOW);
  }
}

void handleLeds() {
  if (server.hasArg("leds")) {
    int number = server.arg("leds").toInt();

    if (number >= 0 && number <= 5) {
      setLeds(number);
      server.send(200, "text/plain", "LEDs: " + String(number));
      return;
    }
  }

  server.send(400, "text/plain", "Invalid number");
}

void setup() {
  Serial.begin(115200);

  for (int i = 0; i < 5; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }

  WiFi.begin(ssid, password);

  Serial.print("Connecting");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());

  server.on("/set", handleLeds);

  server.begin();
}

void loop() {
  server.handleClient();
}