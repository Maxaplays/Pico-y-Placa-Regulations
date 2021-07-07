from PicoyPlaca_Mateo_Andrade import picoyplaca

def test_Sunday():
    assert picoyplaca("PCI-2457","11/07/2021","17:00") == False



def test_EvenDays_CirculationHour_OddLicence():
    assert picoyplaca("PCI-2453","13/07/2021","20:00") == True
    assert picoyplaca("PCI-2459","15/07/2021","20:00") == True
    assert picoyplaca("PCI-2451","17/07/2021","20:00") == True
def test_EvenDays_NotCirculationHour_OddLicence():
    assert picoyplaca("PCI-2457","13/07/2021","17:00") == True
    assert picoyplaca("PCI-2459","15/07/2021","17:00") == True
    assert picoyplaca("PCI-2451","17/07/2021","17:00") == True
def test_OddDays_CirculationHour_OddLicence():
    assert picoyplaca("PCI-2453","12/07/2021","02:00") == True
    assert picoyplaca("PCI-2453","14/07/2021","02:00") == True
    assert picoyplaca("PCI-2451","16/07/2021","02:00") == True
def test_OddDays_NotCirculationHour_OddLicence():
    assert picoyplaca("PCI-2457","12/07/2021","08:00") == False
    assert picoyplaca("PCI-2453","14/07/2021","08:00") == False
    assert picoyplaca("PCI-2457","16/07/2021","08:00") == False




def test_EvenDays_CirculationHour_EvenLicence():
    assert picoyplaca("PCI-2458","13/07/2021","20:00") == True
    assert picoyplaca("PCI-2454","15/07/2021","20:00") == True
    assert picoyplaca("PCI-2456","17/07/2021","20:00") == True
def test_EvenDays_NotCirculationHour_EvenLicence():
    assert picoyplaca("PCI-2458","13/07/2021","17:00") == False
    assert picoyplaca("PCI-2452","15/07/2021","17:00") == False
    assert picoyplaca("PCI-2454","17/07/2021","17:00") == False
def test_OddDays_CirculationHour_EvenLicence():
    assert picoyplaca("PCI-2454","12/07/2021","20:00") == True
    assert picoyplaca("PCI-2458","14/07/2021","20:00") == True
    assert picoyplaca("PCI-2456","16/07/2021","20:00") == True
def test_OddDays_NotCirculationHour_EvenLicence():
    assert picoyplaca("PCI-2452","12/07/2021","17:00") == True
    assert picoyplaca("PCI-2454","14/07/2021","17:00") == True
    assert picoyplaca("PCI-2456","16/07/2021","17:00") == True