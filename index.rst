.. plant keeper documentation master file, created by
   sphinx-quickstart on Thu Apr 23 22:18:53 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to One-Green official documentation!
============================================

This project provides a complete framework for plant cultivation both indoors and outdoors.

About this framework
--------------------

The framework is including:

- **Core**:

   - **IoT nodes controller**:
      built on top of Django and TimeScaleDB to persist user configuration

   - **API**:
      Django based REST Api to connect any other GUI

   - **Admin UI**:
      Graphical interface built on top Python Streamlit to configure **IoT nodes**

   - **MQTT**:
      Message broker

   - **InfluxDB + Telegraf**:
      Capture data from IoT devices and **IoT nodes controller** used by **Grafana** to build nice dashboard

   - **Grafana**:
      Data visualization, alert management: you can connect Slack, Telegram (and lot of others) for push notification


- **Iot nodes firmwares**

   - **Water Tank**:
      Self nutrient, pH level, level controlled device

   - **Sprinkler**:
      endpoint for water filling, can be used  with **Water Tank** or tap, for outdoor usage, this one can provide GPS position
      endpoint for water filling, can be used  with **Water Tank** or tap, for outdoor usage, this one can provide GPS position

   - **Deep water culture**:
      WIP

   - **UV Light**:
      WIP

   - **HVAC**:
      WIP


.. note::

   **Core** is considered the center of decision

   **IoT Node** will follow POWER OFF / POWER ON ordered by **Core**


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart/index
   iot_nodes/index
   flash/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

