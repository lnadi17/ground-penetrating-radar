#include <Servo.h>

Servo myservo;

const int SERVO_PIN = 9;
const int GOTO_DELAY = 15;
const int SWEEP_LOW_DELAY = 15;
const int SWEEP_HIGH_DELAY = 10000;

int sweepSpeed = 50;
int sweepDelay = 108;

int sweepLow = 0;
int sweepHigh = 180;

bool started = false;

int currentPos = -1;
int sweepDir = 1;

void setup() {
  myservo.attach(SERVO_PIN);
  Serial.begin(9600);
  Serial.println("Program started.");
  Serial.println("=====================");
  Serial.println("Available commands:\n1. goto {degree}\n2. speed {0-100}\n3. range {0-180} {0-180}\n4. get\n5. start\n6. stop");
  Serial.println("=====================");
  setupWithoutLaptop();
}

void setupWithoutLaptop(){
  sweepSpeed = 98;
  sweepDelay = 215;
  sweepLow = 70;
  sweepHigh = 110;
  if (currentPos == -1) {
    servoGoto(sweepLow);
  }
  started = true;
  currentPos = myservo.read();
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readString();
    Serial.println(data);
    if (data == "get") {
      Serial.println(myservo.read());
    } else if (data == "start") {
      if (currentPos == -1) {
        servoGoto(sweepLow);
      }
      started = true;
      currentPos = myservo.read();
    } else if (data == "stop") {
      started = false;
    } else if (getValue(data, ' ', 0) == "range") {
       sweepLow = getValue(data, ' ', 1).toInt();
       sweepHigh = getValue(data, ' ', 2).toInt();
    } else if (getValue(data, ' ', 0) == "goto") {
      int gotoDegree = getValue(data, ' ', 1).toInt();
      servoGoto(gotoDegree);
    } else if (getValue(data, ' ', 0) == "speed") {
      sweepSpeed = getValue(data, ' ', 1).toInt();
      sweepDelay = map(sweepSpeed, 0, 100, SWEEP_HIGH_DELAY, SWEEP_LOW_DELAY);
      Serial.println(sweepDelay);
    } else {
      Serial.println("Unknown command.");
    }
  }
  sweepCycle();
}

void servoGoto(int degree) {
  int currentDegree = myservo.read();
  int dir = (degree - currentDegree) > 0 ? 1 : -1;
  for (int i = currentDegree; i != degree; i += dir) {
     myservo.write(i);
     delay(GOTO_DELAY);
  }
}

void sweepCycle() {
  if (started) {
    if (currentPos < sweepHigh && sweepDir == 1) {
      myservo.write(++currentPos);
    } else {
      sweepDir = -1;
    }
    if (currentPos > sweepLow && sweepDir == -1) {
      myservo.write(--currentPos);
    } else {
      sweepDir = 1;
    }
    delay(sweepDelay);
  }
}

String getValue(String data, char separator, int index) {
  int wordIndex = -1;
  int startIndex = 0;
  int endIndex = -1;
  int maxIndex = data.length() - 1;
  
  for (int i = 0; i <= maxIndex; i++) {
    if (data.charAt(i) == separator || i == maxIndex) {
      endIndex = (i == maxIndex) ? i + 1 : i;
      if (++wordIndex == index) {
        return data.substring(startIndex, endIndex);
      } else {
        startIndex = endIndex + 1;
      }
    }
  }
}
