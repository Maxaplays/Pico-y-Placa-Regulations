from datetime import datetime, time

inicioAM = time(7,0,0)
finAM = time(9,30,0)
inicioPM = time(16,0,0)
finPM = time(19,30,0)

def isValidPlaca(placa):
    if(len(placa)==7 or len(placa)==8):
        return True
    return False

def canDriveEvenDay(placa, hora):
    return int(placa[-1]) % 2 != 0 and (inicioAM<=hora<=finAM or inicioPM<=hora<=finPM)

def canDriveOddDay(placa, hora):
    return int(placa[-1]) % 2 == 0 and (inicioAM<=hora<=finAM or inicioPM<=hora<=finPM)


def picoyplaca(plate, date, time):
    '''
    Returns whether you can drive or not.

    Parameters:

    -Plate: Full license plate as a string (eg: PKG-2659)
    
    -Date: Date as a string formatted as %d/%m/%Y (eg: 17/11/2020)

    -Time: Hour as a string formattted as %H:%M (eg: 17:00)
    '''
    if not isValidPlaca(plate):
        raise Exception("Placa invalida")
    
    fechahora = datetime.strptime(f'{date} {time}', "%d/%m/%Y %H:%M")

    dia = fechahora.weekday()
    time = fechahora.time()

    if(dia == 6): # Sunday
        return False
    if(dia % 2 == 0 and canDriveEvenDay(plate,time)):
        return False
    if(dia % 2 != 0 and canDriveOddDay(plate,time)):
        return False
    return True


