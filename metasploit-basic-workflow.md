# Metasploit — Basic Workflow

Metasploit is a penetration-testing framework used for information gathering, scanning, exploitation, and post-exploitation in authorized environments.

## Basic Metasploit Workflow

```text
1. Start Metasploit
   ↓
2. Search for a module
   ↓
3. Select the module
   ↓
4. Read module information
   ↓
5. View required options
   ↓
6. Set the required options
   ↓
7. Choose a compatible payload (if needed)
   ↓
8. Run the module
   ↓
9. Check the result / session
   ↓
10. Perform authorized post-exploitation
```

## Commands

```text
msfconsole
```
Start Metasploit.

```text
search <term>
```
Search for modules.

```text
use <module>
```
Select a module.

```text
info
```
Show information about the selected module.

```text
show options
```
Show the options required by the selected module.

```text
set <option> <value>
```
Set an option for the current module.

```text
show payloads
```
Show compatible payloads.

```text
run
```
Run an auxiliary module.

```text
exploit
```
Execute an exploit in an authorized lab.

```text
sessions
```
View active sessions.

```text
sessions -i <ID>
```
Interact with a session.

```text
back
```
Leave the current module.

```text
exit
```
Exit Metasploit.

## Example Basic Flow

```text
msfconsole
search <term>
use <module>
info
show options
set <option> <value>
show payloads
run / exploit
sessions
```

> Use Metasploit only on TryHackMe labs, your own systems, or systems where you have explicit permission to perform security testing.
