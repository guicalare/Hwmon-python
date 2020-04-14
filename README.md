# Hwmon-python

With the collaboration of Bla6: [Bla6 Gitlab](https://gitlab.com/bla6)

**Important**: these scripts do not work in virtual machines 

# What is Hwmon 

**Hwmon** is a collection of Python 3 scripts which are a native Python solution for obtaining information from Linux system sensors. Currently it is still under development and the idea is to group in the same library the same lm-sensors and psutil functions without having to install anything in the system. 

All the information used in this library is the same information handled by both lm-sensors and psutil (or that is what it is intended to do, so there may be some small differences). At the moment the data extracted from the system are: 

- **Sensor information** (from /sys/class/hwmon)
- **Processor information** (from /proc/cpuinfo and /proc/stat) 
- **System memory information** (from /proc/meminfo) 

# Why use this library instead of others? 

Most of the other libraries require ls-sensors to be installed or use C libraries to call data APIs. While with Hwmon you won't have to install anything or fight with other languages/dependencies or APIs, since Hwmon reads directly the system files and the only library it uses is "os" so it doesn't require any previous installation or other languages.

# Does it show the same thing as lm-sensors? 

Hwmon shows the same as lm-sensors but with different names in some cases. This will be solved in future updates of the library. 

Let's see an example of comparisons between lm-sensors and hwmon: 

# Available sensors and calls 

## Sensor information: 

As far as execution and data collection are concerned, we have: 

- **Print the information** 

```python
>>> import hwmon
>>> hwmon.Hwmon().print_data()
amdgpu
	   vddgfx   0.75 v
	   power1   30.033 w
	   fan1   1124 RPM
	   edge   30.0 ºC
nct6779
	   AUXTIN3   -28.0 ºC
	   in3   3.36 v
	   fan3   0 RPM
	   in7   3.472 v
	   AUXTIN0   -0.5 ºC
	   in12   1.688 v
	   in0   0.256 v
	   PCH_CPU_TEMP   0.0 ºC
	   SMBUSMASTER 0   28.5 ºC
	   in4   1.848 v
	   fan4   0 RPM
	   in8   3.264 v
	   AUXTIN1   86.0 ºC
	   in13   0.944 v
	   in1   0.0 v
	   fan1   0 RPM
	   PCH_CHIP_CPU_MAX_TEMP   0.0 ºC
	   in5   0.84 v
	   SYSTIN   31.0 ºC
	   in10   0.352 v
	   fan5   0 RPM
	   in9   0.0 v
	   AUXTIN2   23.0 ºC
	   in14   1.848 v
	   in2   3.36 v
	   fan2   1928 RPM
	   PCH_CHIP_TEMP   0.0 ºC
	   in6   1.504 v
	   CPUTIN   31.0 ºC
	   in11   1.056 v
k10temp
	   Tdie   28.75 ºC
	   Tctl   28.75 ºC
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
Name
	 AMD Ryzen 5 1400 Quad-Core Processor
CPU_usage
	 5.83
cores
	 4
threads
	 8
Average_MHz
	 1375.64
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
MemTotal   7.768MB
MemFree   3.380MB
MemAvailable   5.091MB
Buffers   166.520KB
Cached   1.811MB
SwapCached   0B
Active   2.436MB
Inactive   1.435MB
Active(anon)   1.896MB
Inactive(anon)   111.848KB
Active(file)   552.703KB
Inactive(file)   1.326MB
Unevictable   16.0B
Mlocked   16.0B
SwapTotal   2.000MB
SwapFree   2.000MB
Dirty   72.0B
Writeback   0B
AnonPages   1.898MB
Mapped   705.699KB
Shmem   113.289KB
KReclaimable   112.453KB
Slab   253.168KB
SReclaimable   112.453KB
SUnreclaim   140.715KB
KernelStack   19.797KB
PageTables   57.680KB
NFS_Unstable   0B
Bounce   0B
WritebackTmp   0B
CommitLimit   5.884MB
Committed_AS   8.894MB
VmallocTotal   32.000GB
VmallocUsed   34.453KB
VmallocChunk   0B
Percpu   14.312KB
HardwareCorrupted   0B
AnonHugePages   0B
ShmemHugePages   0B
ShmemPmdMapped   0B
CmaTotal   0B
CmaFree   0B
HugePages_Total   0B
HugePages_Free   0B
HugePages_Rsvd   0B
HugePages_Surp   0B
Hugepagesize   2.000KB
Hugetlb   0B
DirectMap4k   427.266KB
DirectMap2M   5.518MB
DirectMap1G   3.000MB
```

- **Extract the information in a dictionary**

```python
>>> import memmon
>>> memmon.MEMmon().data()
{'MemTotal': 8145808.0, 'MemFree': 3501300.0, 'MemAvailable': 5296320.0, 'Buffers': 170588.0, 'Cached': 1932316.0, 'SwapCached': 0.0, 'Active': 2558948.0, 'Inactive': 1538684.0, 'Active(anon)': 1992908.0, 'Inactive(anon)': 148100.0, 'Active(file)': 566040.0, 'Inactive(file)': 1390584.0, 'Unevictable': 16.0, 'Mlocked': 16.0, 'SwapTotal': 2097148.0, 'SwapFree': 2097148.0, 'Dirty': 112.0, 'Writeback': 0.0, 'AnonPages': 1994848.0, 'Mapped': 756208.0, 'Shmem': 149556.0, 'KReclaimable': 115188.0, 'Slab': 259216.0, 'SReclaimable': 115188.0, 'SUnreclaim': 144028.0, 'KernelStack': 20272.0, 'PageTables': 59200.0, 'NFS_Unstable': 0.0, 'Bounce': 0.0, 'WritebackTmp': 0.0, 'CommitLimit': 6170052.0, 'Committed_AS': 9362924.0, 'VmallocTotal': 34359738367.0, 'VmallocUsed': 35280.0, 'VmallocChunk': 0.0, 'Percpu': 14656.0, 'HardwareCorrupted': 0.0, 'AnonHugePages': 0.0, 'ShmemHugePages': 0.0, 'ShmemPmdMapped': 0.0, 'CmaTotal': 0.0, 'CmaFree': 0.0, 'HugePages_Total': 0.0, 'HugePages_Free': 0.0, 'HugePages_Rsvd': 0.0, 'HugePages_Surp': 0.0, 'Hugepagesize': 2048.0, 'Hugetlb': 0.0, 'DirectMap4k': 437520.0, 'DirectMap2M': 5785600.0, 'DirectMap1G': 3145728.0}

```
