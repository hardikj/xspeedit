# XspeedIt

Python package  to pack itesm with variable sizes in minimum packages possible

# Usage

```
>> from xspeedit.packer import Packer
>> packer = Packer(10)
>> packages = packer.sortedPack([9,1,2,4,5])
```

# Tests

If you wish to run the tests simply install nose and run `nosetests`.

Tests can be found here [here] (https://github.com/hardikj/xspeedit/tree/master/tests)

### Things that can be improved

- [ ] Adding another better strategy if required after benchmarking while keeping the backward compatibility  
- [ ] Adding more benchmark tests 
- [ ] Adding a CHANGELOG
- [ ] Continous Integration setup using jenkings for eg 
- [ ] Adding another class for Box if the box size need to be defined using more parameters like (height and width)
- [ ] Adding coverage 

