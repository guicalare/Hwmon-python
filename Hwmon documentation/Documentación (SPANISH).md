# Documentación de Hwmon

**Autores:** bla6 y Guillermo-C-A

**Repositorio:** 

## Motivaciones para crear Hwmon

Hwmon se ha creado con la intención de reemplazar librerías y APIs de Linux con las cuales obtener información del sistema sin necesidad de depender de dependencias ajenas a un sistema Linux estándar, es decir, que no se necesite instalar nada.

Los únicos requisitos para ejecutar Hwmon en un sistema son:

- El SO sea Linux
- Disponer de python 3

Hwmon es además un librería desarrollada expresamente por y para Python 3 con funciones sencillas de entender y de funcionar, las cuales leen y sintetizan en una misma librería toda la información útil para monitorizar un sistema Linux que se encuentran en las carpetas /sys, /proc y /dev. Por lo que solo se obtendrá la información que el propio sistema tenga registrada.

## ¿Por que usar Hwmon en vez de otras librerías?

Como ya se ha mencionado, Hwmon no requiere de dependencias ni programas y es una librería creada con las librerías estándares de Python 3. Cosa que no ocurre con otras librerías como son:

- Pysensors
- lm-sensors
- psutil

Donde se necesitan de archivos y programas para poder funcionar, de forma que si te falta algo de eso, simplemente no funciona. Además de son soluciones mas pesadas en cuanto a tamaños de archivos que Hwmon.

## ¿Es realmente una alternativa viable a lm-sensors?

Sí. Hwmon es capaz de retornar e imprimir la misma información que se obtiene al instalar y ejecutar sensors. 

