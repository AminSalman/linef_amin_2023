int sensor1 = 6;
int sensor2 = 5;
int sensor3 = 4;
int sensor4 = 3;
int sensor5 = 2;
int lastBlack = 0;


void setup() {
  pinMode(sensor1, INPUT);
  pinMode(sensor2, INPUT);
  pinMode(sensor3, INPUT);
  pinMode(sensor4, INPUT);
  pinMode(sensor5, INPUT);
  Serial.begin(9600);
}

void loop() {
  int s1 = digitalRead(sensor1);
  int s2 = digitalRead(sensor2);
  int s3 = digitalRead(sensor3);
  int s4 = digitalRead(sensor4);
  int s5 = digitalRead(sensor5);
  if (s1 == 0 && s2 == 0 && s3 == 0 && s4 == 0 && s5 == 0) {       //Condition 0
  straight();
  }
  if (s1 == 0 && s2 == 0 && s3 == 0 && s4 == 0 && s5 == 1) {       //Condition 1
  hardLeft();
  }
  //if (s1 == 0 && s2 == 0 && s3 == 0 && s4 == 1 && s5 == 0) {       //Condition 2
  //NOT POSSIBLE
  // }
  if (s1 == 0 && s2 == 0 && s3 == 0 && s4 == 1 && s5 == 1) {       //Condition 3
  hardLeft();
  }
  //if (s1 == 0 && s2 == 0 && s3 == 1 && s4 == 0 && s5 == 0) {       //Condition 4
  //NOT POSSIBLE
  //}
  //if (s1 == 0 && s2 == 0 && s3 == 1 && s4 == 0 && s5 == 1) {       //Condition 5
  //NOT POSSIBLE
  //}
  if (s1 == 0 && s2 == 0 && s3 == 1 && s4 == 1 && s5 == 0) {       //Condition 6
  curveLeft();
  }
  if (s1 == 0 && s2 == 0 && s3 == 1 && s4 == 1 && s5 == 1) {       //Condition 7
  hardLeft();
  }

  //if (s1 == 0 && s2 == 1 && s3 == 0 && s4 == 0 && s5 == 0) {       //Condition 8
  //NOT POSSIBLE
  //}
  //if (s1 == 0 && s2 == 1 && s3 == 0 && s4 == 0 && s5 == 1) {       //Condition 9
  //NOT POSSIBLE
  //}
  //if (s1 == 0 && s2 == 1 && s3 == 0 && s4 == 1 && s5 == 0) {       //Condition 10
  //NOT POSSIBLE
  //}
  //if (s1 == 0 && s2 == 1 && s3 == 0 && s4 == 1 && s5 == 1) {       //Condition 11
  //NOT POSSIBLE
  //}
  if (s1 == 0 && s2 == 1 && s3 == 1 && s4 == 0 && s5 == 0) {       //Condition 12
  curveRight();
  }
  //if (s1 == 0 && s2 == 1 && s3 == 1 && s4 == 0 && s5 == 1) {       //Condition 13
  // curveRight();
  //}
  if (s1 == 0 && s2 == 1 && s3 == 1 && s4 == 1 && s5 == 0) {       //Condition 14
  straight();
  }
  if (s1 == 0 && s2 == 1 && s3 == 1 && s4 == 1 && s5 == 1) {       //Condition 15
  hardLeft();
  }

  if (s1 == 1 && s2 == 0 && s3 == 0 && s4 == 0 && s5 == 0) {       //Condition 16
  hardRight();
  }
  if (s1 == 1 && s2 == 0 && s3 == 0 && s4 == 0 && s5 == 1) {       //Condition 17
  straight();
  }
  if (s1 == 1 && s2 == 0 && s3 == 0 && s4 == 1 && s5 == 0) {       //Condition 18
  curveLeft();
  }
  if (s1 == 1 && s2 == 0 && s3 == 0 && s4 == 1 && s5 == 1) {       //Condition 19
  curveLeft();
  }
  //if (s1 == 1 && s2 == 0 && s3 == 1 && s4 == 0 && s5 == 0) {       //Condition 20
  //
  //}
  //if (s1 == 1 && s2 == 0 && s3 == 1 && s4 == 0 && s5 == 1) {       //Condition 21
  //
  //}
  if (s1 == 1 && s2 == 0 && s3 == 1 && s4 == 1 && s5 == 0) {       //Condition 22
  curveLeft();
  }
  if (s1 == 1 && s2 == 0 && s3 == 1 && s4 == 1 && s5 == 1) {       //Condition 23
  curveLeft();
  }

  if (s1 == 1 && s2 == 1 && s3 == 0 && s4 == 0 && s5 == 0) {       //Condition 24
  hardRight();
  }
  if (s1 == 1 && s2 == 1 && s3 == 0 && s4 == 0 && s5 == 1) {       //Condition 25
  curveRight();
  }
  if (s1 == 1 && s2 == 1 && s3 == 0 && s4 == 1 && s5 == 0) {       //Condition 26
  straight()
  }
  if (s1 == 1 && s2 == 1 && s3 == 0 && s4 == 1 && s5 == 1) {       //Condition 27
  straight();
  }
  if (s1 == 1 && s2 == 1 && s3 == 1 && s4 == 0 && s5 == 0) {       //Condition 28
  hardRight();
  }
  if (s1 == 1 && s2 == 1 && s3 == 1 && s4 == 0 && s5 == 1) {       //Condition 29
  curveRight();
  }
  if (s1 == 1 && s2 == 1 && s3 == 1 && s4 == 1 && s5 == 0) {       //Condition 30
  hardRight();
  }
  if (s1 == 1 && s2 == 1 && s3 == 1 && s4 == 1 && s5 == 1) {       //Condition 31
  returnWhiteToBlack();
  }
  if (s1 == 0) {       
  lastBlack = "Sensor1"
  }
  if (s5 == 0) {      
  lastBlack = "Sensor5"
  }





}

void hardRight()
{
lastBlack = "Sensor5"
}
void curveRight()
{

}
void hardLeft()
{
lastBlack = "Sensor1"
}
void curveLeft()
{
  
}
void straight()
{
  
}
void returnWhiteToBlack()
{
  
}ij