int zero, t, t_ant, valor;

void setup()
{
  Serial.begin(1000000);
  zero = micros();
  t_ant = micros();
}
 
void loop()
{
  t = micros()-zero;
  valor = analogRead(A0);
  if(t>t_ant+100){
    Serial.print(t);
    Serial.print(";");
    Serial.print(t/1000);
    Serial.print(";");
    Serial.println(valor);
    t_ant = t;
  }
}
