There are a few issues in your setup:

1. The main issue is that you're using `src-link` with a URL. `src-link` is for local directories only. For git repositories, you should use `src-git`. Change your `feeds.conf` to:

```
src-git-full base https://git.openwrt.org/openwrt/openwrt.git;openwrt-23.05
src-git packages https://git.openwrt.org/feed/packages.git^063b2393cbc3e5aab9d2b40b2911cab1c3967c59
src-git luci https://git.openwrt.org/project/luci.git^b07cf9dcfc37e021e5619a41c847e63afbd5d34a
src-git routing https://git.openwrt.org/feed/routing.git^648753932d5a7deff7f2bdb33c000018a709ad84
src-git telephony https://git.openwrt.org/feed/telephony.git^86af194d03592121f5321474ec9918dd109d3057
src-git custom https://github.com/OpenTollGate/custom-nostr-feed.git;main
```

2. After fixing the `feeds.conf`, you need to:

```bash
# Update the feeds
./scripts/feeds update -a

# Install the feeds
./scripts/feeds install -a

# If you want to install specific packages from your custom feed
./scripts/feeds install -p custom tollgate-module-relay-go
```

3. Also, make sure your GitHub repository structure follows the OpenWrt feed structure:

```
custom-nostr-feed/
├── lang
│   └── golang
│       └── ...
├── tollgate-module-relay-go
│   ├── Makefile
│   └── src/
└── README.md
```

4. If you're making changes to the feed configuration, you might need to clean the feeds first:

```bash
# Clean existing feeds
rm -rf tmp feeds
./scripts/feeds clean
./scripts/feeds update -a
./scripts/feeds install -a
```

After making these changes, you should see your custom feed and packages in the `package/feeds/custom` directory.

5. To verify the feed is properly installed:

```bash
# List all available packages
./scripts/feeds list

# List packages from custom feed only
./scripts/feeds list custom

# Check if your specific package is available
./scripts/feeds list | grep tollgate-module-relay-go
```

Remember that the repository needs to be accessible (public or with proper authentication) for the feeds system to fetch it.