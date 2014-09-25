.. section-author:: Edwin van den Oetelaar


USB bus convert chip CH341
==========================

| document version : |version|
| last updated : |today|

.. section-autonumbering::
   :start: 1


.. sidebar:: about this datasheet

   My name is Edwin van den Oetelaar and I made this datasheet to learn `Sphinx-doc <http://sphinx-doc.org/>`_

   The ``CH341`` is commonly used on all kinds of Chinese products and is easily available.

   I copied the datasheet from the website of the manufacturer and did not modify the English, all mistakes were already in the original document.


.. title:: USB bus convert chip CH341

.. header:: English DataSheet

| `link to http://wch.cn <http://wch.cn>`_
| `link to http://wch-ic.com <http://wch-ic.com>`_

Introduction
------------

CH341 is a USB bus convert chip, providing UART, printer port, parallel and synchronous serial with
2-wire or 4-wire through USB bus.

* In UART mode, CH341 provides alternant rate control signals such as serial transfer enable, serial
  receive in ready etc. It also supplies common MODEM communication signal in order to expand UART for
  computer or upgrade common synchronous interface device to USB bus directly.

* In printer port mode, CH341 supplies standard USB printer port which compounds USB relevant
  protocol and Windows operate system used to upgrade ordinary parallel printer to USB bus directly.

* In parallel mode, CH341 gives out 8-bit parallel in EPP or MEM mode. It can be used to input/output
  data directly without MCU/DSP.

Besides, CH341A also supports some common synchronous serial such as 2-wire (SCL, SDA) and
4-wire (CS, SCK/CLK, MISO/SDI/DIN and MOSI/SDO/DOUT) interface.

.. figure:: Figure1.png
   :alt: Dit is een alt tag
   :width: 90%
   :align: center

Features
--------

Introduction
^^^^^^^^^^^^

- Full speed USB device interface, conforms to USB Specification Version 2.0, only needs crystal and capacitance external.
- Optional: define Vender ID, production ID and list number through external low-cost serial EEPROM.
- Supports 5V and 3.3V power source.
- Low-cost, directly convert serial peripheral equipment, parallel printer and parallel peripheral equipment.
- SOP-28 and SSOP-20 package lead free, compatible with RoHS.
- Only compatible with application layer because interfaces are diverted via USB.


UART
^^^^

* Simulate standard serial used to upgrade serial peripheral equipment or increase extra serial via USB.
* Totally compatible with serial application program of computer Windows operation system.
* Hardware full-duplex serial, on-chip transform and receive buffer, supports 50bps~2Mbps communication baud rate.
* Supporting five, six, seven or eight data bits, supporting odd, even, blank, token and no check.
* Supporting serial transfer and receive enable and serial receive ready etc transfer speed control signal and MODEM liaison signal.
* Providing RS232, RS485 and RS422 interface through adding level switch equipment external.
* Supporting indirectly access to outside serial EEPROM memory through standard serial communication.

Printer port
^^^^^^^^^^^^

* Standard USB printer port used to upgrade parallel printer, conforms to relevant USB specification.
* Compatible with Windows operation system, totally compatible with application program under Windows 2000 and XP without drive program.
* Supports various standard parallel printers, low-speed and high-speed print mode are optional.
* Supports bi-directional communication of IEEE-1284 specification, supports single directional and bi-directional transfer printer.

Parallel
^^^^^^^^

* Providing two interface mode: EPP and MEM.
* EPP mode supplies AS#, DS# and WR# etc signal, similar with EPP V1.7 or EPP V1.9.
* MEM mode supplies A0, RD# and WR# etc signal, similar with memory read/write mode.

Synchronous serial
^^^^^^^^^^^^^^^^^^

* Adopts FlexWireTM technology, realize various 2-wire to 5-wire synchronous serial via software.
* As Host/Master endpoint, supports 2-wire and 4-wire etc common synchronous serial.
* 2-wire interface supplies SCL and SDA signal wire, supports four kinds of transfer speed.

Package
^^^^^^^

.. figure:: ch341_package.png
   :align: center


