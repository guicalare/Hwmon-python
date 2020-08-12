# Hwmon's Documentation

![](https://github.com/Guillermo-C-A/Hwmon-python/blob/master/HWmon2.png)

**Authors:**

| Bla | Son-link | Guillermo-C-A |
| :-----------: | :-----------: | :-----------: |
| [![Bla6](https://avatars0.githubusercontent.com/u/15669452?s=200&u=a1b376c4739aee41847b6bb689e60ddc3035d400&v)](https://github.com/bla6-apm)| [![son-link](https://avatars0.githubusercontent.com/u/208409?s=200&u=6682adb4923ec4da56ff95515cb4cb1ac4cf55fa&v)](https://github.com/son-link)|[![Guillermo-C-A](https://avatars2.githubusercontent.com/u/50501108?s=200&u=1d529b0189d724caafb94e29d11798e689c43751&v=4)](https://github.com/Guillermo-C-A)|
| Backend and distribution | GUI frontend | Backend |

# Install Hwmon

```
pip install hwmon
```

# Help us

We are open to new ideas and people who want to improve this project, so feel free to open pull requests or leave us your opinions/problems with the application in [this section](https://github.com/Guillermo-C-A/Hwmon-python/issues).

# Disclaimer

The information presented in this library may vary depending on the distribution or kernel being executed, to the point of giving error in certain functions such as GPU. 

In case this happens, inform us of the error so that we can fix the fault :)

Tested and stable kernels:

- 5.8 (Ubuntu 20)
- 5.4.0.42.46 (Ubuntu 20)

It has also been tested on three different computers with AMD CPU and GPU configurations successfully and stably

# New features 

We are currently working in parallel to develop the interfaces for this library. You can download the terminal interface [this link](https://github.com/Guillermo-C-A/Hwmon-python/tree/script)

In addition, the desktop GUI is in the process of being created.

![](https://github.com/Guillermo-C-A/Hwmon-python/blob/master/rd_data/hwmon-qt_2.png)

## Motivations to create Hwmon 

Hwmon has been created with the intention of replacing Linux libraries and APIs which obtain system information without the need to depend on dependencies outside a standard Linux system.

The only requirements for running Hwmon on a system are: 

- The OS is Linux 
- Have python 3
- Install hwmon library

Hwmon is also a library developed expressly by and for Python 3 with functions that are easy to understand and operate, which read and synthesize in the same library all the useful information for monitoring a Linux system that can be found in the /sys, /proc and /dev folders. So only the information that the system itself has recorded will be obtained. 

## Why use Hwmon instead of other library? 

As already mentioned, Hwmon does not require any dependencies or programs and is a library created with the standard Python 3 libraries. Which is not the case like other library/software such as: 

- Pysensors
- lm-sensors
- psutil

Where you need files and other softwares to be able to work, so if you're missing some of that, it just doesn't work. They are also heavier solutions in terms of file sizes than Hwmon. 

## Is it really a viable alternative to lm-sensors? 

Yes. Hwmon is able to return and print the same information that is obtained when installing and running sensors. 

![](https://github.com/Guillermo-C-A/Hwmon-python/blob/master/rd_data/hwmon-vs-sensors.png)

And it even prints the information on the screen in a nice and friendly way so that it is more useful and easy to understand. 

## What information can I get from Hwmon and where does he get it from? 

Hwmon is able to extract: 

- Information from the sensors available on the computer 
- Processor information 
- System memory information 
- Sent and received packet information 
- USB devices connected to the computer 
- Disks connected to the computer 
- BIOS information
- GPU information

All this information is extracted respectively from the following sites: 

- **Sensors:** /sys/class/hwmon
- **CPU:** /proc/cpuinfo and /proc/stat
- **RAM:** /proc/meminfo
- **Network:** /proc/net/dev
- **USB:** /dev/input/by-id
- **Disks:** /dev/disk/by-id
- **GPU**: /sys/class/graphics or /sys/class/drm/card0/device/
- **BIOS:** /sys/class/dmi/id/

## How to use and call the library? 


```python
from hwmon import Hwmon
```

# Sensor information 
To access the sensor subclass, the following statement will be executed: 


```python
sensors = Hwmon.HW()
```

Being the functions that interest us in this case: data() and print_data() . Let's see an example of each function: 
### Print sensors 
This function will print all the sensor information of the system in a tabular and nice way. 


```python
sensors.print_data()
```

     amdgpu
    	 vddgfx 0.862 v
    	 power1 35.04 w
    	 fan1 1119 RPM
    	 edge 33.0 C
     nct6779
    	 AUXTIN3 -28.0 C
    	 in3 3.344 v
    	 fan3 0 RPM
    	 in7 3.472 v
    	 AUXTIN0 -2.5 C
    	 in12 1.68 v
    	 in0 0.568 v
    	 PCH_CPU_TEMP 0.0 C
    	 SMBUSMASTER 0 32.5 C
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
    	 Tdie 32.625 C
    	 Tctl 32.625 C


### Get data
In case we are interested in getting the information from the sensors instead of printing it on the screen, we will execute the following sentence: 


```python
sensors.data()
```




    {'amdgpu': {'vddgfx': '0.862 v',
      'power1': '34.169 w',
      'fan1': '1120 RPM',
      'edge': '33.0 C'},
     'nct6779': {'AUXTIN3': '-28.0 C',
      'in3': '3.344 v',
      'fan3': '0 RPM',
      'in7': '3.472 v',
      'AUXTIN0': '-2.5 C',
      'in12': '1.68 v',
      'in0': '0.568 v',
      'PCH_CPU_TEMP': '0.0 C',
      'SMBUSMASTER 0': '32.5 C',
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
     'k10temp': {'Tdie': '32.625 C', 'Tctl': '32.625 C'}}



# Processor information
To access the processor subclass, the following sentence will be executed 


```python
cpu = Hwmon.CPU()
```

Being the functions that interest us in this case: data() and print_data(). Let's see an example of each function:
### Print information
This function will print all the information of the system processor in a tabular and nice way. 


```python
cpu.print_data()
```

    Name AMD Ryzen 5 1400 Quad-Core Processor
    CPU_usage 26.71
    cores 4
    threads 8
    cpu MHz
            0 1374.813
            1 1374.788
            2 1374.887
            3 1374.75
            4 1510.204
            5 1501.796
            6 3475.097
            7 2196.461
    Max MHz 3800
    Average_MHz 1772.85


### Get data
In case we are interested in obtaining the information from the processor instead of printing it on the screen, we will execute the following sentence: 


```python
cpu.data()
```

    {'Name': 'AMD Ryzen 5 1400 Quad-Core Processor',
     'CPU_usage': -34.37,
     'cores': '4',
     'threads': '8',
     'cpu MHz': {0: 1374.906,
        1: 1374.774, 
        2: 1374.735, 
        3: 1374.718, 
        4: 1374.724, 
        5: 1374.91, 
        6: 1374.804, 
        7: 1374.706},
     'Max MHz': 3800, 
     'Average_MHz': 1374.78}



# Memory information
To access the system memory subclass, the following sentence will be executed: 


```python
memory = Hwmon.MEM()
```

Being the functions that interest us in this case: data() and print_data() . Let's see an example of each function: 
### Print information
This function will print in a tabular and nice way all the information in the system memory. 


```python
memory.print_data()
```

     MemTotal 7.768MB
     MemFree 2.569MB
     MemAvailable 4.349MB
     Buffers 156.973KB
     Cached 1.850MB
     SwapCached 0B
     Active 3.608MB
     Inactive 1.012MB
     Active(anon) 2.576MB
     Inactive(anon) 116.551KB
     Active(file) 1.032MB
     Inactive(file) 919.520KB
     Unevictable 32.0B
     Mlocked 32.0B
     SwapTotal 2.000MB
     SwapFree 2.000MB
     Dirty 960.0B
     Writeback 0B
     AnonPages 2.617MB
     Mapped 683.496KB
     Shmem 118.547KB
     KReclaimable 122.035KB
     Slab 270.754KB
     SReclaimable 122.035KB
     SUnreclaim 148.719KB
     KernelStack 24.109KB
     PageTables 70.258KB
     NFS_Unstable 0B
     Bounce 0B
     WritebackTmp 0B
     CommitLimit 5.884MB
     Committed_AS 11.335MB
     VmallocTotal 32.000GB
     VmallocUsed 40.414KB
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


### Get data
In case we are interested in obtaining the information from memory instead of printing it out on the screen, we will execute the following sentence: 


```python
memory.data()
```




    {'MemTotal': '7.768MB',
     'MemFree': '2.569MB',
     'MemAvailable': '4.349MB',
     'Buffers': '156.980KB',
     'Cached': '1.850MB',
     'SwapCached': '0B',
     'Active': '3.608MB',
     'Inactive': '1.012MB',
     'Active(anon)': '2.576MB',
     'Inactive(anon)': '116.551KB',
     'Active(file)': '1.032MB',
     'Inactive(file)': '919.520KB',
     'Unevictable': '32.0B',
     'Mlocked': '32.0B',
     'SwapTotal': '2.000MB',
     'SwapFree': '2.000MB',
     'Dirty': '964.0B',
     'Writeback': '0B',
     'AnonPages': '2.616MB',
     'Mapped': '683.496KB',
     'Shmem': '118.547KB',
     'KReclaimable': '122.035KB',
     'Slab': '270.754KB',
     'SReclaimable': '122.035KB',
     'SUnreclaim': '148.719KB',
     'KernelStack': '24.109KB',
     'PageTables': '70.258KB',
     'NFS_Unstable': '0B',
     'Bounce': '0B',
     'WritebackTmp': '0B',
     'CommitLimit': '5.884MB',
     'Committed_AS': '11.335MB',
     'VmallocTotal': '32.000GB',
     'VmallocUsed': '40.414KB',
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



# Network information
To access the network subclass, the following sentence will be executed: 


```python
net = Hwmon.NET()
```

Being the functions that interest us in this case: data() and print_data() . Let's see an example of each function: 
### Print information
This function will print in a tabular and nice way all the information of the system network. 


```python
net.print_data()
```

         lo
    	 receive
    		 bytes 7593337
    		 packets 14478
    		 errs 0
    		 drop 0
    		 fifo 0
    		 frame 0
    		 compressed 0
    		 multicast 0
    	 transmit
    		 bytes 14478
    		 packets 0
    		 errs 0
    		 drop 0
    		 fifo 0
    		 colls 0
    		 carrier 0
     enp37s0
    	 receive
    		 bytes 1279460566
    		 packets 864808
    		 errs 0
    		 drop 0
    		 fifo 0
    		 frame 0
    		 compressed 0
    		 multicast 507
    	 transmit
    		 bytes 362337
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


### Get data
In case we are interested in getting the information from the network instead of printing it on the screen, we will execute the following sentence: 


```python
net.data()
```
    {'    lo': {'receive': {'bytes': 7605359,
       'packets': 14503,
       'errs': 0,
       'drop': 0,
       'fifo': 0,
       'frame': 0,
       'compressed': 0,
       'multicast': 0},
      'transmit': {'bytes': 14503,
       'packets': 0,
       'errs': 0,
       'drop': 0,
       'fifo': 0,
       'colls': 0,
       'carrier': 0}},
     'enp37s0': {'receive': {'bytes': 1279460566,
       'packets': 864808,
       'errs': 0,
       'drop': 0,
       'fifo': 0,
       'frame': 0,
       'compressed': 0,
       'multicast': 507},
      'transmit': {'bytes': 362337,
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



# USB devices information
To access the USB subclass, the following sentence will be executed: 


```python
usb = Hwmon.USB()
```

Being the functions that interest us in this case: data() and print_data() . Let's see an example of each function: 
### Print information
This function will print in a tabular and nice way all the information of the USBs in the system. 


```python
usb.print_data()
```

    usb-Logitech_Gaming_Mouse_G300-mouse
    usb-CHICONY_USB_Keyboard
    usb-Logitech_Gaming_Mouse_G300
    usb-Logitech_Gaming_Mouse_G300-if01


### Get data
In case we are interested in getting the information from the sensors instead of printing it on the screen, we will execute the following sentence: 


```python
usb.data()
```
    ['usb-Logitech_Gaming_Mouse_G300-mouse',
     'usb-CHICONY_USB_Keyboard',
     'usb-Logitech_Gaming_Mouse_G300',
     'usb-Logitech_Gaming_Mouse_G300-if01']



# Disks information
To access the subclass of the disks, the following sentence will be executed: 


```python
disk = Hwmon.DISK()
```

Being the functions that interest us in this case: data() and print_data() . Let's see an example of each function: 
### Print information
This function will print in a tabular and nice way all the information of the disks in the system. 


```python
disk.print_data()
```

    wwn-0x50014ee202380e97
    ata-WDC_WD3200BEVT-22ZCT0_WD-WXEY08F45384
    wwn-0x500080dc007530e0
    ata-TOSHIBA-TL100_27NB51GCKSZU
    wwn-0x50014ee20b769657
    ata-WDC_WD20EZRX-22D8PB0_WD-WCC4M1ZJ83JD


### Get data
In case we are interested in getting the information from the sensors instead of printing it on the screen, we will execute the following sentence: 


```python
disk.data()
```

    ['wwn-0x500080dc007530e0',
     'ata-WDC_WD3200BEVT-22ZCT0_WD-WXEY08F45384',
     'ata-TOSHIBA-TL100_27NB51GCKSZU',
     'wwn-0x50014ee202380e97',
     'wwn-0x50014ee20b769657',
     'ata-WDC_WD20EZRX-22D8PB0_WD-WCC4M1ZJ83JD']

# GPU information 
To access the GPU subclass, the following statement will be executed: 


```python
gpu = Hwmon.GPU()
```

Being the functions that interest us in this case: data() and print_data() . Let's see an example of each function: 
### Print information
This function will print all the information of the GPU in a tabular and nice way. 


```python
gpu.print_data()
```
    amdgpudrmfb
         Resolution 1680x1050p
         gpu_busy_percent 0 %
         mem_info_vram_used 361.31MB
         current_link_width 16
         mem_info_vis_vram_used 46.77MB
         mem_info_vis_vram_total 256.00MB
         current_link_speed 8 GT/s
         mem_busy_percent 19 %
         mem_info_gtt_used 52.29MB
         mem_info_vram_total 8.00GB
         vbios_version 113-C9403100_101
         mem_info_gtt_total 5.83GB

### Get data
In case we are interested in getting the information from the gpu instead of printing it on the screen, we will execute the following sentence: 

```python
gpu.data()
```
    {'amdgpudrmfb':
    {'Resolution': '1680x1050p',
    'gpu_busy_percent': '0 %',
    'mem_info_vram_used': '367.23MB',
    'current_link_width': '16',
    'mem_info_vis_vram_used': '46.77MB',
    'mem_info_vis_vram_total': '256.00MB',
    'current_link_speed': '8 GT/s',
    'mem_busy_percent': '19 %',
    'mem_info_gtt_used': '56.88MB',
    'mem_info_vram_total': '8.00GB',
    'vbios_version': '113-C9403100_101',
    'mem_info_gtt_total': '5.83GB'}}

# BIOS information 
To access the BIOS subclass, the following statement will be executed: 


```python
bios = Hwmon.BIOS()
```

Being the functions that interest us in this case: data() and print_data() . Let's see an example of each function: 
### Print information
This function will print all the information of the GPU in a tabular and nice way. 


```python
bios.print_data()
```
    bios_date 12/20/2018
    bios_version P5.50
    board_vendor ASRock
    chassis_type 3
    bios_vendor American Megatrends Inc.
    board_asset_tag 
    board_version 
    board_name AB350M-HDV


### Get data
In case we are interested in getting the information from the gpu instead of printing it on the screen, we will execute the following sentence: 

```python
bios.data()
```
    {'bios_date': '12/20/2018',
    'bios_version': 'P5.50',
    'board_vendor': 'ASRock',
    'chassis_type': '3',
    'bios_vendor': 'American Megatrends Inc.',
    'board_asset_tag': '',
    'board_version': '',
    'board_name': 'AB350M-HDV'}

