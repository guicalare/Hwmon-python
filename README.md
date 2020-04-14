# Hwmon-python

With the collaboration of Bla6: [Bla6 Gitlab](https://gitlab.com/bla6)

# Important 

- these scripts do not work in virtual machines 
- the information shown by both hwmon and lm-sensors depends on the sensors available to the orderer and even on the component manufacturers

# What is Hwmon 

**Hwmon** is a collection of Python 3 scripts which are a native Python solution for obtaining information from Linux system sensors. Currently it is still under development and the idea is to group in the same library the same lm-sensors and psutil functions without having to install anything in the system. 

All the information used in this library is the same information handled by both lm-sensors and psutil (or that is what it is intended to do, so there may be some small differences). At the moment the data extracted from the system are: 

- **Sensor information** (from /sys/class/hwmon)
- **Processor information** (from /proc/cpuinfo and /proc/stat) 
- **System memory information** (from /proc/meminfo) 
- **Network information** (from /proc/net/dev)

# Why use this library instead of others? 

Most of the other libraries require ls-sensors to be installed or use C libraries to call data APIs. While with Hwmon you won't have to install anything or fight with other languages/dependencies or APIs, since Hwmon reads directly the system files and the only library it uses is "os" so it doesn't require any previous installation or other languages.

# Does it show the same thing as lm-sensors? 

Hwmon shows the same as lm-sensors but with different names in some cases. This will be solved in future updates of the library. 

Let's see an example of comparisons between lm-sensors and hwmon: 

![](https://github.com/Guillermo-C-A/Hwmon-python/blob/master/rd_data/hwmon%20vs%20lm-sensors.png)

**Note:** to see the information of the previous example, you have to uncomment the line of:
```
#Hwmon(). print_data() 
```

# Available sensors and calls 

## Sensor information: 

As far as execution and data collection are concerned, we have: 

- **Print the information** 

```python
>>> import hwmon
>>> hwmon.Hwmon().print_data()
 amdgpu
	 vddgfx 0.8 v
	 power1 32.226 w
	 fan1 1127 RPM
	 edge 32.0 C
 nct6779
	 AUXTIN3 -28.0 C
	 in3 3.36 v
	 fan3 0 RPM
	 in7 3.472 v
	 AUXTIN0 -1.5 C
	 in12 1.688 v
	 in0 0.416 v
	 PCH_CPU_TEMP 0.0 C
	 SMBUSMASTER 0 30.0 C
	 in4 1.848 v
	 fan4 0 RPM
	 in8 3.264 v
	 AUXTIN1 86.0 C
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
	 in14 1.84 v
	 in2 3.36 v
	 fan2 1917 RPM
	 PCH_CHIP_TEMP 0.0 C
	 in6 1.528 v
	 CPUTIN 32.0 C
	 in11 1.056 v
 k10temp
	 Tdie 30.125 C
	 Tctl 30.125 C
```

- **Extract the information in a dictionary**

```python
>>> import hwmon
>>> hwmon.Hwmon().data()
{'amdgpu': {'vddgfx': '0.75 v', 'power1': '30.036 w', 'fan1': '1125 RPM', 'edge': '30.0 ºC'}, 'nct6779': {'AUXTIN3': '-28.0 ºC', 'in3': '3.36 v', 'fan3': '0 RPM', 'in7': '3.472 v', 'AUXTIN0': '-0.5 ºC', 'in12': '1.688 v', 'in0': '0.368 v', 'PCH_CPU_TEMP': '0.0 ºC', 'SMBUSMASTER 0': '28.5 ºC', 'in4': '1.848 v', 'fan4': '0 RPM', 'in8': '3.264 v', 'AUXTIN1': '86.0 ºC', 'in13': '0.944 v', 'in1': '0.0 v', 'fan1': '0 RPM', 'PCH_CHIP_CPU_MAX_TEMP': '0.0 ºC', 'in5': '0.84 v', 'SYSTIN': '31.0 ºC', 'in10': '0.352 v', 'fan5': '0 RPM', 'in9': '0.0 v', 'AUXTIN2': '23.0 ºC', 'in14': '1.848 v', 'in2': '3.36 v', 'fan2': '1936 RPM', 'PCH_CHIP_TEMP': '0.0 ºC', 'in6': '1.504 v', 'CPUTIN': '31.0 ºC', 'in11': '1.056 v'}, 'k10temp': {'Tdie': '28.75 ºC', 'Tctl': '28.75 ºC'}}

```

## Processor information: 

- **Print the information** 

```python
>>> import cpumon
>>> cpumon.CPUmon().print_data()
 Name AMD Ryzen 5 1400 Quad-Core Processor
 CPU_usage 6.52
 cores 4
 threads 8
 Average_MHz 1411.52
```

- **Extract the information in a dictionary**

```python
>>> import cpumon
>>> cpumon.CPUmon().data()
{'Name': 'AMD Ryzen 5 1400 Quad-Core Processor', 'CPU_usage': 5.8, 'cores': '4', 'threads': '8', 'Average_MHz': 1389.01}
```

## Memory information: 

- **Print the information** 

```python
>>> import memmon
>>> memmon.MEMmon().print_data()
 MemTotal 7.768MB
 MemFree 2.567MB
 MemAvailable 4.162MB
 Buffers 201.270KB
 Cached 1.700MB
 SwapCached 0B
 Active 3.507MB
 Inactive 1.102MB
 Active(anon) 2.711MB
 Inactive(anon) 191.277KB
 Active(file) 815.184KB
 Inactive(file) 936.867KB
 Unevictable 16.0B
 Mlocked 16.0B
 SwapTotal 2.000MB
 SwapFree 2.000MB
 Dirty 80.0B
 Writeback 0B
 AnonPages 2.712MB
 Mapped 638.508KB
 Shmem 193.512KB
 KReclaimable 178.371KB
 Slab 318.594KB
 SReclaimable 178.371KB
 SUnreclaim 140.223KB
 KernelStack 20.688KB
 PageTables 61.000KB
 NFS_Unstable 0B
 Bounce 0B
 WritebackTmp 0B
 CommitLimit 5.884MB
 Committed_AS 10.218MB
 VmallocTotal 32.000GB
 VmallocUsed 35.203KB
 VmallocChunk 0B
 Percpu 12.875KB
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
 DirectMap4k 513.266KB
 DirectMap2M 6.434MB
 DirectMap1G 2.000MB
```

- **Extract the information in a dictionary**

```python
>>> import memmon
>>> memmon.MEMmon().data()
{'MemTotal': '7.768MB', 'MemFree': '2.542MB', 'MemAvailable': '4.138MB', 'Buffers': '201.305KB', 'Cached': '1.701MB', 'SwapCached': '0B', 'Active': '3.531MB', 'Inactive': '1.102MB', 'Active(anon)': '2.735MB', 'Inactive(anon)': '191.277KB', 'Active(file)': '815.223KB', 'Inactive(file)': '936.965KB', 'Unevictable': '16.0B', 'Mlocked': '16.0B', 'SwapTotal': '2.000MB', 'SwapFree': '2.000MB', 'Dirty': '1000.0B', 'Writeback': '0B', 'AnonPages': '2.736MB', 'Mapped': '638.492KB', 'Shmem': '193.508KB', 'KReclaimable': '178.375KB', 'Slab': '318.598KB', 'SReclaimable': '178.375KB', 'SUnreclaim': '140.223KB', 'KernelStack': '20.703KB', 'PageTables': '61.023KB', 'NFS_Unstable': '0B', 'Bounce': '0B', 'WritebackTmp': '0B', 'CommitLimit': '5.884MB', 'Committed_AS': '10.217MB', 'VmallocTotal': '32.000GB', 'VmallocUsed': '35.219KB', 'VmallocChunk': '0B', 'Percpu': '12.875KB', 'HardwareCorrupted': '0B', 'AnonHugePages': '0B', 'ShmemHugePages': '0B', 'ShmemPmdMapped': '0B', 'CmaTotal': '0B', 'CmaFree': '0B', 'HugePages_Total': '0B', 'HugePages_Free': '0B', 'HugePages_Rsvd': '0B', 'HugePages_Surp': '0B', 'Hugepagesize': '2.000KB', 'Hugetlb': '0B', 'DirectMap4k': '513.266KB', 'DirectMap2M': '6.434MB', 'DirectMap1G': '2.000MB'}
```

## Network information: 

- **Print the information** 

```python
>>> import netmon
>>> netmon.NETmon().print_data()
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
     lo
	 receive
		 bytes 1524122
		 packets 13975
		 errs 0
		 drop 0
		 fifo 0
		 frame 0
		 compressed 0
		 multicast 0
	 transmit
		 bytes 13975
		 packets 0
		 errs 0
		 drop 0
		 fifo 0
		 colls 0
		 carrier 0
 enp37s0
	 receive
		 bytes 134518372
		 packets 155778
		 errs 0
		 drop 0
		 fifo 0
		 frame 0
		 compressed 0
		 multicast 1507
	 transmit
		 bytes 132055
		 packets 0
		 errs 0
		 drop 0
		 fifo 0
		 colls 0
		 carrier 0
```

- **Extract the information in a dictionary**

```python
>>> import netmon
>>> netmon.NETmon().data()
{'docker0': {'receive': {'bytes': 0, 'packets': 0, 'errs': 0, 'drop': 0, 'fifo': 0, 'frame': 0, 'compressed': 0, 'multicast': 0}, 'transmit': {'bytes': 0, 'packets': 0, 'errs': 0, 'drop': 0, 'fifo': 0, 'colls': 0, 'carrier': 0}}, '    lo': {'receive': {'bytes': 1505999, 'packets': 13803, 'errs': 0, 'drop': 0, 'fifo': 0, 'frame': 0, 'compressed': 0, 'multicast': 0}, 'transmit': {'bytes': 13803, 'packets': 0, 'errs': 0, 'drop': 0, 'fifo': 0, 'colls': 0, 'carrier': 0}}, 'enp37s0': {'receive': {'bytes': 134343470, 'packets': 155096, 'errs': 0, 'drop': 0, 'fifo': 0, 'frame': 0, 'compressed': 0, 'multicast': 1489}, 'transmit': {'bytes': 131526, 'packets': 0, 'errs': 0, 'drop': 0, 'fifo': 0, 'colls': 0, 'carrier': 0}}}
```
