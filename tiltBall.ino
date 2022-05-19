int tiltPin = 2;
int tiltVal;
int RedLED = 12;
int BlueLED = 13;
int r;

void setup() {                
  pinMode(tiltPin,INPUT);
  pinMode(RedLED,OUTPUT);
  pinMode(BlueLED,OUTPUT);
  digitalWrite(tiltPin,HIGH);
  Serial.begin(9600);
}

void loop() {
  if((r = Serial.read()) == 50){
    for(int i = 1; i <= 10; i++){
        tiltVal=digitalRead(tiltPin);
        Serial.println(tiltVal);
        if (tiltVal == 0){
          digitalWrite(RedLED,HIGH);
          digitalWrite(BlueLED,LOW);
        }
        if (tiltVal == 1){
        digitalWrite(RedLED,LOW);
        digitalWrite(BlueLED,HIGH);
      }
        delay(2000);
    }
  }else if((r = Serial.read()) >50){
    for(int i = 1; i <= 5; i++){
        tiltVal=digitalRead(tiltPin);
        Serial.println(tiltVal);
        if (tiltVal == 0){
          digitalWrite(RedLED,HIGH);
          digitalWrite(BlueLED,LOW);
        }
        if (tiltVal == 1){
        digitalWrite(RedLED,LOW);
        digitalWrite(BlueLED,HIGH);
      }
        delay(2000);
    }
  }

}
