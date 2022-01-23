# Changelog

## 1.2.0

### Phone Call Counter
Added a feature to see how many calls are
- missed
- incoming
- outgoing

In addition, the total time spent on these call types is also counted.

This feature uses a local SQLite database to store the calls and to avoid duplicates while a day.
It stores some data there, to allow more statistics later.
The data will also be cleaned up after some days to avoid too much redundant data.
In the YAML configuration file it is possible to configure this feature. 

### YAML configuration possibility
With this release it is possible to configure most parameters via a YAML configuration file.
The only parameter, which still has to be used via CLI is the the address `-i` parameter.

Arguments from the CLI will always overwrite this config.

To have a full separation between default config and custom config and to not overwrite something, a custom configuration should be written in a file called `config_custom.yaml`.
The configuration of this file will be merged with the default `config.yaml` file.

For more information about this feature, please look into the `README.md`.

### install.sh optimization
The `install.sh` file will not longer overwrite the `telegraf_fritzbox.conf` file in `/etc/telegraf/telegraf.d/`` 
