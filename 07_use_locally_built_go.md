The issue you are facing is related to compiling a Go-based package within the OpenWRT SDK environment. The error messages indicate that various Go standard library packages are not found during the compilation process. Here's a step-by-step guide to understand and potentially resolve the problem:

### Understanding the Issue

1. **Missing Go Standard Library Packages:**
   The error messages indicate that the Go compiler cannot find standard library packages. This is unusual because these packages are part of the Go distribution.

2. **OpenWRT SDK Environment:**
   The compilation is happening within the OpenWRT SDK, which might not properly set up the Go environment or might be using a stripped-down version of Go that lacks these standard libraries.

### Potential Solutions

1. **Check Go Environment Setup:**
   Ensure that the Go environment is correctly set up within the OpenWRT SDK. Specifically, check the `GOROOT` and `GOPATH` variables to ensure they point to the correct locations.

   - In your `Makefile`, you have set `GOROOT` and `GOPATH`. Verify that these paths are correct and that the Go standard library is indeed located under `GOROOT`.

     ```makefile
     export GOROOT:=$(STAGING_DIR_HOST)/go
     export GOPATH:=$(PKG_BUILD_DIR)/gopath
     ```

2. **Verify Go Installation:**
   Make sure that the Go installation within the OpenWRT SDK is complete and not corrupted. You might need to reinstall Go SDK or ensure that the SDK's Go environment includes all necessary standard libraries.

3. **Cross-Compilation Issues:**
   Since you're cross-compiling for a different architecture (`arm64`), ensure that the Go environment is properly configured for cross-compilation. This includes setting `GOOS`, `GOARCH`, and potentially other variables correctly, which you have done:

   ```makefile
   GOOS=linux
   GOARCH=arm64
   ```

4. **Check Dependencies:**
   The package you're trying to compile depends on external Go packages (e.g., `github.com/fiatjaf/khatru`, `github.com/nbd-wtf/go-nostr`). Ensure that these dependencies are correctly fetched and available during compilation.

5. **OpenWRT SDK Version:**
   Consider upgrading or checking the version of the OpenWRT SDK you are using. There might be known issues with Go compilation in older versions that have been fixed in newer releases.

6. **Manual Compilation Test:**
   As a troubleshooting step, try compiling a simple Go program manually within the OpenWRT SDK environment to see if the issue persists. This can help isolate whether the problem is specific to the package you're trying to build or a general issue with the Go environment.

### Example Troubleshooting Command

To verify the Go environment setup, you can try a simple Go compilation within the SDK environment:

```sh
# Enter the SDK's Go environment
cd /tmp/openwrt-sdk/openwrt-sdk-23.05.3-mediatek-filogic_gcc-12.3.0_musl.Linux-x86_64/staging_dir/host/go

# Try compiling a simple Go program
go build -o test main.go
```

Replace `main.go` with a simple Go program (e.g., `package main; func main() {}`). If this fails due to missing standard libraries, it indicates a problem with the Go environment setup within the SDK.

By following these steps, you should be able to identify and potentially resolve the issue related to missing Go standard library packages during compilation within the OpenWRT SDK.