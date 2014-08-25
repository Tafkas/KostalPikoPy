# PikoPy
This package is for working with a Piko Inverter from [Kostal](http://www.kostal-solar-electric.com/)

## Where has it been tested?
PikoPy has been tested with a Kostal Piko 5.5. It should work with other Kostal inverters as well since they provide the same interface.

## Requirements
 * Python
 * lxml
 * httplib2
 * httpretty (for testing)
 
## Installing
```bash
$ pip install pikopy
```

## Usage
    import pikopy
    
    #create a new piko instance
    p = Piko('host', 'username', 'password')
    
    #get current power 
    print p.get_current_power()
    
    #get voltage from string 1
    print p.get_string1_voltage()

