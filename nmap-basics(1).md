# Nmap Basics

## What is Nmap?

**Nmap (Network Mapper)** is a free, open-source network scanning and security auditing tool. It is commonly used by network administrators, cybersecurity professionals, and penetration testers to discover devices on a network, identify open ports, detect services, and assess security.

### What Nmap does

Nmap can help you:

- **Discover hosts:** Find which devices are online on a network.
- **Scan ports:** Determine which TCP or UDP ports are open, closed, or filtered.
- **Identify services:** Detect what services (such as HTTP, SSH, or FTP) are running on open ports.
- **Detect operating systems:** Estimate a target's operating system from network responses.
- **Detect service versions:** Identify versions of software running on services.
- **Run security checks:** Use the Nmap Scripting Engine (NSE) for additional security and configuration checks.

### How Nmap works

Nmap sends network packets to a target and analyzes the responses. From those responses, it can infer whether a host is reachable, which ports are open, what applications may be listening, and characteristics of the operating system.

### Example output

Suppose you manage a server with SSH on port 22, HTTP on port 80, and HTTPS on port 443. Nmap could report:

```text
Host: 192.168.1.10
Host is up.

PORT    STATE  SERVICE
22/tcp  open   ssh
80/tcp  open   http
443/tcp open   https
```

### Common uses

- Network inventory
- Security auditing
- Troubleshooting firewall rules
- Verifying exposed services
- Monitoring changes in network infrastructure

### Common scan types

- **Host discovery** — Finds active devices.
- **TCP connect scan** — Establishes full TCP connections.
- **SYN scan** — Probes TCP ports without completing the full connection handshake.
- **UDP scan** — Checks UDP services.
- **Version detection** — Identifies service software and versions.
- **OS detection** — Estimates the operating system.
- **NSE scripts** — Performs additional checks and enumeration.

> **Important:** Only scan systems and networks that you own or have explicit permission to test.

---

## How to Use Nmap

The safest way to learn Nmap is to use it on your own computer or in an authorized lab.

### 1. Check whether Nmap is installed

Open Command Prompt or PowerShell and run:

```bash
nmap --version
```

### 2. Find your own IP address

On Windows:

```bash
ipconfig
```

Look for your IPv4 address, such as:

```text
192.168.1.10
```

### 3. Scan your own computer

Replace the example IP with your own:

```bash
nmap 192.168.1.10
```

This performs a basic scan and reports accessible ports.

### 4. Scan a specific port

For example, to check port 80:

```bash
nmap -p 80 192.168.1.10
```

You can scan several ports:

```bash
nmap -p 22,80,443 192.168.1.10
```

### 5. Find devices on your own home network

If your network uses the `192.168.1.x` range:

```bash
nmap -sn 192.168.1.0/24
```

`-sn` performs host discovery without a normal port scan.

### 6. Identify services and versions

On a machine you are authorized to test:

```bash
nmap -sV 192.168.1.10
```

`-sV` attempts to identify the software and version behind open ports.

### 7. Try service and OS detection

```bash
nmap -sV -O 192.168.1.10
```

- `-sV` = service/version detection
- `-O` = operating-system detection

## A Simple Learning Path

Start with:

```bash
nmap --version
```

Then:

```bash
nmap YOUR-IP
```

Then practice:

```bash
nmap -p 80 YOUR-IP
nmap -sV YOUR-IP
nmap -sV -O YOUR-IP
```

Learn to read the `PORT`, `STATE`, and `SERVICE` columns before moving on to more advanced options.

> **Security reminder:** Do not scan public or third-party systems without authorization.


---

# Advanced Nmap Commands

The examples below are intended for **systems and networks you own or are explicitly authorized to test**.

## 8. Scan all TCP ports

A basic Nmap scan checks a common set of ports. To scan all TCP ports:

```bash
nmap -p- 192.168.1.10
```

`-p-` means ports `1-65535`.

You can combine this with service detection:

```bash
nmap -p- -sV 192.168.1.10
```

## 9. Scan selected port ranges

Scan a range:

```bash
nmap -p 1-1000 192.168.1.10
```

Scan multiple ranges:

```bash
nmap -p 22,80,443,8000-8080 192.168.1.10
```

## 10. SYN scan

A SYN scan is a common TCP scanning method:

```bash
nmap -sS 192.168.1.10
```

It is useful for authorized security testing and requires appropriate permissions on some operating systems.

## 11. TCP connect scan

Use a full TCP connection:

```bash
nmap -sT 192.168.1.10
```

