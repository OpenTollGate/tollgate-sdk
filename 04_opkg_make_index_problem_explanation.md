chandran@chandran-TUXEDO-InfinityBook-S-15-Gen6:~/TollGate/toll_gate_sdk$ ./build-firmware helloworld
...
...
...
install -d -m0755 /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/bin/packages/mipsel_24kc/base
/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/staging_dir/host/bin/fakeroot /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/staging_dir/host/bin/bash /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/scripts/ipkg-build -m "" /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/build_dir/target-mipsel_24kc_musl/helloworld-1.0.1/ipkg-mipsel_24kc/helloworld /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/bin/packages/mipsel_24kc/base
Packaged contents of /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/build_dir/target-mipsel_24kc_musl/helloworld-1.0.1/ipkg-mipsel_24kc/helloworld into /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/bin/packages/mipsel_24kc/base/helloworld_1.0-1_mipsel_24kc.ipk
rm -rf /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/stage-helloworld
mkdir -p /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/stage-helloworld/host /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mipsel_24kc_musl/packages
find /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/stage-helloworld -name '*.la' | xargs -r rm -f; 
if [ -f /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mipsel_24kc_musl/packages/helloworld.list ]; then /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/scripts/clean-package.sh "/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mipsel_24kc_musl/packages/helloworld.list" "/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mipsel_24kc_musl"; fi
if [ -d /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/stage-helloworld ]; then (cd /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/stage-helloworld; find ./ > /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/stage-helloworld.files); 	SHELL= flock /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/.staging-dir.flock -c ' mv /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/stage-helloworld.files /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mipsel_24kc_musl/packages/helloworld.list && cp -fpR /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/stage-helloworld/* /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mipsel_24kc_musl/; '; fi
rm -rf /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/tmp/stage-helloworld
touch /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/staging_dir/target-mipsel_24kc_musl/stamp/.helloworld_installed
touch -r /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/build_dir/target-mipsel_24kc_musl/helloworld-1.0.1/.built /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/build_dir/target-mipsel_24kc_musl/helloworld-1.0.1/.autoremove 2>/dev/null >/dev/null
find /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/build_dir/target-mipsel_24kc_musl/helloworld-1.0.1 -mindepth 1 -maxdepth 1 -not '(' -type f -and -name '.*' -and -size 0 ')' -and -not -name '.pkgdir'  -print0 | xargs -r -0 rm -rf
make[2]: Leaving directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64/package/helloworld'
time: package/helloworld/compile#1.09#0.74#2.21
make[1]: Leaving directory '/tmp/openwrt-sdk/openwrt-sdk-23.05.3-ramips-mt76x8_gcc-12.3.0_musl.Linux-x86_64'
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
./opkg-make-index: fork: retry: Resource temporarily unavailable
./opkg-make-index: fork: retry: Resource temporarily unavailable
./opkg-make-index: fork: retry: Resource temporarily unavailable
./opkg-make-index: fork: retry: Resource temporarily unavailable
./opkg-make-index: fork: Resource temporarily unavailable


The warnings you're encountering are indicative of an issue with how `opkg-make-index` is being invoked in your script. Let's break down what's happening and how to fix it.

### **Understanding the Warnings**

1. **Shell Level Too High**:
    ```
    /bin/bash: warning: shell level (1000) too high, resetting to 1
    ```
    This message indicates that your script is recursively calling itself or another script, causing the shell to reach its maximum recursion depth (`SHLVL`), which defaults to 1000 in Bash.

2. **Resource Temporarily Unavailable**:
    ```
    ./opkg-make-index: fork: retry: Resource temporarily unavailable
    ```
    This error suggests that the system is running out of resources, likely due to too many simultaneous processes spawned by recursive script calls.

### **Root Cause**

The issue stems from the way `opkg-make-index` is set up in your `build-firmware` script. Specifically, in the `setup_python_environment` function:

```bash
setup_python_environment() {
    local sdk_path=$1
    
    if [ ! -f "${sdk_path}/staging_dir/host/bin/opkg-make-index" ]; then
        echo "Installing opkg-make-index..."
        mkdir -p "${sdk_path}/staging_dir/host/bin"
        wget https://raw.githubusercontent.com/shr-project/opkg-utils/master/opkg-make-index -O "${sdk_path}/staging_dir/host/bin/opkg-make-index.py"
        
        # Create a simple wrapper script
        cat > "${sdk_path}/staging_dir/host/bin/opkg-make-index" << 'EOF'
    #!/usr/bin/env python3
    [Python script content...]
    EOF
        chmod +x "${sdk_path}/staging_dir/host/bin/opkg-make-index"
    else
        echo "opkg-make-index is already installed."
    fi
}
```

**Issues:**

- **Naming Confusion**: You're downloading a shell script (`opkg-make-index`) and saving it as `opkg-make-index.py`, then creating a Python script also named `opkg-make-index`.
- **Recursive Calls**: The wrapper script might be calling itself recursively due to conflicting names or incorrect invocation.
- **Mismatch of Languages**: The original `opkg-make-index` from SHR Project is a shell script, not a Python script.

### **Is It Safe to Suppress the Warnings?**

No, it's **not safe** to suppress these warnings. They indicate a problem that could lead to:

- **Incomplete Package Index**: Your package index (`Packages` file) might not be correctly generated, causing issues when installing packages.
- **System Instability**: Excessive resource usage can impact your system's performance.

