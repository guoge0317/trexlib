# trexlib
## STL Client API lib of cisco trex working on windows platform


## Install:
```
pip install -r requirements.txt
pip install trexlib-0.0.1-py3-none-any.whl
```

## Example:
```
from trexlib.stl.api import *


size = 60
base_pkt = Ether(dst="11:22:33:44:55:66", src="11:22:33:44:55:77") / IP(src="16.0.0.1", dst="48.0.0.1") / UDP(dport=12, sport=1025)
pad = max(0, size - len(base_pkt)) * "x"
s1 = STLProfile([STLStream(isg=1.0, packet=STLPktBuilder(pkt=base_pkt / pad), mode=STLTXCont(pps=10))])
c = STLClient(username="test", server="192.168.1.1", verbose_level="info")
try:
    # connect to server
    c.connect()

    # prepare our ports
    c.reset(ports=[0, 1])

    # add both streams to ports
    c.add_streams(s1, ports=[0, 1])

    # clear the stats before injecting
    c.clear_stats()

    c.start(ports=[0, 1], mult="5mpps", duration=3)

    # block until done
    c.wait_on_traffic(ports=[0, 1])

    # check for any warnings
    if c.get_warnings():
        # handle warnings here
        pass

finally:
    c.disconnect()
```

## cisco trex doc
[https://trex-tgn.cisco.com/trex/doc/cp_stl_docs/api/index.html](https://trex-tgn.cisco.com/trex/doc/cp_stl_docs/api/index.html)
