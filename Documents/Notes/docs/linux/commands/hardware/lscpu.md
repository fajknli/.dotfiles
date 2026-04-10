# lscpu - 查看CPU信息

## 一句话理解

lscpu 显示 CPU 架构信息，包括核心数、线程数、型号、频率等。

```bash
# 查看 CPU 信息
lscpu

# 只查看核心数
lscpu | grep "^CPU(s):"
```

## 常用场景

### 1. 查看 CPU 基本信息

```bash
# 查看所有信息
lscpu

# 输出示例：
# Architecture:            x86_64
# CPU op-mode(s):         32-bit, 64-bit
# Address sizes:          48 bits physical, 48 bits virtual
# Byte Order:             Little Endian
# CPU(s):                 16
# On-line CPU(s) list:    0-15
# Vendor ID:              AuthenticAMD
# Model name:             AMD Ryzen 7 5800H
# CPU family:             25
# Model:                  80
# Thread(s) per core:     2
# Core(s) per socket:     8
# Socket(s):              1
# Stepping:               0
# BogoMIPS:               6787.64
# Flags:                  fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid movdiri movdir64b fsrm avx512vbmi avx512_vbmi2 avx512_vnni avx512_bitalg avx512_vpopcntdq rdctl wbnoinvd avx512_vp2intersect
```

### 2. 查看核心和线程数

```bash
# 总核心数（逻辑核心，含超线程）
lscpu | grep "^CPU(s):"

# 物理核心数
lscpu | grep "^Core(s) per socket"

# 插槽数（物理 CPU 数量）
lscpu | grep "^Socket(s):"

# 线程数 = CPU(s) / 插槽数
```

### 3. 查看 CPU 型号和频率

```bash
# CPU 型号
lscpu | grep "Model name"

# 最大频率
lscpu | grep "CPU max MHz"

# 最小频率
lscpu | grep "CPU min MHz"

# 当前频率（动态）
watch -n 1 "grep MHz /proc/cpuinfo"
```

### 4. 查看 CPU 架构特性

```bash
# 查看是否支持虚拟化
lscpu | grep Virtualization

# 查看 CPU 指令集
lscpu | grep Flags

# 检查特定指令集（如 AVX2）
lscpu | grep -o avx2

# 查看字节序
lscpu | grep "Byte Order"
```

### 5. 以不同格式输出

```bash
# JSON 格式（便于脚本）
lscpu --json

# 可解析格式
lscpu --parse

# 只显示特定字段
lscpu --extended
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-a` | 显示所有 CPU 信息 | `lscpu -a` |
| `-b` | 只显示在线 CPU | `lscpu -b` |
| `-c` | 显示离线 CPU | `lscpu -c` |
| `-e` | 显示 CPU 列表 | `lscpu -e` |
| `-p` | 可解析格式输出 | `lscpu -p` |
| `-J` | JSON 格式 | `lscpu -J` |
| `-s` | 不显示字段名 | `lscpu -s` |
| `-x` | 十六进制显示 | `lscpu -x` |

## 常见问题

### 1. 物理核心和逻辑核心区别？

| 概念 | 说明 |
|------|------|
| 物理核心 | 真实存在的 CPU 核心数 |
| 逻辑核心 | 物理核心 × 每核心线程数（含超线程） |

```bash
# 物理核心数
lscpu | grep "Core(s) per socket"
lscpu -p | grep -v "^#" | cut -d, -f4 | sort -u | wc -l

# 逻辑核心数
nproc
lscpu | grep "^CPU(s):"
```

### 2. 如何实时查看 CPU 频率？

```bash
# 方法1
watch -n 1 "grep MHz /proc/cpuinfo"

# 方法2
watch -n 1 "lscpu | grep MHz"

# 方法3
sudo turbostat
```

### 3. 如何检查是否支持虚拟化？

```bash
lscpu | grep Virtualization

# 输出 VT-x（Intel）或 AMD-V（AMD）
# 如果有输出，说明支持硬件虚拟化
```

## 快捷别名

```bash
alias cpu='lscpu'
alias cpus='lscpu | grep "^CPU(s):"'
alias cpumodel='lscpu | grep "Model name"'
alias cpucores='lscpu | grep -E "^CPU\(s\):|^Core\(s\) per socket|^Socket\(s\)"'
alias cpuvirt='lscpu | grep Virtualization'
```

## 相关命令

| 命令 | 说明 |
|------|------|
| `lscpu` | CPU 信息 |
| `lspci` | PCI 设备 |
| `lsusb` | USB 设备 |
| `lshw` | 硬件信息 |
| `dmidecode` | DMI/SMBIOS 信息 |
| `cat /proc/cpuinfo` | 原始 CPU 信息 |

## 一句话总结

lscpu 核心：查看 CPU 总核心数 `lscpu | grep "^CPU(s):"`，查看型号 `lscpu | grep "Model name"`，查看虚拟化支持 `lscpu | grep Virtualization`。脚本用 `lscpu -p` 或 `-J`。配合 `nproc` 获取核心数。