### **Recommended Solution**

#### **1. Use the System's `opkg-utils` Package**

Install the official `opkg-utils` package, which includes `opkg-make-index`, from your Ubuntu repository:

```bash
sudo apt-get update
sudo apt-get install opkg-utils
```

#### **2. Update Your `build-firmware` Script**

Replace the `setup_python_environment` function and any custom `opkg-make-index` setups with a simple symlink to the system's `opkg-make-index`.

**Updated `build-firmware` Script:**

```bash
#!/bin/bash
set -e

# Install required dependencies
install_dependencies() {
    local packages=("libncurses5-dev" "libncursesw5-dev" "opkg-utils")
    local missing_packages=()

    for pkg in "${packages[@]}"; do
        if ! dpkg -s "$pkg" >/dev/null 2>&1; then
            missing_packages+=("$pkg")
        fi
    done

    if [ ${#missing_packages[@]} -ne 0 ]; then
        echo "Installing missing packages: ${missing_packages[*]}"
        sudo apt-get update
        sudo apt-get install -y "${missing_packages[@]}"
    else
        echo "All required packages are already installed."
    fi
}

# Create symlink to opkg-make-index
setup_opkg_make_index() {
    local sdk_path=$1
    local opkg_make_index="${sdk_path}/staging_dir/host/bin/opkg-make-index"
    
    if [ ! -f "${opkg_make_index}" ]; then
        echo "Linking opkg-make-index..."
        mkdir -p "${sdk_path}/staging_dir/host/bin"
        ln -s "$(which opkg-make-index)" "${opkg_make_index}"
    else
        echo "opkg-make-index is already set up."
    fi
}

# Main script logic
install_dependencies

VERSION=23.05.3
SDKDIR=/tmp/openwrt-sdk
PLATFORM="ramips"
SUBTARGET="mt76x8"
SDK_ARCHIVE="openwrt-sdk-${VERSION}-${PLATFORM}-${SUBTARGET}_gcc-12.3.0_musl.Linux-x86_64.tar.xz"
DOWNLOAD_URL="https://downloads.openwrt.org/releases/${VERSION}/targets/${PLATFORM}/${SUBTARGET}/${SDK_ARCHIVE}"

# Check if the required arguments are provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <package_name>"
    exit 1
fi

PACKAGE_NAME=$1

# Prepare SDK directory
mkdir -p "${SDKDIR}"

if [ ! -d "${SDKDIR}/openwrt-sdk" ] ; then
    if [ ! -f "${SDKDIR}/${SDK_ARCHIVE}" ]; then
        (cd "${SDKDIR}" && curl -O "${DOWNLOAD_URL}")
    fi
    tar -xf "${SDKDIR}/${SDK_ARCHIVE}" -C "${SDKDIR}"
fi

SDK_PATH=$(find "${SDKDIR}" -maxdepth 1 -type d -name "openwrt-sdk-*")
cd "${SDK_PATH}"

# Set up opkg-make-index
setup_opkg_make_index "${SDK_PATH}"

# Update and install feeds
./scripts/feeds update -a
./scripts/feeds install -a

# Copy the custom package into the SDK
cp -r ~/TollGate/openwrt_helloworld/"${PACKAGE_NAME}" package/

# Configure the SDK to include the package
make defconfig

# Build the package
make package/"${PACKAGE_NAME}"/compile V=s

# Move built package to a local directory
BUILT_PACKAGE_PATH=$(find bin/packages -name "${PACKAGE_NAME}_*.ipk")
DEST_DIR=~/local_feed

mkdir -p "${DEST_DIR}"
cp "${BUILT_PACKAGE_PATH}" "${DEST_DIR}"

# Generate package index using opkg-make-index
cd "${DEST_DIR}"
"${SDK_PATH}"/staging_dir/host/bin/opkg-make-index . > Packages
gzip -k Packages

echo "Package ${PACKAGE_NAME} has been built and stored in ${DEST_DIR}"
```

**Explanation:**

- **Install Dependencies**: The script now ensures `opkg-utils` is installed.
- **Symlink Creation**: `opkg-make-index` is symlinked from the system to where the SDK expects it.
- **Removed Custom Scripts**: All custom `opkg-make-index` scripts and functions are removed to prevent conflicts.

#### **3. Rebuild Your Package**

Run your build script again:

```bash
./build-firmware helloworld
```

### **Addressing Your Questions**

1. **Why Am I Still Getting These Warnings?**

   The warnings are due to recursion caused by your custom `opkg-make-index` setup. The script is likely invoking itself repeatedly until the system resources are exhausted, leading to those warnings.

2. **Is It Safe to Suppress Them?**

   No, suppressing these warnings without fixing the underlying cause is not recommended. They indicate a problem that can affect the correctness of your package index and the stability of your system.

3. **How Can I Suppress Them?**

   Instead of suppressing, it's better to fix the issue by using the proper `opkg-make-index` utility from `opkg-utils`. With the updated script above, these warnings should no longer occur.

### **Conclusion**

By installing `opkg-utils` and properly setting up `opkg-make-index`, you eliminate the root cause of the warnings. This approach ensures:

- **Correct Package Indexing**: Your `Packages` file will be correctly generated.
- **System Stability**: Avoids unnecessary resource consumption.
- **Simplified Script**: Reduces complexity by removing unnecessary custom scripts.

Feel free to let me know if you have any further questions or need assistance with the updated script.