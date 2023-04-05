<h2 align="center">
    <img src="https://www.redbytes.in/wp-content/uploads/2018/04/arduino-1-logo-png-transparent.png" alt="arduino logo" height="200" width="200"></br>
    <br> Missão Arduino </br>
</h2>

> O Arduino é uma placa microcontroladora programável de código aberto, projetada para criar projetos eletrônicos interativos, acessíveis tanto em preço quanto em nível de dificuldade. Sua plataforma permite a criação de uma grande variedade de aplicaç, como robôs, sensores, dispositivos de IoT e outros. 

<img src="./circuito.png"> </igm>
>Tinkercad Link: https://www.tinkercad.com/things/l59BRV1MPYP?sharecode=_D0ukdK0UZrTuy1bJTvIayRe9nH0VUIRE3Z_6ymjVWQ

### 🎯 Desafio da Missão
- Montar o circuito para acender um LED com Arduino em uma protoboard no TinkerCAD;
- Dimensionar o resistor ideal para a cor do LED escolhida;
- Programar o Arduino para piscar um LED com 3 períodos de tempo diferentes.

### 📓 Requisitos
- Nesse pequeno projeto foi usado um Arduino, foi usado:
    - Arduino;
    - Protoboard;
    - LED vermelha (2,0V);
    - Resistor (150R);
    - Fios.

### 📒 Steps

1. Primeiramente, é necessario energizar a placa. Para isso, conectei um fio saindo do terminal GND do Arduino até o polo negativo da protoboard, caracterizando um fio terra. Após isso, liguei um fio, saindo de um terminal qualquer (usei o 13), até o polo positivo da protoboard.

2. A seguir, é de suma importancia escolher um resistor que consiga suportar a voltagem vinda da protoboard. Então, tendo em vista que o arduino fornece 5V à palca, quando enviamos um sinal HIGH, e que a led vermelha tem uma tensão máxima de 2 volts e corrente de até 20 Miliamperes, calculei resistência do resistor através da fórmula:

$$
R = (Valimentacao - Vled)/CorrenteLed
$$

$$
R = (5V -  2V)/0,020A
$$

$$
R = 150Ω
$$

<ul>
    <em> Valimentação = 5V; </em><br>
    <em> Vled = 2V; </em><br>
    <em> CorrenteLed = 0,020A; </em>
    
</ul>

3. Por isso, liguei um fio partindo do polo negativo da placa até a ponta de um resistor com 150Ω. Nesse sentido, a outra ponta do resistor foi ligada ao cátodo luz led.

4. Em seguida, conectei o ânodo da luz de led ao polo positivo da placa.

5. Ao final, escrevi o seguinte codigo em c++ para o funcionamento da placa:

``` cpp
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
  
  digitalWrite(LED1, LOW); // Acende LED1
  delay(interval); // Aguarda o valor do intervalo em millisegundos(s)
   
  // Acende em 3 intervalos diferentes
  interval += (interval < 3000) ? 1000 : -2000;
}
```
