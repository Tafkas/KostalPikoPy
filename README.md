# PikoPy
This package is for working with a PIKO Inverter from [KOSTAL](http://www.kostal-solar-electric.com/)

## Where has it been tested?
PikiPy has been tested with a Kostal Piko 5.5. It should work with other Kostal inverters as well since they provide the same interface.

## quirements
 * Python
 * lxml
 * httplib2
 * httpretty (for testing)
 
## Installing
```bash
$ pip install gscholar
```

## Usage
    import piko
    
    #create a new piko instance
    p = Piko('host', 'username', 'password')
    
    #get current power 
    print p.get_current_power()
    
    #get voltage from string 1
    print p.get_string1_voltage()

