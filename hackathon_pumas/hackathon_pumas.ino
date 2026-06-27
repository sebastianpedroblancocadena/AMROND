#include <Servo.h>

Servo servo;

void setup()
{
    Serial.begin(9600);

    servo.attach(9);

    servo.write(0);
}

void loop()
{
    if(Serial.available())
    {
        String cmd = Serial.readStringUntil('\n');

        cmd.trim();

        if(cmd=="TRAP")
        {
            servo.write(180);

            delay(3000);

            servo.write(0);

            Serial.println("OK");
        }
    }
}
