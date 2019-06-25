#define PIN_VREF_R 5 // PWM
#define PIN_VREF_L 6 // PWM
#define PIN_IN1_R  8
#define PIN_IN2_R  9
#define PIN_IN1_L  11
#define PIN_IN2_L  12

void drive_ad_R() {
  digitalWrite(PIN_IN1_R,HIGH);
  digitalWrite(PIN_IN2_R,LOW);
}

void drive_ad_L() {
  digitalWrite(PIN_IN1_L,HIGH);
  digitalWrite(PIN_IN2_L,LOW);
}

void drive_rev_R() {
  digitalWrite(PIN_IN1_R,LOW);
  digitalWrite(PIN_IN2_R,HIGH);    
}

void drive_rev_L() {
  digitalWrite(PIN_IN1_L,LOW);
  digitalWrite(PIN_IN2_L,HIGH);    
}

void brake_R() {
  digitalWrite(PIN_IN1_R,HIGH);
  digitalWrite(PIN_IN2_R,HIGH);
}

void brake_L() {
  digitalWrite(PIN_IN1_L,HIGH);
  digitalWrite(PIN_IN2_L,HIGH);
}

void stop_R() {
  digitalWrite(PIN_IN1_R,LOW);
  digitalWrite(PIN_IN2_R,LOW);
}

void stop_L() {
  digitalWrite(PIN_IN1_L,LOW);
  digitalWrite(PIN_IN2_L,LOW);
}

void straight(int duty,int movetime) {
  analogWrite(PIN_VREF_R,duty); 
  analogWrite(PIN_VREF_L,duty);
  drive_ad_R();
  drive_ad_L();
  delay(movetime);
}

void back(int duty,int movetime) {
  analogWrite(PIN_VREF_R,duty); 
  analogWrite(PIN_VREF_L,duty);
  drive_rev_R();
  drive_rev_L();
  delay(movetime);
}

void turn_right(int duty,int movetime) {
  analogWrite(PIN_VREF_R,0); 
  analogWrite(PIN_VREF_L,duty);
  drive_ad_R();
  drive_ad_L();
  delay(movetime);
}

void turn_left(int duty,int movetime) {
  analogWrite(PIN_VREF_R,duty); 
  analogWrite(PIN_VREF_L,0);
  drive_ad_R();
  drive_ad_L();
  delay(movetime);
}

void Brake(int movetime) {
  brake_R();
  brake_L();Sha
  delay(movetime);
}

void Stop(int movetime) {
  stop_R();
  stop_L();
  delay(movetime);
}

void setup() {
  pinMode(PIN_IN1_R,OUTPUT); 
  pinMode(PIN_IN2_R,OUTPUT); 
  pinMode(PIN_IN1_L,OUTPUT); 
  pinMode(PIN_IN2_L,OUTPUT); 
}

void loop() {
  straight(175,5000);
  Brake(10);
  back(175,5000);
  Brake(2000);
  back(175,5000);
  Stop(2000);
}
