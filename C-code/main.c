#include <C:\Users\tombe\Documents\Atmel Studio\7.0\GccApplication4\GccApplication4\AVR_TTC_scheduler.h>
#include <string.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6
#include <util/delay.h>


// output on USB = PD1 = board pin 1
// datasheet p.190; F_OSC = 16 MHz & baud rate = 19.200
#define UBBRVAL 51// voor het checken van bits#define CHECK_BIT(var,pos) (((var)>>(pos)) & 1)//	variabele voor uitrol/inrolint huidige_uitrol;int max_uitrol = 50;			//default-waarde, dit is de uitrol in centimetersint min_uitrol = 10;			//default-waarde, dit is de uitrol in centimetersint uitrol;int inrol;//variabele voor het aan- en uitzetten van handmatig uitrollenint manual = 0;// variabele voor inputuint8_t input;
void uart_init(void)
{
	// set the baud rate
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// enable transmitter and enable receiver
	UCSR0B = (1<<RXEN0)|(1<<TXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

void transmit(uint8_t data)
{
	// wait for an empty transmit buffer
	// UDRE is set when the transmit buffer is empty
	loop_until_bit_is_set(UCSR0A, UDRE0);
	// send the data
	UDR0 = data;
}uint8_t receive(void){	if(UCSR0A & (1 << RXC0))	{	 	return UDR0;	}	return 0;}

//spull voor de sensoren

void initPortManipulator() {
	// Source: https://medium.com/@jrejaud/arduino-to-avr-c-reference-guide-7d113b4309f7
	// 16Mhz / 128 = 125kHz ADC reference clock
	ADCSRA |= ((1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0));
	// Voltage reference from AVcc (5V on ATMega328p)
	ADMUX |= (1<<REFS0);
	ADCSRA |= (1<<ADEN);    // Turn on ADC
	ADCSRA |= (1<<ADSC);    // Do a preliminary conversion
}

// Read analog pins
int analogRead(uint8_t pin) {
	// Source: https://medium.com/@jrejaud/arduino-to-avr-c-reference-guide-7d113b4309f7
	ADMUX &= 0xF0;    // Clear previously read channel
	ADMUX |= pin;    // Define new ADC Channel to read, analog pins 0 to 5 on ATMega328p
	ADCSRA |= (1<<ADSC);    // New Conversion
	ADCSRA |= (1<<ADSC);    // Do a preliminary conversion
	// Wait until conversion is finished
	while(ADCSRA & (1<<ADSC));
	// Return ADC value
	return ADCW;
}


// The array of tasks
sTask SCH_tasks_G[SCH_MAX_TASKS];


/*------------------------------------------------------------------*-

  SCH_Dispatch_Tasks()

  This is the 'dispatcher' function.  When a task (function)
  is due to run, SCH_Dispatch_Tasks() will run it.
  This function must be called (repeatedly) from the main loop.

-*------------------------------------------------------------------*/

void SCH_Dispatch_Tasks(void)
{
   unsigned char Index;

   // Dispatches (runs) the next task (if one is ready)
   for(Index = 0; Index < SCH_MAX_TASKS; Index++)
   {
      if((SCH_tasks_G[Index].RunMe > 0) && (SCH_tasks_G[Index].pTask != 0))
      {
         (*SCH_tasks_G[Index].pTask)();  // Run the task
         SCH_tasks_G[Index].RunMe -= 1;   // Reset / reduce RunMe flag

         // Periodic tasks will automatically run again
         // - if this is a 'one shot' task, remove it from the array
         if(SCH_tasks_G[Index].Period == 0)
         {
            SCH_Delete_Task(Index);
         }
		 // Tasks hebben een aantal 'repeats' die bij elke uitvoer verminderen
		 // Als ze op zijn wordt de task verwijderd.
		 if(SCH_tasks_G[Index].Repeats > 0)
		 {
			 SCH_tasks_G[Index].Repeats -= 1;
		 }
		 if(SCH_tasks_G[Index].Repeats == 0)
		 {
			 SCH_Delete_Task(Index);
		 }
      }
   }
}

/*------------------------------------------------------------------*-

  SCH_Add_Task()

  Causes a task (function) to be executed at regular intervals 
  or after a user-defined delay

  pFunction - The name of the function which is to be scheduled.
              NOTE: All scheduled functions must be 'void, void' -
              that is, they must take no parameters, and have 
              a void return type. 
                   
  DELAY     - The interval (TICKS) before the task is first executed

  PERIOD    - If 'PERIOD' is 0, the function is only called once,
              at the time determined by 'DELAY'.  If PERIOD is non-zero,
              then the function is called repeatedly at an interval
              determined by the value of PERIOD (see below for examples
              which should help clarify this).


  RETURN VALUE:  

  Returns the position in the task array at which the task has been 
  added.  If the return value is SCH_MAX_TASKS then the task could 
  not be added to the array (there was insufficient space).  If the
  return value is < SCH_MAX_TASKS, then the task was added 
  successfully.  

  Note: this return value may be required, if a task is
  to be subsequently deleted - see SCH_Delete_Task().

  EXAMPLES:

  Task_ID = SCH_Add_Task(Do_X,1000,0);
  Causes the function Do_X() to be executed once after 1000 sch ticks.            

  Task_ID = SCH_Add_Task(Do_X,0,1000);
  Causes the function Do_X() to be executed regularly, every 1000 sch ticks.            

  Task_ID = SCH_Add_Task(Do_X,300,1000);
  Causes the function Do_X() to be executed regularly, every 1000 ticks.
  Task will be first executed at T = 300 ticks, then 1300, 2300, etc.            
 
-*------------------------------------------------------------------*/

unsigned char SCH_Add_Task(void (*pFunction)(), const unsigned int DELAY, const unsigned int PERIOD, const unsigned int REPEATS)
{
   unsigned char Index = 0;

   // First find a gap in the array (if there is one)
   while((SCH_tasks_G[Index].pTask != 0) && (Index < SCH_MAX_TASKS))
   {
      Index++;
   }

   // Have we reached the end of the list?   
   if(Index == SCH_MAX_TASKS)
   {
      // Task list is full, return an error code
      return SCH_MAX_TASKS;  
   }

   // If we're here, there is a space in the task array
   SCH_tasks_G[Index].pTask = pFunction;
   SCH_tasks_G[Index].Delay =DELAY;
   SCH_tasks_G[Index].Period = PERIOD;
   SCH_tasks_G[Index].RunMe = 0;
   SCH_tasks_G[Index].Repeats = REPEATS;

   // return position of task (to allow later deletion)
   return Index;
}

/*------------------------------------------------------------------*-

  SCH_Delete_Task()

  Removes a task from the scheduler.  Note that this does
  *not* delete the associated function from memory: 
  it simply means that it is no longer called by the scheduler. 
 
  TASK_INDEX - The task index.  Provided by SCH_Add_Task(). 

  RETURN VALUE:  RETURN_ERROR or RETURN_NORMAL

-*------------------------------------------------------------------*/

unsigned char SCH_Delete_Task(const unsigned char TASK_INDEX)
{
   // Return_code can be used for error reporting, NOT USED HERE THOUGH!
   unsigned char Return_code = 0;

   SCH_tasks_G[TASK_INDEX].pTask = 0;
   SCH_tasks_G[TASK_INDEX].Delay = 0;
   SCH_tasks_G[TASK_INDEX].Period = 0;
   SCH_tasks_G[TASK_INDEX].RunMe = 0;
   SCH_tasks_G[TASK_INDEX].Repeats = 0;

   return Return_code;
}

/*------------------------------------------------------------------*-

  SCH_Init_T1()

  Scheduler initialisation function.  Prepares scheduler
  data structures and sets up timer interrupts at required rate.
  You must call this function before using the scheduler.  

-*------------------------------------------------------------------*/

void SCH_Init_T1(void)
{
   unsigned char i;

   for(i = 0; i < SCH_MAX_TASKS; i++)
   {
      SCH_Delete_Task(i);
   }

   // Set up Timer 1
   // Values for 1ms and 10ms ticks are provided for various crystals

   // Hier moet de timer periode worden aangepast ....!
   OCR1A = (uint16_t)625;   		     // 10ms = (256/16.000.000) * 625
   TCCR1B = (1 << CS12) | (1 << WGM12);  // prescale op 64, top counter = value OCR1A (CTC mode)
   TIMSK1 = 1 << OCIE1A;   		     // Timer 1 Output Compare A Match Interrupt Enable
}

/*------------------------------------------------------------------*-

  SCH_Start()

  Starts the scheduler, by enabling interrupts.

  NOTE: Usually called after all regular tasks are added,
  to keep the tasks synchronised.

  NOTE: ONLY THE SCHEDULER INTERRUPT SHOULD BE ENABLED!!! 
 
-*------------------------------------------------------------------*/

void SCH_Start(void)
{
      sei();
}

/*------------------------------------------------------------------*-

  SCH_Update

  This is the scheduler ISR.  It is called at a rate 
  determined by the timer settings in SCH_Init_T1().

-*------------------------------------------------------------------*/

ISR(TIMER1_COMPA_vect)
{
   unsigned char Index;
   for(Index = 0; Index < SCH_MAX_TASKS; Index++)
   {
      // Check if there is a task at this location
      if(SCH_tasks_G[Index].pTask)
      {
         if(SCH_tasks_G[Index].Delay == 0)
         {
            // The task is due to run, Inc. the 'RunMe' flag
            SCH_tasks_G[Index].RunMe += 1;

            if(SCH_tasks_G[Index].Period)
            {
               // Schedule periodic tasks to run again
               SCH_tasks_G[Index].Delay = SCH_tasks_G[Index].Period;
               SCH_tasks_G[Index].Delay -= 1;
            }
         }
         else
         {
            // Not yet ready to run: just decrement the delay
            SCH_tasks_G[Index].Delay -= 1;
         }
      }
   }
}

// ------------------------------------------------------------------

//functies:

//in- en uitrol
void roodaan(void)
{
	PORTB |= 0x01;
}

void rooduit(void)
{
	PORTB &= 0xfe;
}

void groenaan(void)
{
	PORTB |= 0x02;
}

void groenuit(void)
{
	PORTB &= 0xfd;
}

void geelaan(void)
{
	PORTB |= 0x04;
}

void geeluit(void)
{
	PORTB &= 0xfb;
}

void roluit(void)
{
	if (huidige_uitrol < max_uitrol)				//als de nieuwe max_uitrol kleiner is dan de oude, dan moet er niet uitgerold worden
	{
		uitrol = abs(max_uitrol-huidige_uitrol);	//hoe ver er uitgerold moet worden
	} 
	else
	{
		uitrol = 0;									//uitrol = 0 oftewel, er moet niet uitgerold worden
	}
	int flitsen = uitrol/10;					//hoe vaak het gele LEDje moet flitsen, dit is de afstand in centimers gedeeld door 10
	groenuit();
	roodaan();
	SCH_Add_Task(geelaan, 0, 100, flitsen);
	SCH_Add_Task(geeluit, 50, 100, flitsen);
	huidige_uitrol = max_uitrol;
	transmit(max_uitrol/10);					//de max_uitrol wordt teruggestuurd, voor testen
}

void rolin(void)
{
	if (huidige_uitrol > min_uitrol)				//als de nieuwe min_uitrol groter is dan de oude, dan moet er niet ingerold worden
	{
		inrol = abs(huidige_uitrol-min_uitrol);		//hoe ver er ingerold moet worden
	}
	else
	{
		inrol = 0;									// inrol = 0 oftewel, er wordt niet ingerold
	}
	int flitsen = inrol/10;						//hoe vaak het gele LEDje moet flitsen, dit is de afstand in centimers gedeeld door 10
	rooduit();
	groenaan();
	SCH_Add_Task(geelaan, 0, 100, flitsen);
	SCH_Add_Task(geeluit, 50, 100, flitsen);
	huidige_uitrol = min_uitrol;
	transmit(min_uitrol/10);					//de min_uitrol wordt teruggestuurd, voor testen
}

void tempsend(void)
{
	transmit(analogRead(1));
}

void lichtsend(void)
{
	transmit(analogRead(0));
}

void receivecheck(void)
{
	input = receive();
	
	if (input != 0)								//checken of er wel input is
	{
		//transmit(input);
		if (manual == 1 && input == 0x01)						//er moet ingerold worden
		{
			rolin();
		}
		if (manual == 1 && input == 0x02)						//er moet uitgerold worden
		{
			roluit();
		}
		if (CHECK_BIT(input, 7) == 1 && CHECK_BIT(input, 6) == 0)	//als het eerste bit op 1 staat en het tweede op 0, wordt de max-afstand ingesteld
		{
			transmit(input);
			max_uitrol = (input - 128)*10;							//128 wordt van de waarde afgetrokken als compensatie voor de markeringsbits, er wordt met 10 vermenigvuldigd omdat de afstand in decimeters wordt meegegeven
			transmit(max_uitrol/10);
		}
		if (CHECK_BIT(input, 7) == 1 && CHECK_BIT(input, 6) == 1)	//als de eerste en tweede bits op 1 staan, wordt de min-afstand ingesteld
		{
			min_uitrol = (input - 192)*10;							//192 wordt van de waarde afgetrokken als compensatie voor de markeringsbits, er wordt met 10 vermenigvuldigd omdat de afstand in decimeters wordt meegegeven
		}
		if (CHECK_BIT(input, 7) == 0 && CHECK_BIT(input, 6) == 1)
		{
			manual = input-64;
		}
		
		input = 0;
	}
}

int main()
{
	DDRB = 7;									//zet de gepaste pinnen op output
	SCH_Init_T1();								//initialisatie scheduler
	SCH_Start();
	
	huidige_uitrol = 30;						//de huidige status van het scherm, dit is de uitrol in centimeters
	
	initPortManipulator();
	uart_init();
	SCH_Start();
	
	SCH_Add_Task(receivecheck, 0, 100, -1);
	SCH_Add_Task(tempsend, 0, 500, -1);
	SCH_Add_Task(lichtsend, 0, 500, -1);
	while(1)
	{
		SCH_Dispatch_Tasks();
	}
	return 1;
}