.. table:: Available packages

   +---------------+------------------+--------------+-----------------------------------------+---------------+
   | Package shape | Width of plastic | Pitch of Pin | Instruction of package                  | Ordering type |
   +===============+==================+==============+=========================================+===============+
   | SOP-28        | 7.62mm 300mil    | 1.27mm 50mil | Small outline package of 28-pin         | CH341A        |
   +---------------+------------------+--------------+-----------------------------------------+---------------+
   | SSOP-20       | 5.30mm 209mil    | 0.65mm 25mil | Shrink small outline package of 20-pin  | CH341T        |
   +---------------+------------------+--------------+-----------------------------------------+---------------+
   | SOP-28        | 7.62mm 300mil    | 1.27mm 50mil | Small outline package of 28-pin         | CH341H        |
   +---------------+------------------+--------------+-----------------------------------------+---------------+

.. Note::

   * CH341T is only used to USB convert to serial interface or USB convert to 2-wire interface,
   * CH341H is only used to USB convert to 4-wire interfaces etc. (such as SPI)


Pins
----

Some info about pins.

General explanation
^^^^^^^^^^^^^^^^^^^

The detail function of CH341 is decided by function configuration after reset.
The same pin may have different define under different function.
CH341T and CH341H adopts SSOP-20 package, the simple vision of CH341A, the pins with same pin name have the same function of them.
The multiply VCC pins parallel connect as VCC and multiply GND pins parallel connect as GND in CH341T and CH341H.

Standard public pins
^^^^^^^^^^^^^^^^^^^^

+---------------------+----------+----------+---------------------------------------------------------------------------+
| Pin No.             | Pin Name | Pin Type | Pin Description                                                           |
+------+-------+------+          |          |                                                                           |
| 341A | 341T  | 341H |          |          |                                                                           |
+======+=======+======+==========+==========+===========================================================================+
| 28   | 13,20 | 20   | VCC      | POWER    | Positive power input port, requires an 0.1uF power decoupling capacitance |
+------+-------+------+----------+----------+---------------------------------------------------------------------------+


7,18 GND POWER Public ground, ground connection for USB bus
341A 341T 341H
28 13,20 12 11,12 9 6 4 V3 POWER Attachment of VCC input external power while
                                3.3V;connects of 0.01uF decoupling capacitance
                               outside while 5V
13 9 8 XI IN Input of crystal oscillator, attachment of crystal
            and crystal oscillator capacitance external
14 10 9 XO OUT Opposite output of crystal oscillator, attachment of
              crystal and crystal oscillator capacitance outside
10 7 5 UD+ USB signal Directly connects to D+ data wire of USB bus
11 8 6 UD- USB signal Directly connects to D- data wire of USB bus
1 1 1 ACT# OUT After USB device configuration output status, low
              active
2 No 2 RSTI IN Input of external reset, active with high-level, with
              pull-down resistor
SCL Drain open Output of chip function configuration, with
    Output pull-up resistor, connect with SCL of serial
          EEPROM configuration chip
SDA drain open Input of chip function configuration, with pull-up
    OUT/IN resistor, connect with SDA of serial EEPROM
          configuration chip
24
23
16
15
No
No
The DataSheet of CH341 (the first)
4
4.3.Asynchronous serial interface pins
Pin No.
Pin Name Pin Type Pin Description
3 TXD OUT Serial data output
6 4 RXD IN Serial data input, with pull-up resistor
27 19 TEN# IN Serial transfer enable, active with low-level, with pull-up
             resistor
25 17 RDY# OUT Serial receive is ready, low-level active
26 18 TNOW OUT Indicate serial interface transfer is carrying out, high-level
              active
4 2 ROV# Tri-state Serial receive buffer overflow, low-level active
         Output
15 No CTS# IN MODEM liaison input signal, clear transfer, low-level
             active
16 No DSR# IN MODEM liaison input signal, data equipment is ready,
             low-level active
17 No RI# IN MODEM liaison input signal, indication with bell,
            low-level active
18 No DCD# IN MODEM communication input signal, carrier wave
             detection, low-level active
20 No DTR# Tri-state MODEM liaison output signal, data terminal ready,
           Output low-level active
21 No RST# Tri-state MODEM liaison output signal, request transferring,
           Output low-level active
19 No OUT# Tri-state Self-define common output signal, low-level active
           Output
7 5 INT# IN Self-define interrupt request, rising edge active, with
           pull-up resistor