This is useful when a SYN scan is unavailable or you are working without the required raw-packet privileges.

## 12. UDP scan

Check UDP ports on an authorized target:

```bash
nmap -sU 192.168.1.10
```

UDP scans can take longer than TCP scans. You can limit the ports:

```bash
nmap -sU -p 53,67,68,123,161 192.168.1.10
```

## 13. Combine TCP and UDP scans

```bash
nmap -sS -sU 192.168.1.10
```

For a narrower test:

```bash
nmap -sS -sU -p T:22,80,443,U:53,123,161 192.168.1.10
```

`T:` specifies TCP ports and `U:` specifies UDP ports.

## 14. Aggressive detection

Nmap's `-A` option enables several detection features together:

```bash
nmap -A 192.168.1.10
```

It includes features such as:

- OS detection
- Version detection
- Script scanning
- Traceroute

Because it performs more probing, use it only where you have authorization.

## 15. Run specific NSE scripts

Nmap includes the **Nmap Scripting Engine (NSE)**.

List available scripts:

```bash
nmap --script-help default
```

Run a specific script against an authorized target:

```bash
nmap --script=banner 192.168.1.10
```

Run a category of scripts:

```bash
nmap --script=default 192.168.1.10
```

NSE scripts can perform many different tasks, so review what a script does before running it.

## 16. Check common web-related information

For a web server you are authorized to test:

```bash
nmap --script=http-title 192.168.1.10
```

You can combine it with service detection:

```bash
nmap -sV --script=http-title 192.168.1.10
```

## 17. Detect common service versions

```bash
nmap -sV --version-intensity 5 192.168.1.10
```

Higher version intensity generally means more probing and can take longer.

## 18. Save scan results

Save normal output:

```bash
nmap -oN scan.txt 192.168.1.10
```

Save XML output:

```bash
nmap -oX scan.xml 192.168.1.10
```

Save output in all major formats:

```bash
nmap -oA myscan 192.168.1.10
```

This creates files such as:

```text
myscan.nmap
myscan.xml
myscan.gnmap
```

## 19. Increase or reduce scan speed

Nmap supports timing templates from `-T0` through `-T5`.

For example:

```bash
nmap -T4 192.168.1.10
```

`-T4` is commonly useful on reliable networks. Very aggressive timing can increase network load and may reduce accuracy, so use it carefully.

## 20. Show more detailed output

Verbose mode:

```bash
nmap -v 192.168.1.10
```

More verbosity:

```bash
nmap -vv 192.168.1.10
```

Debug mode:

```bash
nmap -d 192.168.1.10
```

Debug output can become very large, so it is mainly useful for troubleshooting.

## 21. Scan a subnet

Scan a small authorized network range:

```bash
nmap 192.168.1.0/24
```

Perform host discovery first:

```bash
nmap -sn 192.168.1.0/24
```

Then scan selected hosts as appropriate.

## 22. Disable DNS resolution

This can make some scans faster:

```bash
nmap -n 192.168.1.10
```

## 23. Perform a traceroute

```bash
nmap --traceroute 192.168.1.10
```

This can help show the network path between your machine and the target.

## 24. Use a custom source port

For authorized lab testing and firewall troubleshooting:

```bash
nmap --source-port 53 192.168.1.10
```

This changes the source port used by Nmap probes. Only use such testing on networks where you have permission.

## 25. Scan IPv6

If the target and network support IPv6:

```bash
nmap -6 2001:db8::10
```

Use the actual IPv6 address of an authorized device instead of the documentation address above.

## 26. Exclude a host from a network scan

```bash
nmap 192.168.1.0/24 --exclude 192.168.1.1
```

This is useful when a particular device should not be probed.

## 27. Combine advanced options

A practical authorized assessment might combine several features:

```bash
nmap -sS -sV -O -p 1-1000 -T4 192.168.1.10
```

This combines:

- `-sS` — SYN scan
- `-sV` — service/version detection
- `-O` — OS detection
- `-p 1-1000` — ports 1 through 1000
- `-T4` — faster timing template

## 28. Example lab workflow

For a machine in your own lab, you can progressively build a scan:

```bash
# Step 1: Host discovery
nmap -sn 192.168.1.0/24

# Step 2: Basic port scan
nmap 192.168.1.10

# Step 3: All TCP ports
nmap -p- 192.168.1.10

# Step 4: Service detection
nmap -sV -p- 192.168.1.10

# Step 5: OS and service detection
nmap -sV -O 192.168.1.10

# Step 6: Save the results
nmap -sV -O -p- -oA lab-scan 192.168.1.10
```

