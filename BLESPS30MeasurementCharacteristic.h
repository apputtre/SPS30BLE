#ifndef BLESPS30MEASUREMENTCHARACTERISTIC_H
#define BLESPS30MEASUREMENTCHARACTERISTIC_H

#include <sps30.h>
#include <ArduinoBLE.h>

class BLESPS30MeasurementCharacteristic : public BLETypedCharacteristic<sps30_measurement>
{
public:
  BLESPS30MeasurementCharacteristic(const char* uuid, unsigned int permissions);
};

#endif BLESPS30MEASUREMENTCHARACTERISTIC_H