8 No IN3 IN Self-define common input signal, un-connection is
           recommended
3 No IN7 IN Self-define common input signal, un-connection is
           recommended
22 14 SLP# Tri-state Sleep state output signal, low-level active
           Output
341A 341T
5
4.4.Print interface mode pins
341A Pin Name Pin Type Pin Description
Pin No.
22~15 D7~D0 Tri-state 8-bit parallel data output, connect to DATA7~DATA0
            Output
25 STB# OUT Data strobe output, low-level active, connect to STROBE
4 AFD# OUT Automatically feed output, low-level active, connect to
          AUTO-FEED
The DataSheet of CH341 (the first)
5
26 INI# OUT Initialize printer, low-level active, connect to INIT
3 SIN# Tri-state Select printer, low-level active, connect to SELECT-IN
       Output
5 ERR# IN Error with printer, low-level active, with pull-up resistor,
         connect to ERROR or FAULT
8 SLCT IN Printer is selected, high-level active, with pull-up resistor,
         connect to SELECT or SLCT
6 PEMP IN Printer is short of papers, high-level active, connect to
         PEMPTY or PERROR
7 ACK# IN Printer data receive answer, active with rising edge, with
         pull-up resistor, connect to ACK
27 BUSY IN Printer is busy, high-level active, with pull-up resistor, connect
          to BUSY
4.5.Parallel mode pins
341A Pin Name Pin Type Pin Description
Pin No.
22~15 D7~D0 Bi-directional 8-bit bi-directional data bus, with pull-up resistor
            tri-state
25
WR#
EPP mode: indicate write operation, write with low-level,
read with high-level
OUT
MEM mode: write strobe output WR#, low-level active
EPP mode: data operation select, low-level active
4 DS# OUT 26 RST# OUT Reset output, low-level active
3 AS# Tri-state EPP mode: address operation strobe, low-level active
      Output
27 WAIT# IN CH341A: request to wait, low-level active, with pull-up
           resistor
7 INT# IN Interrupt request input, active with rising edge, with
         pull-up resistor
5 ERR# IN Self-define common input, with pull-up resistor
8 SLCT IN Self-define common input, with pull-up resistor
6 PEMP IN Self-define common input, with pull-up resistor
MEM mode: read strobe output RD#, low-level active
MEM mode: address wire output ADDR or A0
4.6.Synchronous serial interface pins
Pin No.
Pin Name Pin Type Pin Description
17 DIN IN 4-wire serial data input, with pull-up resistor
21 16 DIN2 IN 5-wire serial data input 2,with pull-up resistor
20 15 DOUT Tri-state 4-wire serial data output, other name is MOSI or SDO
           Output
19 14 DOUT2 Tri-state 5-wire serial data output 2
341A 341H
22
The DataSheet of CH341 (the first)
6
Output
18
13
17~15 12~10
DCK Tri-state 4-wire/5-wire serial interface clock output, other name is
    Output SCK
CS2~CS0 Tri-state 4-wire serial interface chip select output 2#~0#
        Output
24 No SCL Drain open 2-wire serial interface clock output, with pull-up resistor
          Output
23 No SDA Drain open 2-wire serial interface data input/output, with pull-up
          OUT/IN resistor
26 19 RST# OUT Reset output, low-level active
7 3 INT# IN Interrupt request input, active with rising edge, with
           pull-up resistor
