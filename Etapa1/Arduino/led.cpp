#define LED1 13         // número do terminal do arduino conectado à protoboard
int interval = 1000;    // delay inicializado em 1000 millisegundos (s)	

void setup()
{
  pinMode(LED1, OUTPUT);
}

void loop()
{
  
  digitalWrite(LED1, HIGH); // Liga LED1
  delay(interval); // Aguarda o valor do intervalo em millisegundos(s)
  
  digitalWrite(LED1, LOW); // Ascende LED1
  delay(interval); // Aguarda o valor do intervalo em millisegundos(s)
   
  // Acende em 3 intervalos diferentes
  interval += (interval < 3000) ? 1000 : -2000;
}