## Command Option Reference

| Option | Purpose |
|---|---|
| `-sn` | Host discovery without a port scan |
| `-p-` | Scan all TCP ports |
| `-p` | Select specific ports or ranges |
| `-sS` | TCP SYN scan |
| `-sT` | TCP connect scan |
| `-sU` | UDP scan |
| `-sV` | Service/version detection |
| `-O` | OS detection |
| `-A` | Aggressive detection features |
| `--script` | Run NSE scripts |
| `-T4` | Faster timing template |
| `-n` | Skip DNS resolution |
| `-v` / `-vv` | Increase verbosity |
| `-oN` | Save normal output |
| `-oX` | Save XML output |
| `-oA` | Save output in multiple formats |
| `--traceroute` | Perform traceroute |

> **Safety reminder:** Advanced scanning can generate significant network traffic and may trigger security systems. Use these commands only against systems you own or have explicit permission to test.
# Nmap TCP Scan Options

A GitHub-ready reference for the Nmap scan options shown in the screenshots.

> **Authorized use only:** Run scans only against systems you own or have explicit permission to test. Replace the example IP and placeholder values with values from your authorized lab.

## TCP scan types

| Scan type | Command | Purpose / notes |
|---|---|---|
| TCP Null Scan | `sudo nmap -sN 10.113.132.230` | Sends TCP probes with no flags set. |
| TCP FIN Scan | `sudo nmap -sF 10.113.132.230` | Sends TCP probes with the FIN flag set. |
| TCP Xmas Scan | `sudo nmap -sX 10.113.132.230` | Sends TCP probes with FIN, PSH, and URG flags set. |
| TCP Maimon Scan | `sudo nmap -sM 10.113.132.230` | Uses the TCP FIN/ACK flag combination. |
| TCP ACK Scan | `sudo nmap -sA 10.113.132.230` | Helps analyze firewall filtering; it does not directly determine whether a port is open. |
| TCP Window Scan | `sudo nmap -sW 10.113.132.230` | Uses TCP window responses to help distinguish some port states. |
| Custom TCP Scan | `sudo nmap --scanflags URGACKPSHRSTSYNFIN 10.113.132.230` | Sets a custom combination of TCP flags. |
| Spoofed Source IP | `sudo nmap -S SPOOFED_IP 10.113.132.230` | Sets a chosen source IP address; replies may go to that address. Use only in an authorized lab. |
| Spoofed MAC Address | `sudo nmap --spoof-mac SPOOFED_MAC 10.113.132.230` | Sets a chosen source MAC address on supported local Ethernet scans. |
| Decoy Scan | `sudo nmap -D DECOY_IP,ME 10.113.132.230` | Adds decoy source addresses to the scan. Use only in an authorized lab. |
| Idle (Zombie) Scan | `sudo nmap -sI ZOMBIE_IP 10.113.132.230` | Uses a suitable idle host as a side channel; requires an appropriate zombie host. |

## Packet fragmentation

| Option | Meaning |
|---|---|
| `-f` | Fragment IP packets; Nmap documents this as splitting packets into small fragments (typically 8 bytes of payload per fragment unit). |
| `-ff` | Use the `-f` option twice for smaller fragments (typically 16 bytes of IP data per fragment unit, as described in the source notes). |

## Additional options

| Option | Purpose |
|---|---|
| `--source-port PORT_NUM` | Specify the source port number. |
| `--data-length NUM` | Append random data to probes to reach the specified additional data length. |
| `--reason` | Explain why Nmap assigned a particular port or host state. |
| `-d` | Enable debugging output. |
| `-dd` | Enable more detailed debugging output. |

## Notes

- Null, FIN, and Xmas scans often rely on how closed ports respond to unusual TCP flag combinations. Results can vary by operating system and network equipment.
- Maimon, ACK, and Window scans use different response behavior; an ACK scan is primarily useful for understanding filtering, not for confirming open ports.
- Firewalls, packet filters, and the target operating system can affect scan results.
- The IP address `10.113.132.230` is copied from the screenshots as an example target. Replace it with your authorized lab target.

## Basic usage

```bash
sudo nmap -sN <AUTHORIZED_TARGET>
sudo nmap -sF <AUTHORIZED_TARGET>
sudo nmap -sX <AUTHORIZED_TARGET>
```

For official option details, see the [Nmap Reference Guide](https://nmap.org/book/man.html).