5,8,6 No IN Self-define common input, with pull-up resistor
5. Function explanation
5.1.General explanation
The data in this manual has three types. Binary numbers are followed by a “B”. Hexadecimal numbers
are followed by an “H”. Numbers without annotations are decimals.
CH341 is a convert chip of USB bus, providing asynchronous serial interface, standard USB printer
port, parallel interface and synchronous serial interface. The manual mainly supplies asynchronous serial
interface and printer port explanation. The introduction of parallel interface and asynchronous serial
interface can refer to the second manual.
5.2.Hardware introduction
Some pins of the CH341 have many functions, so they have different features during reset period and
working normally after reset. All the pins with tri-state output have set pull-up resistors internal. They are
output pins after chip reset and during the reset time they are forbidden with tri-state output, pull-up resistors
supply pull-up current. If necessary, set pull-up resistors or pull-down resistors outside to set default level in
relevant pins during reset time. The external resistors are 2KΩ~5KΩ. For example, the tri-state is forbidden
of AS# during reset time in parallel interface mode, only depends on pull-up current to retain high-level. In
order to avoid disturbing peripheral circuit, a 3KΩ pull-up resistor can add to keep steady high-level.
The ACT# of CH341 is output state of USB device configuration completion. The pin output high-level
when USB device is un-configuration or configuration is cancelled. After USB configuration, the pin output
low-level. The ACT# pin of CH341 can attach to current-limited resistance LED to indicate relative state of
USB device configuration.
CH341 sets USB pull-up resistance internal, UD+ and UD- pin must connect to USB bus directly.
CH341 set power-up reset circuit internal. RSTI is used to input asynchronous reset signal from outside.
The CH341 is reset when RETI is high-level; the CH341 will delay about 20mS to reset then step into work
normally when the RSTI recover to low-level. In order to reset credibly during power up and decrease
disturb from outside, recommend to over connect a 0.47uF capacitance between RSTI and VCC.
Supplies 12MHz clock signal for XI pin to ensure CH341 work normally. In common, the clock signal
is generated by inverter in CH341 through oscillating of crystal keeping frequency. A crystal of 12MHz
between XI and XO can compose the peripheral circuit and connects an oscillator capacitance to ground
respectively.
The DataSheet of CH341 (the first)
7
CH341 support 5V and 3.3V source voltage. When working on 5V source voltage, the VCC input 5V
power from outside, and V3 connects to 4700pF or 0.01uF decoupling capacitance. If the work power is
3.3V, connect V3 to VCC, input 3.3V source voltage. The voltage of other circuit which is connected to
CH341 is no pass than 3.3V.
5.3.Function configuration
CH341 configures chip function through SCL and SDA, there are two modes: assemble configure
directly and peripheral chip configure.
Assemble configure directly connects SCL to SDA to configure function of CH341. The characteristics
are list: additional cost is no need, only use default vender ID and production ID etc. In assemble configure
directly mode, the information is the same with default value in peripheral chip configure except production
ID. And in the inner of CH341H, the SDA is low-level.
State of SCL and SDA Chip function Default production ID
SDA and SCL are suspended USB change to asynchronous serial 5523H
                          interface, simulate computer serial
                          interface
SDA connect to low-level while USB change to EPP/MEM parallel 5512H
SCL is suspended interface and asynchronous interface
Connect SDA to SCL directly Change parallel interface printer to 5584H
                            standard USB printer
The peripheral chip configure is composed as following: SCL and SDA are as 2-wire synchronous
serial interface connect to external serial EEPROM configuration chip, via EEPROM chip define chip
function, vender ID, production ID and so on. The configuration chip is 24CXX of 7-bit address, such as:
24C01A, 24C02, 24C04, 24C16 and so on. The features are: define chip function and various pieces of
identification information of USB productions flexibly. On-line modify data in serial EEPROM and redefine
chip function and various identification information of CH341 via the tool software CH341CFG.EXE in
Windows.
In generally, CH341 detects the content of peripheral configuration chip through SCL and SDA. If the
content is invalid, accord SCL and SDA to use assemble configure directly. To avoid effect 2-wire
synchronous serial interface when using SCL and SDA to configure, the ACT# of CH341 is set to low-level
through 2KΩ resistance during configuration time. The CH341 is enforced as EPP/MEM parallel interface
and synchronous serial interface, it doesn’t detect outside configuration chip forwardly.
The following table is content of peripheral serial EEPROM configuration chip.
Byte
address
Shortened Explanation Default value
form
SIG The peripheral configuration chip is valid, former byte must be 53H, 53H
    other value imply the configuration data invalid, use assemble
    configure directly
01H MODE Select communication interface: 23H=serial interface, 12H=print 23H or 12H
         port or parallel interface, other value imply the configuration data
         invalid, use assemble configure directly
