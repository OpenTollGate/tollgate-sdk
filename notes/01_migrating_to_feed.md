To pull custom feeds from a git server instead of using local paths, you should modify the `feeds.conf` file to use `src-git` instead of `src-link`. Here's how you can do it:

1. First, modify your `feeds.conf` to use a git repository:

```
src-git-full base https://openwrt/openwrt.git;openwrt-23.05
src-git packages https://git.openwrt.org/feed/packages.git^063b2393cbc3e5aab9d2b40b2911cab1c3967c59
src-git luci https://git.openwrt.org/project/luci.git^b07cf9dcfc37e021e5619a41c847e63afbd5d34a
src-git routing https://git.openwrt.org/feed/routing.git^648753932d5a7deff7f2bdb33c000018a709ad84
src-git telephony https://git.openwrt.org/feed/telephony.git^86af194d03592121f5321474ec9918dd109d3057
src-git custom https://github.com/YourOrganization/custom-openwrt-packages.git
```

2. Modify your `build-firmware` script to remove the local copy operations and use git instead:

```bash
# Remove these lines
#cp -r ~/TollGate/toll_gate_sdk/custom_feeds "${SDK_PATH}"/.
#cp -r ~/TollGate/toll_gate_sdk/feeds.conf "${SDK_PATH}"/.

# Instead, just copy the feeds.conf
cp feeds.conf "${SDK_PATH}"/feeds.conf

# Remove these lines as packages will come from git
#mkdir -p "${SDK_PATH}/package/${PACKAGE_NAME}"
#mkdir -p "${SDK_PATH}/custom_feeds/packages/${PACKAGE_NAME}"
#cp -r ~/TollGate/tollgate-module-relay-go/{Makefile,src} "${SDK_PATH}/package/${PACKAGE_NAME}/"
#cp -r ~/TollGate/tollgate-module-relay-go/{Makefile,src} "${SDK_PATH}/custom_feeds/packages/${PACKAGE_NAME}/"
```

3. Create a proper git repository structure:

```
custom-openwrt-packages/
├── lang
│   └── golang
│       └── golang/
│           ├── Config.in
│           ├── Makefile
│           └── files/
├── tollgate-module-relay-go/
│   ├── Makefile
│   └── src/
└── README.md
```

4. Host this repository on GitHub or your preferred git hosting service

5. Update your modification to the golang package handling in the script:

```bash
# Handle golang specifically
echo "Setting up golang..."
rm -rf "${SDK_PATH}/feeds/packages/lang/golang"
./scripts/feeds install -a -p custom
./scripts/feeds install golang
```

Benefits of this approach:

1. Version control for your packages
2. Easier collaboration and distribution
3. No dependency on local files
4. Better reproducibility
5. Can specify specific commits or tags using the caret notation (^commit-hash)
6. Can use branches for different versions

Example repository URL formats:

```
# Main branch
src-git custom https://github.com/YourOrg/custom-openwrt-packages.git

# Specific branch
src-git custom https://github.com/YourOrg/custom-openwrt-packages.git;branch-name

# Specific commit
src-git customOrg/custom-openwrt-packages.git^commit-hash
```

Make sure to:

1. Create a GitHub/GitLab repository for your custom packages
2. Push your package structure to this repository
3. Update the `feeds.conf` with the correct repository URL
4. Use proper versioning and tags in your repository
5. Update your build scripts to use the git-based approach

This will make your build process more robust and easier to maintain across different machines and environments.