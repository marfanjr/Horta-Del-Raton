/*
	This header is for DEFINES ONLY
	These #defines are them, parsed by agent/utils.py to expose the values in
    our python context, so when you add a #define here to use. REMEMBER to
    add a new "if" in the method parseLine() of Constants class (utils.py)
*/

// SENSORS PINS

// ACTUATORS PINS

// SERIAL
#define PORT_PATH /dev/tty.usbmodem621
#define BAUD_RATE 9600

// COMMANDS
#define CMD_LUMINOSITY          0
#define CMD_HUMIDITY            1
#define CMD_SOLENOID            2