*************************
Flash Water Tank firmware
*************************

Requirements
------------

Platform requirements: :ref:`Water Tank`

Software requirements:

  - :ref:`Prepare Arduino IDE`
  - :ref:`Deploy Core on Raspberry Pi (MicroK8s)`

Flash
-----

Download **zip** from last release : https://github.com/One-Green/node-water-nutrient-ph-firmware/releases

Unzip files

.. image:: _static/img_18.png
  :width: 400
  :alt: folder


Connect Mega 2560 USB-UART, open **mega-2560/mega-2560.ino** with Arduino IDE, select appropriated PORT and flash

.. image:: _static/img_19.png
  :width: 400
  :alt: flash mega-2560


Connect ESP32 USB-UART, open **esp32/esp32.ino** with Arduino IDE.
Change: Wifi and Mqtt parameters.

.. image:: _static/img_20.png
  :width: 400
  :alt: esp32 wifi/mqtt parameter

Change Board, PORT and flash

.. image:: _static/img_21.png
  :width: 400
  :alt: flash esp32