![https://github.com/Guillermo-C-A/Hwmon-python/blob/master/rd_data/hwmon%20vs%20lm-sensors.png](attachment:imagen.png)

E incluso imprime por pantalla la información de una forma bonita y amigable de forma que sea mas útil y fácil de entender.

## ¿Que información puedo obtener con Hwmon y de donde la obtiene?

Hwmon es capaz de extraer:

- Información de los sensores disponibles en el ordenador
- Información del procesador
- Información de la memoria del sistema
- Información de los paquetes enviados y recibidos
- Dispositivos USB conectados al ordenador
- Discos conectados al ordenador

Toda esa información se extrae respectivamente de los siguientes sitios:

- /sys/class/hwmon
- /proc/cpuinfo y /proc/stat
- /proc/meminfo
- /proc/net/dev
- /dev/input/by-id
- /dev/disk/by-id

## ¿Como usar y llamar a la librería?


```python
from hwmon import HWmon
```

# Información de los sensores

Para acceder a la subclase de los sensores, se ejecutara la siguiente sentencia:



```python
sensors = Hwmon.HW()
```

Siendo las funciones que nos interesan en este caso: data() y print_data() . Veamos un ejemplo de cada función:

### Imprimir sensores

Esta función imprimirá de forma tabulada y bonita toda la información de los sensores del sistema.


```python
sensors.print_data()
```

     amdgpu
    	 vddgfx 0.862 v
    	 power1 35.026 w
    	 fan1 1119 RPM
    	 edge 32.0 C
     nct6779
    	 AUXTIN3 -28.0 C
    	 in3 3.344 v
    	 fan3 0 RPM
    	 in7 3.472 v
    	 AUXTIN0 -2.5 C
    	 in12 1.68 v
    	 in0 0.6 v
    	 PCH_CPU_TEMP 0.0 C
    	 SMBUSMASTER 0 35.0 C
    	 in4 1.84 v
    	 fan4 0 RPM
    	 in8 3.264 v
    	 AUXTIN1 85.0 C
    	 in13 0.944 v
    	 in1 0.0 v
    	 fan1 0 RPM
    	 PCH_CHIP_CPU_MAX_TEMP 0.0 C
    	 in5 0.84 v
    	 SYSTIN 31.0 C
    	 in10 0.352 v
    	 fan5 0 RPM
    	 in9 0.0 v
    	 AUXTIN2 23.0 C
    	 in14 1.848 v
    	 in2 3.344 v
    	 fan2 1945 RPM
    	 PCH_CHIP_TEMP 0.0 C
    	 in6 1.536 v
    	 CPUTIN 33.0 C
    	 in11 1.056 v
     k10temp
    	 Tdie 35.0 C
    	 Tctl 35.0 C


### Obtener datos

En el caso de que nos interese obtener la información de los sensores en vez de imprimirlos por pantalla, ejecutaremos la siguiente sentencia:


```python
sensors.data()
```




    {'amdgpu': {'vddgfx': '0.837 v',
      'power1': '34.004 w',
      'fan1': '1118 RPM',
      'edge': '32.0 C'},
     'nct6779': {'AUXTIN3': '-28.0 C',
      'in3': '3.344 v',
      'fan3': '0 RPM',
      'in7': '3.472 v',
      'AUXTIN0': '-2.5 C',
      'in12': '1.68 v',
      'in0': '0.6 v',
      'PCH_CPU_TEMP': '0.0 C',
      'SMBUSMASTER 0': '35.0 C',
      'in4': '1.84 v',
      'fan4': '0 RPM',
      'in8': '3.264 v',
      'AUXTIN1': '85.0 C',
      'in13': '0.944 v',
      'in1': '0.0 v',
      'fan1': '0 RPM',
      'PCH_CHIP_CPU_MAX_TEMP': '0.0 C',
      'in5': '0.84 v',
      'SYSTIN': '31.0 C',
      'in10': '0.352 v',
      'fan5': '0 RPM',
      'in9': '0.0 v',
      'AUXTIN2': '23.0 C',
      'in14': '1.848 v',
      'in2': '3.344 v',
      'fan2': '1945 RPM',
      'PCH_CHIP_TEMP': '0.0 C',
      'in6': '1.536 v',
      'CPUTIN': '33.0 C',
      'in11': '1.056 v'},
     'k10temp': {'Tdie': '34.875 C', 'Tctl': '34.875 C'}}



# Información del procesador

Para acceder a la subclase del procesador, se ejecutara la siguiente sentencia:


```python
cpu = Hwmon.CPU()
```

Siendo las funciones que nos interesan en este caso: data() y print_data() . Veamos un ejemplo de cada función:

### Imprimir información

Esta función imprimirá de forma tabulada y bonita toda la información del procesador del sistema.


```python
cpu.print_data()
```

     Name AMD Ryzen 5 1400 Quad-Core Processor
     CPU_usage 14.3
     cores 4
     threads 8
     Average_MHz 1387.48


### Obtener datos

En el caso de que nos interese obtener la información del procesador en vez de imprimirlos por pantalla, ejecutaremos la siguiente sentencia:


```python
cpu.data()
```




    {'Name': 'AMD Ryzen 5 1400 Quad-Core Processor',
     'CPU_usage': 14.3,
     'cores': '4',
     'threads': '8',
     'Average_MHz': 2061.04}



# Información de la memoria

Para acceder a la subclase de la memoria del sistema, se ejecutara la siguiente sentencia:


```python
memory = Hwmon.MEM()
```

Siendo las funciones que nos interesan en este caso: data() y print_data() . Veamos un ejemplo de cada función:

### Imprimir información

Esta función imprimirá de forma tabulada y bonita toda la información de la memoria del sistema.


```python
memory.print_data()
```

     MemTotal 7.768MB
     MemFree 2.523MB
     MemAvailable 4.303MB
     Buffers 156.773KB
     Cached 1.866MB
     SwapCached 0B
     Active 3.638MB
     Inactive 1.028MB
     Active(anon) 2.606MB
     Inactive(anon) 132.734KB
     Active(file) 1.032MB
     Inactive(file) 919.504KB
     Unevictable 32.0B
     Mlocked 32.0B
     SwapTotal 2.000MB
     SwapFree 2.000MB
     Dirty 11.285KB
     Writeback 0B
     AnonPages 2.647MB
     Mapped 699.680KB
     Shmem 134.730KB
     KReclaimable 121.957KB
     Slab 270.539KB
     SReclaimable 121.957KB
     SUnreclaim 148.582KB
     KernelStack 24.062KB
     PageTables 70.359KB
     NFS_Unstable 0B
     Bounce 0B
     WritebackTmp 0B
     CommitLimit 5.884MB
     Committed_AS 11.376MB
     VmallocTotal 32.000GB
     VmallocUsed 40.430KB
     VmallocChunk 0B
     Percpu 14.250KB
     HardwareCorrupted 0B
     AnonHugePages 0B
     ShmemHugePages 0B
     ShmemPmdMapped 0B
     CmaTotal 0B
     CmaFree 0B
     HugePages_Total 0B
     HugePages_Free 0B
     HugePages_Rsvd 0B
     HugePages_Surp 0B
     Hugepagesize 2.000KB
     Hugetlb 0B
     DirectMap4k 447.266KB
     DirectMap2M 6.498MB
     DirectMap1G 2.000MB


### Obtener datos

En el caso de que nos interese obtener la información de la memoria en vez de imprimirlos por pantalla, ejecutaremos la siguiente sentencia:


```python
memory.data()
```




    {'MemTotal': '7.768MB',
     'MemFree': '2.523MB',
     'MemAvailable': '4.303MB',
     'Buffers': '156.781KB',
     'Cached': '1.866MB',
     'SwapCached': '0B',
     'Active': '3.638MB',
     'Inactive': '1.028MB',
     'Active(anon)': '2.606MB',
     'Inactive(anon)': '132.734KB',
     'Active(file)': '1.032MB',
     'Inactive(file)': '919.520KB',
     'Unevictable': '32.0B',
     'Mlocked': '32.0B',
     'SwapTotal': '2.000MB',
     'SwapFree': '2.000MB',
     'Dirty': '11.285KB',
     'Writeback': '0B',
     'AnonPages': '2.647MB',
     'Mapped': '699.680KB',
     'Shmem': '134.730KB',
     'KReclaimable': '121.957KB',
     'Slab': '270.539KB',
     'SReclaimable': '121.957KB',
     'SUnreclaim': '148.582KB',
     'KernelStack': '24.062KB',
     'PageTables': '70.355KB',
     'NFS_Unstable': '0B',
     'Bounce': '0B',
     'WritebackTmp': '0B',
     'CommitLimit': '5.884MB',
     'Committed_AS': '11.376MB',
     'VmallocTotal': '32.000GB',
     'VmallocUsed': '40.430KB',
     'VmallocChunk': '0B',
     'Percpu': '14.250KB',
     'HardwareCorrupted': '0B',
     'AnonHugePages': '0B',
     'ShmemHugePages': '0B',
     'ShmemPmdMapped': '0B',
     'CmaTotal': '0B',
     'CmaFree': '0B',
     'HugePages_Total': '0B',
     'HugePages_Free': '0B',
     'HugePages_Rsvd': '0B',
     'HugePages_Surp': '0B',
     'Hugepagesize': '2.000KB',
     'Hugetlb': '0B',
     'DirectMap4k': '447.266KB',
     'DirectMap2M': '6.498MB',
     'DirectMap1G': '2.000MB'}



# Información de la red

Para acceder a la subclase de la red, se ejecutara la siguiente sentencia:


```python
net = Hwmon.NET()
```

Siendo las funciones que nos interesan en este caso: data() y print_data() . Veamos un ejemplo de cada función:

### Imprimir información

Esta función imprimirá de forma tabulada y bonita toda la información de la red del sistema.


```python
net.print_data()
```

         lo
    	 receive
    		 bytes 7334996
    		 packets 13743
    		 errs 0
    		 drop 0
    		 fifo 0
    		 frame 0
    		 compressed 0
    		 multicast 0
    	 transmit
    		 bytes 13743
    		 packets 0
    		 errs 0
    		 drop 0
    		 fifo 0
    		 colls 0
    		 carrier 0
     enp37s0
    	 receive
    		 bytes 1279458977
    		 packets 864793
    		 errs 0
    		 drop 0
    		 fifo 0
    		 frame 0
    		 compressed 0
    		 multicast 506
    	 transmit
    		 bytes 362330
    		 packets 0
    		 errs 0
    		 drop 0
    		 fifo 0
    		 colls 0
    		 carrier 0
     docker0
    	 receive
    		 bytes 0
    		 packets 0
    		 errs 0
    		 drop 0
    		 fifo 0
    		 frame 0
    		 compressed 0
    		 multicast 0
    	 transmit
    		 bytes 0
    		 packets 0
    		 errs 0
    		 drop 0
    		 fifo 0
    		 colls 0
    		 carrier 0


### Obtener datos

En el caso de que nos interese obtener la información de la red en vez de imprimirlos por pantalla, ejecutaremos la siguiente sentencia:


```python
net.data()
```




    {'    lo': {'receive': {'bytes': 7346602,
       'packets': 13760,
       'errs': 0,
       'drop': 0,
       'fifo': 0,
       'frame': 0,
       'compressed': 0,
       'multicast': 0},
      'transmit': {'bytes': 13760,
       'packets': 0,
       'errs': 0,
       'drop': 0,
       'fifo': 0,
       'colls': 0,
       'carrier': 0}},
     'enp37s0': {'receive': {'bytes': 1279458977,
       'packets': 864793,
       'errs': 0,
       'drop': 0,
       'fifo': 0,
       'frame': 0,
       'compressed': 0,
       'multicast': 506},
      'transmit': {'bytes': 362330,
       'packets': 0,
       'errs': 0,
       'drop': 0,
       'fifo': 0,
       'colls': 0,
       'carrier': 0}},
     'docker0': {'receive': {'bytes': 0,
       'packets': 0,
       'errs': 0,
       'drop': 0,
       'fifo': 0,
       'frame': 0,
       'compressed': 0,
       'multicast': 0},
      'transmit': {'bytes': 0,
       'packets': 0,
       'errs': 0,
       'drop': 0,
       'fifo': 0,
       'colls': 0,
       'carrier': 0}}}



# Información de los USBs

Para acceder a la subclase de los USB, se ejecutara la siguiente sentencia:


```python
usb = Hwmon.USB()
```

Siendo las funciones que nos interesan en este caso: data() y print_data() . Veamos un ejemplo de cada función:

### Imprimir información

Esta función imprimirá de forma tabulada y bonita toda la información de los USBs del sistema.


```python
usb.print_data()
```

    usb-CHICONY_USB_Keyboard
    usb-Logitech_Gaming_Mouse_G300-if01
    usb-Logitech_Gaming_Mouse_G300
    usb-Logitech_Gaming_Mouse_G300-mouse


### Obtener datos

En el caso de que nos interese obtener la información de los sensores en vez de imprimirlos por pantalla, ejecutaremos la siguiente sentencia:


```python
usb.data()
```




    ['usb-CHICONY_USB_Keyboard',
     'usb-Logitech_Gaming_Mouse_G300-if01',
     'usb-Logitech_Gaming_Mouse_G300',
     'usb-Logitech_Gaming_Mouse_G300-mouse']



# Información de los discos

Para acceder a la subclase de los discos, se ejecutara la siguiente sentencia:


```python
disk = Hwmon.DISK()
```

Siendo las funciones que nos interesan en este caso: data() y print_data() . Veamos un ejemplo de cada función:

### Imprimir información

Esta función imprimirá de forma tabulada y bonita toda la información de los discos del sistema.


```python
disk.print_data()
```

    wwn-0x500080dc007530e0
    ata-WDC_WD3200BEVT-22ZCT0_WD-WXEY08F45384
    ata-TOSHIBA-TL100_27NB51GCKSZU
    wwn-0x50014ee202380e97
    wwn-0x50014ee20b769657
    ata-WDC_WD20EZRX-22D8PB0_WD-WCC4M1ZJ83JD


### Obtener datos

En el caso de que nos interese obtener la información de los sensores en vez de imprimirlos por pantalla, ejecutaremos la siguiente sentencia:


```python
disk.data()
```




    ['wwn-0x500080dc007530e0',
     'ata-WDC_WD3200BEVT-22ZCT0_WD-WXEY08F45384',
     'ata-TOSHIBA-TL100_27NB51GCKSZU',
     'wwn-0x50014ee202380e97',
     'wwn-0x50014ee20b769657',
     'ata-WDC_WD20EZRX-22D8PB0_WD-WCC4M1ZJ83JD']


