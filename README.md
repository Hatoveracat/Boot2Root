# Boot2Root
A Boot2Root Machine built to give you a real world hacking experience and showcase how basic defenses get bypassed and how we can mitigate them.

This is a repository where I have uploaded all the files and the design pdf of the Boot2Root Machine and below are commands so that you can configure 
and learn yourself how to SSH secure your linux systems and mitigate breaches.

# Server Download
You can download the server [here](https://releases.ubuntu.com/22.04/ubuntu-22.04.5-live-server-amd64.iso)
# Creation of users

**Low priviledged user**

```bash
useradd -m breacher (or any other username)
passwd <Specify your own passwd>
```

**Highly privilegded user**

```bash
useradd -m pwnuser -s /bin/bash (or any other username)
passwd <Specify your own passwd>
```

```
-s = Configures a shell type for the given user.
```

```
-m = Creates home directory for the given user.
```

Here, We create two users who have there home directory's and have different permissions.
We can # sudo do to configure a root level change in the system.

# SSH Keys Generation and Configuration

Firstly, we switch to the user we want to create **SSH Keys**.

```bash
su <username>
```
Creating the SSH Key using **SSH-Keygen** command.

```bash
ssh-keygen -t rsa -d 4096 -C "boot2root@example.com"
```

```
-t = Sets the type of encryption to apply
-d = No. of iteration to be performed for encryption
-C = Comments if any necessary (optional)
```

Press **yes** after the command to enusre smooth configuration.

Verify your configuration using the command below

Navigate to the home directory using 

```bash
cd ~
```

or directly,

```bash
ls ~/.ssh
```
We will find two files namely id_rsa and id_rsa.pub

```
id_rsa - > holdes the private key that can be used to access the user directly.
id_rsa.pub -> holdes the public key for exchange between client and server.
```

# Configuring files for ports (666  and 1001)

We will place the files **keyfind.py** and **userfind.py** given above in the **/opt** directory of linux filesystem.

```bash
mv keyfind.py /opt/myfiles
mv userfind.py /opt/myfiles
```

If permission denied error happens try using **sudo** before the commands.

# Using socat to open ports with multi-threading

We will open ports in a linux system using sudo priviledges with socat tool.

Installing **socat** tool

```bash
sudo apt-get update && apt-get upgrade -y
sudo apt-get install socat
```
Port opening with multi-threading
```bash
socat TCP-LISTEN:(666 or your choice),reuseaddr,fork EXEC:"python3 /opt/keyfind.py"
socat TCP-LISTEN:(1001 or your choice),reuseaddr,fork EXEC:"python3 /opt/userfind.py"
```
**sudo** is required to open ports.

The above two commands open two extra ports in the system.

**reuseaddr** = Allows for multi-threading.

**fork** = Repeats the same command in **EXEC** for each thread.

**EXEC** = Executes the lines in between quotes.

**TCP-LISTEN** =  Opens a TCP Socket.

# Verify for the ports got opened or not
```bash
netstat -ltpn
```
**Netstat** displays all listening ports.

# Verify by connecting with netcat or nc
```bash
nc <ip address of the server> <port>
```

# Conclusion
Many results can be seen and found when we deploy the system on a CTF challenge as it can showcase the level of 
skills our attackers can have on breaching this machine.We can harden this machine more to test and understand how attackks are done to the system.
