SwLOLs
===

Stupid White List For Linux Servers

If your company has a very strong security policy and you're requested constantly to sent your common sense whitelist for your linux servers (ok, microsoft as well) you can just download this list and send to them. 

This project is a kind of fork of swot initiative that is sourcing a list of educational institutions for discounts, but applied to guarantee that servers may have access to essential repositories such as docker, github, kernel.org, etc

## Usage 

### For import

##### Importing tsv file
```shell
$ python txt2lib.py list.txt

```

TSV format file as 4 columns:
    - Host (may include *)
    - Description
    - TCP ports (comma separated)
    - UDP ports (comma separated)
    
Example:

```text
*.microsoft.com	Microsoft	80,443	
*.ubuntu.com	Ubuntu's Mirror	80,443	
alpine.42.fr	Alpine's Mirror	80,443	
alpine.mirror.far.fi	Alpine's Mirror	80,443	
alpine.mirror.vexxhost.ca	Alpine's Mirror 80,443
```


##### Importing one domain
```shell
$ python txt2lib.py mydomain.com "Personal domain" "80,443" "80,443"

```


### Export the list
```shell
$ python lib2txt.py whitelist.txt

```
### Contributing to SwLOLs

Contributions welcome! Please see the [contribution guidelines](CONTRIBUTING.md) for details on how to add, update, or delete servers. Code contributions and ports to different languages welcome too.