# Ubuntu LAMP Stack Core Setup

Spin up a LAMP VM using Ubuntu.

## Getting Started

Instantiate Ubuntu VM and ssh into it.

### Update and Upgrade

Update update update:

```
sudo apt-get update --fix-missing
sudo apt-get update
sudo apt-get dist-upgrade
```

All set.

## Install Core Software

### Apache

Install Apache:

```
sudo apt-get install apache2
```

Test with:

```
sudo service apache2 restart
```

All set.

### PHP

Grab the PHP repo:

```
sudo LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
sudo apt-get update
```

Install the correct version:

```
sudo apt-get install php5.6
```

Install mcrypt:

```
sudo apt-get install php5.6-mcrypt
```

Install dom:

```
sudo apt-get install php5.6-dom
```

Install mbstring:

```
sudo apt-get install php5.6-mbstring
```

All set.

### MySQL

Install MySQL:

```
sudo apt-get install mysql-server
```

Update:

```
sudo apt-get update
```

Restart Apache once MySQL install is complete:

```
sudo service apache2 restart
```

### Git

Install Git:

```
sudo apt-get install git-core
```

Generate ssh key to link with GitHub:

```
ssh-keygen -t rsa -C "your@email.com"
```

Leave the following blank for default path:

```
Enter file in which to save the key (/root/.ssh/id_rsa):
```

Grab the public key and copy it to your clipboard. Then navigate to your github settings and add it as a new ssh key. You can view the public key by running:

```
cat /root/.ssh/id_rsa.pub
```

Test the key by pinging github with an ssh request:

```
ssh -T git@github.com
```

All set.