02H CFG Detail configuration, refer to the below table FEH
(Reserved unit, must be set as 00H or 0FFH 00H
Vender ID, high byte is behind, any value 1A86H
00H
03H
05H~04H
VID
The DataSheet of CH341 (the first)
8
07H~06H PID Product ID, high byte is behind, any value 55??H
09H~08H RID Release ID, high byte is behind, any value 0100H
17H~10H SN Serial number, the size is 8 12345678
DID Printer port: defined printer device ID string accord IEEE-1284 PIDS Serial interface or printer port: production explanation string of 00H, 00H
                                                                         un-printer
(Reserved unit) 00H or FFH
7FH~20H
Others
The following table is CFG defining detail configuration, explanation is according bit.
Bit
address
Shortened Explanation Default value
form
7 PRT Select communication interface: for serial interface, the value 1
      must be 1
      For un-serial interface select: 0=standard USB printer port;
      1=parallel interface
6 PWR USB device supply power mode: 0=peripheral and USB; 1
      1=USB bus only
5 SN-S Production serial number string: 0=valid; 1=invalid 1
DID-S Printer’s device ID string:0=valid; 1=invalid 1
PID-S Product explanation string of un-printer: 0=valid; 1=invalid 1
3 SPD Data transfer speed of printer port:0=high-speed; 1
      1=low-speed/standard
2 SUSP Automatically suspend and low-cost when USB is not busy, 1
       0=forbid; 1=allow
PROT Define interface protocol in configuration description sign of 1
     USB device: for serial or parallel interface, the valid value is 0
     0 to 3, 0 is recommended,
     For standard USB printer port: the valid value is 1 and 2, 2 is
     recommended
4
1
0
5.4.Asynchronous serial interface
In the asynchronous serial mode the CH341’s pins contain: data transfer pin, hardware speed control
pin, operation state pin, MODEM communication signal pin and assistant pin.
Data transfer pin consists: TXD and RXD pins. When serial interface is leisure TXD and RXD are
high-level.
Hardware speed control pin consists: TEN# and RDY#. TEN# is serial interface transfer enable, when it
is high-level, CH341 will stop transfer data from serial interface. Until it is low-level, CH341 will go on
transferring data. RDY# is serial interface receive ready. When it is high-level indicate CH341 is not ready
to receive data, maybe the chip is reset, USB is un-configure, cancel configuration or serial interface receive
buffer is full etc.
Operation state pins consist: TNOW and ROV# pins. TNOW with high-level indicates CH341 is
transferring data from serial interface. When the transfer is completed the TNOW is low-level. TNOW can
indicate serial interface receive and transfer switch state in semi-duplex serial interface mode. ROV#
indicates CH341 internal serial interface receive buffer will overflow or have overflowed and the following
data will discard. In common, the receive buffer is not overflow, so the ROV# is high-level.
MODEM communicate signal pins consist: CTS#, DSR#, RI#, DCD# , DTR# and RST# pin. All the
MODEM communication signals are controlled and defined by computer applied program, not directly
The DataSheet of CH341 (the first)
9
controlled by CH341. If needing higher-speed to control signal, instead of hardware speed signals.
Assistant pins consist: INT#, OUT#, IN3 and IN7 pin. INT# is a self-defined interrupt request input,
when it detects rising edge of the CLK pin, it will inform computer. OUT# is common low-level active
output signal and its state is determined by computer applied program. These assistant pins are not standard
serial interface and their functions are similar with MODEM communication signals.
CH341 sets separate transceiver buffer internal and supports simplex, semi-duplex and full duplex
asynchronous serial communication. Serial data consist of one low-level starting bit, five to nine data bits
and one or two high-level stopping bit, supports odd checkout/even checkout/flag checkout/blank checkout.
The following communication band rates are supported by CH341:
50,75,100,110,134.5,150,300,600,900,1200,1800,2400,3600,4800,9600,14400,19200,28800,33600,38400,
56000,57600,76800,115200,28000,53600,30400,60800,21600,500000,2000000 and so on. The band rate
error of serial transfer signal is less then 0.3% and the allowance receive signals error is not less then 2%.
In the Windows operation system of computer, driver program of CH341 can simulate standard serial
interface, the most former serial interfaces applied programs are totally compatible without any modify. In
addition, CH341 supports indirectly access to serial EEPROM memory external via standard serial interface
communication mode.
CH341 may use to upgrade serial peripheral equipments or add extra serial interface for computer
through USB bus. External additional of level switch equipment can supply interface such as
RS232,RS485,RS422 and so on.
5.5.Printer interface
The pins of CH341 in printer port can consult interface signals of standard Centronic printer.
CH341 supplies standard USB printer port, conforms to USB specification, IEEE-1284 specification
and Windows operation system. There is no need of driver program in Windows 2000, XP and Vista
operation system of computer. (The truth is that Windows takes driver program itself). All driver program
and applied program supported print are compatible and without and amending.
Printer ports in CH341 support two kinds of interface protocol of USB printer. The two kinds of
interface protocol can be defined in external EEPROM configuration chip and be point out through
configuration description sign in USB device: PROT=1 indicates single directional transfer interface while
PROT=2 indicates bi-directional transfer interface. In default, CH341 selects bi-directional transfer interface
because the data transfer speed is higher than single directional transfer interface according to IEEE-1284
specification.
CH341 printer ports support two kinds data transfer speed: the low speed print mode (standard print
mode) and high-speed print mode. In the low speed mode, CH341 needs to detect answer clock ACK# and
busy signal BUSY of printer. The effective width of data select pulse STB# is 1uS. Data transfer speed is
500KB/S in ideal. In the high-speed mode, the effective width of data select pulse STB# is 0.5uS. Data
transfer speed is 800KB/S in ideal.
CH341 changes various criterions parallel interface printer to USB printer.
6. Parameter
6.1. Absolute maximum rating (Stresses above those listed can cause permanent damage to the device.
Exposure to maximum rated conditions can affect device operation and reliability.)
Name
TA
Parameter note
Ambient operating
Min.
VCC=5V
Max. Units
-40 85 °C
The DataSheet of CH341 (the first)
TS
10
VCC=V3=3.3V
temperature
Storage temperature
-40 85 °C
-55 125 °C
VCC Voltage source (VCC connects to power, GND to ground) -0.5 6.5 V
VIO The voltage of input or output pin -0.5 VCC+0.5 V
6.2. Electrical parameter (test conditions: TA=25°C, VCC=5V, excluding pin connection of USB bus)
(If the source voltage is 3.3V, multiply 40% of the current parameter)
Name
VCC
Parameter note
Source voltage
Min. Typical Max. Units
V3 doesn’t connect to VCC 4.5 5 5.3 V
V3 connect to VCC 3.3 3.3 3.6 V
15 30 mA
0.15 0.5 mA
ICC Total source current when working ISLP Total source current when USB suspending 0.05 VIL Input Voltage LOW -0.5 0.7 V
VIH Input Voltage HIGH 2.0 VCC+0.5 V
VOL Output Voltage LOW (draw 4mA current) 0.5 V
VOH Output Voltage HIGH (output 4mA current) VCC-0.5 IUPs SCL and SDA output current HIGH 100 200 500 uA
    (Output 100uA current during chip reset)
IUP Input current with pull-up resistor internal 30 70 160 uA
IDN Input current with pull-down resistor internal -50 -180 uA
VR Restrict voltage when power-up reset 2.6 2.9 V
2.3
V
6.3. Basic time sequence parameter (test conditions: TA=25°C, VCC=5V or VCC=V3=3.3V)
Name Parameter note Min. Typical Max. Units
FCLK Frequency of input clock in XI 11.98 12.00 12.02 MHz
TPR Reset time of power-up 20 40 mS
TRI Effective signal width of external reset input TRD Reset delay time of external reset input
100
nS
30
mS
6.4. Print interface time sequence parameter (test conditions: TA=25°C, VCC=5V or
VCC=V3=3.3V, refer to the accessorial image)
Name
Parameter note
TWPRT STB# low-level width
TSPRT STB# high-level width
Min. Typical Max. Units
Low speed 800 840 10000 nS
High speed 400 420 10000 nS
Low speed 800 nS
High speed 560 nS
TDS Data to STB# Low set-up time 240 nS
TDH Data hold time after STB# high 240 nS
TBZ BUSY low to STB# low 160 nS
TWA ACK# pulse width 100 nS
TAK ACK# high to STB# low 160 nS
The DataSheet of CH341 (the first)
11
7. Application
7.1. Basic connection (consult following picture)
P3 is USB endpoint, USB bus contains a double 5V source wires and a double data signal wires.
Usually, the +5V source wire is red while connects to ground wire is black. D+ signal wire is green, D-
signal wire is white. The source current is up to 500mA supplied by USB bus. Generally, CH341 and other
low-cost USB productions can use 5V source directly. If USB productions supply common power by other
mode, CH341 need to use the common power. If these productions use other common power and USB bus
power at the same time, connects 5V power wire of USB bus to 5V common power of USB productions via
1Ω resistance. And join ground wire of the two power devices.
C13 and C14 are monolithic or high frequency ceramic capacitances. The capacity of C13 varies from
4700pF to 0.02uF, eliminates the coupling of inner power of CH341. The capacity of C14 is 0.1uF,
eliminates the coupling of external power. The crystal X3、capacitance C11 and C12 are composed of clock
oscillating circuit of CH341. Frequency of X3 is 12MHz. C11 and C12 are monolithic or high frequency
with capacity of 15pF~30pF capacitances.
If USB production use USB bus power and parallel connects capacitance C15 between VCC and GND,
the process of power-up is slow and release power is not in time when cut power, so the CH341 reset is not
credible. Over connects a 0.1uF or 0.47uF capacitance C26 between RSTI and VCC to delay reset time is
recommended.
When designing the PCB, pay much attention to some notes: decoupling capacitance C13 and C14 must
keep near to connection pin of CH341; makes sure D+ and D- are parallel and supply ground or covering
copper besides to decrease the disturb from outside signal; the relevant signal leads between XI and XO
must be kept as short as possible. In order to lessen the high frequency clock disturb outside, setting ground
wire on the circle or covering copper to the relative equipments.
LED L1 and limited current resistance R1 are optional components and can be omit. External serial
EEPROM configuration chip U3 is optional equipment, when it is omitted, connects SCL and SDA to select
chip function.
The DataSheet of CH341 (the first)
12
7.2. Convert parallel interface printer (consult the following picture)
In the picture, SDA is connected to SCL, so the CH341 is configured as standard USB printer port, used
to change parallel interface printer to USB printer. The right signal wires in the picture are corresponding to
signal wire of IEEE-1284 specification or standard Centronic printer port.
In practice, advise consulting IEEE-1284 specification in view of resistance match., adding
2kΩ to 5KΩ pull-up resistance to each signal wires and 20Ω to 40Ω resistance to every signal wire of printer
ports then connects to parallel interface printer.
7.3. USB change to TTL asynchronous serial interface (consult the following picture)
SDA and SCL are suspended so the CH341 is configured as asynchronous serial interface. The right
signal wires of following picture is corresponding to common serial signals and MODEM signals. Through
MC1488/MC1489, MAX232/ICL232 or MAX213/ADM213/ SP213 change TTL level to RS232 level then
change to RS232C serial interface.
The right signal wires in the picture can connect RXD, TXD, TEN# and public wires only, other signal
wires are optional when using. They can be suspended when not using them. TEN# must connect to
low-level or ground because when it is low-level CH341 can transfer.
The DataSheet of CH341 (the first)
13
7.4. USB change to 3-wire RS232 serial interface (consult the following picture)
The following picture describes the USB change to RS232 serial interface, and the P6 is needle of DB9.
The 3-wire serial interface is basic and common asynchronous serial interface.
7.5. USB change to RS485 interface (consult the following picture)
Crystal, oscillate capacitance and power decoupling capacitance can refer to basic connection picture.
TEN# is connected to ground directly allowing CH341 transfer data through serial interface. TNOW controls
bus semi-duplex transceiver U5 of RS485.
7.6. Connection MCU serial interface (consult the following picture)
The DataSheet of CH341 (the first)
14
The picture realizes USB communication between MCU and computer through serial interface
MPU/MCU connects to CH341.
The baud rate of serial interface is high or MCU is too busy to receive, then any output pin of MCU can
control TEN# of CH341. When MCU is idle and can receive data set TEN# as low-level. When MCU is
busy or not convenient to receive serial interface data set TEN# as high-level to make CH341 pause to send
next byte, realize controlling speed.
7.7. Serial interface connection (consult the following picture)
RDY# of the second side connects to TEN# of the opposite side. The opposite side can transfer data
until the second is ready. No matter what the serial interface communication speed, the two sides can keep
data synchronous avoid to loss data. If the serial interface communication speed is high or the speed of two
sides do not match or low speed MCU connects to CH341 serial interface, use hardware to control signal to
ensure data synchronous.
