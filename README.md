# Boot2Root
A Boot2Root Machine built to give you a real world hacking experience and showcase how basic defenses get bypassed and how we can mitigate them

This is a repository where I have uploaded all the files and the design pdf of the Boot2Root Machine and below are commands so that you can configure 
and learn yourself how to SSH secure your linux systems and mitigate breaches.

# Creation of users

Low priviledged user
```bash
useradd -m breacher (or any other username)
passwd <Specify your own passwd>
```
Highly privilegded user
```bash
useradd -m pwnuser -s /bin/bash (or any other username)
passwd <Specify your own passwd>
```

```
-s = Configures a Shell type for the given user.
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
Creating the SSH Key using **SSH-Keygen** command

```bash
ssh-keygen -t rsa -d 4096 -C "boot2root@example.com"
```

