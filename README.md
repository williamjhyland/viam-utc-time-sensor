# Viam UTC Time Sensor Module
## Description

This project demonstrates the integration of a Viam sensor component with a boards System Clock, enabling the sensor to read the system clock and return current time. When integrated with Viam SDKs this means any system with access to the Viam Server can simply poll this sensor to access the system clock and configure the current time.

## Viam Module

A module is a package with streamlined deployment to a Viam server. Modules can run alongside viam-server as separate processes, communicating with viam-server over UNIX sockets. A Viam Module can deploy and manage components such as a Viam Sensor.

## Viam Sensor

A sensor component sends can send information returned from the “GetReadings” method to the computer controlling the machine. We can customize capture data continuously, or only when specific conditions are met.