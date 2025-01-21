/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64$ make --debug=b package/feeds/packages/golang/prepare V=s
GNU Make 4.3
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Reading makefiles...
Updating makefiles....
Updating goal targets....
 File 'package/feeds/packages/golang/prepare' does not exist.
Must remake target 'package/feeds/packages/golang/prepare'.
GNU Make 4.3
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Reading makefiles...
Updating makefiles....
Updating goal targets....
 File 'prereq' does not exist.
   File 'prepare-tmpinfo' does not exist.
     File 'FORCE' does not exist.
    Must remake target 'FORCE'.
    Successfully remade target file 'FORCE'.
  Must remake target 'prepare-tmpinfo'.
GNU Make 4.3
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Reading makefiles...
Updating makefiles....
Updating goal targets....
Collecting package info: done
WARNING: Makefile 'package/kernel/linux/Makefile' has a dependency on 'kmod-phy-bcm-ns-usb2', which does not exist
WARNING: Makefile 'package/kernel/linux/Makefile' has a dependency on 'kmod-phy-bcm-ns-usb3', which does not exist
  Successfully remade target file 'prepare-tmpinfo'.
     Prerequisite 'FORCE' of target 'scripts/config/conf' does not exist.
    Must remake target 'scripts/config/conf'.
make[2]: Entering directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/scripts/config'
make[2]: 'conf' is up to date.
make[2]: Leaving directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/scripts/config'
    Successfully remade target file 'scripts/config/conf'.
   Prerequisite 'prepare-tmpinfo' of target '.config' does not exist.
  Must remake target '.config'.
  Successfully remade target file '.config'.
Must remake target 'prereq'.
GNU Make 4.3
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Reading makefiles...
Updating makefiles....
Updating goal targets....
 File 'prereq' does not exist.
   Prerequisite '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/tmp/.build' is newer than target '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mips_24kc_musl/stamp/.package_prereq'.
  Must remake target '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mips_24kc_musl/stamp/.package_prereq'.
  Successfully remade target file '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mips_24kc_musl/stamp/.package_prereq'.
