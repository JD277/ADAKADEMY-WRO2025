// Motors pins
int IN3 = 3;
int IN4 = 4;
int speed = 100;

void initMotor() {
  pinMode(speed, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

void goForward(int sp) {
  analogWrite(speed, sp);
  digitalWrite(IN4, 1);
  digitalWrite(IN3, 0);
}

void goBackward(int sp) {
  analogWrite(speed, sp);
  digitalWrite(IN4, 0);
  digitalWrite(IN3, 1);
}

void stop() {
  digitalWrite(IN4, 0);
  digitalWrite(IN3, 0);
}

void setup() {
  // put your setup code here, to run once:
  initMotor();
}

void loop() {
  // put your main code here, to run repeatedly:
  goForward(100);
}
