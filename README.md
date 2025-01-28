

### Building:

Clone `https://github.com/OpenTollGate/tollgate-sdk.git` and run:

```
./build-firmware gl-ar300m tollgate-module-relay-go
./build-firmware gl-mt3000 tollgate-module-relay-go

```

# Populate the `json` so that your binaries can be pushed to blossom
```
$ cat blossom_secrets.json 
{
  "servers": [
    "https://files.v0l.io/",
    "https://nostr.download/",
    "https://blossom.poster.place/"
  ],
  "relays": [
    "wss://orangesync.tech",
    "wss://nostr.mom",
    "wss://relay.stens.dev"
  ],
  "secret_key": "nsec[your_secret_key]",
  "secret_key_hex": "[hex_version_of_your_secret_key]"
}
```

# Install blossom and noscl cli
```
$ ./blossom-installer.sh 
$ ./noscl-installer.sh 

```


Expected output:
```
toll_gate_sdk$ ./build-firmware gl-ar300m helloworld
libncurses5-dev and libncursesw5-dev are already installed.
Extracting SDK...
...
...
...
find /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/build_dir/target-mips_24kc_musl/helloworld-1.0.2 -mindepth 1 -maxdepth 1 -not '(' -type f -and -name '.*' -and -size 0 ')' -and -not -name '.pkgdir'  -print0 | xargs -r -0 rm -rf
make[2]: Leaving directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/package/helloworld'
time: package/helloworld/compile#0.70#0.68#4.71
make[1]: Leaving directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64'
Package built successfully!
IPK file location: /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/bin/packages/mips_24kc/base/helloworld_1.0-2_mips_24kc.ipk

```

Ready!


### Installing:

```

root@GL-AR300M:/tmp# scp username@192.168.8.113:/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Lin
ux-x86_64/bin/packages/mips_24kc/base/helloworld_1.0-2_mips_24kc.ipk .
username@192.168.8.113's password: 
helloworld_1.0-2_mips_24kc.ipk                                                      100% 2363     2.3KB/s   00:00    
root@GL-AR300M:/tmp# opkg install helloworld_1.0-2_mips_24kc.ipk 
Upgrading helloworld on root from 1.0-1 to 1.0-2...
Configuring helloworld.
Updating database.
Database update completed.
root@GL-AR300M:/tmp# helloworld 
Hello world, this is a C++14 test

```

### Debugging:

```
./build-firmware gl-ar300m helloworld  > compile_logs.md 2> >(tee -a compile_logs.md >&2)

grep -n -E "Error|failed" -C 5 compile_log.md

```