Must remake target 'prereq'.
Successfully remade target file 'prereq'.
Successfully remade target file 'prereq'.
tmp/.config-feeds.in:9:warning: ignoring type redefinition of 'FEED_packages' from 'bool' to 'tristate'
tmp/.config-feeds.in:17:warning: ignoring type redefinition of 'FEED_luci' from 'bool' to 'tristate'
tmp/.config-feeds.in:25:warning: ignoring type redefinition of 'FEED_routing' from 'bool' to 'tristate'
tmp/.config-feeds.in:33:warning: ignoring type redefinition of 'FEED_telephony' from 'bool' to 'tristate'
tmp/.config-package.in:55:warning: ignoring type redefinition of 'PACKAGE_base-files' from 'bool' to 'tristate'
tmp/.config-package.in:147:warning: ignoring type redefinition of 'PACKAGE_busybox' from 'bool' to 'tristate'
tmp/.config-package.in:177:warning: ignoring type redefinition of 'PACKAGE_ca-bundle' from 'bool' to 'tristate'
tmp/.config-package.in:195:warning: ignoring type redefinition of 'PACKAGE_dnsmasq' from 'bool' to 'tristate'
tmp/.config-package.in:274:warning: ignoring type redefinition of 'PACKAGE_dropbear' from 'bool' to 'tristate'
tmp/.config-package.in:321:warning: ignoring type redefinition of 'PACKAGE_firewall4' from 'bool' to 'tristate'
tmp/.config-package.in:341:warning: ignoring type redefinition of 'PACKAGE_fstools' from 'bool' to 'tristate'
tmp/.config-package.in:375:warning: ignoring type redefinition of 'PACKAGE_fwtool' from 'bool' to 'tristate'
tmp/.config-package.in:384:warning: ignoring type redefinition of 'PACKAGE_getrandom' from 'bool' to 'tristate'
tmp/.config-package.in:404:warning: ignoring type redefinition of 'PACKAGE_jsonfilter' from 'bool' to 'tristate'
tmp/.config-package.in:479:warning: ignoring type redefinition of 'PACKAGE_libc' from 'bool' to 'tristate'
tmp/.config-package.in:507:warning: ignoring type redefinition of 'PACKAGE_libgcc' from 'bool' to 'tristate'
tmp/.config-package.in:628:warning: ignoring type redefinition of 'PACKAGE_libpthread' from 'bool' to 'tristate'
tmp/.config-package.in:810:warning: ignoring type redefinition of 'PACKAGE_logd' from 'bool' to 'tristate'
tmp/.config-package.in:822:warning: ignoring type redefinition of 'PACKAGE_mtd' from 'bool' to 'tristate'
tmp/.config-package.in:833:warning: ignoring type redefinition of 'PACKAGE_netifd' from 'bool' to 'tristate'
tmp/.config-package.in:873:warning: ignoring type redefinition of 'PACKAGE_openwrt-keyring' from 'bool' to 'tristate'
tmp/.config-package.in:883:warning: ignoring type redefinition of 'PACKAGE_opkg' from 'bool' to 'tristate'
tmp/.config-package.in:932:warning: ignoring type redefinition of 'PACKAGE_procd' from 'bool' to 'tristate'
tmp/.config-package.in:962:warning: ignoring type redefinition of 'PACKAGE_procd-seccomp' from 'bool' to 'tristate'
tmp/.config-package.in:993:warning: ignoring type redefinition of 'PACKAGE_procd-ujail' from 'bool' to 'tristate'
tmp/.config-package.in:1086:warning: ignoring type redefinition of 'PACKAGE_rpcd' from 'bool' to 'tristate'
tmp/.config-package.in:1101:warning: ignoring type redefinition of 'PACKAGE_rpcd-mod-file' from 'bool' to 'tristate'
tmp/.config-package.in:1113:warning: ignoring type redefinition of 'PACKAGE_rpcd-mod-iwinfo' from 'bool' to 'tristate'
tmp/.config-package.in:1138:warning: ignoring type redefinition of 'PACKAGE_rpcd-mod-ucode' from 'bool' to 'tristate'
tmp/.config-package.in:1200:warning: ignoring type redefinition of 'PACKAGE_swconfig' from 'bool' to 'tristate'
tmp/.config-package.in:1211:warning: ignoring type redefinition of 'PACKAGE_ubox' from 'bool' to 'tristate'
tmp/.config-package.in:1225:warning: ignoring type redefinition of 'PACKAGE_ubus' from 'bool' to 'tristate'
tmp/.config-package.in:1237:warning: ignoring type redefinition of 'PACKAGE_ubusd' from 'bool' to 'tristate'
tmp/.config-package.in:1273:warning: ignoring type redefinition of 'PACKAGE_uci' from 'bool' to 'tristate'
tmp/.config-package.in:1343:warning: ignoring type redefinition of 'PACKAGE_urandom-seed' from 'bool' to 'tristate'
tmp/.config-package.in:1354:warning: ignoring type redefinition of 'PACKAGE_urngd' from 'bool' to 'tristate'
tmp/.config-package.in:1374:warning: ignoring type redefinition of 'PACKAGE_usign' from 'bool' to 'tristate'
tmp/.config-package.in:6854:warning: ignoring type redefinition of 'PACKAGE_libiwinfo-data' from 'bool' to 'tristate'
tmp/.config-package.in:10416:warning: ignoring type redefinition of 'PACKAGE_wireless-regdb' from 'bool' to 'tristate'
tmp/.config-package.in:11702:warning: ignoring type redefinition of 'PACKAGE_kmod-gpio-button-hotplug' from 'bool' to 'tristate'
tmp/.config-package.in:11991:warning: ignoring type redefinition of 'PACKAGE_kmod-ath' from 'bool' to 'tristate'
tmp/.config-package.in:12234:warning: ignoring type redefinition of 'PACKAGE_kmod-ath9k' from 'bool' to 'tristate'
tmp/.config-package.in:12271:warning: ignoring type redefinition of 'PACKAGE_kmod-ath9k-common' from 'bool' to 'tristate'
tmp/.config-package.in:12657:warning: ignoring type redefinition of 'PACKAGE_kmod-cfg80211' from 'bool' to 'tristate'
tmp/.config-package.in:12749:warning: ignoring type redefinition of 'PACKAGE_kmod-mac80211' from 'bool' to 'tristate'
tmp/.config-package.in:28039:warning: ignoring type redefinition of 'PACKAGE_ucode' from 'bool' to 'tristate'
tmp/.config-package.in:28062:warning: ignoring type redefinition of 'PACKAGE_ucode-mod-fs' from 'bool' to 'tristate'
tmp/.config-package.in:28083:warning: ignoring type redefinition of 'PACKAGE_ucode-mod-math' from 'bool' to 'tristate'
tmp/.config-package.in:28093:warning: ignoring type redefinition of 'PACKAGE_ucode-mod-nl80211' from 'bool' to 'tristate'
tmp/.config-package.in:28115:warning: ignoring type redefinition of 'PACKAGE_ucode-mod-rtnl' from 'bool' to 'tristate'
tmp/.config-package.in:28137:warning: ignoring type redefinition of 'PACKAGE_ucode-mod-ubus' from 'bool' to 'tristate'
tmp/.config-package.in:28149:warning: ignoring type redefinition of 'PACKAGE_ucode-mod-uci' from 'bool' to 'tristate'
tmp/.config-package.in:28160:warning: ignoring type redefinition of 'PACKAGE_ucode-mod-uloop' from 'bool' to 'tristate'
tmp/.config-package.in:39643:warning: ignoring type redefinition of 'PACKAGE_libmbedtls' from 'bool' to 'tristate'
tmp/.config-package.in:41620:warning: ignoring type redefinition of 'PACKAGE_jansson' from 'bool' to 'tristate'
tmp/.config-package.in:42081:warning: ignoring type redefinition of 'PACKAGE_libblobmsg-json' from 'bool' to 'tristate'
tmp/.config-package.in:44721:warning: ignoring type redefinition of 'PACKAGE_libiwinfo' from 'bool' to 'tristate'
tmp/.config-package.in:44757:warning: ignoring type redefinition of 'PACKAGE_libjson-c' from 'bool' to 'tristate'
tmp/.config-package.in:44881:warning: ignoring type redefinition of 'PACKAGE_liblucihttp' from 'bool' to 'tristate'
tmp/.config-package.in:44901:warning: ignoring type redefinition of 'PACKAGE_liblucihttp-ucode' from 'bool' to 'tristate'
tmp/.config-package.in:45068:warning: ignoring type redefinition of 'PACKAGE_libmnl' from 'bool' to 'tristate'
tmp/.config-package.in:45517:warning: ignoring type redefinition of 'PACKAGE_libnftnl' from 'bool' to 'tristate'
tmp/.config-package.in:45632:warning: ignoring type redefinition of 'PACKAGE_libnl-tiny' from 'bool' to 'tristate'
tmp/.config-package.in:47663:warning: ignoring type redefinition of 'PACKAGE_libubox' from 'bool' to 'tristate'
tmp/.config-package.in:47683:warning: ignoring type redefinition of 'PACKAGE_libubus' from 'bool' to 'tristate'
tmp/.config-package.in:47704:warning: ignoring type redefinition of 'PACKAGE_libuci' from 'bool' to 'tristate'
tmp/.config-package.in:47736:warning: ignoring type redefinition of 'PACKAGE_libuclient' from 'bool' to 'tristate'
tmp/.config-package.in:47746:warning: ignoring type redefinition of 'PACKAGE_libucode' from 'bool' to 'tristate'
tmp/.config-package.in:47924:warning: ignoring type redefinition of 'PACKAGE_libustream-mbedtls' from 'bool' to 'tristate'
tmp/.config-package.in:48671:warning: ignoring type redefinition of 'PACKAGE_rpcd-mod-luci' from 'bool' to 'tristate'
tmp/.config-package.in:48708:warning: ignoring type redefinition of 'PACKAGE_rpcd-mod-rrdns' from 'bool' to 'tristate'
tmp/.config-package.in:48935:warning: ignoring type redefinition of 'PACKAGE_luci' from 'bool' to 'tristate'
tmp/.config-package.in:48961:warning: ignoring type redefinition of 'PACKAGE_luci-light' from 'bool' to 'tristate'
tmp/.config-package.in:49000:warning: ignoring type redefinition of 'PACKAGE_luci-ssl' from 'bool' to 'tristate'
tmp/.config-package.in:49051:warning: ignoring type redefinition of 'PACKAGE_luci-base' from 'bool' to 'tristate'
tmp/.config-package.in:49088:warning: ignoring type redefinition of 'LUCI_LANG_ar' from 'bool' to 'tristate'
tmp/.config-package.in:49091:warning: ignoring type redefinition of 'LUCI_LANG_bg' from 'bool' to 'tristate'
tmp/.config-package.in:49094:warning: ignoring type redefinition of 'LUCI_LANG_bn_BD' from 'bool' to 'tristate'
tmp/.config-package.in:49097:warning: ignoring type redefinition of 'LUCI_LANG_ca' from 'bool' to 'tristate'
tmp/.config-package.in:49100:warning: ignoring type redefinition of 'LUCI_LANG_cs' from 'bool' to 'tristate'
tmp/.config-package.in:49103:warning: ignoring type redefinition of 'LUCI_LANG_da' from 'bool' to 'tristate'
tmp/.config-package.in:49106:warning: ignoring type redefinition of 'LUCI_LANG_de' from 'bool' to 'tristate'
tmp/.config-package.in:49109:warning: ignoring type redefinition of 'LUCI_LANG_el' from 'bool' to 'tristate'
tmp/.config-package.in:49112:warning: ignoring type redefinition of 'LUCI_LANG_es' from 'bool' to 'tristate'
tmp/.config-package.in:49115:warning: ignoring type redefinition of 'LUCI_LANG_fi' from 'bool' to 'tristate'
tmp/.config-package.in:49118:warning: ignoring type redefinition of 'LUCI_LANG_fr' from 'bool' to 'tristate'
tmp/.config-package.in:49121:warning: ignoring type redefinition of 'LUCI_LANG_he' from 'bool' to 'tristate'
tmp/.config-package.in:49124:warning: ignoring type redefinition of 'LUCI_LANG_hi' from 'bool' to 'tristate'
tmp/.config-package.in:49127:warning: ignoring type redefinition of 'LUCI_LANG_hu' from 'bool' to 'tristate'
tmp/.config-package.in:49130:warning: ignoring type redefinition of 'LUCI_LANG_it' from 'bool' to 'tristate'
tmp/.config-package.in:49133:warning: ignoring type redefinition of 'LUCI_LANG_ja' from 'bool' to 'tristate'
tmp/.config-package.in:49136:warning: ignoring type redefinition of 'LUCI_LANG_ko' from 'bool' to 'tristate'
tmp/.config-package.in:49139:warning: ignoring type redefinition of 'LUCI_LANG_lt' from 'bool' to 'tristate'
tmp/.config-package.in:49142:warning: ignoring type redefinition of 'LUCI_LANG_mr' from 'bool' to 'tristate'
tmp/.config-package.in:49145:warning: ignoring type redefinition of 'LUCI_LANG_ms' from 'bool' to 'tristate'
tmp/.config-package.in:49148:warning: ignoring type redefinition of 'LUCI_LANG_nb_NO' from 'bool' to 'tristate'
tmp/.config-package.in:49151:warning: ignoring type redefinition of 'LUCI_LANG_nl' from 'bool' to 'tristate'
tmp/.config-package.in:49154:warning: ignoring type redefinition of 'LUCI_LANG_pl' from 'bool' to 'tristate'
tmp/.config-package.in:49157:warning: ignoring type redefinition of 'LUCI_LANG_pt' from 'bool' to 'tristate'
tmp/.config-package.in:49160:warning: ignoring type redefinition of 'LUCI_LANG_pt_BR' from 'bool' to 'tristate'
tmp/.config-package.in:49163:warning: ignoring type redefinition of 'LUCI_LANG_ro' from 'bool' to 'tristate'
tmp/.config-package.in:49166:warning: ignoring type redefinition of 'LUCI_LANG_ru' from 'bool' to 'tristate'
tmp/.config-package.in:49169:warning: ignoring type redefinition of 'LUCI_LANG_sk' from 'bool' to 'tristate'
tmp/.config-package.in:49172:warning: ignoring type redefinition of 'LUCI_LANG_sv' from 'bool' to 'tristate'
tmp/.config-package.in:49175:warning: ignoring type redefinition of 'LUCI_LANG_tr' from 'bool' to 'tristate'
tmp/.config-package.in:49178:warning: ignoring type redefinition of 'LUCI_LANG_uk' from 'bool' to 'tristate'
tmp/.config-package.in:49181:warning: ignoring type redefinition of 'LUCI_LANG_vi' from 'bool' to 'tristate'
tmp/.config-package.in:49184:warning: ignoring type redefinition of 'LUCI_LANG_zh_Hans' from 'bool' to 'tristate'
tmp/.config-package.in:49187:warning: ignoring type redefinition of 'LUCI_LANG_zh_Hant' from 'bool' to 'tristate'
tmp/.config-package.in:49222:warning: ignoring type redefinition of 'PACKAGE_luci-mod-admin-full' from 'bool' to 'tristate'
tmp/.config-package.in:49288:warning: ignoring type redefinition of 'PACKAGE_luci-mod-network' from 'bool' to 'tristate'
tmp/.config-package.in:49312:warning: ignoring type redefinition of 'PACKAGE_luci-mod-status' from 'bool' to 'tristate'
tmp/.config-package.in:49325:warning: ignoring type redefinition of 'PACKAGE_luci-mod-system' from 'bool' to 'tristate'
tmp/.config-package.in:49748:warning: ignoring type redefinition of 'PACKAGE_luci-app-firewall' from 'bool' to 'tristate'
tmp/.config-package.in:50150:warning: ignoring type redefinition of 'PACKAGE_luci-app-opkg' from 'bool' to 'tristate'
tmp/.config-package.in:50693:warning: ignoring type redefinition of 'PACKAGE_luci-theme-bootstrap' from 'bool' to 'tristate'
tmp/.config-package.in:50828:warning: ignoring type redefinition of 'PACKAGE_luci-proto-ipv6' from 'bool' to 'tristate'
tmp/.config-package.in:50911:warning: ignoring type redefinition of 'PACKAGE_luci-proto-ppp' from 'bool' to 'tristate'
tmp/.config-package.in:85912:warning: ignoring type redefinition of 'PACKAGE_nftables-json' from 'bool' to 'tristate'
tmp/.config-package.in:105311:warning: ignoring type redefinition of 'PACKAGE_cgi-io' from 'bool' to 'tristate'
tmp/.config-package.in:106721:warning: ignoring type redefinition of 'PACKAGE_uhttpd' from 'bool' to 'tristate'
tmp/.config-package.in:106747:warning: ignoring type redefinition of 'PACKAGE_uhttpd-mod-ubus' from 'bool' to 'tristate'
tmp/.config-package.in:107233:warning: ignoring type redefinition of 'PACKAGE_hostapd-common' from 'bool' to 'tristate'
tmp/.config-package.in:107893:warning: ignoring type redefinition of 'PACKAGE_wpad-basic-mbedtls' from 'bool' to 'tristate'
tmp/.config-package.in:110625:warning: ignoring type redefinition of 'PACKAGE_iw' from 'bool' to 'tristate'
tmp/.config-package.in:112477:warning: ignoring type redefinition of 'PACKAGE_odhcp6c' from 'bool' to 'tristate'
tmp/.config-package.in:112524:warning: ignoring type redefinition of 'PACKAGE_odhcpd-ipv6only' from 'bool' to 'tristate'
tmp/.config-package.in:112793:warning: ignoring type redefinition of 'PACKAGE_ppp' from 'bool' to 'tristate'
tmp/.config-package.in:112830:warning: ignoring type redefinition of 'PACKAGE_ppp-mod-pppoe' from 'bool' to 'tristate'
tmp/.config-package.in:114097:warning: ignoring type redefinition of 'PACKAGE_uclient-fetch' from 'bool' to 'tristate'
tmp/.config-package.in:115798:warning: ignoring type redefinition of 'PACKAGE_uboot-envtools' from 'bool' to 'tristate'
tmp/.config-package.in:117485:warning: ignoring type redefinition of 'PACKAGE_px5g-mbedtls' from 'bool' to 'tristate'
tmp/.config-package.in:124003:warning: ignoring type redefinition of 'PACKAGE_iwinfo' from 'bool' to 'tristate'
tmp/.config-package.in:124023:warning: ignoring type redefinition of 'PACKAGE_jshn' from 'bool' to 'tristate'
tmp/.config-package.in:124288:warning: ignoring type redefinition of 'PACKAGE_libjson-script' from 'bool' to 'tristate'
tmp/.config-package.in:131391:warning: ignoring type redefinition of 'PACKAGE_ucode-mod-html' from 'bool' to 'tristate'
Config-build.in:4071:warning: defaults for choice values not supported
Config-build.in:4075:warning: defaults for choice values not supported
Config-build.in:4079:warning: defaults for choice values not supported
Config-build.in:9047:warning: defaults for choice values not supported
Config-build.in:9051:warning: defaults for choice values not supported
Config-build.in:9055:warning: defaults for choice values not supported
Config-build.in:12707:warning: defaults for choice values not supported
Config-build.in:12711:warning: defaults for choice values not supported
Config-build.in:12715:warning: defaults for choice values not supported
Config-build.in:12719:warning: defaults for choice values not supported
Config-build.in:12723:warning: defaults for choice values not supported
Config-build.in:12727:warning: defaults for choice values not supported
Config-build.in:12743:warning: defaults for choice values not supported
Config-build.in:13107:warning: defaults for choice values not supported
Config-build.in:13111:warning: defaults for choice values not supported
Config-build.in:13115:warning: defaults for choice values not supported
Config-build.in:14195:warning: defaults for choice values not supported
Config-build.in:14199:warning: defaults for choice values not supported
Config-build.in:14203:warning: defaults for choice values not supported
#
# No change to .config
#
GNU Make 4.3
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Reading makefiles...
make[1]: Entering directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64'
Updating makefiles....
Updating goal targets....
 File 'package/feeds/packages/golang/prepare' does not exist.
Must remake target 'package/feeds/packages/golang/prepare'.
make[1]: [package/Makefile:128: package/feeds/packages/golang/prepare] Error 2 (ignored)
GNU Make 4.3
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Reading makefiles...
make[2]: Entering directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/feeds/packages/lang/golang/golang'
Makefile:222: warning: overriding recipe for target '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/dl/go1.20.6.src.tar.gz'
Makefile:203: warning: ignoring old recipe for target '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/dl/go1.20.6.src.tar.gz'
Makefile:423: *** missing separator (did you mean TAB instead of 8 spaces?).  Stop.
make[2]: Leaving directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/feeds/packages/lang/golang/golang'
time: package/feeds/packages/golang/prepare#0.09#0.07#0.13
    ERROR: package/feeds/packages/golang failed to build.
make[1]: *** [package/Makefile:129: package/feeds/packages/golang/prepare] Error 1
make[1]: Leaving directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64'
make: *** [/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/include/toplevel.mk:225: package/feeds/packages/golang/prepare] Error 2
