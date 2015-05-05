#include <DS1307.h>
#include "libSmartGrow.h"
#include "EtherCard.h"
#include "enc28j60.h"
#include "net.h"


String input; // a string to hold incoming data
int led = 13;
int cmd;
int OperationMode;
boolean changeOperationMode;

/*----------------------------------------------------------------------------*/
void setup() {
  pinMode(led, OUTPUT);     

  Serial.begin(BAUD_RATE); 
  input.reserve(32);
  OperationMode = 1;
}
/*----------------------------------------------------------------------------*/
void loop() {

  switch (OperationMode) {
      case 1:
        // selfControl
        // Serial.println("selfControl");
        digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(1000);               // wait for a second
        digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
        delay(1000);               // wait for a second
        if (Serial.available()){
          clear_input_buffer();
          OperationMode = 2;
        }

      break;
      case 2:
        // remoteControl
        remote_control();
      break;
      default:
        // do something
      break;
  }
  delay(50);        // delay in between reads for stability
}
/*----------------------------------------------------------------------------*/
void clear_input_buffer(void){
  while(Serial.available())
    Serial.read();
}
/*----------------------------------------------------------------------------*/
