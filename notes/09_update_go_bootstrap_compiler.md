The error you're encountering occurs because Go 1.22 and later versions require at least Go 1.20.6 as the bootstrap compiler. In your case, the build process is attempting to use Go 1.17.13 as the bootstrap compiler, which is too old for building Go 1.23.4.

From the error message:

```
Building Go cmd/dist using /.../.go_bootstrap_1.17. (go1.17.13 linux/amd64)
found packages main (build.go) and building_Go_requires_Go_1_20_6_or_later (notgo120.go) in /.../go-1.23.4/src/cmd/dist
```

The file `notgo120.go` exists specifically to prevent building Go 1.22+ with a bootstrap compiler older than Go 1.20.6. To resolve this error, you'll need to update the bootstrap Go compiler used during the build process to at least Go 1.20.6.

Here's how you can fix this issue:

---

## Steps to Update the Bootstrap Go Compiler in OpenWrt SDK

### 1. Build Go 1.20.6 as the New Bootstrap Compiler

First, we need to build Go 1.20.6 using the existing Go 1.17 compiler.

**Note:** Go 1.20.6 can be bootstrapped with Go 1.17, according to the [Go release notes](https://golang.org/doc/devel/release.html#go1.20.min_requirements).

#### a. Download and Extract Go 1.20.6 Source Code

```bash
cd /tmp
wget https://dl.google.com/go/go1.20.6.src.tar.gz
tar -C /usr/local -xzf go1.20.6.src.tar.gz
```

#### b. Build Go 1.20.6

```bash
cd /usr/local/go/src
# Set GOROOT_BOOTSTRAP to your existing Go 1.17 installation
export GOROOT_BOOTSTRAP=/path/to/go1.17
./make.bash
```

This will build Go 1.20.6 using Go 1.17.

### 2. Install Go 1.20.6 as the Bootstrap Compiler

Now, we'll install Go 1.20.6 to be used as the bootstrap compiler for building Go 1.23.4 in the OpenWrt SDK.

#### a. Install Go 1.20.6 to a Custom Location

To avoid interfering with system Go installations, install Go 1.20.6 in a custom location, such as `/opt/go1.20.6`:

```bash
mkdir -p /opt/go1.20.6
cp -r /usr/local/go/* /opt/go1.20.6/
```

### 3. Modify the OpenWrt SDK to Use the New Bootstrap Compiler

#### a. Update the `golang` Package Makefile

In your custom feed's `golang` package, modify the `Makefile` to point to the new bootstrap compiler.

```bash
# File: ${SDK_PATH}/custom_feeds/packages/lang/golang/golang/Makefile

# Add or modify the following lines
GO_BOOTSTRAP_ROOT=/opt/go1.20.6
```

Alternatively, set the `GOROOT_BOOTSTRAP` environment variable in your build script.

#### b. Export `GOROOT_BOOTSTRAP` in Your Build Script

```bash
export GOROOT_BOOTSTRAP=/opt/go1.20.6
```

### 4. Proceed with Building Go 1.23.4 in OpenWrt SDK

Continue with your build process. The OpenWrt build system should now use Go 1.20.6 as the bootstrap compiler to build Go 1.23.4.

### 5. Adjust the `update_golang_feed` Function

Modify your `update_golang_feed` function to handle the newer bootstrap compiler.

```bash
update_golang_feed() {
    local sdk_path="$1"
    local custom_feed_path="${sdk_path}/custom_feeds/packages/lang/golang"

    # ... existing code ...

    # Update Makefile with new Go version
    sed -i 's/PKG_VERSION:=.*/PKG_VERSION:=1.23.4/' "${custom_feed_path}/golang/Makefile"

    # Update hash (ensure to get the correct hash for Go 1.23.4)
    sed -i 's/PKG_HASH:=.*/PKG_HASH:=<correct_hash_for_go1.23.4>/' "${custom_feed_path}/golang/Makefile"

    # Set GOROOT_BOOTSTRAP in the Makefile
    echo 'export GOROOT_BOOTSTRAP=/opt/go1.20.6' >> "${custom_feed_path}/golang/Makefile"
}
```

### 6. Verify and Update `golang-package.mk`

Ensure that `golang-package.mk` has the correct configurations for Go 1.23.4.

```bash
# File: ${custom_feed_path}/golang-package.mk

# Update GO_VERSION_MAJOR_MINOR and GO_VERSION_PATCH
sed -i 's/GO_VERSION_MAJOR_MINOR:=.*/GO_VERSION_MAJOR_MINOR:=1.23/' "${custom_feed_path}/golang-package.mk"
sed -i 's/GO_VERSION_PATCH:=.*/GO_VERSION_PATCH:=4/' "${custom_feed_path}/golang-package.mk"
```

---

## Additional Considerations

- **Ensure Correct Hashes:** Make sure to update `PKG_HASH` with the correct SHA256 hash for the Go 1.23.4 source tarball. You can get it from the official Go downloads page.

- **Test the Build Process:** After making these changes, run the build process and monitor for any errors.

---

## Alternative Approach: Pre-Build Go Binary and Package It

If the above steps are too complex or not feasible, you might consider an alternative approach:

### Build Go Binary Separately

1. **Cross-Compile Your Go Application**

   Build your Go application using Go 1.23.4 on your host machine, targeting the appropriate architecture.

   ```bash
   GOOS=linux GOARCH=mipsle go build -o your_app
   ```

2. **Package the Binary**

   Create an OpenWrt package that includes your pre-built binary. You can write a simple `Makefile` that installs the binary into the correct directory.

---

## Summary

The error occurs because the build process uses an outdated Go compiler as the bootstrap compiler for Go 1.23.4. By updating the bootstrap compiler to Go 1.20.6, you can resolve the error and proceed with building Go 1.23.4 in the OpenWrt SDK.

Feel free to ask if you need further clarification or assistance with any of the steps.